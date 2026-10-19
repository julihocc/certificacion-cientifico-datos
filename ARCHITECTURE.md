# Repository Architecture & Technical Documentation

## Overview

This document provides a comprehensive technical overview of the Data Scientist Program repository structure, organization, and content details.

---

## Directory Tree Structure

```
certificacion-cientifico-datos/
│
├── README.md                      # Main repository documentation
├── README.pdf                     # PDF version of README
├── .gitignore                     # Git ignore configuration
├── .gitattributes                 # Git attributes
│
├── s01-programacion/                         # Section 1: Python Programming (12 modules)
│   ├── m01-introduccion-a-python/           # Module 1: Introduction to Python
│   ├── m02-estructuras-y-tipos-de-datos/    # Module 2: Data Structures & Types
│   ├── m03-instrucciones-de-control/        # Module 3: Control Statements
│   ├── m04-ciclos/                          # Module 4: Loops
│   ├── m05-funciones/                       # Module 5: Functions
│   ├── m06-programacion-orientada-a-objetos/ # Module 6: Object-Oriented Programming
│   ├── m07-pandas/                          # Module 7: Pandas
│   ├── m08-numpy/                           # Module 8: NumPy
│   ├── m09-visualizacion-1/                 # Module 9: Visualization I
│   ├── m10-visualizacion-2/                 # Module 10: Visualization II
│   ├── m11-funciones-avanzadas/             # Module 11: Advanced Functions
│   └── m12-modulos-y-paquetes/              # Module 12: Modules & Packages
│
├── s02-ciencia-de-datos/                    # Section 2: Data Science Fundamentals
│   ├── m13-historia-contexto-y-definiciones/ # Module 13: History & Definitions
│   ├── m14-tipos-de-analitica/              # Module 14: Types of Analytics
│   ├── m15-soluciones-basadas-en-datos/     # Module 15: Solution-Based Approaches
│   └── m16-aplicacion-de-analitica/         # Module 16: Analytics Applications (Spotify)
│
├── s03-metodologia/                         # Section 3: Methodologies & Frameworks
│   ├── m17-metodologia/                     # Module 17: Data Science Methodology
│   ├── m18-kdd-crisp-dm/                    # Module 18: KDD & CRISP-DM
│   ├── m19-tdsp-bspf-y-orange-1/            # Module 19: TDSP Framework
│   └── m20-agile-data-science-y-orange-2/   # Module 20: Data Mining with Orange
│
├── s04-aprendizaje-supervisado/             # Section 4: Supervised Learning (7 modules)
│   ├── m21-regresion-lineal-simple/         # Simple Linear Regression
│   ├── m22-regresion-regularizada/          # Regularized Regression
│   ├── m23-knn/                             # K-Nearest Neighbors (KNN)
│   ├── m24-svm/                             # Support Vector Machines (SVM)
│   ├── m25-metodos-de-ensamble/             # Ensemble Methods (Bagging, Boosting)
│   └── m26-regresion-logistica/             # Logistic Regression
│
├── s05-aprendizaje-no-supervisado/          # Section 5: Unsupervised Learning (5 modules)
│   ├── m27-clustering-jerarquico/           # Hierarchical Clustering
│   ├── m28-kmeans/                          # K-Means
│   ├── m29-pca/                             # Principal Component Analysis (PCA)
│   ├── m30-svd/                             # Singular Value Decomposition (SVD)
│   └── m31-agrupamiento-knn/                # KNN-based Clustering
│
├── s06-estadistica/                         # Section 6: Statistics (3 modules)
│   ├── m32-estadistica-descriptiva/         # Descriptive Statistics
│   ├── m33-estadistica-inferencial/         # Inferential Statistics (Hypothesis Testing)
│   └── m34-estadistica-avanzada/            # Advanced Statistics (Regression)
│
├── s07-sql/                                 # Section 7: SQL & Databases (9 modules, 52 scripts)
│   ├── m35-introduccion-a-sql/              # SQL Introduction
│   ├── m36-operaciones-en-tablas/           # Table Operations (10 scripts)
│   ├── m37-operaciones-con-multiples-tablas/ # Multi-table Operations (8 scripts)
│   ├── m38-agrupacion-y-particionamiento/   # Aggregation & Partitioning
│   ├── m39-sql-avanzado/                    # Advanced SQL (6 scripts)
│   ├── m40-sqlite-con-python/               # SQLite with Python
│   ├── m41-importacion-y-consultas-sql/     # SQL Import & Queries
│   ├── m42-consultas-avanzadas-sql/         # Advanced SQL Queries
│   └── m43-temas-avanzados-sql/             # Advanced Topics
│
├── s08-power-bi/                            # Section 8: Business Intelligence (146 MB)
│   ├── m44-preparacion-de-datos/            # Data Preparation
│   ├── m45-modelado-de-datos/               # Data Modelling
│   ├── m46-formato-condicional/             # Conditional Formatting
│   ├── m47-dax/                             # DAX (Data Analysis Expressions)
│   ├── m48-objetos-dinamicos/               # Dynamic Objects
│   ├── m49-diseno-de-dashboards/            # Dashboard Design
│   ├── m50-publicacion-de-dashboards/       # Publishing Dashboards
│   └── practica-ventas/                     # Practice dashboard & sales datasets
│
├── s09-modelado/                            # Section 9: Advanced Modelling (6 modules)
│   ├── m51-analisis-de-regresion/           # Regression Analysis
│   ├── m52-pruebas-de-hipotesis/            # Hypothesis Testing
│   ├── m53-modelos-de-regresion/            # Regression Models
│   ├── m54-series-de-tiempo/                # Time Series Analysis
│   ├── m55-modelos-ar/                      # AR(p) Models (AutoRegressive)
│   └── m56-modelos-arima/                   # ARIMA Models
│
├── s10-storytelling/                        # Section 10: Data Storytelling (7.8 MB)
│   └── m57-storytelling/                    # Module 57: notebook + UN economic activity dataset
│
└── proyectos/                               # Capstone Projects (95 MB)
    ├── p01-resenas-de-apps/                 # User clustering analysis (7.7 MB)
    ├── p02-aprendizaje-supervisado/         # Prediction modeling (76+ MB)
    ├── p03-segmentacion-de-clientes/        # Customer segmentation (unsupervised learning)
    ├── p04-analisis-de-peliculas-sql/       # Movie database analysis (1.5+ MB)
    └── p05-dashboard-covid/                 # COVID-19 dashboard
```

