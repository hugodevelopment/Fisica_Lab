"""parser/excel_reader.py — Lê o Excel e retorna dicionário simbólico."""

import pandas as pd
import sympy as sp


def ler_dados(caminho: str) -> dict:
    """
    Lê Excel com colunas 'variavel' e 'valor'.
    Retorna dict {Symbol: float}.

    Exemplo de Excel:
        | variavel        | valor  |
        | deltaL          | 0.006  |
        | incertezadeltaL | 0.0005 |
    """
    df = pd.read_excel(caminho)
    df.columns = df.columns.str.lower()
    return {sp.Symbol(str(row.variavel)): float(row.valor) for _, row in df.iterrows()}


def separar(dados: dict) -> tuple[dict, dict]:
    """Separa medições de incertezas pelo prefixo 'incerteza'."""
    medicoes  = {k: v for k, v in dados.items() if "incerteza" not in str(k)}
    incertezas = {k: v for k, v in dados.items() if "incerteza"     in str(k)}
    return medicoes, incertezas
