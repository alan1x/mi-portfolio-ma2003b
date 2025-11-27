## ***Contexto del negocio***

### **Descripción del cliente y problema**

TechnoServe Solutions recolectó datos de 300 clientes a través de 25 indicadores de satisfacción con el objetivo de entender:

- Qué impulsa la satisfacción general.
- Qué factores predicen mejor la renovación, el NPS, el crecimiento y los referidos.
- Dónde priorizar inversiones para mejorar la experiencia del cliente.

### **Importancia estratégica del análisis**

El análisis es clave porque:

- Reduce 25 indicadores en 5 factores estratégicos (simplifica la toma de decisiones).
- Permite dirigir inversiones a los drivers estadísticamente más influyentes.
- Conecta métricas de satisfacción con impacto financiero directo (renovación y crecimiento de ingresos).
- Genera un mapa claro de prioridades para operaciones, ventas y producto.

## ***Metodología***

Método multivariado aplicado. Se emplearon:

### **Análisis Factorial**

- Normalización: StandardScaler
- Validación:
    - KMO = 0.94 (excelente adecuación)
    - Bartlett p < 0.001 (matriz apta)
- Extracción inicial con sklearn y rotación Varimax.
- Se retuvieron 5 factores, confirmados por scree plot.

### **Modelos de regresión OLS**

Se ejecutaron regresiones independientes usando los puntajes factoriales como predictores para:

- Overall Satisfaction
- NPS
- Renewal Likelihood
- Revenue Growth
- Referrals

### **Justificación de la elección**

- El EFA permite revelar patrones latentes y reducir dimensionalidad.
- La regresión permite entender el impacto cuantitativo de cada factor.
- Juntos, permiten:
    - Interpretabilidad del modelo.
    - Priorización de acciones basadas en impacto estadístico.

### **Herramientas y librerías utilizadas**

- Pandas → limpieza y manejo de datos
- NumPy → cálculos matriciales
- Scikit-Learn → estandarización y extracción de componentes
- FactorAnalyzer → KMO, Bartlett, rotación Varimax
- Statsmodels → regresiones OLS
- Matplotlib / Seaborn → gráficos del análisis (heatmaps, scree plot)

## ***Datos***

### **Descripción del dataset**

- 300 observaciones
- 25 variables que miden la percepción del cliente sobre:
    - Experiencia técnica
    - Gestión de cuenta
    - Ejecución de proyectos
    - Valor comercial
    - Soporte y documentación

### **Procesamiento realizado (del notebook):**

- Imputación por media
- Estandarización con StandardScaler
- Cálculo de:
    - Matriz de correlación
    - KMO
    - Bartlett
    - Scree plot
    - Cargas rotadas
    - Puntajes factoriales

### **Variables clave**

*Cargas ≥ 0.70*

- innovation_solutions — 0.72
- problem_solving — 0.71
- system_integration — 0.71
- technical_documentation — 0.70

*Cargas entre 0.69 y 0.65*

- technical_expertise — 0.69
- project_management — 0.65
- trust_reliability — 0.64
- quality_deliverables — 0.64
- timeline_adherence — 0.64
- executive_access — 0.63
- long_term_partnership — 0.63

*Cargas entre 0.62 y 0.60*

- change_management — 0.62
- budget_control — 0.62
- account_manager_responsive — 0.61
- communication_clarity — 0.61
- billing_accuracy — 0.60

*Cargas entre 0.57 y 0.53*

- competitive_pricing — 0.57
- roi_demonstration — 0.57
- cost_transparency — 0.57
- value_for_money — 0.53

*Cargas menores a 0.50*

- training_quality — 0.46
- support_responsiveness — 0.44
- documentation_help — 0.42

### **Link al diccionario de datos**

Diccionario de datos: [Descargar diccionario de datos](../diccionario_datos.pdf)

## ***Hallazgos principales***
• 3-5 hallazgos clave en bullet points
• Visualización destacada (imagen embebida)
• Métricas de performance del modelo
## ***Recomendaciones de negocio***
• 3 recomendaciones accionables
• Impacto esperado
• Próximos pasos