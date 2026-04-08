"""calculus/derivatives.py — Derivadas parciais e avaliação numérica."""

import sympy as sp


def calcular(expressao_str: str, variaveis: list[str], dados: dict) -> dict:
    """
    Calcula derivadas parciais e avalia numericamente.

    Retorna dict:
        { Symbol: {"simbolica": Expr, "numerica": float} }
    """
    simbolos = {v: sp.Symbol(v) for v in variaveis}
    expr = sp.sympify(expressao_str, locals=simbolos)

    resultado = {}
    for nome, sym in simbolos.items():
        deriv = sp.diff(expr, sym)
        resultado[sym] = {
            "simbolica": deriv,
            "numerica":  float(deriv.subs(dados)),
        }
    return resultado


def avaliar(expressao_str: str, variaveis: list[str], dados: dict) -> float:
    """Avalia numericamente a expressão principal."""
    simbolos = {v: sp.Symbol(v) for v in variaveis}
    expr = sp.sympify(expressao_str, locals=simbolos)
    return float(expr.subs(dados))
