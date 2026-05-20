"""
main.py — Pipeline reproducible completo.
Ejecutar desde la raíz del proyecto:
    python main.py
"""
import sys
from pathlib import Path

# Asegura que src/ sea importable
sys.path.insert(0, str(Path(__file__).resolve().parent))

from src.io       import load_csv, save_csv
from src.utils    import assert_columns, summary, check_ranges
from src.cleaning import clean
from src.features import build_features
from src.viz      import (
    plot_grades_distribution,
    plot_gaming_vs_grades,
    plot_grades_by_genre,
    plot_correlation_heatmap,
    plot_addiction_vs_grades,
    plot_study_vs_grades,
)


def main():
    print("=" * 60)
    print("  EDA: Videojuegos y Rendimiento Académico")
    print("=" * 60)

    # 1. Cargar
    df = load_csv()

    # 2. Validar
    assert_columns(df)
    check_ranges(df)
    print("\n--- Resumen inicial ---")
    print(summary(df).to_string())

    # 3. Limpiar
    print("\n--- Limpieza ---")
    df = clean(df)

    # 4. Feature engineering
    print("\n--- Features ---")
    df = build_features(df)

    # 5. Exportar
    print("\n--- Exportar ---")
    save_csv(df)

    # 6. Visualizaciones
    print("\n--- Visualizaciones ---")
    plot_grades_distribution(df)
    plot_gaming_vs_grades(df)
    plot_grades_by_genre(df)
    plot_correlation_heatmap(df)
    plot_addiction_vs_grades(df)
    plot_study_vs_grades(df)

    print("\n✓ Pipeline completado.")


if __name__ == "__main__":
    main()