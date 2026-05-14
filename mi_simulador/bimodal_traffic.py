import numpy as np

def _p_star(x: np.ndarray, mu1: float, sigma1: float, mu2: float, sigma2: float) -> np.ndarray:
    """
    Calcula la función de densidad no normalizada objetivo p*(x).
    Representa un tráfico bimodal: un pico principal en horas de oficina
    y un pico menor nocturno.
    """
    term1 = np.exp(-((x - mu1)**2) / (2 * sigma1**2))
    term2 = 0.5 * np.exp(-((x - mu2)**2) / (2 * sigma2**2))
    return term1 + term2

def rejection_sampling_trafico(
    n_simulaciones: int = 100000,
    mu1: float = 12.0, sigma1: float = 2.0,  # Pico 1: Ej. 12:00 PM
    mu2: float = 22.0, sigma2: float = 1.5,  # Pico 2: Ej. 10:00 PM
    low: float = 0.0, high: float = 24.0,    # Dominio de horas (0 a 24)
    semilla: int = None
) -> tuple[np.ndarray, float]:
    """
    Genera tráfico sintético bimodal usando el algoritmo de Rejection Sampling.

    Utilizamos una distribución Uniforme como distribución envolvente q(x).
    
    Parameters
    ----------
    n_simulaciones : int, opcional
        Número de muestras aceptadas requeridas.
    mu1, sigma1 : float
        Media y desviación estándar del primer pico (tráfico diurno).
    mu2, sigma2 : float
        Media y desviación estándar del segundo pico (sincronización nocturna).
    low, high : float
        Dominio de la distribución envolvente Uniforme q(x).
    semilla : int, opcional
        Semilla de reproducibilidad.

    Returns
    -------
    tuple[np.ndarray, float]
        Un arreglo con las muestras aceptadas y la tasa de aceptación empírica.
    """
    if semilla is not None:
        np.random.seed(semilla)
        
    muestras_aceptadas = []
    total_generadas = 0
    
    # Análisis de la constante empírica 'k' para la envolvente q(x):
    # La función q(x) para una Uniforme es 1 / (high - low).
    # El valor máximo teórico de p*(x) ocurre en la media del pico más alto (mu1), y es aproximadamente 1.0.
    # Por lo tanto, k * q(x) >= max(p*(x)) implica que:
    # k * (1 / (high - low)) >= 1.0  =>  k = high - low
    # Esto equivale a probar si una variable U(0, k_max) <= p*(x), donde k_max = 1.0.
    k_max = 1.05  # Le damos un ligero margen del 5% superior
    
    tamaño_lote = int(n_simulaciones * 2.5)
    
    while len(muestras_aceptadas) < n_simulaciones:
        x_prop = np.random.uniform(low, high, size=tamaño_lote)
        
        y_prop = np.random.uniform(0, k_max, size=tamaño_lote)
        
        p_val = _p_star(x_prop, mu1, sigma1, mu2, sigma2)
        
        aceptadas = x_prop[y_prop <= p_val]
        
        muestras_aceptadas.extend(aceptadas)
        total_generadas += tamaño_lote
        
    muestras_finales = np.array(muestras_aceptadas[:n_simulaciones])
    
    tasa_aceptacion = n_simulaciones / total_generadas
    
    return muestras_finales, tasa_aceptacion