<h1 align=center>Portfolio MA2003B</h1>

<div align=center>

![GitHub last commit](https://img.shields.io/github/last-commit/alan1x/mi-portfolio-ma2003b?style=for-the-badge)

![GitHub repo size](https://img.shields.io/github/repo-size/alan1x/mi-portfolio-ma2003b?style=for-the-badge)

![GitHub top language](https://img.shields.io/github/languages/top/alan1x/mi-portfolio-ma2003b?style=for-the-badge&color=purple)

</div>

# Team members

- Luis Alan Morales Castillo (A01659147)
- Paulina Díaz Arroyo (A01029592)
- Rodrigo Jiménez Ortiz (A01029623)

## Study cases

| Case                              | Method                | Business Question                                       | Key Finding                                                                             | Link                                                                                 |
| --------------------------------- | --------------------- | ------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| TechnoServe Customer Satisfaction | Factor Analysis       | What latent dimensions drive customer satisfaction?     | 5 factors explain 67% of variance; Technical Excellence is the most important           | [View case →](./case-01-factor-analysis/notebooks/factor_analysis.ipynb)             |
| LendSmart Credit Risk             | Discriminant Analysis | How to classify credit applicants into risk categories? | Model with 85% accuracy; income and credit history are key predictors                   | [View case →](./case-02-discriminant-analysis/notebooks/discriminant_analysis.ipynb) |
| ShopSmart Customer Segmentation   | Cluster Analysis      | What natural segments exist in the customer base?       | 5 clusters identified; "High-Value Loyalists" represent 18% but generate 45% of revenue | [View case →](./case-03-cluster-analysis/notebooks/cluster_analysis.ipynb)           |

## Methodological Comparison

| **Aspect**           | **Factor Analysis**                                                                                                               | **Discriminant Analysis**                                                                                    | **Cluster Analysis**                                                                                            |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| **Type of learning** | Unsupervised                                                                                                                      | Supervised                                                                                                   | Unsupervised                                                                                                    |
| **Main objective**   | Dimensionality reduction                                                                                                          | Classification                                                                                               | Segmentation                                                                                                    |
| **Required input**   | Continuous variables                                                                                                              | Categorical variable (target) + predictors                                                                   | Continuous variables                                                                                            |
| **Main output**      | Latent factors                                                                                                                    | Discriminant functions                                                                                       | Groups/clusters                                                                                                 |
| **Ideal use case**   | Identifying hidden dimensions that explain variability across a set of variables (psychometrics, marketing, satisfaction studies) | Classifying observations into existing groups and understanding which variables discriminate between classes | Finding natural groups without prior labels                                                                     |
| **Limitations**      | Requires high correlation among variables; results may be subjective; sensitive to outliers and scaling                           | Assumes multivariate normality and similar variances across groups; sensitive to multicollinearity           | May produce hard-to-interpret clusters; depends on hyperparameters (e.g., k); sensitive to scaling and outliers |

## Lessons Learned

- Syntax Differences:
  Each analysis method (Factor, Discriminant, Cluster) required different libraries with distinct syntaxes so we learned to create standardized code templates for data loading, preprocessing, and visualization.
- Mathematical Assumptions:
  Understanding when to use LDA vs QDA, or hierarchical vs K-means clustering, which in consecuence, drive us to a deep dive into statistical theory, validating assumptions before the model selection.
- Interpretation of Results:
  Translating statistical outputs (eigenvalues, coefficients, silhouette scores) into business insights.
- Data Preprocessing:
  The standardization is critical in the process and it makes a significantly impact to the results in distance-based methods.
- Code Integration:
  Different coding styles across team members, forced us to establish naming conventions and folder structures.
- Analysis:
  Review sessions before finalizing conclusions.
- Version Control:
  Managing notebook conflicts in git.

## Setup and Dependencies

### Prerequisites

Before running the project, ensure you have the following installed:

- **Python** >= 3.10
- **pip** >= 23.0
- **Git**
- **Jupyter Notebook** or **JupyterLab**

### Installation

#### 1. Clone repository

```bash
git clone https://github.com/alan1x/mi-portfolio-ma2003b.git
cd mi-portfolio-ma2003b
```

#### 2. Create virtual environment (recommended)

**Using `conda`**

```bash
conda create -n ma2003b python=3.11
conda activate ma2003b
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Contributors

<a href="https://github.com/alan1x/mi-portfolio-ma2003b/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=alan1x/mi-portfolio-ma2003b&anon=1&max=10" />
</a>
