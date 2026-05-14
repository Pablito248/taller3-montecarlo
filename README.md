# Mi Simulador - Taller 3: Simulación Montecarlo

Esta es una librería de Python orientada a la simulación estadística, aplicando los fundamentos del Método de Montecarlo y técnicas de muestreo avanzado para la evaluación de riesgos e infraestructura.

## 📦 Casos de Uso Implementados

Esta librería contiene tres módulos principales para diferentes escenarios de simulación:

1. **Caso 1: Análisis Estocástico de Latencia en Arquitecturas RAG** (`rag_latency.py`)
   - Utiliza el Método de Monte Carlo Estándar para sumar distribuciones Normal, Uniforme y Lognormal.
2. **Caso 2: Estimación de Cuellos de Botella en Pipelines Bioinformáticos** (`bio_pipeline.py`)
   - Implementa *Importance Sampling* para estimar eventos raros de falla en infraestructuras de cola pesada.
3. **Caso 3: Generación de Tráfico Sintético Bimodal** (`bimodal_traffic.py`)
   - Utiliza el algoritmo de *Rejection Sampling* para generar muestras aleatorias a partir de una distribución envolvente uniforme.

## ⚙️ Instalación

Para instalar esta librería en modo editable localmente, asegúrate de tener un entorno virtual activado y ejecuta el siguiente comando en la raíz del proyecto:

```bash
pip install -e .

🛠️ Requisitos
Python 3.8+

NumPy >= 1.20.0

SciPy >= 1.7.0

Matplotlib >= 3.4.0

👨‍💻 Autor
Desarrollado para el Taller 3 de Modelos y Simulación.

Juan Pablo Acevedo - juan.acevedo949@pascualbravo.edu.co