**Naming convention:** all folders and files use lowercase ASCII kebab-case Spanish names. Sections are `sNN-tema/`, modules are `mNN-tema/` (numbered globally M01–M57), projects are `proyectos/pNN-tema/`, and each module's main deliverable is named after its folder: `mNN-tema.{ipynb,pdf,md}`.

---

## File Type Distribution

### Code & Notebooks (103 files)
| Type | Count | Size | Primary Use |
|------|-------|------|------------|
| Jupyter Notebooks (.ipynb) | 21 | Variable | Data analysis, model development, exploration |
| Python Scripts (.py) | 3 | <10 KB | Preprocessing, utilities |
| SQL Scripts (.sql) | 52 | ~16 MB | Database queries, exercises, solutions |
| **Total** | **76** | **~16+ MB** | **Executable code** |

### Data Files (30 files)
| Type | Count | Format | Use Cases |
|------|-------|--------|-----------|
| CSV Datasets | 30 | Tabular | Analysis datasets, machine learning, exercises |
| ZIP Archives | 1 | Compressed | Large dataset storage (55 MB sales data) |
| **Total** | **31** | **Mixed** | **Data storage** |

### Documentation (178 files)
| Type | Count | Size | Purpose |
|------|-------|------|---------|
| PDF Documents | 78 | ~50 MB | Class materials, reports, solutions |
| Markdown Guides | 26 | ~500 KB | Instructions, theory, exercises |
| PNG Images | 85 | ~20 MB | Visualizations, screenshots, diagrams |
| **Total** | **189** | **~70+ MB** | **Reference & documentation** |

### Configuration Files
- `.gitignore` - Standard Python/data science exclusions
- `.gitattributes` - Git file handling configuration
- `README.md` / `README.pdf` - Repository documentation

