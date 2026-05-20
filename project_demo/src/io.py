"""
Funciones de entrada/salida de datos.
"""
import pandas as pd
from pathlib import Path
from src.config import RAW_PATH, OUT_PATH


def load_csv(path: str | Path = RAW_PATH) -> pd.DataFrame:
    """Carga el CSV raw y devuelve un DataFrame."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {path}")
    df = pd.read_csv(path)
    print(f"[io] Cargadas {len(df):,} filas y {df.shape[1]} columnas desde '{path.name}'")
    return df


def save_csv(df: pd.DataFrame, path: str | Path = OUT_PATH) -> None:
    """Guarda el DataFrame limpio en la carpeta processed/."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    print(f"[io] Dataset guardado en '{path}' ({len(df):,} filas)")