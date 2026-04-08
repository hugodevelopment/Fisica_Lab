"""exemplo.py — Uso completo da biblioteca FísicaLab."""

import pandas as pd
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Cria Excel de exemplo
pd.DataFrame({
    "variavel": ["deltaL", "Lo", "deltaT",
                 "incertezadeltaL", "incertezadeltaLo", "incertezadeltaT",
                 "alpha_teorico"],
    "valor":    [0.006, 0.500, 10.0,
                 0.0005, 0.001, 0.5,
                 12e-6]
}).to_excel("dados.xlsx", index=False)

# Executa o pipeline
from fisica_lab import executar

resultado = executar(
    caminho_excel = "dados.xlsx",
    expressao     = "deltaL / (Lo * deltaT)",
    variaveis     = ["deltaL", "Lo", "deltaT"],
    titulo        = "Dilatação Térmica Linear",
    valor_teorico = 12e-6,
    caminho_saida = "relatorio.docx",
)

# Exemplo de estatística descritiva
from fisica_lab import resumo, correlacao

medicoes = [11.8e-6, 12.1e-6, 11.9e-6, 12.3e-6, 12.0e-6]
stats = resumo(medicoes)
print(f"  Média:    {stats['media']:.4g}")
print(f"  Desvio:   {stats['desvio_padrao']:.2g}")
print(f"  Incerteza:{stats['incerteza_media']:.2g}")
