# Projeto Integrador - Predição de Vendas

Projeto do 6º semestre de Ciência da Computação (Uninove) com foco em predição de vendas usando séries temporais e Machine Learning.

O fluxo principal está no notebook `recursive.ipynb`, onde os dados são preparados, transformados em formato supervisionado e usados para treinar um modelo de Regressão Linear para previsão de vendas mensais.

## Objetivo

Estimar vendas futuras a partir de dados históricos de vendas, com:

- agregação temporal mensal
- transformação por diferenciação para reduzir não estacionaridade
- criação de variáveis de atraso (lags) de 12 meses
- treino, validação e avaliação do modelo
- visualização dos resultados reais vs previstos

## Stack

- Python 3.13+
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- TensorFlow (dependência já declarada)
- Jupyter Notebook
- Poetry (gerenciamento de dependências)

## Estrutura do Projeto

```text
.
├── csv/
│   ├── Ecommerce_Sales_Prediction_Dataset.csv
│   ├── train.csv
│   ├── Predict.csv
│   └── predict_df.csv
├── src/
│   └── projeto/
│       └── __init__.py
├── tests/
│   └── __init__.py
├── recursive.ipynb
├── pyproject.toml
└── README.md
```

## Dados

Arquivos disponíveis em `csv/`:

- `train.csv`: base principal usada no notebook (`date`, `store`, `item`, `sales`)
- `Predict.csv`: base com `date` e `sales`
- `predict_df.csv`: saída com previsões (`date`, `Linear Prediction`)
- `Ecommerce_Sales_Prediction_Dataset.csv`: base complementar de e-commerce

## Métricas de Avaliação

No notebook são calculadas:

- RMSE (raiz do erro quadrático médio)
- MAE (erro absoluto médio)
- R² (coeficiente de determinação)

## Observações

- O núcleo do projeto está no notebook, com foco acadêmico e exploratório.
- A pasta `src/` ainda está preparada para futura modularização do pipeline em scripts reutilizáveis.
- O diretório `tests/` está criado como base para evolução de testes automatizados.

## Próximos Passos (Sugestões)

- separar o pipeline em módulos Python dentro de `src/projeto/`
- criar script de treino e script de inferência
- adicionar testes unitários para transformação de dados e métricas
- incluir baseline comparativa com outros modelos (ex.: XGBoost, LSTM)
- versionar artefatos de modelo e resultados
