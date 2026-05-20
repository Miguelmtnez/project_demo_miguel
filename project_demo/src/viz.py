"""
Funciones de visualización para el EDA.
"""

import matplotlib.pyplot as plt
import seaborn as sns


def plot_histogram(df, column):
    """Histograma de una variable numérica."""
    
    plt.figure(figsize=(6,4))
    
    sns.histplot(df[column], kde=True)
    
    plt.title(f"Histograma de {column}")
    plt.xlabel(column)
    plt.ylabel("Frecuencia")
    
    plt.show()


def plot_boxplot(df, column):
    """Boxplot de una variable numérica."""
    
    plt.figure(figsize=(6,4))
    
    sns.boxplot(x=df[column])
    
    plt.title(f"Boxplot de {column}")
    
    plt.show()


def plot_bar(df, column):
    """Gráfico de barras para variables categóricas."""
    
    plt.figure(figsize=(6,4))
    
    df[column].value_counts().plot(kind="bar")
    
    plt.title(f"Frecuencia de {column}")
    plt.xlabel(column)
    plt.ylabel("Frecuencia")
    
    plt.show()


def plot_scatter(df, x_col, y_col):
    """Scatterplot entre dos variables numéricas."""
    
    plt.figure(figsize=(6,4))
    
    plt.scatter(df[x_col], df[y_col])
    
    plt.title(f"{x_col} vs {y_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    
    plt.show()


def plot_heatmap(df):
    """Heatmap de correlaciones."""
    
    corr = df.select_dtypes(include="number").corr()

    plt.figure(figsize=(12,8))

    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Matriz de correlación")

    plt.show()