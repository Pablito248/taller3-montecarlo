# Mi Simulador - Taller 3: Simulación Montecarlo

Esta es una librería de Python profesional orientada a la simulación estadística, aplicando los fundamentos del Método de Montecarlo y técnicas de muestreo avanzado para la evaluación de riesgos en sistemas RAG, pipelines bioinformáticos y tráfico de red.

## 📦 Casos de Uso Implementados

Esta librería contiene tres módulos principales desarrollados para el taller:

1. **Caso 1: Análisis Estocástico de Latencia en Arquitecturas RAG** (`rag_latency.py`)
   - Simulación de tiempos de respuesta combinando distribuciones Normal, Uniforme y Lognormal para evaluar acuerdos de nivel de servicio (SLA).
2. **Caso 2: Estimación de Cuellos de Botella en Pipelines Bioinformáticos** (`bio_pipeline.py`)
   - Implementación de **Importance Sampling** para la estimación eficiente de eventos raros (fallos por tiempo límite) en distribuciones de cola pesada.
3. **Caso 3: Generación de Tráfico Sintético Bimodal** (`bimodal_traffic.py`)
   - Uso del algoritmo de **Rejection Sampling** con distribuciones envolventes para modelar picos de tráfico en APIs.

## ⚙️ Instalación

Para instalar esta librería en modo desarrollo (editable) dentro de un entorno virtual:

```bash
pip install -e .