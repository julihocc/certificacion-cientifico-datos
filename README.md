# EBAC Data Scientist Program

Projects and exercises developed during the EBAC Data Scientist Program (2024). Most of the material is written in Spanish.

Author: Juliho Castillo Colmenares

- [LinkedIn](https://www.linkedin.com/in/julihocc/)
- [Kaggle](https://www.kaggle.com/julihocc)
- [GitHub](https://github.com/julihocc)

![Power BI sales dashboard built in the S08 practice](%7B865FEE50-8BAD-45DD-AEB3-68EC4FDEBFE1%7D.png)

## Projects

| Project | Topic | Tools | Main file |
| --- | --- | --- | --- |
| [P01 User Reviews](Projects/P01-User-Reviews/) | Google Play Store apps and user reviews: cleaning, EDA and sentiment | pandas, matplotlib | [Python.ipynb](Projects/P01-User-Reviews/Python.ipynb) |
| [P02 Heart Attack](Projects/P02-Heart-Attack/) | Supervised classification of heart-attack risk, plus multiclass classification on MNIST | scikit-learn | [Aprendizaje Supervisado.ipynb](Projects/P02-Heart-Attack/Aprendizaje%20Supervisado.ipynb) |
| [P04 Movie Data Analysis](Projects/P04-movie-data-analysis/) | SQL analysis of the `dvdrental` movie-rental database | PostgreSQL | [project-04.md](Projects/P04-movie-data-analysis/project-04.md) |
| [P05 COVID-19 Dashboard](Projects/project-05/) | COVID-19 cases, deaths and mortality rate by country | Power BI | [project-05.pdf](Projects/project-05/project-05.pdf) |

## Sections

| Section | Modules |
| --- | --- |
| [S02 Data Science](S02-Ciencia-de-datos/) | M11–M14: history and definitions, types of analytics, analytics solutions |
| [S03 Methodology](S03-Metodología/) | M15–M18: KDD, CRISP-DM, TDSP, BSPF, Agile Data Science, data mining with Orange |
| [S04 Supervised Learning](S04-Aprendizaje-supervisado/) | M19–M25: linear and regularized regression, KNN, SVM, ensembles, logistic regression |
| [S06 Statistics](S06-Estadística/) | M31–M33: descriptive, inferential and advanced statistics |
| [S07 SQL](S07-SQL/) | M35–M43: queries, joins, grouping, window functions, SQLite from Python |
| [S08 Power BI](S08-PowerBI/) | M45–M51: data preparation, modelling, DAX, dynamic objects, dashboard design and publishing |
| [S09 Modelling](S09-Modelling/) | M51–M56: regression, hypothesis testing, time series, AR and ARIMA models |
| [M57 Storytelling](M57-Storytelling/) | Storytelling with data |

## Running the notebooks

The environment is managed with [uv](https://docs.astral.sh/uv/) (Python 3.11):

```bash
uv sync               # create .venv with every dependency from uv.lock
uv run jupyter lab    # open Jupyter in that environment
```

pandas is pinned below 3 and statsmodels below 0.15, because the notebooks were written for those versions and newer majors break some of them.

Each notebook reads its data with a relative path, so run it from its own folder.

To rebuild the P04 database, edit the file paths in [restore.sql](Projects/P04-movie-data-analysis/dvdrental/restore.sql) to point at your local copy of the `dvdrental` data files. The data files themselves are not stored in this repository.
