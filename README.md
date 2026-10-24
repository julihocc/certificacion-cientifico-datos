# Data Scientist Program - Comprehensive Portfolio

A complete learning and project repository documenting the Data Scientist Professional Certification Program journey. This repository showcases progression through 56+ modules across 7 major data science domains, culminating in 4 capstone projects.

**Author:** Juliho Castillo Colmenares

- [LinkedIn](https://www.linkedin.com/in/julihocc/)
- [Kaggle](https://www.kaggle.com/julihocc)
- [GitHub](https://github.com/julihocc)

---

## Repository Overview

**Repository Size:** 260 MB | **Total Files:** 447 | **Modules Completed:** 56+ | **Projects:** 4

This repository contains comprehensive coursework, practical exercises, and real-world projects demonstrating proficiency across all major data science disciplines including Python, SQL, Machine Learning, Statistics, Business Intelligence, and Advanced Modelling.

### Quick Stats
| Metric | Count |
|--------|-------|
| Jupyter Notebooks | 151 |
| SQL Scripts | 40 |
| CSV Datasets | 44 |
| PDF Documentation | 50 |
| PNG Visualizations | 81 |
| Markdown Guides | 28 |

---

## Repository Structure

```
certificacion-cientifico-datos/
├── s01-programacion/                Python programming fundamentals (M01-M12)
├── s02-ciencia-de-datos/            Data science theory & fundamentals (M13-M16)
├── s03-metodologia/                 Frameworks & workflows (M17-M20)
├── s04-aprendizaje-supervisado/     Supervised learning algorithms (M21-M26)
├── s05-aprendizaje-no-supervisado/  Unsupervised learning algorithms (M27-M31)
├── s06-estadistica/                 Statistical analysis methods (M32-M34)
├── s07-sql/                         Database & SQL queries (M35-M43)
├── s08-dashboards/                  BI & dashboards with Streamlit (M44-M50 + practica-ventas/)
├── s09-modelado/                    Advanced statistical modelling (M51-M56)
├── s10-storytelling/                Data visualization & presentation (M57)
└── proyectos/                       Capstone projects (P01-P05)
```

### Naming convention

- All names are lowercase ASCII kebab-case in Spanish (no accents, spaces or underscores).
- Sections are `sNN-tema/`, modules `mNN-tema/` and projects `proyectos/pNN-tema/`. Modules are numbered sequentially from M01 to M57 across the whole program.
- Each module folder holds files named after the module, distinguished by a suffix:

| File | Content |
| --- | --- |
| `mNN-tema-guia.ipynb` | Student guide: context, data, instructions and empty answer cells |
| `mNN-tema-solucion.*` | The solved exercise (`.ipynb`, `.md`, `.sql`, `.pdf`…) |
| `mNN-tema-leccion.*` | Complementary lesson (only in some modules) |
| `mNN-tema-app.py` | Streamlit app built in the module (S08 and P05 only) |

- For example, `s04-aprendizaje-supervisado/m21-regresion-lineal-simple/` contains `m21-regresion-lineal-simple-guia.ipynb` and `m21-regresion-lineal-simple-solucion.ipynb`.

---

## Section Details

### S01: Programación (Programming)
Python programming fundamentals
- **M01-M06:** Introduction to Python, data structures, control flow, loops, functions, object-oriented programming
- **M07-M08:** Pandas and NumPy
- **M09-M10:** Data visualization (2 modules)
- **M11-M12:** Advanced functions, modules and packages

### S02: Ciencia de Datos (Data Science Fundamentals) - 1.8 MB
Foundational concepts and theory of data science
- **M13:** History, context, and basic definitions
- **M14:** Types of analytics
- **M15:** Solution-based approaches
- **M16:** Analytics applications (Spotify case study)

### S03: Metodología (Methodology) - 2.6 MB
Data science methodologies and frameworks
- **M17:** Data science methodology
- **M18:** KDD and CRISP-DM frameworks
- **M19-M20:** TDSP and data mining with Orange (2 modules)

### S04: Aprendizaje Supervisado (Supervised Learning) - 6.7 MB
Machine learning algorithms and techniques
- **M21:** Simple Linear Regression (GDP data)
- **M22:** Regularized Regression
- **M23:** K-Nearest Neighbors (KNN)
- **M24:** Support Vector Machines (SVM)
- **M25:** Ensemble Methods
- **M26:** Logistic Regression

### S05: Aprendizaje No Supervisado (Unsupervised Learning)
Clustering and dimensionality reduction
- **M27:** Hierarchical Clustering
- **M28:** K-Means
- **M29:** Principal Component Analysis (PCA)
- **M30:** Singular Value Decomposition (SVD)
- **M31:** KNN-based clustering (wine data)

### S06: Estadística (Statistics) - 2.8 MB
Statistical analysis and hypothesis testing
- **M32:** Descriptive Statistics
- **M33:** Inferential Statistics (hypothesis testing)
- **M34:** Advanced Statistics (housing price analysis)

### S07: SQL (Database & Queries) - 16 MB
SQL fundamentals and advanced database querying
- **M35-M43:** 9 modules covering SQL introduction through advanced topics
- **37 SQL scripts** with practical exercises and solutions
- Topics include: table operations, multi-table queries, aggregation, partitioning, SQLite with Python, and advanced querying

### S08: Dashboards (Business Intelligence)
Business intelligence and dashboard development with free, open-source tools: pandas and DuckDB for data preparation and modelling, Plotly for charts and Streamlit for the interactive apps
- **M44:** Data Preparation (pandas)
- **M45:** Data Modelling (star schema in DuckDB)
- **M46:** Conditional Formatting (first dashboard)
- **M47:** Measures and KPIs (time intelligence in SQL and pandas)
- **M48:** Interactivity (filters, cross-filtering, drill-down and drill-through)
- **M49:** Dashboard Design (layout, theme, navigation)
- **M50:** Publishing Dashboards (Streamlit Community Cloud, row-level security)
- `practica-ventas/` holds the sales extract (`datos-ventas/`, 57 MB), the cleaned model in Parquet (`datos-modelo/`), the shared module [`ventas.py`](s08-dashboards/practica-ventas/ventas.py) with the cleaning steps and measures, and the section's final multipage app (`app.py`)
- The section was originally done in Power BI; it was redone in Python so it does not depend on paid or Windows-only software. The Power BI files remain in the git history.

### S09: Modelling (Advanced Analytics) - 17 MB
Advanced statistical and time series modelling
- **M51:** Regression Analysis (housing data)
- **M52:** Hypothesis Testing
- **M53:** Regression Models (advertising data)
- **M54:** Time Series Analysis
- **M55:** AR(p) Models (AutoRegressive)
- **M56:** ARIMA Models (New York temperature data)

### S10: Storytelling (M57: Storytelling with Data) - 7.8 MB
Data visualization and presentation techniques
- Jupyter notebook with practical examples
- UN economic activity data analysis
- Presentation best practices

---

## Capstone Projects

### P01: User Reviews Analysis - 7.7 MB
**Objective:** Clustering analysis of user review data
- **Dataset:** 7.7 MB user reviews
- **Techniques:** Clustering analysis, unsupervised learning
- **Deliverables:** Jupyter notebook, PDF analysis report, visualizations

### P02: Heart Attack Prediction - 76+ MB
**Objective:** Predictive modeling for heart attack risk assessment
- **Datasets:** Medical dataset (11 KB), MNIST digits (76 MB)
- **Techniques:** Supervised learning, classification models, feature engineering
- **Deliverables:** Jupyter notebook, PDF report, model analysis

### P03: Customer Segmentation
**Objective:** Customer segmentation of online retail transactions
- **Dataset:** Online Retail (UCI)
- **Techniques:** Unsupervised learning, clustering
- **Deliverables:** Jupyter notebook, PDF report

### P04: Movie Data Analysis - 1.5+ MB
**Objective:** Comprehensive SQL and data analysis of movie rental database
- **Dataset:** DVD rental database with SQL restore scripts
- **Techniques:** SQL queries, data aggregation, exploratory analysis
- **Deliverables:** 2 SQL analysis scripts, 15+ visualization screenshots, markdown documentation, comprehensive PDF report (1.5 MB)

### P05: COVID-19 Dashboard
**Objective:** Dashboard ranking countries by COVID-19 cases, deaths, mortality and recovery rates
- **Tools:** pandas, DuckDB, Plotly, Streamlit
- **Dataset:** Johns Hopkins CSSE COVID-19 time series (confirmed, deaths, recovered), local copy in `datos/`
- **Deliverables:** Jupyter notebook and Streamlit app ([`p05-dashboard-covid-app.py`](proyectos/p05-dashboard-covid/p05-dashboard-covid-app.py))

---

## Technologies & Tools

### Programming Languages
- **Python:** Data analysis, machine learning, statistical computing (151 Jupyter notebooks)
- **SQL:** Database querying and data manipulation (40 scripts)
- **Markdown:** Technical documentation (28 guides)

### Data Science Stack
| Category | Tools | Usage |
|----------|-------|-------|
| **Data Analysis** | Pandas, NumPy | Data manipulation & processing |
| **Machine Learning** | Scikit-learn, Ensemble methods | Classification, regression, clustering |
| **Statistics** | SciPy, Statsmodels | Hypothesis testing, time series analysis |
| **Visualization** | Matplotlib, Seaborn, Plotly | Data visualization & exploration |
| **BI & Dashboarding** | Streamlit, DuckDB, Orange | Interactive dashboards & visual data mining |
| **Database** | SQLite, DuckDB, SQL | Data storage & querying |

### File Type Distribution
- Jupyter Notebooks (.ipynb): 151 files
- SQL Scripts (.sql): 40 files
- CSV Datasets (.csv): 44 files
- PDF Documentation (.pdf): 50 files
- PNG Images (.png): 81 files
- Markdown Guides (.md): 28 files
- Parquet Files (.parquet): 5 files
- Orange Workflows (.ows): 3 files
- Python Scripts (.py): 19 files, including the Streamlit apps

---

## Submitted work, guides and lessons

Every module holds my submitted work in its `-solucion` files, except [M01 Introducción a Python](s01-programacion/m01-introduccion-a-python/m01-introduccion-a-python.ipynb). M01 is a complementary lesson written later to complete S01.

Every exercise, projects included, also has a student guide (`-guia.ipynb`). The guide is a notebook with the context, the data, the numbered tasks and empty cells to answer them, so the exercise can be worked from scratch before you open the solution. Each solution starts with the same context and instructions, and its work is organized by task.

Some modules had no surviving original statement. For those, the instructions were reconstructed from the solution, and the solution says so.

Modules whose folders contained only solved exercises also include a complementary lesson. The lesson covers the theory behind the exercise, with worked examples, common mistakes, a new exercise with its solution, and a summary. It sits next to the exercise, named after the module with a `-leccion` suffix:

| Sections | Format | Example |
| --- | --- | --- |
| S01 (M02–M12), S07 (M35–M43), S09 (M51–M56), M24, M27, M30, M57 | Executed notebook | [m07-pandas-leccion.ipynb](s01-programacion/m07-pandas/m07-pandas-leccion.ipynb) |
| S08 (M44–M50) | Executed notebook, with the module's Streamlit app | [m47-medidas-y-kpis-leccion.ipynb](s08-dashboards/m47-medidas-y-kpis/m47-medidas-y-kpis-leccion.ipynb) |
| S02 (M13–M16), S03 (M17–M18) | Markdown: the module's original text, written during the course | [m18-kdd-crisp-dm-leccion.md](s03-metodologia/m18-kdd-crisp-dm/m18-kdd-crisp-dm-leccion.md) |

In M13–M18 the exercise is new: the guide poses an applied case with written questions plus a Python practice on synthetic data, and the solution is a reference notebook written for it.

Apart from the M13–M18 texts, lessons are not part of the submitted work. The notebook lessons run offline, using the datasets in each folder or simulated data. The SQL lessons use an in-memory SQLite database and show the SQL Server syntax used in the course wherever it differs.

Some submitted exercises were corrected after review. For example, M51 had a singular matrix caused by collinear columns, and in M55 the forecast intervals were never drawn. Each corrected notebook or script ends with a **Revisión posterior (2026-10)** note describing the change. The accompanying PDFs keep the version that was originally submitted. S08 and P05 are the exception: they were redone from scratch in Python and Streamlit, so they have no PDFs, and the original Power BI work is only in the git history.

## Running the notebooks

The environment is managed with [uv](https://docs.astral.sh/uv/) (Python 3.11):

```bash
uv sync               # create .venv with every dependency from uv.lock
uv run jupyter lab    # open Jupyter in that environment
```

pandas is pinned below 3 and statsmodels below 0.15, because the notebooks were written for those versions and newer majors break some of them.

Each notebook reads its data with a relative path, so run it from its own folder.

The S08 and P05 notebooks save their Plotly charts as PNG images with kaleido, which needs Chrome. If re-running one fails while exporting a chart, install it with `uv run plotly_get_chrome`.

## Running the apps

The Streamlit apps of S08 and P05 are launched from the repository root, so they pick up the theme in `.streamlit/config.toml`:

```bash
uv run streamlit run s08-dashboards/practica-ventas/app.py                    # final S08 dashboard
uv run streamlit run s08-dashboards/m46-formato-condicional/m46-formato-condicional-app.py
uv run streamlit run proyectos/p05-dashboard-covid/p05-dashboard-covid-app.py
```

The S08 apps read the cleaned model from `s08-dashboards/practica-ventas/datos-modelo/*.parquet`. If the cleaning in `ventas.py` changes, rebuild it with `uv run python s08-dashboards/practica-ventas/preparar_datos.py`. `uv run python s08-dashboards/verificar_apps.py` runs every app headless as a smoke test.

## Large files

Zip archives and the large datasets are stored with [Git LFS](https://git-lfs.com/). Run `git lfs install` once before cloning, or `git lfs pull` after cloning, to get their contents instead of pointer files. The Parquet model used by the S08 apps is small enough to be stored as a regular file, so the apps also work where LFS files are not downloaded (for example, on Streamlit Community Cloud).

| Dataset | Used by | Source |
| --- | --- | --- |
| `proyectos/p02-aprendizaje-supervisado/mnist.csv` | P02 | `train.csv` from Kaggle's [Digit Recognizer](https://www.kaggle.com/competitions/digit-recognizer/data) competition |
| `proyectos/p03-segmentacion-de-clientes/online-retail.csv` | P03 | Course-provided copy of the [UCI Online Retail](https://archive.ics.uci.edu/dataset/352/online+retail) dataset, with columns renamed to upper case (`INVOICE_NO`, `CUSTOMER_ID`, `REGION`…) and dates shifted to 2019 |
| `s08-dashboards/practica-ventas/datos-ventas/` | S08 practice dashboard | Sales extract provided by the course |

P05 uses a local copy of the [JHU CSSE COVID-19 Data Repository](https://github.com/CSSEGISandData/COVID-19) time series (`proyectos/p05-dashboard-covid/datos/`, under 2 MB each, so not in LFS). The repository was archived in March 2023 and is licensed under CC BY 4.0.

## Not included

- The `dvdrental` data files for P04 come from the PostgreSQL `dvdrental` sample database. To rebuild it, edit the file paths in [restore.sql](proyectos/p04-analisis-de-peliculas-sql/dvdrental/restore.sql) to point at your local copy.
- Course material (class guides, glossaries, FAQs and assignment PDFs) is not included.

---

## Datasets Used

The repository includes multiple real-world and educational datasets:
- **GDP Data:** Economic growth analysis
- **Heart Attack Dataset:** Medical prediction modeling
- **Movie Rental Database (dvdrental):** SQL and relational database exercises
- **Marketing Campaign Data:** Statistical analysis and hypothesis testing
- **Housing/Price Data:** Regression modelling
- **MNIST Handwritten Digits:** Machine learning (76 MB)
- **User Reviews:** Clustering and unsupervised learning
- **Sales Dataset:** Dashboard creation with Streamlit (57 MB)
- **COVID-19 Data:** Dashboard of country rankings (JHU CSSE)
- **New York Temperature Data:** Time series analysis
- **UN Economic Activity Data:** Data storytelling

---

## Documentation & Resources

### Included Documentation
- **28 Markdown guides** with module instructions, exercises, and theory
- **50 PDF documents** including class materials, solutions, and project reports
- **81 PNG images** showing visualizations, screenshots, and diagrams
- **Jupyter notebooks** with detailed analysis and code comments

### Learning Path
The repository is organized as a progressive learning path:
1. **Foundation** (S01-S03): Programming, theory and methodology
2. **Technical Skills** (S04-S07): ML, statistics, SQL
3. **Advanced Tools** (S08-S09): BI, modelling, time series
4. **Integration** (S10, proyectos): Storytelling and capstone projects

---

## Key Achievements

✓ **56+ modules** completed across 7 data science domains
✓ **4 capstone projects** with end-to-end delivery
✓ **40 SQL scripts** demonstrating database expertise
✓ **151 Jupyter notebooks** showcasing analysis workflows
✓ **Interactive Streamlit dashboards** built on a DuckDB star schema
✓ **Comprehensive documentation** with 28 guides and 50 PDFs
✓ **Real-world datasets** across multiple industries and domains

---

## How to Navigate

- **Learning Sequential:** Start in S01 and progress through sections in numerical order
- **By Technology:**
  - Python/ML: S01, S04, S05 and proyectos
  - SQL: S07 and P04
  - Statistics: S06 and S09
  - BI and dashboards: S08 and P05
  - Methodology: S03 and S10
- **By Project:** Jump to `proyectos/` folder for capstone deliverables

---

## Contact & Links

- **LinkedIn:** [Juliho Castillo Colmenares](https://www.linkedin.com/in/julihocc/)
- **Kaggle:** [julihocc](https://www.kaggle.com/julihocc)
- **GitHub:** [julihocc](https://github.com/julihocc)

---

**Repository Type:** Educational Portfolio | **Last Updated:** 2026 | **Language:** Spanish (Content) | **License:** Personal Learning Archive