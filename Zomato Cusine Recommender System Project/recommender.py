import pickle

# Load the exported files
new_df = pickle.load(open("dishes.pkl", "rb"))
similarity = pickle.load(open("dishes_similarity.pkl", "rb"))


def recommend(dish, top_n=10):
    """
    Returns the top recommended dishes.
    """

    # Check if dish exists
    if dish not in new_df["dish_liked"].values:
        print(f"'{dish}' not found in the dataset.")
        return

    # Find the first occurrence
    dish_index = new_df[new_df["dish_liked"] == dish].index[0]

    # Similarity scores
    distances = similarity[dish_index]

    # Sort by similarity
    dishes_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:]

    seen = set()
    count = 0

    print(f"\nRecommendations for '{dish}'\n")
    print("-" * 70)

    for i, score in dishes_list:

        recommended_dish = new_df.iloc[i]["dish_liked"]

        # Skip duplicates
        if recommended_dish == dish or recommended_dish in seen:
            continue

        print(
            f"{recommended_dish:25}"
            f"Restaurant: {new_df.iloc[i]['name']:30}"
            f"Similarity: {score:.2f}"
        )

        seen.add(recommended_dish)
        count += 1

        if count == top_n:
            break

recommend("Masala Dosa")
recommend("Coffee")
recommend("Biryani")