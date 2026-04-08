"""calculus/statistics.py — Estatística descritiva para dados experimentais."""

import numpy as np
from scipy import stats


def resumo(dados: list) -> dict:
    """
    Média, mediana, moda, desvio padrão, incerteza da média e correlação.

    Retorna dict com todas as métricas prontas para exibição.
    """
    arr = np.array(dados, dtype=float)
    n   = len(arr)
    med = np.mean(arr)
    dp  = np.std(arr, ddof=1)
    moda_res = stats.mode(arr, keepdims=True)

    return {
        "n":               n,
        "media":           med,
        "mediana":         float(np.median(arr)),
        "moda":            float(moda_res.mode[0]),
        "desvio_padrao":   dp,
        "incerteza_media": dp / np.sqrt(n),        # incerteza tipo A
        "coef_variacao":   dp / med * 100 if med else None,
        "minimo":          float(np.min(arr)),
        "maximo":          float(np.max(arr)),
    }


def correlacao(x: list, y: list) -> dict:
    """Correlação de Pearson entre duas variáveis."""
    r, p = stats.pearsonr(np.array(x, dtype=float), np.array(y, dtype=float))
    return {"r": r, "r2": r**2, "p_valor": p, "significativo": p < 0.05}


def regressao(x: list, y: list) -> dict:
    """Regressão linear y = a + b·x."""
    res = stats.linregress(np.array(x, dtype=float), np.array(y, dtype=float))
    return {
        "inclinacao":  res.slope,
        "intercepto":  res.intercept,
        "r2":          res.rvalue ** 2,
        "equacao":     f"y = {res.slope:.4g}·x + {res.intercept:.4g}",
        "y_predito":   (res.slope * np.array(x) + res.intercept).tolist(),
    }
