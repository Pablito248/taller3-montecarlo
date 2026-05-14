import numpy as np

def simular_latencia_rag(
    mu_emb: float, sigma_emb: float,
    low_db: float, high_db: float,
    mu_llm: float, sigma_llm: float,
    n_simulaciones: int = 100000,
    semilla: int = None
) -> np.ndarray:
    """
    Simula el tiempo total de respuesta de un sistema RAG (Caso 1).
    
    Cumple con el modelado de tres etapas independientes[cite: 8]:
    1. Generación de embeddings: Distribución Normal[cite: 8].
    2. Búsqueda vectorial: Distribución Uniforme[cite: 9].
    3. Inferencia del LLM: Distribución Lognormal[cite: 10].

    Parameters
    ----------
    mu_emb : float
        Media del tiempo de generación de embeddings.
    sigma_emb : float
        Desviación estándar (embeddings).
    low_db, high_db : float
        Límites de la búsqueda en base de datos vectorial.
    mu_llm, sigma_llm : float
        Parámetros de la distribución lognormal para el LLM.
    n_simulaciones : int
        Número de consultas (por defecto 100,000 según requerimiento)[cite: 11].
    semilla : int, opcional
        Garantiza consistencia y reproducibilidad[cite: 28].

    Returns
    -------
    np.ndarray
        Arreglo con los tiempos totales de latencia.
    """
    if semilla is not None:
        np.random.seed(semilla)
        
    t_emb = np.random.normal(loc=mu_emb, scale=sigma_emb, size=n_simulaciones)
    t_db = np.random.uniform(low=low_db, high=high_db, size=n_simulaciones)
    t_llm = np.random.lognormal(mean=mu_llm, sigma=sigma_llm, size=n_simulaciones)
    
    t_emb = np.maximum(0, t_emb)
    
    return t_emb + t_db + t_llm