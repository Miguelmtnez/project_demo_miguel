"""
Ingeniería de features para el dataset de videojuegos y rendimiento académico.
"""
import pandas as pd
import numpy as np


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """Crea todas las features nuevas y devuelve el DataFrame enriquecido."""
    df = df.copy()

    # --- Feature 1: gaming_study_ratio ---
    # Relación horas de gaming / horas de estudio.
    # Valores altos → el estudiante prioriza gaming sobre estudio.
    df["gaming_study_ratio"] = (
        df["gaming_hours"] / df["study_hours"].replace(0, np.nan)
    ).round(3)

    # --- Feature 2: wellness_score ---
    # Puntuación de bienestar combinando sueño normalizado + asistencia normalizada
    # − nivel de estrés codificado (Low=0, Medium=1, High=2).
    stress_map = {"Low": 0, "Medium": 1, "High": 2}
    stress_num = df["stress_level"].map(stress_map).fillna(1)

    sleep_norm      = df["sleep_hours"] / 9          # referencia: 9h óptimas
    attendance_norm = df["attendance"]  / 100

    df["wellness_score"] = (
        (sleep_norm + attendance_norm - stress_num / 2) / 2
    ).clip(0, 1).round(3)

    # --- Feature 3: addiction_category ---
    # Categorización del addiction_score en tres niveles.
    bins   = [-np.inf, 8, 16, np.inf]
    labels = ["Bajo", "Moderado", "Alto"]
    df["addiction_category"] = pd.cut(
        df["addiction_score"], bins=bins, labels=labels
    ).astype("category")

    # --- Feature 4: performance_tier ---
    # Cuartiles de notas → segmenta rendimiento académico.
    df["performance_tier"] = pd.qcut(
        df["grades"],
        q=4,
        labels=["Q1_Bajo", "Q2_MedioBajo", "Q3_MedioAlto", "Q4_Alto"]
    ).astype("category")

    print("[features] Features creadas: gaming_study_ratio, wellness_score, "
          "addiction_category, performance_tier")
    return df