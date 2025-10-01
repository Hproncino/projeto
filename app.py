import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

st.title("Predição de Vendas com Regressão Linear")
st.divider()

uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploaded_file is not None:
    df = pd.read.csv(uploaded_file)

    st.subheader("Visualização dos Dados")
    st.dataframe(df.head())