---

## Module Organization

### Section S02 `s02-ciencia-de-datos/` (1.8 MB, 4 modules)
**Focus:** Foundational concepts and theory

| Module | Topic | Resources | Datasets |
|--------|-------|-----------|----------|
| M13 | Data Science History & Definitions | 1-2 PDFs, 1 Markdown | - |
| M14 | Types of Analytics | PDF guide, exercises | - |
| M15 | Solution-Based Approaches | PDF, theory | - |
| M16 | Analytics Applications | PDF, case study | Spotify data |

### Section S03 `s03-metodologia/` (2.6 MB, 4 modules)
**Focus:** Data science frameworks and workflows

| Module | Topic | Resources | Tools |
|--------|-------|-----------|-------|
| M17 | Data Science Methodology | 2 PDFs, markdown | - |
| M18 | KDD & CRISP-DM | 2 PDFs, theory | - |
| M19 | TDSP Framework | 1 PDF | - |
| M20 | Data Mining | Orange workflows (.ows), PDF | Orange ML |

### Section S04 `s04-aprendizaje-supervisado/` (6.7 MB, 7 modules)
**Focus:** Machine learning algorithms

| Module | Algorithm | Resources | Datasets |
|--------|-----------|-----------|----------|
| M21 | Simple Linear Regression | 2 PDFs, jupyter notebook | GDP data |
| M22 | Regularized Regression | 2 PDFs, exercises | - |
| M23 | K-Nearest Neighbors | 2 PDFs, documentation | Various |
| M24 | Support Vector Machines | 2 PDFs | - |
| M25 | Ensemble Methods | 3 PDFs, python script | - |
| M26 | Logistic Regression | 2 PDFs, python script | - |

### Section S06 `s06-estadistica/` (2.8 MB, 3 modules)
**Focus:** Statistical analysis and hypothesis testing

| Module | Topic | Resources | Datasets |
|--------|-------|-----------|----------|
| M32 | Descriptive Statistics | 2 PDFs | - |
| M33 | Inferential Statistics | 3 PDFs, jupyter notebook | Marketing data |
| M34 | Advanced Statistics | 2 PDFs, jupyter notebook | Housing price data |

### Section S07 `s07-sql/` (16 MB, 9 modules)
**Focus:** Database and SQL expertise

| Module | Topic | SQL Scripts | Exercises | Solutions |
|--------|-------|-------------|-----------|-----------|
| M35 | SQL Introduction | 2 | 2 | 2 |
| M36 | Table Operations | 4 | 3 | 3 |
| M37 | Multi-table Operations | 3 | 3 | 2 |
| M38 | Aggregation & Partitioning | 2 | 2 | 2 |
| M39 | Advanced SQL | 6 | 2 | 4 |
| M40 | SQLite with Python | 3 | 2 | 1 |
| M41 | SQL Import & Queries | 4 | 2 | 2 |
| M42 | Advanced Queries | 4 | 2 | 2 |
| M43 | Advanced Topics | 4 | 2 | 2 |
| **Total** | | **32 scripts** | **20 files** | Many integrated |

**Database:** DVD Rental Database (dvdrental) with SQL restore scripts

### Section S08 `s08-power-bi/` (146 MB, 7 modules + `practica-ventas/`)
**Focus:** Business intelligence and dashboard development

| Module | Topic | Resources | File Size |
|--------|-------|-----------|-----------|
| M44 | Data Preparation | 2 PDFs, .pbix file | 5-10 MB |
| M45 | Data Modelling | 3 PDFs, .pbix file | 8-12 MB |
| M46 | Conditional Formatting | 2 PDFs, .pbix file | 5 MB |
| M47 | DAX (Expressions) | 3 PDFs, .pbix file | 8 MB |
| M48 | Dynamic Objects | 2 PDFs, .pbix file | 6 MB |
| M49 | Dashboard Design | 3 PDFs, .pbix file | 10 MB |
| M50 | Publishing | 2 PDFs | 2 MB |
| `practica-ventas/` | Sample Dashboards | .pbix files, sales data | 55 MB (ZIP) |

