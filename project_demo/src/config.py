from pathlib import Path
 
# Raíz del proyecto (un nivel arriba de src/)
ROOT = Path(__file__).resolve().parent.parent
 
# Rutas de datos
RAW_PATH  = ROOT / "data" / "raw"  / "raw_dataset.csv"
OUT_PATH  = ROOT / "data" / "processed" / "clean_dataset.csv"
 
# Columnas esperadas
EXPECTED_COLUMNS = [
    "student_id", "age", "gender", "gaming_hours", "study_hours",
    "sleep_hours", "attendance", "gaming_genre", "social_activity",
    "device_usage", "reaction_time_ms", "addiction_score",
    "stress_level", "grades"
]
 
# Columnas numéricas y categóricas
NUMERIC_COLS = [
    "age", "gaming_hours", "study_hours", "sleep_hours",
    "attendance", "social_activity", "device_usage",
    "reaction_time_ms", "addiction_score", "grades"
]