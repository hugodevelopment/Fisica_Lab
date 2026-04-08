"""
pipeline.py — Orquestrador do FísicaLab.

Une todos os módulos em uma única chamada.
"""

from .parser.excel_reader import ler_dados, separar
from .calculus.derivatives import calcular, avaliar
from .calculus.uncertainty  import propagar, erro_percentual
from .report.word_generator import gerar


def executar(
    caminho_excel:  str,
    expressao:      str,
    variaveis:      list[str],
    titulo:         str   = "Relatório de Física Experimental",
    valor_teorico:  float = None,
    caminho_saida:  str   = "relatorio.docx",
    verbose:        bool  = True,
) -> dict:
    """
    Pipeline completo: Excel → cálculo → relatório Word.

    Parâmetros
    ----------
    caminho_excel : caminho do arquivo .xlsx
    expressao     : ex: "deltaL / (Lo * deltaT)"
    variaveis     : ex: ["deltaL", "Lo", "deltaT"]
    titulo        : título do experimento
    valor_teorico : (opcional) para calcular erro percentual
    caminho_saida : caminho do .docx gerado
    verbose       : imprime resultados no terminal

    Retorna dict com todos os resultados.
    """

    # 1. Ler dados
    dados = ler_dados(caminho_excel)
    medicoes, incertezas = separar(dados)

    # 2. Derivadas parciais
    derivadas = calcular(expressao, variaveis, dados)

    # 3. Valor numérico
    valor = avaliar(expressao, variaveis, dados)

    # 4. Propagação de incertezas
    incerteza = propagar(derivadas, incertezas)

    # 5. Erro percentual (opcional)
    erro_pct = erro_percentual(valor, valor_teorico) if valor_teorico else None

    # 6. Relatório Word
    caminho_doc = gerar(
        titulo        = titulo,
        expressao     = expressao,
        dados         = dados,
        derivadas     = derivadas,
        incerteza     = incerteza,
        valor         = valor,
        valor_teorico = valor_teorico,
        caminho       = caminho_saida,
    )

    if verbose:
        print(f"\n{'─'*45}")
        print(f"  {titulo}")
        print(f"{'─'*45}")
        print(f"  Resultado:  {valor:.6g}")
        print(f"  Incerteza:  {incerteza:.2g}")
        print(f"  Final:      ({valor:.4g} ± {incerteza:.2g})")
        if erro_pct is not None:
            print(f"  Erro %:     {erro_pct:.2f}%")
        print(f"  Relatório:  {caminho_doc}")
        print(f"{'─'*45}\n")

    return {
        "dados":       dados,
        "derivadas":   derivadas,
        "valor":       valor,
        "incerteza":   incerteza,
        "erro_pct":    erro_pct,
        "relatorio":   caminho_doc,
    }
