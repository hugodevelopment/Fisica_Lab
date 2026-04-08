"""calculus/uncertainty.py — Propagação de incertezas e erro percentual."""

import numpy as np


def propagar(derivadas: dict, incertezas: dict) -> float:
    """
    σ_f = sqrt( Σ (∂f/∂xi · σ_xi)² )

    Busca automaticamente a incerteza de cada variável
    pelo padrão 'incerteza' + nome_da_variavel.
    """
    soma = 0.0
    for var, info in derivadas.items():
        nome = str(var)
        # procura incertezadeltaL, incerteza_deltaL, etc.
        sigma = next(
            (v for k, v in incertezas.items() if nome.lower() in str(k).lower()),
            None
        )
        if sigma is not None:
            soma += (info["numerica"] * sigma) ** 2
    return float(np.sqrt(soma))


def erro_percentual(experimental: float, teorico: float) -> float:
    """Erro percentual entre valor experimental e teórico."""
    return abs((experimental - teorico) / teorico) * 100
