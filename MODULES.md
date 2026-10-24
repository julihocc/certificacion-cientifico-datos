# Data Scientist Program - Complete Module Guide

## Table of Contents
- [Section 2: Data Science Fundamentals](#section-2-data-science-fundamentals)
- [Section 3: Methodology](#section-3-methodology)
- [Section 4: Supervised Learning](#section-4-supervised-learning)
- [Section 6: Statistics](#section-6-statistics)
- [Section 7: SQL & Databases](#section-7-sql--databases)
- [Section 8: Dashboards (Business Intelligence)](#section-8-dashboards-business-intelligence)
- [Section 9: Advanced Modelling](#section-9-advanced-modelling)
- [Module 57: Storytelling with Data](#module-57-storytelling-with-data)

---

## Section 2: Ciencia de Datos (Data Science Fundamentals)

**Directory:** `s02-ciencia-de-datos/`
**Size:** 1.8 MB | **Modules:** 4 | **Duration:** Introductory

### Purpose
Establish foundational understanding of data science concepts, terminology, and applications.

### Modules

#### M13: History and Definitions of Data Science
- **Topics:**
  - Definition and scope of data science
  - Historical evolution of data science
  - Core concepts and terminology
- **Resources:**
  - Theory PDF: `m13-historia-contexto-y-definiciones-leccion.pdf`
  - Markdown guide: `m13-historia-contexto-y-definiciones-leccion.md`
- **Learning Outcome:** Understand data science as discipline

#### M14: Types of Analytics
- **Topics:**
  - Descriptive analytics
  - Predictive analytics
  - Prescriptive analytics
  - Diagnostic analytics
- **Resources:**
  - Class material: `m14-tipos-de-analitica-leccion.pdf`
  - Exercises: `m14-tipos-de-analitica-leccion.md`
- **Learning Outcome:** Differentiate analytics types

#### M15: Solution-Based Approaches
- **Topics:**
  - Problem-solving frameworks
  - Solution design methodologies
  - Business impact consideration
- **Resources:**
  - PDF guide: `m15-soluciones-basadas-en-datos-leccion.pdf`
- **Learning Outcome:** Apply data science to business problems

#### M16: Analytics Applications & Case Studies
- **Topics:**
  - Real-world analytics applications
  - Industry case studies
  - Spotify analytics example
- **Resources:**
  - Case study: `m16-aplicacion-de-analitica-leccion.md`
  - Dataset: `spotify_data.csv`
- **Learning Outcome:** Connect theory to real applications

---

## Section 3: Metodología (Data Science Methodologies)

**Directory:** `s03-metodologia/`
**Size:** 2.6 MB | **Modules:** 4 | **Duration:** Intermediate

### Purpose
Master established data science frameworks and project methodologies.

### Modules

#### M17: Data Science Methodology
- **Topics:**
  - Scientific method application
  - Hypothesis formulation
  - Experiment design
  - Validation approaches
- **Resources:**
  - `m17-metodologia-leccion.pdf`
  - `m17-metodologia-leccion.md`
- **Prerequisites:** M13-M16
- **Learning Outcome:** Design data science projects methodically

#### M18: KDD and CRISP-DM Frameworks
- **Topics:**
  - Knowledge Discovery in Databases (KDD)
  - CRISP-DM (Cross Industry Standard Process)
  - Framework comparison
  - Implementation steps
- **Resources:**
  - `m18-kdd-crisp-dm-leccion.pdf` (comprehensive guide)
  - `m18-kdd-crisp-dm-leccion.md`
  - Visual diagrams and flowcharts
- **Learning Outcome:** Apply industry-standard frameworks

#### M19: TDSP (Team Data Science Process)
- **Topics:**
  - Microsoft TDSP framework
  - Team-based project structure
  - Lifecycle phases
  - Deliverables at each stage
- **Resources:**
  - `m19-tdsp-bspf-y-orange-1-solucion.pdf`
  - Process documentation
- **Learning Outcome:** Plan team data science projects

#### M20: Data Mining with Orange
- **Topics:**
  - Visual data mining concepts
  - Orange software introduction
  - Workflow design
  - Classification and clustering with Orange
- **Resources:**
  - `m20-agile-data-science-y-orange-2-solucion.pdf`
  - Orange workflow files: `modelo.ows`, `m19-tdsp-bspf-y-orange-1-solucion.ows` (M19)
  - Tutorial: `m20-agile-data-science-y-orange-2-solucion.md`
- **Tools:** Orange ML platform
- **Learning Outcome:** Use visual data mining tools

---

## Section 4: Aprendizaje Supervisado (Supervised Learning)

**Directory:** `s04-aprendizaje-supervisado/`
**Size:** 6.7 MB | **Modules:** 7 | **Duration:** Intermediate-Advanced

### Purpose
Master machine learning algorithms for classification and regression tasks.

### Modules

#### M21: Simple Linear Regression
- **Topics:**
  - Regression fundamentals
  - Ordinary Least Squares (OLS)
  - Model interpretation
  - Assumption validation
- **Resources:**
  - `m21-regresion-lineal-simple-solucion.pdf` (theory)
  - `M21-Exercises.pdf`
  - `m21-regresion-lineal-simple-solucion.ipynb` (Jupyter notebook)
- **Dataset:** `data/pib-por-pais.csv`
- **Tools:** Python, Scikit-learn, Pandas, Matplotlib
- **Learning Outcome:** Implement and interpret linear regression

#### M22: Regularized Regression
- **Topics:**
  - Ridge regression (L2 regularization)
  - Lasso regression (L1 regularization)
  - Elastic Net
  - Hyperparameter tuning
- **Resources:**
  - `m22-regresion-regularizada-solucion.pdf`
  - `M22-Exercise-Guide.md`
- **Prerequisites:** M21
- **Learning Outcome:** Apply regularization techniques

#### M23: K-Nearest Neighbors (KNN)
- **Topics:**
  - KNN algorithm mechanics
  - Distance metrics
  - Hyperparameter selection (k value)
  - Classification and regression with KNN
- **Resources:**
  - `m23-knn-solucion.pdf` (comprehensive guide)
  - `M23-Implementation.md`
- **Tools:** Scikit-learn
- **Learning Outcome:** Implement KNN classifier/regressor

#### M24: Support Vector Machines (SVM)
- **Topics:**
  - SVM theory and math
  - Kernel methods
  - Linear and non-linear SVM
  - Multi-class classification
- **Resources:**
  - `M24-SVM.pdf`
  - `M24-Practical-Guide.md`
- **Tools:** Scikit-learn
- **Learning Outcome:** Apply SVM to classification problems

#### M25: Ensemble Methods
- **Topics:**
  - Bagging and Bootstrap Aggregating
  - Random Forests
  - Boosting concepts
  - Gradient Boosting
- **Resources:**
  - `m25-metodos-de-ensamble-solucion.pdf` (3 files)
  - Python script: `preprocess.py`
  - Exercises and examples
- **Tools:** Scikit-learn, XGBoost
- **Learning Outcome:** Build ensemble models

#### M26: Logistic Regression
- **Topics:**
  - Logistic function and odds ratios
  - Binary classification
  - Multi-class classification
  - Model evaluation for classification
- **Resources:**
  - `m26-regresion-logistica-solucion.pdf`
  - Python script: `preprocess.py`
  - Practical examples
- **Tools:** Scikit-learn
- **Prerequisites:** M21 (recommended)
- **Learning Outcome:** Implement logistic regression classifier

---

## Section 6: Estadística (Statistics)

**Directory:** `s06-estadistica/`
**Size:** 2.8 MB | **Modules:** 3 | **Duration:** Intermediate

### Purpose
Master statistical analysis and hypothesis testing for data-driven decisions.

### Modules

#### M32: Descriptive Statistics
- **Topics:**
  - Measures of central tendency
  - Measures of dispersion
  - Distribution analysis
  - Data summarization
- **Resources:**
  - `m32-estadistica-descriptiva-solucion.pdf` (2 files)
  - Markdown guide: `m32-estadistica-descriptiva-solucion.md`
- **Learning Outcome:** Summarize data statistically

#### M33: Inferential Statistics & Hypothesis Testing
- **Topics:**
  - Probability distributions
  - Confidence intervals
  - Hypothesis testing (t-tests, chi-square)
  - P-values and significance
  - Type I and Type II errors
- **Resources:**
  - `m33-estadistica-inferencial-solucion.pdf` (3 files)
  - Jupyter notebook: `m33-estadistica-inferencial-solucion.ipynb`
- **Dataset:** Marketing campaign data
- **Tools:** SciPy, Statsmodels
- **Prerequisites:** M32 (recommended)
- **Learning Outcome:** Conduct hypothesis tests

#### M34: Advanced Statistics & Regression Analysis
- **Topics:**
  - Multiple regression
  - ANOVA (Analysis of Variance)
  - Regression diagnostics
  - Model validation
- **Resources:**
  - `m34-estadistica-avanzada-solucion.pdf` (2 files)
  - Jupyter notebook: `m34-estadistica-avanzada-solucion.ipynb`
- **Dataset:** Housing price data
- **Tools:** Statsmodels, Scipy
- **Prerequisites:** M33
- **Learning Outcome:** Conduct advanced statistical analysis

---

## Section 7: SQL (Database & Queries)

**Directory:** `s07-sql/`
**Size:** 16 MB | **Modules:** 9 | **Duration:** Intermediate-Advanced

### Purpose
Master SQL and database querying for data extraction and manipulation.

### SQL Scripts Inventory

#### M35: SQL Introduction (4 files)
- **Topics:**
  - SQL fundamentals
  - SELECT, FROM, WHERE clauses
  - Basic filtering
  - Data types
- **Resources:**
  - `M35-intro-01.sql`, `M35-intro-02.sql` (examples)
  - `M35-exercise-01.sql`, `M35-exercise-02.sql` (exercises)
  - Solution files
- **Learning Outcome:** Write basic SQL queries

#### M36: Table Operations (10 files)
- **Topics:**
  - CREATE TABLE
  - INSERT, UPDATE, DELETE
  - ALTER TABLE
  - Table constraints
- **Resources:**
  - 4 example scripts
  - 3 exercise scripts
  - 3 solution scripts
- **Learning Outcome:** Create and modify tables

#### M37: Multi-table Operations (8 files)
- **Topics:**
  - INNER JOIN
  - LEFT/RIGHT/FULL OUTER JOIN
  - CROSS JOIN
  - Union operations
- **Resources:**
  - 3 example scripts
  - 3 exercise scripts
  - 2 solution scripts
- **Learning Outcome:** Join multiple tables

#### M38: Aggregation & Partitioning (4 files)
- **Topics:**
  - GROUP BY clause
  - Aggregate functions (SUM, COUNT, AVG, etc.)
  - HAVING clause
  - Window functions
- **Resources:**
  - Example and exercise scripts
  - Solutions
- **Learning Outcome:** Aggregate and partition data

#### M39: Advanced SQL (6 files)
- **Topics:**
  - Subqueries
  - Common Table Expressions (CTEs)
  - Complex joins
  - Performance optimization
- **Resources:**
  - 2 example scripts
  - 2 exercise scripts
  - 2 solution scripts
- **Prerequisites:** M35-M38
- **Learning Outcome:** Write complex SQL queries

#### M40: SQLite with Python (3 files)
- **Topics:**
  - SQLite in Python
  - Database connection
  - Query execution from Python
  - Data integration
- **Resources:**
  - Python example scripts
  - Exercises
  - Integration patterns
- **Tools:** Python, sqlite3
- **Learning Outcome:** Use SQLite with Python

#### M41: SQL Import & Queries (4 files)
- **Topics:**
  - Data import techniques
  - CSV to database loading
  - Data validation
  - Query on imported data
- **Resources:**
  - Import scripts
  - Query examples
- **Learning Outcome:** Import and query data

#### M42: Advanced SQL Queries (4 files)
- **Topics:**
  - Optimization techniques
  - Index usage
  - Query planning
  - Performance analysis
- **Resources:**
  - Advanced query examples
  - Optimization patterns
- **Prerequisites:** M35-M39
- **Learning Outcome:** Optimize SQL queries

#### M43: Advanced Topics (4 files)
- **Topics:**
  - Transactions and rollback
  - Stored procedures
  - Triggers
  - Advanced features
- **Resources:**
  - Advanced scripts
  - Implementation examples
- **Prerequisites:** M35-M42
- **Learning Outcome:** Use advanced SQL features

### Database: dvdrental
**Description:** DVD rental database for SQL practice
**Files:**
- `proyectos/p04-analisis-de-peliculas-sql/dvdrental/restore.sql` - Database schema and restore script
- 16 tables including: customers, films, actors, rentals, payments
- ~3000+ records
**Use Cases:** Inventory management, rental analysis, customer queries

---

## Section 8: Dashboards (Business Intelligence)

**Directory:** `s08-dashboards/`
**Size:** 68 MB (57 MB of it is the raw sales extract) | **Modules:** 7 + Practice | **Duration:** Advanced

### Purpose
Build a business intelligence dashboard end to end with free, open-source tools: prepare the data with pandas, model it as a star schema in DuckDB, compute measures in SQL, chart it with Plotly and serve it as an interactive Streamlit app.

The section was originally done in Power BI. It was redone in Python so it does not depend on paid or Windows-only software; the Power BI files remain in the git history.

### Module structure
Every module has a guide (`-guia.ipynb`), an executed lesson (`-leccion.ipynb`) and an executed solution (`-solucion.ipynb`). From M46 on, each module also ships a Streamlit app; M49 and M50 build the section's final app in `practica-ventas/`.

### Modules

#### M44: Data Preparation
- **Topics:** reading CSV (with BOM), pipe-separated TXT, a folder of yearly files and Excel sheets; column profiling; the five real cleaning cases of the extract (duplicate countries, trailing-comma ghost column, junk rows above the header, packed customer field, Open/Closed store duplicates); append vs merge; calculated columns; saving to Parquet
- **Tools:** pandas, DuckDB (`read_csv` with a glob)
- **Learning Outcome:** Write a reproducible cleaning recipe that never touches the source files

#### M45: Data Modelling
- **Topics:** fact vs dimension tables, star vs snowflake schema, keys and cardinality, fan-out from duplicated keys, filter direction (joins and semi-joins), role-playing dates, measures as functions
- **Tools:** DuckDB, SQL
- **Learning Outcome:** Design and validate a star schema

#### M46: Conditional Formatting
- **Topics:** preattentive attributes, sequential and diverging colour scales, rules, colour computed by a function, data bars, icons, accessibility
- **Tools:** pandas `Styler`, `st.dataframe` with `column_config`, Plotly
- **App:** `m46-formato-condicional-app.py`, a first dashboard with KPIs, bubble map, donut, trend line and a formatted country table
- **Learning Outcome:** Make the important values of a table visible at a glance

#### M47: Measures and KPIs
- **Topics:** measures vs calculated columns, filter context, sum of products vs product of sums, share of total with window functions, safe division, calendar table, time intelligence (previous month, same month last year, year to date) and month-over-month and year-over-year changes
- **Tools:** DuckDB window functions, pandas
- **App:** `m47-medidas-y-kpis-app.py`, with a summary tab and a measure-validation tab
- **Learning Outcome:** Write correct business measures

#### M48: Interactivity
- **Topics:** Streamlit's execution model and session state, sidebar filters, date ranges, cross-filtering with chart selections, drill-down (treemap), drill-through (dialog), tooltips, dynamic titles
- **Tools:** Streamlit, Plotly
- **App:** `m48-interactividad-app.py`
- **Learning Outcome:** Build interactive reports

#### M49: Dashboard Design
- **Topics:** visual hierarchy, grid layout, the five-second rule, choosing the chart, themes, presets ("bookmarks"), multipage navigation, narrow screens
- **Tools:** `st.navigation`, `.streamlit/config.toml`, Plotly templates
- **Learning Outcome:** Design a clear, navigable dashboard

#### M50: Publishing Dashboards
- **Topics:** Streamlit Community Cloud, dependency files, secrets, data refresh, sharing, static and dynamic row-level security, free-tier limits vs self-hosting
- **Tools:** Streamlit Community Cloud, `st.secrets`, `st.login`/`st.user`
- **Learning Outcome:** Publish a dashboard and control who sees which rows

### Practice & Datasets (`practica-ventas/`)
- **Raw extract (`datos-ventas/`, 57 MB, Git LFS):** 1 499 000 sales from 2019 to 2021 in three CSV files, a countries TXT and an Excel catalogue (customers, stores, products)
- **Clean model (`datos-modelo/`, 8.6 MB of Parquet):** one fact table and four dimensions, rebuilt by `preparar_datos.py`
- **`ventas.py`:** shared cleaning steps, DuckDB model and measures, used by the notebooks of M45–M50 and by every app
- **Final app:** `app.py` with the pages in `paginas/` (home, summary, time measures, country analysis, about), `estilo.py`, `seguridad.py` and `requirements.txt` for Streamlit Community Cloud
- **Smoke test:** `s08-dashboards/verificar_apps.py` runs every app headless

---

## Section 9: Advanced Modelling (Advanced Analytics)

**Directory:** `s09-modelado/`
**Size:** 17 MB | **Modules:** 6 | **Duration:** Advanced

### Purpose
Master advanced statistical and time series modelling techniques.

### Modules

#### M51: Regression Analysis
- **Topics:**
  - Multiple regression
  - Regression diagnostics
  - Assumption checking
  - Model selection
  - Interpretation and inference
- **Resources:**
  - `m51-analisis-de-regresion-solucion.pdf` (2 files)
  - Jupyter notebook: `m51-analisis-de-regresion-solucion.ipynb`
- **Dataset:** Housing price data
- **Tools:** Statsmodels, Scikit-learn
- **Learning Outcome:** Conduct comprehensive regression analysis

#### M52: Hypothesis Testing & Statistical Inference
- **Topics:**
  - Test selection
  - Effect sizes
  - Power analysis
  - Multiple testing correction
- **Resources:**
  - `m52-pruebas-de-hipotesis-solucion.pdf` (2 files)
  - Jupyter notebook: `m52-pruebas-de-hipotesis-solucion.ipynb`
- **Dataset:** Housing data
- **Prerequisites:** M32-M34
- **Learning Outcome:** Conduct rigorous hypothesis tests

#### M53: Regression Models for Prediction
- **Topics:**
  - Model performance metrics
  - Cross-validation
  - Regularization
  - Feature selection
  - Comparison of models
- **Resources:**
  - `m53-modelos-de-regresion-solucion.pdf` (2 files)
  - Jupyter notebook: `m53-modelos-de-regresion-solucion.ipynb`
- **Dataset:** Advertising data
- **Tools:** Scikit-learn
- **Learning Outcome:** Build predictive regression models

#### M54: Time Series Analysis
- **Topics:**
  - Time series components
  - Stationarity testing
  - Autocorrelation and partial autocorrelation
  - Decomposition methods
- **Resources:**
  - `m54-series-de-tiempo-solucion.pdf` (2 files)
  - Python script: `m54-series-de-tiempo-solucion.py`
- **Tools:** Statsmodels, Pandas
- **Learning Outcome:** Analyze time series data

#### M55: AR(p) Models (AutoRegressive)
- **Topics:**
  - AR model fundamentals
  - ACF and PACF
  - Order selection
  - Model fitting and forecasting
- **Resources:**
  - `m55-modelos-ar-solucion.pdf` (2 files)
  - Jupyter notebook: `m55-modelos-ar-solucion.ipynb`
- **Tools:** Statsmodels
- **Prerequisites:** M54
- **Learning Outcome:** Implement AR models

#### M56: ARIMA Models
- **Topics:**
  - ARIMA framework
  - I (Integration) component
  - MA (Moving Average) component
  - ARIMA order selection
  - Forecasting with ARIMA
- **Resources:**
  - `m56-modelos-arima-solucion.pdf` (2 files)
  - Jupyter notebook: `m56-modelos-arima-solucion.ipynb`
- **Dataset:** New York temperature data
- **Tools:** Statsmodels
- **Prerequisites:** M54-M55
- **Learning Outcome:** Build and forecast with ARIMA models

---

## Module 57: Storytelling with Data

**Directory:** `s10-storytelling/m57-storytelling/`
**Size:** 7.8 MB | **Duration:** 1 module

### Purpose
Master data storytelling and communication for business audiences.

### Content

#### Topics
- Data visualization principles
- Narrative construction
- Audience analysis
- Presentation techniques
- Visual design for communication
- Business storytelling

#### Resources
- Theory PDF: `m57-storytelling-solucion.pdf` (2 files)
- Practical Jupyter notebook: `m57-storytelling-solucion.ipynb`
  - Real data examples
  - Visualization techniques
  - Storytelling patterns
- UN Economic Activity Dataset: `valor-agregado-bruto-por-actividad.csv`
- Best practices guide: `M57-Guide.md`

#### Key Concepts
- Hook (Data discovery)
- Context (Data setting)
- Conflict (Data insight)
- Resolution (Data action)

#### Learning Outcome
Communicate data insights effectively to non-technical audiences

---

## Learning Paths & Prerequisites

### Sequential Learning Path
```
S02 (Foundations)
    ↓
S03 (Methodology)
    ↓
S04 (Supervised Learning) + S06 (Statistics) parallel
    ↓
S07 (SQL)
    ↓
S08 (Dashboards)
    ↓
S09 (Advanced Modelling)
    ↓
M57 (Storytelling)
    ↓
Projects (Integration)
```

### By Technology Interest
**Data Science/ML Path:**
- S02-S03 (Foundation)
- S04 (Machine Learning)
- S06 (Statistics)
- Projects P01, P02

**Data Engineering/SQL Path:**
- S02-S03 (Foundation)
- S07 (SQL)
- Project P04

**Business Intelligence Path:**
- S02-S03 (Foundation)
- S06 (Statistics basics)
- S08 (Dashboards)
- Project P05

**Full Stack Path:**
- All sections S02-S09
- M57 (Storytelling)
- All projects

---

## Time Estimates by Module

| Module | Scope | Estimated Hours |
|--------|-------|-----------------|
| M13-M16 | Data Science Fundamentals | 8-12 |
| M17-M20 | Methodology | 12-16 |
| M21-M26 | Supervised Learning | 40-60 |
| M32-M34 | Statistics | 20-30 |
| M35-M43 | SQL | 30-50 |
| M44-M50 | Dashboards (BI) | 40-60 |
| M51-M56 | Advanced Modelling | 40-60 |
| M57 | Storytelling | 8-12 |
| P01-P05 | Projects | 60-100 |
| **Total** | **Full Program** | **250-400 hours** |

---

**Module Guide Updated:** 2026
**Total Modules:** 56+ across 8 sections
**Capstone Projects:** 4
**Datasets:** 12+
