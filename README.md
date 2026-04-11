# FísicaLab 🔬

> *"Automatizando o que todo estudante de Física faz na mão."*

---

## O problema

Qualquer estudante de Física Experimental conhece bem essa rotina:

1. Mede os dados no laboratório
2. Abre o caderno e calcula as **derivadas parciais** à mão
3. Aplica a **fórmula de propagação de incertezas** — variável por variável
4. Formata tudo em um **relatório** seguindo as normas do professor

Isso consome horas por experimento. E se errar um sinal na derivada, o resultado inteiro vai junto.

**O FísicaLab resolve isso.**

---

## A solução

Uma biblioteca Python que automatiza todo esse processo. Você fornece os dados em um Excel e a expressão do experimento — o resto é automático.

```python
from fisica_lab import executar

executar(
    caminho_excel = "dados.xlsx",
    expressao     = "deltaL / (Lo * deltaT)",
    variaveis     = ["deltaL", "Lo", "deltaT"],
    titulo        = "Dilatação Térmica Linear",
    valor_teorico = 12e-6,
)
```

**O que acontece por baixo:**

```
✔ Lê os dados do Excel automaticamente
✔ Calcula as derivadas parciais simbolicamente (SymPy)
✔ Propaga as incertezas pela fórmula σ_f = √Σ(∂f/∂xi · σxi)²
✔ Calcula o erro percentual em relação ao valor teórico
✔ Gera o relatório Word formatado e pronto para entregar
```

**Output no terminal:**
```
─────────────────────────────────────────────
  Dilatação Térmica Linear
─────────────────────────────────────────────
  Resultado:  0.000527273
  Incerteza:  2.6e-06
  Final:      (0.0005273 ± 2.6e-06)
  Erro %:     4.32%
  Relatório:  relatorio.docx
─────────────────────────────────────────────
```

O que antes levava horas vira segundos. Exemplo abaixo do arquivo gerado em Word:

---

![c29e0a4c-3b67-4bed-9225-7677404f74b4](https://github.com/user-attachments/assets/6da63787-cb1b-4bb3-879c-69beeea070b5)


## Por que isso importa

O cálculo de incertezas é obrigatório em qualquer laboratório sério — não só na universidade, mas em empresas de metrologia, laboratórios industriais e institutos de pesquisa como INMETRO e FIOCRUZ. A maioria ainda faz isso manualmente em planilhas sujeitas a erro humano.

Automatizar esse processo elimina erros de cálculo, padroniza os relatórios e libera o tempo do pesquisador para o que realmente importa: **analisar os resultados**.

---

## Como usar

**1. Instale as dependências**
```bash
git clone https://github.com/hugodevelopment/fisica_lab.git
pip install -r requirements.txt
```

**2. Prepare o Excel com seus dados**

| variavel         | valor    |
|------------------|----------|
| deltaL           | 0.006    |
| Lo               | 0.500    |
| deltaT           | 10.0     |
| incertezadeltaL  | 0.0005   |
| incertezadeltaLo | 0.001    |
| incertezadeltaT  | 0.5      |

> Incertezas são identificadas automaticamente pelo prefixo `incerteza` no nome da variável.

**3. Crie um `main.py` fora da pasta e rode**
```bash
python main.py
```

---

## Funcionalidades

**Pipeline principal**
Dado bruto → derivadas parciais → propagação de incertezas → relatório Word.

**Estatística descritiva**
Para análise de medições repetidas: média, mediana, moda, desvio padrão, incerteza da média, coeficiente de variação, correlação de Pearson e regressão linear.

```python
from fisica_lab import resumo, correlacao

medicoes = [11.8e-6, 12.1e-6, 11.9e-6, 12.3e-6, 12.0e-6]
stats = resumo(medicoes)
print(f"Média:     {stats['media']:.4g}")
print(f"Incerteza: {stats['incerteza_media']:.2g}")
```

---

## Estrutura do projeto

```
fisica_lab/
├── pipeline.py              # Orquestrador — une tudo em uma chamada
├── parser/
│   └── excel_reader.py      # Lê o Excel e converte em símbolos
├── calculus/
│   ├── derivatives.py       # Derivadas parciais simbólicas (SymPy)
│   ├── uncertainty.py       # Propagação de incertezas
│   └── statistics.py        # Estatística descritiva
└── report/
    └── word_generator.py    # Gera o relatório Word formatado
```

Cada módulo tem uma responsabilidade única. Isso facilita adicionar novos tipos de experimento, novos formatos de relatório ou uma interface web sem modificar o núcleo da biblioteca.

---

## Roadmap

- [x] Pipeline de derivadas e propagação de incertezas
- [x] Módulo de estatística descritiva
- [ ] Interface Streamlit — app web para uso sem código
- [ ] Biblioteca de experimentos pré-configurados
- [ ] Geração automática de gráficos

---

🛠️ Tecnologias
- Python
- Pandas
- Numpy
- Sympy
- OpenPyXL / Docx

## Autor

**Hugo Alves da Costa**
Graduando em Física — UERJ | Analista de Dados

[LinkedIn](https://www.linkedin.com/in/hugo-costa22) • [GitHub](https://github.com/hugodevelopment)
