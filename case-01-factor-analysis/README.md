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

## ***Datos***
• Descripción del dataset
• Variables clave
• Link al diccionario de datos
## ***Hallazgos principales***
• 3-5 hallazgos clave en bullet points
• Visualización destacada (imagen embebida)
• Métricas de performance del modelo
## ***Recomendaciones de negocio***
• 3 recomendaciones accionables
• Impacto esperado
• Próximos pasos