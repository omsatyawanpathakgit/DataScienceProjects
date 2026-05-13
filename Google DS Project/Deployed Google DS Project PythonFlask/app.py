from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

install_model = joblib.load("AppInstalls_PredictionModel.pkl")
performance_model = joblib.load("AppPerformancePrediction.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict_installs", methods=["POST"])
def predict_installs():
    category = request.form["category"]
    rating = float(request.form["rating"])
    reviews = int(request.form["reviews"])
    size = request.form["size"]
    price = float(request.form["price"])
    content_rating = request.form["content_rating"]
    main_genre = request.form["main_genre"]
    last_updated = request.form["last_updated"]

    input_data = pd.DataFrame([{
        "Category": category,
        "Rating": rating,
        "Reviews": reviews,
        "Size": size,
        "Price": price,
        "Content Rating": content_rating,
        "Main_Genre": main_genre,
        "Last Updated": last_updated
    }])

    log_prediction = install_model.predict(input_data)[0]
    predicted_installs = int(np.expm1(log_prediction))

    return render_template(
        "index.html",
        install_prediction=f"Expected Installs: {predicted_installs:,}"
    )


@app.route("/predict_performance", methods=["POST"])
def predict_performance():
    category = request.form["category"]
    size_mb = float(request.form["size_mb"])
    price = float(request.form["price"])
    content_rating = request.form["content_rating"]
    main_genre = request.form["main_genre"]
    days_since_update = int(request.form["days_since_update"])
    app_name_length = int(request.form["app_name_length"])
    genre_count = int(request.form["genre_count"])
    is_free = int(request.form["is_free"])

    log_price = np.log1p(price)

    input_data = pd.DataFrame([{
        "Category": category,
        "Size_MB": size_mb,
        "Price": price,
        "Content Rating": content_rating,
        "Main_Genre": main_genre,
        "Days_Since_Update": days_since_update,
        "App_Name_Length": app_name_length,
        "Genre_Count": genre_count,
        "Is_Free": is_free,
        "Log_Price": log_price
    }])

    prediction = performance_model.predict(input_data)[0]

    result = "High Performing App" if prediction == 1 else "Not High Performing App"

    return render_template(
        "index.html",
        performance_prediction=result
    )


if __name__ == "__main__":
    app.run(debug=True)