"""
Funciones de limpieza y transformación del dataset.
"""
import pandas as pd
from src.config import NUMERIC_COLS, CATEGORICAL_COLS


def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Elimina filas duplicadas."""
    before = len(df)
    df = df.drop_duplicates()
    removed = before - len(df)
    print(f"[cleaning] Duplicados eliminados: {removed}")
    return df


def fix_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    """Convierte columnas a sus tipos correctos."""
    # Numéricas → float/int
    for col in NUMERIC_COLS:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Categóricas → category con normalización de texto
    for col in CATEGORICAL_COLS:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.title().astype("category")

    print("[cleaning] Tipos de datos corregidos.")
    return df


def handle_nulls(df: pd.DataFrame) -> pd.DataFrame:
    """
    Imputa nulos:
    - Numéricas  → mediana
    - Categóricas → moda
    """
    null_before = df.isnull().sum().sum()

    for col in NUMERIC_COLS:
        if col in df.columns and df[col].isnull().any():
            median = df[col].median()
            df[col] = df[col].fillna(median)

    for col in CATEGORICAL_COLS:
        if col in df.columns and df[col].isnull().any():
            mode = df[col].mode()[0]
            df[col] = df[col].fillna(mode)

    null_after = df.isnull().sum().sum()
    print(f"[cleaning] Nulos antes: {null_before} → después: {null_after}")
    return df


def remove_outliers_iqr(df: pd.DataFrame, cols: list = None, factor: float = 3.0) -> pd.DataFrame:
    """
    Elimina outliers extremos (factor IQR = 3.0 para ser conservador).
    Solo se aplica a las columnas indicadas.
    """
    if cols is None:
        cols = ["gaming_hours", "study_hours", "grades", "addiction_score"]

    before = len(df)
    for col in cols:
        if col not in df.columns:
            continue
        Q1, Q3 = df[col].quantile(0.25), df[col].quantile(0.75)
        IQR = Q3 - Q1
        df = df[(df[col] >= Q1 - factor * IQR) & (df[col] <= Q3 + factor * IQR)]

    removed = before - len(df)
    print(f"[cleaning] Outliers eliminados (IQR ×{factor}): {removed} filas")
    return df.reset_index(drop=True)


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Pipeline completo de limpieza."""
    df = drop_duplicates(df)
    df = fix_dtypes(df)
    df = handle_nulls(df)
    df = remove_outliers_iqr(df)
    print(f"[cleaning] ✓ Dataset limpio: {len(df):,} filas")
    return df