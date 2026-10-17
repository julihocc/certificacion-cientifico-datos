# EBAC Data Scientist Program

Projects and exercises developed during the EBAC Data Scientist Program (2024). Most of the material is written in Spanish.

Author: Juliho Castillo Colmenares

- [LinkedIn](https://www.linkedin.com/in/julihocc/)
- [Kaggle](https://www.kaggle.com/julihocc)
- [GitHub](https://github.com/julihocc)

![Power BI sales dashboard built in the S08 practice](S08-PowerBI/Practice/sales-dashboard.png)

## Projects

| Project | Topic | Tools | Main file |
| --- | --- | --- | --- |
| [P01 User Reviews](Projects/P01-User-Reviews/) | Google Play Store apps and user reviews: cleaning, EDA and sentiment | pandas, matplotlib | [Python.ipynb](Projects/P01-User-Reviews/Python.ipynb) |
| [P02 Heart Attack](Projects/P02-Heart-Attack/) | Supervised classification of heart-attack risk, plus multiclass classification on MNIST | scikit-learn | [Aprendizaje Supervisado.ipynb](Projects/P02-Heart-Attack/Aprendizaje%20Supervisado.ipynb) |
| [P03 Customer Segmentation](Projects/P03-Customer-Segmentation/) | RFM customer segmentation of online-retail transactions with k-means | scikit-learn | [M30 Aprendizaje no Supervisado.ipynb](Projects/P03-Customer-Segmentation/M30%20Aprendizaje%20no%20Supervisado.ipynb) |
| [P04 Movie Data Analysis](Projects/P04-Movie-Data-Analysis/) | SQL analysis of the `dvdrental` movie-rental database | PostgreSQL | [project-04.md](Projects/P04-Movie-Data-Analysis/project-04.md) |
| [P05 COVID-19 Dashboard](Projects/P05-Covid-Dashboard/) | COVID-19 cases, deaths and mortality rate by country | Power BI | [project-05.pdf](Projects/P05-Covid-Dashboard/project-05.pdf) |

## Sections

| Section | Modules |
| --- | --- |
| [S01 Programming](S01-Programación/) | M01–M12: Python basics, data structures, control flow, loops, functions, OOP, pandas, NumPy, visualization, modules |
| [S02 Data Science](S02-Ciencia-de-datos/) | M11–M14: history and definitions, types of analytics, analytics solutions |
| [S03 Methodology](S03-Metodología/) | M15–M18: KDD, CRISP-DM, TDSP, BSPF, Agile Data Science, data mining with Orange |
| [S04 Supervised Learning](S04-Aprendizaje-supervisado/) | M19–M25: linear and regularized regression, KNN, SVM, ensembles, logistic regression |
| [S05 Unsupervised Learning](S05-Aprendizaje-no-supervisado/) | M26–M30: hierarchical clustering, k-means, PCA, SVD, KNN |
| [S06 Statistics](S06-Estadística/) | M31–M33: descriptive, inferential and advanced statistics |
| [S07 SQL](S07-SQL/) | M35–M43: queries, joins, grouping, window functions, SQLite from Python |
| [S08 Power BI](S08-PowerBI/) | M45–M51: data preparation, modelling, DAX, dynamic objects, dashboard design and publishing |
| [S09 Modelling](S09-Modelling/) | M51–M56: regression, hypothesis testing, time series, AR and ARIMA models |
| [S10 Storytelling](S10-Storytelling/) | M57: storytelling with data |

Every module holds my submitted work, except [M01 Introducción a Python](S01-Programación/M01-Introducción-a-Python/m01-introduccion-a-python.ipynb). M01 is a complementary lesson written later to complete S01.

## Running the notebooks

The environment is managed with [uv](https://docs.astral.sh/uv/) (Python 3.11):

```bash
uv sync               # create .venv with every dependency from uv.lock
uv run jupyter lab    # open Jupyter in that environment
```

pandas is pinned below 3 and statsmodels below 0.15, because the notebooks were written for those versions and newer majors break some of them.

Each notebook reads its data with a relative path, so run it from its own folder.

## Large files

Power BI files (`*.pbix`), zip archives and the large datasets are stored with [Git LFS](https://git-lfs.com/). Run `git lfs install` once before cloning, or `git lfs pull` after cloning, to get their contents instead of pointer files.

| Dataset | Used by | Source |
| --- | --- | --- |
| `Projects/P02-Heart-Attack/MNIST.csv` | P02 | `train.csv` from Kaggle's [Digit Recognizer](https://www.kaggle.com/competitions/digit-recognizer/data) competition |
| `Projects/P03-Customer-Segmentation/M30 Online Retail.csv` | P03 | Course-provided copy of the [UCI Online Retail](https://archive.ics.uci.edu/dataset/352/online+retail) dataset, with columns renamed to upper case (`INVOICE_NO`, `CUSTOMER_ID`, `REGION`…) and dates shifted to 2019 |
| `S08-PowerBI/Practice/Sales Extract/` | S08 practice dashboard | Sales extract provided by the course |

## Not included

- The `dvdrental` data files for P04 come from the PostgreSQL `dvdrental` sample database. To rebuild it, edit the file paths in [restore.sql](Projects/P04-Movie-Data-Analysis/dvdrental/restore.sql) to point at your local copy.
- EBAC course material (class guides, glossaries, FAQs and assignment PDFs) is not included.
