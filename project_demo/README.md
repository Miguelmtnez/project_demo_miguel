# 🎮 Videojuegos y Rendimiento Académico — EDA

**Máster en Data Science & AI | Proyecto Entregable**

---

## Objetivo

Explorar si existe relación entre el tiempo dedicado a los videojuegos, el nivel de adicción y otras variables de hábitos (sueño, estudio, asistencia, estrés) con el rendimiento académico de estudiantes universitarios.

## Dataset

| Atributo | Detalle |
|---|---|
| Fuente | Kaggle — *Student Gaming & Academic Performance* |
| Archivo | `data/raw/raw_dataset.csv` |
| Filas | 8 000 estudiantes |
| Columnas | 14 variables (ver abajo) |

**Columnas principales:**

| Columna | Tipo | Descripción |
|---|---|---|
| `student_id` | int | Identificador único |
| `age` | float | Edad del estudiante |
| `gender` | cat | Género |
| `gaming_hours` | float | Horas diarias de gaming |
| `study_hours` | float | Horas diarias de estudio |
| `sleep_hours` | float | Horas diarias de sueño |
| `attendance` | float | % de asistencia |
| `gaming_genre` | cat | Género de videojuego (FPS, RPG, Casual…) |
| `social_activity` | float | Nivel de actividad social |
| `device_usage` | float | Horas diarias de uso de dispositivos |
| `reaction_time_ms` | float | Tiempo de reacción en ms |
| `addiction_score` | float | Puntuación de adicción (0–30) |
| `stress_level` | cat | Nivel de estrés (Low / Medium / High) |
| `grades` | float | Calificación final (0–100) |

## Preguntas de investigación

1. ¿Más horas de gaming se asocian con peores notas?
2. ¿Qué género de videojuego se asocia con mayor o menor rendimiento?
3. ¿El nivel de adicción modera la relación entre gaming y notas?
4. ¿Cuáles son los factores más correlacionados con las calificaciones?

## Estructura del proyecto

```
project_demo/
├── data/
│   ├── raw/          ← raw_dataset.csv (incluido)
│   └── processed/    ← clean_dataset.csv (generado por main.py)
├── figures/          ← gráficos exportados (generados al ejecutar)
├── notebooks/
│   └── eda.ipynb     ← análisis principal (narrado)
├── src/
│   ├── __init__.py
│   ├── config.py     ← rutas y constantes
│   ├── io.py         ← load_csv / save_csv
│   ├── utils.py      ← assert_columns / summary / check_ranges
│   ├── cleaning.py   ← clean pipeline (duplicados, tipos, nulos, outliers)
│   ├── features.py   ← build_features (4 features nuevas)
│   └── viz.py        ← 6 funciones de visualización
├── main.py           ← pipeline reproducible end-to-end
├── requirements.txt
└── README.md
```

## Pipeline

```
load_csv → assert_columns → check_ranges → clean → build_features → save_csv → visualize
```

Cada paso está en un módulo separado en `src/` y orquestado en:
- `main.py` — ejecución desde terminal
- `notebooks/eda.ipynb` — análisis narrado paso a paso

## Features creadas

| Feature | Descripción |
|---|---|
| `gaming_study_ratio` | gaming_hours / study_hours — trade-off ocio/estudio |
| `wellness_score` | Índice compuesto: sueño + asistencia − estrés (0–1) |
| `addiction_category` | Bins del addiction_score: Bajo / Moderado / Alto |
| `performance_tier` | Cuartiles de notas: Q1_Bajo → Q4_Alto |

## Pasos para reproducir

```bash
# 1. Descomprimir y entrar al proyecto
cd project_demo

# 2. Inicializar git (opcional)
git init

# 3. Crear entorno virtual
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Ejecutar pipeline completo
python main.py

# 6. O abrir el notebook
jupyter notebook notebooks/eda.ipynb
```

## Hallazgos principales

1. **El gaming excesivo perjudica las notas, especialmente con alta adicción.**  
   Estudiantes con `addiction_score` alto obtienen calificaciones significativamente más bajas (gráfico 05).

2. **Las horas de estudio y la asistencia son los predictores positivos más fuertes de las notas.**  
   Correlaciones ~0.6 en el heatmap (gráfico 04), superando al resto de variables.

3. **El estrés modera el efecto del estudio: a mayor estrés, mayor variabilidad en notas incluso estudiando muchas horas** (gráfico 06).

## Siguientes pasos

- Modelado predictivo: regresión lineal / Random Forest para predecir `grades`
- Análisis de subgrupos por `gaming_genre` controlando horas totales
- Análisis de mediación: ¿el sueño media entre gaming y notas?