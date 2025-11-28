## ***Business Context***

### **Client Description and Problem**

TechnoServe Solutions collected data from 300 clients across 25 satisfaction indicators with the goal of understanding:

- What drives overall satisfaction.
- Which factors best predict renewal, NPS, growth, and referrals.
- Where to prioritize investments to improve customer experience.

### **Strategic Importance of the Analysis**

The analysis is key because:

- It reduces 25 indicators into 5 strategic factors (simplifies decision-making).
- Allows directing investments toward the statistically most influential drivers.
- Connects satisfaction metrics with direct financial impact (renewals and revenue growth).
- Generates a clear priority map for operations, sales, and product teams.

## ***Methodology***

Multivariate method applied. The following were used:

### **Factor Analysis**

- Normalization: StandardScaler  
- Validation:
    - KMO = 0.94 (excellent adequacy)
    - Bartlett p < 0.001 (matrix suitable)
- Initial extraction with sklearn and Varimax rotation.
- Five factors retained, confirmed by the scree plot.

### **OLS Regression Models**

Independent regressions were executed using factor scores as predictors for:

- Overall Satisfaction  
- NPS  
- Renewal Likelihood  
- Revenue Growth  
- Referrals

### **Justification of the Approach**

- EFA reveals latent patterns and reduces dimensionality.
- Regression quantifies the impact of each factor.
- Together, they allow:
    - Model interpretability.
    - Action prioritization based on statistical impact.

### **Tools and Libraries Used**

- Pandas → data cleaning and handling  
- NumPy → matrix calculations  
- Scikit-Learn → standardization and component extraction  
- FactorAnalyzer → KMO, Bartlett, Varimax rotation  
- Statsmodels → OLS regressions  
- Matplotlib / Seaborn → analysis visualizations (heatmaps, scree plot)

## ***Data***

### **Dataset Description**

- 300 observations  
- 25 variables measuring customer perception on:
    - Technical experience
    - Account management
    - Project execution
    - Business value
    - Support and documentation

### **Processing Performed**

- Mean imputation  
- Standardization with StandardScaler  
- Computation of:
    - Correlation matrix
    - KMO
    - Bartlett test
    - Scree plot
    - Rotated loadings
    - Factor scores

### **Key Variables**

*Loadings ≥ 0.70*

- innovation_solutions — 0.72  
- problem_solving — 0.71  
- system_integration — 0.71  
- technical_documentation — 0.70  

*Loadings between 0.69 and 0.65*

- technical_expertise — 0.69  
- project_management — 0.65  
- trust_reliability — 0.64  
- quality_deliverables — 0.64  
- timeline_adherence — 0.64  
- executive_access — 0.63  
- long_term_partnership — 0.63  

*Loadings between 0.62 and 0.60*

- change_management — 0.62  
- budget_control — 0.62  
- account_manager_responsive — 0.61  
- communication_clarity — 0.61  
- billing_accuracy — 0.60  

*Loadings between 0.57 and 0.53*

- competitive_pricing — 0.57  
- roi_demonstration — 0.57  
- cost_transparency — 0.57  
- value_for_money — 0.53  

*Loadings below 0.50*

- training_quality — 0.46  
- support_responsiveness — 0.44  
- documentation_help — 0.42  

### **Link to Data Dictionary**

[Download data dictionary](data/customer_satisfaction_data.csv)

## ***Main Findings***

### **Key Findings**

- Five factors explain 65–70% of the dataset variance.
- The Technical and Relational factors have the highest statistical impact on:
    - Overall Satisfaction
    - NPS
    - Renewal Likelihood
    - Revenue Growth
    - Referrals
- Regression models perform solidly (MSE 0.28–0.42).
- The notebook confirms via heatmaps that factors have clear structures.
- The scree plot shows the natural drop justifying 5 factors.

### **Highlighted Visualization**

[Scree Plot](visualizations/scree_plot.png)

The Scree Plot shows the explained variance by each component and justifies selecting 5 factors, as a clear elbow appears after the fifth component.

### **Model Performance Metrics**

| **Metric**            | **Values**                           |
| --------------------- | ------------------------------------- |
| **MSE (models)**      | 0.28 – 0.42                           |
| **Explained variance** | 58–68%                               |
| **Significance**      | p < 0.05 for the first two factors    |

## ***Business Recommendations***

### **Strategic Investment in Technical Delivery and Innovation**

- Strengthen technical skills (integration, documentation, expertise).  
- Create innovation labs.  
- Rapid problem-solving protocols.  
- Expected impact: Higher satisfaction, NPS, growth, and referrals.

### **Strengthen Commercial Relationship & Account Management**

- Establish strict KPIs for responsiveness.  
- Quarterly executive check-ins.  
- Standardize communication protocols and partnership frameworks.  
- Expected impact: Higher renewals and NPS.

### **Standardize Project Execution & Governance**

- Apply uniform project management methodologies.  
- Improve time and cost predictions.  
- More proactive risk and change control.  
- Expected impact: Reduced friction and improved revenue growth.

### **Next Steps**

- Build dashboards with the 5 factors + KPIs.  
- Update the analysis quarterly with new data.  
- Design specific initiatives for each factor.

### **Project Structure**

```
case-01-factor-analysis/
│
├── data/
│   ├── customer_satisfaction_data_dictionary.md
│   └── customer_satisfaction_data.csv
│
├── notebooks/
│   ├── factor_analysis.ipynb
│   └── factor_analysis.pdf
│
├── reports/
│   └── executive_summary.pdf
│
├── visualizations/
│   ├── correlation_matrix.png
│   ├── factor_loadings_heatmap.png
│   ├── factors_impact_heatmap.png
│   ├── importance_nps_score.png
│   ├── importance_overall_satisfaction.png
│   ├── importance_predictive_power.png
│   └── ...
│
└── README.md
```

### **How to Run**

```
git clone <repository-url>
cd case-01-factor-analysis/notebooks
jupyter notebook notebooks/factor_analysis.ipynb
```

### **Additional Documentation**

- Executive report  
- Executive video presentation
