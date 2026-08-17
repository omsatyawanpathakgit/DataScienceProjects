
---

## 6. Laptop Segmentation using K-Means

```markdown
# Laptop Segmentation using K-Means Clustering

## Project Overview
A clustering project that segments laptops into meaningful customer segments using K-Means clustering. The project includes hypothesis testing to validate business claims and unsupervised learning to categorize laptops into market segments.

## Problem Statement
A laptop company wants to segment its laptops into different customer segments based on specifications, pricing, and customer feedback. Build a clustering model that groups laptops into meaningful categories such as Budget, Professional, Gaming, and Premium laptops.

## Dataset
- **Source**: Laptop pricing dataset
- **Records**: 823 laptops
- **Features**: 19 columns (after processing)

### Features Used
- Price, RAM (GB), Graphic Card (GB), Total Storage, Performance Score
- Rating, Number of Ratings, Number of Reviews
- Brand, Processor Brand, OS

## Hypothesis Testing Results

### One-Sample Z-Test (Mean)
| Test | Result | Significance |
|------|--------|--------------|
| Average price ≠ ₹60,000 | ✅ Reject H₀ | Significant difference |
| SSD proportion > 70% | ✅ Reject H₀ | SSD proportion > 70% |
| SSD proportion < 40% | ❌ Fail to reject | Not less than 40% |

### Two-Sample Z-Test
| Test | Result | Significance |
|------|--------|--------------|
| HP vs Lenovo price difference | ❌ Fail to reject | No significant difference |

### One-Sample T-Test
| Test | Result | Significance |
|------|--------|--------------|
| Apple rating ≠ 3.5 stars | ✅ Reject H₀ | Rating significantly different |

### Independent T-Test
| Test | Result | Significance |
|------|--------|--------------|
| GPU vs No-GPU price difference | ✅ Reject H₀ | Significant price difference |

### Paired T-Test
| Test | Result | Significance |
|------|--------|--------------|
| Ratings vs Reviews difference ≠ 0 | ✅ Reject H₀ | Significant difference |

### ANOVA Tests
| Test | Result | Significance |
|------|--------|--------------|
| Processor brand effect on price | ✅ Reject H₀ | Different avg prices |
| Brand × GPU interaction | ✅ Reject H₀ | Significant interaction |

## Clustering Analysis

### Elbow Method Results
- Identified optimal number of clusters using WCSS
- K=3 selected based on Silhouette Score

### Silhouette Scores
| K | Silhouette Score |
|---|-----------------|
| 2 | 0.3039 |
| 3 | **0.3262** (Best) |
| 4 | 0.1927 |
| 5 | 0.2006 |
| 6 | 0.2071 |
| 7 | 0.2041 |
| 8 | 0.2084 |
| 9 | 0.2163 |
| 10 | 0.2091 |

### Cluster Profiles

| Cluster | Segment | Avg Price | RAM (GB) | GPU (GB) | Storage (GB) | Performance | Rating |
|---------|---------|-----------|----------|----------|--------------|-------------|--------|
| 0 | Mid-Price | ₹63,649 | 6.57 | 0.86 | 651.91 | 18.28 | 3.58 |
| 1 | **Premium/High-Performance** | **₹123,263** | **15.96** | **2.43** | **795.73** | **40.77** | **3.51** |
| 2 | Budget/Mass-Market | ₹65,956 | 6.40 | 0.90 | 678.40 | 17.65 | 3.80 |

### Cluster Distribution
- **Mid-Price Laptops**: Most dominant segment
- **Budget Laptops**: Fewest number
- **Premium Laptops**: Moderate quantity

## Technologies Used
- Python 3.x
- Pandas, NumPy
- Scikit-learn (KMeans, PCA)
- Statsmodels (Hypothesis Testing)
- Scipy (Statistical Tests)
- Matplotlib, Seaborn