**Datasets:** Sales Extract Dataset (55 MB compressed), various analysis data

### Section S09 `s09-modelado/` (17 MB, 6 modules)
**Focus:** Advanced statistical and time series modelling

| Module | Topic | Resources | Datasets |
|--------|-------|-----------|----------|
| M51 | Regression Analysis | 2 PDFs, jupyter | Housing data |
| M52 | Hypothesis Testing | 2 PDFs, jupyter | Housing data |
| M53 | Regression Models | 2 PDFs, jupyter | Advertising data |
| M54 | Time Series | 2 PDFs, python script | Climate/economic data |
| M55 | AR(p) Models | 2 PDFs, jupyter | Time series data |
| M56 | ARIMA Models | 2 PDFs, jupyter | NY temperature data |

### Section S10 `s10-storytelling/`: Module M57 Storytelling (7.8 MB, 1 module)
**Focus:** Data visualization and presentation

| Component | Content | Resources |
|-----------|---------|-----------|
| Theory | Data storytelling concepts | 2 PDFs |
| Practice | Jupyter notebook with examples | Interactive notebook |
| Data | UN economic activity analysis | CSV dataset |

---

## Capstone Projects

### P01: User Reviews Analysis (7.7 MB)
**Objective:** Unsupervised learning - clustering analysis
**Structure:**
```
proyectos/p01-resenas-de-apps/
├── apps.csv                       # App metadata dataset
├── user-reviews.csv               # 7.7 MB review dataset
├── p01-resenas-de-apps-solucion.ipynb      # Clustering analysis
└── p01-resenas-de-apps-solucion.pdf        # Formal report
```
**Technologies:** Python, Pandas, Scikit-learn, Matplotlib
**Key Skills:** Data clustering, dimensionality reduction, pattern recognition

### P02: Heart Attack Prediction (76+ MB)
**Objective:** Supervised learning - medical risk prediction
**Structure:**
```
proyectos/p02-aprendizaje-supervisado/
├── heart-attack.csv               # 11 KB medical data
├── mnist.csv                      # 76 MB MNIST digits
├── imagen-muestra.png             # Sample digit image
├── p02-aprendizaje-supervisado-solucion.ipynb  # ML model development
└── p02-aprendizaje-supervisado-solucion.pdf    # Analysis & results
```
**Technologies:** Python, Scikit-learn, TensorFlow, XGBoost
**Key Skills:** Feature engineering, model selection, classification, cross-validation

### P04: Movie Data Analysis (1.5+ MB)
**Objective:** SQL and data analytics - relational database analysis
**Structure:**
```
proyectos/p04-analisis-de-peliculas-sql/
├── dvdrental/                     # DVD rental database files
│   └── restore.sql                # Database restore script
├── p04-analisis-de-peliculas-sql-solucion.sql  # SQL analysis queries
├── p04-avance-parte-4.sql         # SQL analysis queries (part 4 progress)
├── p04-analisis-de-peliculas-sql-solucion.pdf  # 1.5 MB comprehensive report
├── ejercicio-01.png … ejercicio-15.png  # 15 PNG screenshots
└── p04-analisis-de-peliculas-sql-solucion.md   # Detailed documentation
```
**Technologies:** SQL, SQLite, Database design, Data visualization
**Key Skills:** Complex SQL queries, data aggregation, reporting, visualization

### P05: PowerBI COVID-19 Analysis
**Objective:** Business intelligence - pandemic data dashboard
**Structure:**
```
proyectos/p05-dashboard-covid/
├── p05-dashboard-covid-solucion.pbix       # PowerBI file (data embedded)
└── p05-dashboard-covid-solucion.pdf        # Analysis report
```
**Technologies:** Microsoft PowerBI, DAX, Data modeling
**Key Skills:** Dashboard design, KPI design, interactive visualization, storytelling

---

## Dataset Inventory

