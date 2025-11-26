# LendSmart Credit Risk Analysis

## Descripción del Proyecto

Este proyecto desarrolla un **sistema de análisis de riesgo crediticio** para LendSmart, una institución financiera que busca optimizar sus decisiones de aprobación de préstamos. Utilizando técnicas de **Análisis Discriminante**, el proyecto clasifica a los solicitantes de crédito según su probabilidad de incumplimiento (default).

## Objetivo

Construir modelos predictivos capaces de:

- Distinguir entre clientes confiables y no confiables
- Identificar las variables más relevantes para predecir el riesgo de incumplimiento
- Comparar el rendimiento de diferentes técnicas de clasificación (LDA vs QDA)

## Metodología

### Técnicas Implementadas

| Modelo                                    | Descripción                                                                |
| ----------------------------------------- | -------------------------------------------------------------------------- |
| **LDA** (Linear Discriminant Analysis)    | Asume covarianza igual entre clases, genera fronteras de decisión lineales |
| **QDA** (Quadratic Discriminant Analysis) | Permite covarianzas diferentes por clase, genera fronteras cuadráticas     |

### Flujo del Análisis

1. **Carga y exploración de datos** - Inspección inicial del dataset
2. **Análisis Exploratorio (EDA)** - Correlaciones y distribuciones
3. **Preprocesamiento** - División train/test y estandarización
4. **Pruebas de supuestos** - Normalidad multivariada y homogeneidad de covarianzas
5. **Modelado LDA** - Entrenamiento e interpretación de coeficientes
6. **Modelado QDA** - Entrenamiento con covarianzas flexibles
7. **Evaluación** - Métricas, matrices de confusión y curvas ROC
8. **Conclusiones** - Selección del modelo óptimo

## Variables del Dataset

El archivo `credit_risk_data-1.csv` contiene 2,500 registros con las siguientes variables:

### Variables Predictoras

| Variable                | Descripción                                       |
| ----------------------- | ------------------------------------------------- |
| `loan_amount`           | Monto del préstamo solicitado ($5,000 - $500,000) |
| `annual_income`         | Ingreso anual del solicitante                     |
| `credit_score`          | Puntuación crediticia                             |
| `payment_history_score` | Historial de pagos previos                        |
| `debt_to_income_ratio`  | Relación deuda/ingreso                            |
| `job_stability_score`   | Estabilidad laboral                               |
| `credit_utilization`    | Porcentaje de uso del crédito disponible          |
| `employment_years`      | Años de empleo                                    |
| `asset_value`           | Valor de activos                                  |
| `savings_ratio`         | Ratio de ahorro                                   |
| `age`                   | Edad del solicitante                              |
| `residential_stability` | Estabilidad residencial                           |

### Variable Objetivo

- `loan_status`: Estado del préstamo (0 = Cumplimiento, 1 = Incumplimiento)

## Principales Hallazgos

### Top 5 Predictores de Riesgo (según coeficientes LDA)

| Variable              | Coeficiente | Interpretación                       |
| --------------------- | ----------- | ------------------------------------ |
| Payment History Score | -15.54      | Historial pobre aumenta riesgo       |
| Job Stability Score   | -13.07      | Inestabilidad laboral aumenta riesgo |
| Credit Utilization    | +11.64      | Alta utilización indica riesgo       |
| Debt-to-Income Ratio  | +4.51       | Alta deuda relativa aumenta riesgo   |
| Credit Score          | -3.94       | Score bajo correlaciona con default  |

### Resultados de los Modelos

Ambos modelos alcanzaron **rendimiento perfecto** en el conjunto de prueba:

- **AUC Score LDA**: 1.0000
- **AUC Score QDA**: 1.0000
- Precisión, Recall y F1-Score: 100%

### Recomendación Final

Se recomienda **LDA** por su simplicidad e interpretabilidad, dado que ambos modelos obtuvieron resultados equivalentes.

## Estructura del Proyecto

```
case-02-discriminant-analysis/
│
├── data/
│   └── credit_risk_data-1.csv
│
├── notebooks/
│   ├── LendSmart_Analysis.ipynb
│   └── LendSmart_Analysis.pdf
│
├── reports/
│   ├── business_report.pdf
│   └── LendSmart credit risk analysis.pdf
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

## Cómo ejecutar

```
git clone <repository-url>
cd case-02-discriminant-analysis/notebooks
jupyter notebook notebooks/LendSmart_Analysis.ipynb
```

## Documentación adicional
- Reporte ejecutivo
- Presentación ejecutiva

