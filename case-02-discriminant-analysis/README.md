# LendSmart Credit Risk Analysis

## Project Description

This project develops a **credit risk analysis system** for LendSmart, a financial institution seeking to optimize its loan approval decisions. Using **Discriminant Analysis** techniques, the project classifies credit applicants based on their probability of default.

## Objective

Build predictive models capable of:

- Distinguishing between reliable and unreliable customers
- Identifying the most relevant variables for predicting default risk
- Comparing the performance of different classification techniques (LDA vs QDA)

## Methodology

### Implemented Techniques

| Model                                     | Description                                                                    |
| ----------------------------------------- | ------------------------------------------------------------------------------ |
| **LDA** (Linear Discriminant Analysis)    | Assumes equal covariance between classes, generates linear decision boundaries |
| **QDA** (Quadratic Discriminant Analysis) | Allows different covariances per class, generates quadratic boundaries         |

### Analysis Workflow

1. **Data loading and exploration** - Initial dataset inspection
2. **Exploratory Data Analysis (EDA)** - Correlations and distributions
3. **Preprocessing** - Train/test split and standardization
4. **Assumption testing** - Multivariate normality and covariance homogeneity
5. **LDA Modeling** - Training and coefficient interpretation
6. **QDA Modeling** - Training with flexible covariances
7. **Evaluation** - Metrics, confusion matrices and ROC curves
8. **Conclusions** - Optimal model selection

## Dataset Variables

The file `credit_risk_data-1.csv` contains 2,500 records with the following variables:

### Predictor Variables

| Variable                | Description                               |
| ----------------------- | ----------------------------------------- |
| `loan_amount`           | Requested loan amount ($5,000 - $500,000) |
| `annual_income`         | Applicant's annual income                 |
| `credit_score`          | Credit score                              |
| `payment_history_score` | Previous payment history                  |
| `debt_to_income_ratio`  | Debt-to-income ratio                      |
| `job_stability_score`   | Job stability                             |
| `credit_utilization`    | Percentage of available credit used       |
| `employment_years`      | Years of employment                       |
| `asset_value`           | Asset value                               |
| `savings_ratio`         | Savings ratio                             |
| `age`                   | Applicant's age                           |
| `residential_stability` | Residential stability                     |

### Target Variable

- `loan_status`: Loan status (0 = Compliance, 1 = Default)

## Key Findings

### Top 5 Risk Predictors (based on LDA coefficients)

| Variable              | Coefficient | Interpretation                    |
| --------------------- | ----------- | --------------------------------- |
| Payment History Score | -15.54      | Poor history increases risk       |
| Job Stability Score   | -13.07      | Job instability increases risk    |
| Credit Utilization    | +11.64      | High utilization indicates risk   |
| Debt-to-Income Ratio  | +4.51       | High relative debt increases risk |
| Credit Score          | -3.94       | Low score correlates with default |

### Model Results

Both models achieved **perfect performance** on the test set:

- **LDA AUC Score**: 1.0000
- **QDA AUC Score**: 1.0000
- Precision, Recall and F1-Score: 100%

### Final Recommendation

**LDA** is recommended for its simplicity and interpretability, given that both models achieved equivalent results.

## Project Structure

```
case-02-discriminant-analysis/
│
├── data/
│   └── credit_risk_data-1.csv
│
├── notebooks/
│   ├── discriminant_analysis.ipynb
│   └── discriminant_analysis.pdf
│
├── reports/
│   ├── business_report.pdf
│   └── presentation.pdf
│
├── visualizations/
│   ├── confusion_matrix_LDA.png
│   ├── confusion_matrix_QDA.png
│   ├── correlation_matrix.png
│   ├── credit_score_*.png
│   ├── credit_utilization_*.png
│   ├── debt_to_income_ratio_*.png
│   └── ...
│
└── README.md
```

## How to run

```bash
git clone https://github.com/alan1x/mi-portfolio-ma2003b.git
cd case-02-discriminant-analysis/notebooks
jupyter notebook notebooks/discriminant_analysis.ipynb
```

## Additional Documentation

- Executive Summary
- Executive Presentation
