"""
Utilidades y validaciones del dataset.
"""
import pandas as pd
from src.config import EXPECTED_COLUMNS, NUMERIC_COLS


def assert_columns(df: pd.DataFrame, required: list = EXPECTED_COLUMNS) -> None:
    """Lanza AssertionError si faltan columnas esperadas."""
    missing = set(required) - set(df.columns)
    assert not missing, f"Columnas faltantes: {missing}"
    print(f"[utils] ✓ Todas las {len(required)} columnas esperadas están presentes.")


def summary(df: pd.DataFrame) -> pd.DataFrame:
    """Devuelve un resumen de nulos, tipos y estadísticas básicas."""
    info = pd.DataFrame({
        "dtype":    df.dtypes,
        "nulls":    df.isnull().sum(),
        "null_%":   (df.isnull().mean() * 100).round(2),
        "n_unique": df.nunique(),
    })
    return info


def check_ranges(df: pd.DataFrame) -> None:
    """Imprime alertas si alguna columna numérica tiene valores fuera de rango lógico."""
    rules = {
        "gaming_hours":   (0, 24),
        "study_hours":    (0, 24),
        "sleep_hours":    (0, 24),
        "attendance":     (0, 100),
        "grades":         (0, 100),
        "addiction_score":(0, 30),
    }
    for col, (lo, hi) in rules.items():
        if col not in df.columns:
            continue
        out = df[(df[col] < lo) | (df[col] > hi)]
        if len(out):
            print(f"[utils] ⚠ '{col}': {len(out)} valores fuera de [{lo}, {hi}]")
        else:
            print(f"[utils] ✓ '{col}': todos los valores en [{lo}, {hi}]")