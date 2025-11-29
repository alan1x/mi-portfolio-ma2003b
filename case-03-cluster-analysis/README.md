# MegaMart Customer Segmentation

## Project Description

This project implements a **customer segmentation system** for **MegaMart**, a national retail chain. Using **unsupervised clustering techniques** (K-means and hierarchical clustering), the goal is to identify natural behavioral groups among 3,000 active customers to:

- Optimize marketing campaigns
- Improve customer retention
- Increase Customer Lifetime Value (CLV)

---

## Objective

Identify distinct customer segments based on 9 behavioral variables to:

- Enhance targeting in marketing campaigns
- Reduce customer churn
- Increase conversion rates and engagement
- Personalize the customer experience based on profile

---

## Methodology

### Analysis Workflow

1. **Data Loading & Exploration**  
   A clean dataset with 3,000 customers and 9 behavioral variables was analyzed. No missing values were found.

2. **Exploratory Data Analysis (EDA)**  
   Key insights were derived from relationships between spending, purchase frequency, and engagement.

3. **Data Standardization**  
   Applied `StandardScaler` to normalize variables before clustering.

4. **Hierarchical Clustering**  
   Tested various linkage methods. The **Ward method** was the most effective, suggesting 3–4 potential clusters.

5. **K-means Clustering**  
   Used the Elbow Method and silhouette analysis.  
   Chose **k = 4** as the optimal number of clusters, achieving a silhouette score of **0.32**.

6. **Cluster Profiling**  
   Each cluster was profiled using its average behavioral metrics to define clear customer personas.

7. **Validation**  
   Cluster quality was validated using silhouette plots and PCA (Principal Component Analysis) projections.

---

## Discovered Segments

| Segment Name               | % Customers | Profile Description                         |
| -------------------------- | ----------- | ------------------------------------------- |
| High-Value Loyalists       | 17.5%       | Frequent shoppers, high spend, very loyal   |
| Low-Engagement Browsers    | 31.0%       | Browse often, purchase rarely               |
| Growth-Potential Customers | 14.4%       | Moderate frequency, strong upsell potential |
| Consistent Moderates       | 37.1%       | Steady spenders with medium activity        |

---

## Marketing Recommendations

### 1. High-Value Loyalists

- VIP loyalty program with exclusive rewards
- Personalized recommendations via email
- Assign dedicated account managers

### 2. Low-Engagement Browsers

- Cart abandonment emails with discounts
- First-purchase incentives ($10 off)
- Improve product information and reviews

### 3. Growth-Potential Customers

- Frequency-based offers (e.g., buy 3 times → 20% off)
- Curated bundles
- Fast-track them to VIP tier

### 4. Consistent Moderate Shoppers

- Cross-sell campaigns to increase AOV
- Weekly personalized email offers
- Expand category interest with recommendations

---

## Expected Impact

| Metric                        | Before | Projected | Improvement |
| ----------------------------- | ------ | --------- | ----------- |
| Email open rate               | 44%    | 61%       | +40%        |
| Conversion rate               | 12%    | 14.4%     | +20%        |
| High-value customer churn     | 15%    | 11.25%    | -25%        |
| Average Order Value (AOV)     | $9.10  | $10.50    | +15%        |
| Customer Lifetime Value (CLV) | $2,109 | $2,530    | +20%        |

---

## How to Run

```bash
git ```bash
git clone https://github.com/alan1x/mi-portfolio-ma2003b.git
cd case-03-customer-segmentation/
jupyter notebook mega_mart.ipynb
```

---

## Project Structure

```
case-03-customer-segmentation/
│
├── data/
│   ├── retail_customer_data.csv
│   ├── retail_customer_data_with_labels.csv
│   └── retail_customer_data_dictionary.pdf
│
├── notebooks/
│   ├── cluster_analysis.ipynb
│   └── mega_mart.ipynb
│
├── reports/
│   ├── cluster_analysis.pdf
│   ├── executive_summary.pdf
│   ├── technical_report.pdf
│   └── README.md
│
└── visualizations/
    ├── cluster_profiles/
    │   ├── cluster_profiles_k3.png
    │   └── cluster_profiles_k4.png
    │
    ├── correlation_analysis/
    │   └── correlation_matrix_heatmap.png
    │
    ├── dendrograms/
    │   ├── Focused_Dendrogram_Ward_Linkage.png
    │   └── hierarchical_clustering_dendrograms.png
    │
    ├── elbow_silhouette_plots/
    │   ├── elbow_and_silhouette_plots.png
    │   ├── elbow_plot_k_vs_inertia.png
    │   ├── silhouette_plot_k3.png
    │   ├── silhouette_plot_k4.png
    │   ├── silhouette_score_vs_k.png
    │   └── silhouette_score_vs_k_line_plot.png
    │
    ├── pca_scatter_plots/
    │   ├── PCA_Projection_of_Clusters_K3.png
    │   ├── PCA_Projection_of_Clusters_K3_with_Centroids.png
    │   ├── PCA_Projection_of_Clusters_K4.png
    │   └── PCA_Projection_of_Clusters_K4_with_Centroids.png
    │
    ├── variable_analysis/
    │   ├── key_variable_relationships.png
    │   ├── variable_distributions_histograms.png
    │   └── outlier_detection_boxplots.png

---

##  Additional Documentation

- Executive Summary.
- Executive Presentation.
- [Video Presentation] 
```