### Educational Datasets
1. **GDP Data** - Economic growth analysis
2. **Heart Attack Medical Data** - 11 KB, health prediction
3. **MNIST Handwritten Digits** - 76 MB, image recognition training
4. **Housing/Real Estate Data** - Regression modeling
5. **Marketing Campaign Data** - Statistical testing, hypothesis validation
6. **Advertising Data** - Regression model training
7. **User Reviews** - 7.7 MB clustering exercise
8. **Movie Rental Database (dvdrental)** - SQL relational database
9. **Sales Extract Dataset** - 55 MB, PowerBI training
10. **Temperature Data (New York)** - Time series analysis
11. **UN Economic Activity Data** - Data storytelling exercise
12. **Spotify Data** - Analytics case study

---

## Technology Stack

### Data Processing & Analysis
- **Pandas:** Data manipulation and transformation
- **NumPy:** Numerical computing
- **SciPy:** Scientific computing

### Machine Learning
- **Scikit-learn:** Classification, regression, clustering, preprocessing
- **XGBoost:** Gradient boosting
- **Statsmodels:** Statistical modelling
- **TensorFlow:** Deep learning (MNIST)

### Visualization
- **Matplotlib:** Static visualizations
- **Seaborn:** Statistical graphics
- **PowerBI:** Business intelligence dashboards
- **Orange:** Visual data mining

### Database & SQL
- **SQLite:** Lightweight database
- **SQL:** Database querying and manipulation

### Environment & Tools
- **Jupyter Notebook:** Interactive Python environment
- **Python 3.x:** Primary programming language
- **Git:** Version control
- **Markdown:** Documentation

---

## Documentation Strategy

### Markdown Guides (26 files)
- Module-level instructions
- Exercise specifications
- Theory explanations
- Project guidelines
- Class summaries

### PDF Documentation (78 files)
- Class materials and slides
- Exercise solutions with evidence
- Project reports
- Best practices guides
- Theory reference materials

### Jupyter Notebooks (21 files)
- Interactive analysis examples
- Code walkthroughs
- Model development
- Data exploration
- Results visualization

### README Files
- Module introductions
- Project overviews
- Navigation guides

---

## Size Distribution

| Component | Size | % of Total |
|-----------|------|-----------|
| s08-power-bi (BI & dashboards) | 146 MB | 49.5% |
| p02-aprendizaje-supervisado (Project) | 76 MB | 25.8% |
| PDF Documentation | ~50 MB | 17% |
| s07-sql (Database & scripts) | 16 MB | 5.4% |
| s09-modelado | 17 MB | 5.8% |
| CSV Datasets | Variable | ~3-4% |
| PNG Images | ~20 MB | 6.8% |
| Other Modules | ~15 MB | 5% |
| **Total** | **295 MB** | **100%** |

---

## Learning Progression

### Phase 1: Foundation (S02–S03)
**Concepts & Frameworks**
- Data science fundamentals
- Analytics types and methodologies
- CRISP-DM and KDD frameworks

### Phase 2: Technical Skills (S04, S06, S07)
**Core Technical Competencies**
- Supervised learning algorithms
- Statistical analysis and testing
- SQL and database querying

### Phase 3: Advanced Tools (S08–S09)
**Professional & Advanced Topics**
- Business intelligence dashboarding
- Advanced time series modelling
- DAX and data modelling

### Phase 4: Integration & Specialization (S10/M57, Projects)
**Capstone & Specialization**
- Data storytelling
- End-to-end project delivery
- Industry-specific applications

---

## Quality Metrics

- **Module Completion:** 56+ modules
- **Project Deliverables:** 4 capstone projects
- **Code Quality:** Python scripts follow data science best practices
- **Documentation:** Comprehensive guides and PDFs
- **Dataset Diversity:** 12+ different datasets across multiple domains
- **Technology Breadth:** 6+ major technologies (Python, SQL, PowerBI, Orange, etc.)

---

## Repository Configuration

**Version Control:** Git
**Platform:** GitHub
**Branch Strategy:** Main branch with feature/learning branches
**File Tracking:** Standard Python/data science .gitignore

---

## Maintenance Notes

- No external dependencies file (requirements.txt not included)
- Self-contained datasets and materials
- Platform-independent content (mostly CSV and notebooks)
- Windows-compatible SQL scripts (dvdrental database)

---

**Last Updated:** 2026
**Repository Type:** Educational Portfolio
**Access:** Public GitHub repository
