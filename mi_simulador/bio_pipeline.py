import numpy as np
import scipy.stats as stats

def importance_sampling_bio(
    limite_horas: float,
    mu_f: float = 2.0,
    sigma_f: float = 0.8,
    escala_g: float = 2.0,
    n_simulaciones: int = 100000,
    semilla: int = None
) -> tuple[float, float]:
    """
    Estima la probabilidad de fallo en un pipeline bioinformático usando Importance Sampling.
    
    Parameters
    ----------
    limite_horas : float
        Límite máximo de horas asignado en el clúster antes de la cancelación.
    mu_f : float, opcional
        Parámetro de media subyacente para la distribución Lognormal (distribución objetivo).
    sigma_f : float, opcional
        Parámetro de forma para la distribución Lognormal.
    escala_g : float, opcional
        Parámetro de escala para la distribución Exponencial desplazada (distribución propuesta).
    n_simulaciones : int, opcional
        Número de muestras a generar.
    semilla : int, opcional
        Semilla para asegurar la reproducibilidad.

    Returns
    -------
    tuple[float, float]
        Una tupla con (probabilidad_estimada, varianza_del_estimador).
    """
    if semilla is not None:
        np.random.seed(semilla)
        
    f_dist = stats.lognorm(s=sigma_f, scale=np.exp(mu_f))
    
    g_dist = stats.expon(loc=limite_horas, scale=escala_g)
    
    muestras_g = g_dist.rvs(size=n_simulaciones)
    
    pesos = f_dist.pdf(muestras_g) / g_dist.pdf(muestras_g)
    
    prob_estimada = np.mean(pesos)
    varianza_estimador = np.var(pesos, ddof=1) / n_simulaciones
    
    return prob_estimada, varianza_estimador

def montecarlo_estandar_bio(
    limite_horas: float,
    mu_f: float = 2.0,
    sigma_f: float = 0.8,
    n_simulaciones: int = 100000,
    semilla: int = None
) -> tuple[float, float]:
    """
    Estima la probabilidad de fallo usando Monte Carlo estándar para fines de comparación.
    """
    if semilla is not None:
        np.random.seed(semilla)
        
    f_dist = stats.lognorm(s=sigma_f, scale=np.exp(mu_f))
    muestras = f_dist.rvs(size=n_simulaciones)
    
    excesos = (muestras > limite_horas).astype(float)
    
    prob_estimada = np.mean(excesos)
    varianza_estimador = np.var(excesos, ddof=1) / n_simulaciones
    
    return prob_estimada, varianza_estimador