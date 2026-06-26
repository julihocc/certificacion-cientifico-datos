# Repository Architecture & Technical Documentation

## Overview

This document provides a comprehensive technical overview of the EBAC Data Scientist Program repository structure, organization, and content details.

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
├── S02-Ciencia-de-datos/          # Section 2: Data Science Fundamentals
│   ├── M11/                       # Module 11: History & Definitions
│   ├── M12/                       # Module 12: Types of Analytics
│   ├── M13/                       # Module 13: Solution-Based Approaches
│   └── M14/                       # Module 14: Analytics Applications (Spotify)
│
├── S03-Metodología/               # Section 3: Methodologies & Frameworks
│   ├── M15/                       # Module 15: Data Science Methodology
│   ├── M16/                       # Module 16: KDD & CRISP-DM
│   ├── M17/                       # Module 17: TDSP Framework
│   └── M18/                       # Module 18: Data Mining with Orange
│
├── S04-Aprendizaje-supervisado/   # Section 4: Supervised Learning (7 modules)
│   ├── M19/                       # Simple Linear Regression
│   ├── M20/                       # Regularized Regression
│   ├── M21/                       # K-Nearest Neighbors (KNN)
│   ├── M22/                       # Support Vector Machines (SVM)
│   ├── M23/                       # Ensemble Methods (Bagging, Boosting)
│   ├── M24/                       # Advanced Ensemble Methods
│   └── M25/                       # Logistic Regression
│
├── S06-Estadística/               # Section 6: Statistics (3 modules)
│   ├── M31/                       # Descriptive Statistics
│   ├── M32/                       # Inferential Statistics (Hypothesis Testing)
│   └── M33/                       # Advanced Statistics (Regression)
│
├── S07-SQL/                       # Section 7: SQL & Databases (9 modules, 52 scripts)
│   ├── M35/                       # SQL Introduction
│   ├── M36/                       # Table Operations (10 scripts)
│   ├── M37/                       # Multi-table Operations (8 scripts)
│   ├── M38/                       # Aggregation & Partitioning
│   ├── M39/                       # Advanced SQL (6 scripts)
│   ├── M40/                       # SQLite with Python
│   ├── M41/                       # SQL Import & Queries
│   ├── M42/                       # Advanced SQL Queries
│   └── M43/                       # Advanced Topics
│
├── S08-PowerBI/                   # Section 8: Business Intelligence (146 MB)
│   ├── M45/                       # Data Preparation
│   ├── M46/                       # Data Modelling
│   ├── M47/                       # Conditional Formatting
│   ├── M48/                       # DAX (Data Analysis Expressions)
│   ├── M49/                       # Dynamic Objects
│   ├── M50/                       # Dashboard Design
│   ├── M51/                       # Publishing Dashboards
│   ├── Practice/                  # Practice dashboards & datasets
│   └── wetransfer_sales-*.zip     # 55 MB sales dataset
│
├── S09-Modelling/                 # Section 9: Advanced Modelling (6 modules)
│   ├── M51/                       # Regression Analysis
│   ├── M52/                       # Hypothesis Testing
│   ├── M53/                       # Regression Models
│   ├── M54/                       # Time Series Analysis
│   ├── M55/                       # AR(p) Models (AutoRegressive)
│   └── M56/                       # ARIMA Models
│
├── M57-Storytelling/              # Module 57: Data Storytelling (7.8 MB)
│   ├── Notebook/                  # Jupyter notebooks with examples
│   └── Data/                      # UN economic activity datasets
│
└── Projects/                      # Capstone Projects (95 MB)
    ├── P01-User-Reviews/          # User clustering analysis (7.7 MB)
    ├── P02-Heart-Attack/          # Prediction modeling (76+ MB)
    ├── P04-Movie-Data/            # Movie database analysis (1.5+ MB)
    └── P05-PowerBI-COVID19/       # COVID-19 dashboard
```

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

### Section S02: Ciencia de Datos (1.8 MB, 4 modules)
**Focus:** Foundational concepts and theory

| Module | Topic | Resources | Datasets |
|--------|-------|-----------|----------|
| M11 | Data Science History & Definitions | 1-2 PDFs, 1 Markdown | - |
| M12 | Types of Analytics | PDF guide, exercises | - |
| M13 | Solution-Based Approaches | PDF, theory | - |
| M14 | Analytics Applications | PDF, case study | Spotify data |

### Section S03: Metodología (2.6 MB, 4 modules)
**Focus:** Data science frameworks and workflows

| Module | Topic | Resources | Tools |
|--------|-------|-----------|-------|
| M15 | Data Science Methodology | 2 PDFs, markdown | - |
| M16 | KDD & CRISP-DM | 2 PDFs, theory | - |
| M17 | TDSP Framework | 1 PDF | - |
| M18 | Data Mining | Orange workflows (.ows), PDF | Orange ML |

### Section S04: Aprendizaje Supervisado (6.7 MB, 7 modules)
**Focus:** Machine learning algorithms

| Module | Algorithm | Resources | Datasets |
|--------|-----------|-----------|----------|
| M19 | Simple Linear Regression | 2 PDFs, jupyter notebook | GDP data |
| M20 | Regularized Regression | 2 PDFs, exercises | - |
| M21 | K-Nearest Neighbors | 2 PDFs, documentation | Various |
| M22 | Support Vector Machines | 2 PDFs | - |
| M24 | Ensemble Methods | 3 PDFs, python script | - |
| M25 | Logistic Regression | 2 PDFs, python script | - |

### Section S06: Estadística (2.8 MB, 3 modules)
**Focus:** Statistical analysis and hypothesis testing

| Module | Topic | Resources | Datasets |
|--------|-------|-----------|----------|
| M31 | Descriptive Statistics | 2 PDFs | - |
| M32 | Inferential Statistics | 3 PDFs, jupyter notebook | Marketing data |
| M33 | Advanced Statistics | 2 PDFs, jupyter notebook | Housing price data |

### Section S07: SQL (16 MB, 9 modules)
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

### Section S08: PowerBI (146 MB, 7 modules + Practice)
**Focus:** Business intelligence and dashboard development

| Module | Topic | Resources | File Size |
|--------|-------|-----------|-----------|
| M45 | Data Preparation | 2 PDFs, .pbix file | 5-10 MB |
| M46 | Data Modelling | 3 PDFs, .pbix file | 8-12 MB |
| M47 | Conditional Formatting | 2 PDFs, .pbix file | 5 MB |
| M48 | DAX (Expressions) | 3 PDFs, .pbix file | 8 MB |
| M49 | Dynamic Objects | 2 PDFs, .pbix file | 6 MB |
| M50 | Dashboard Design | 3 PDFs, .pbix file | 10 MB |
| M51 | Publishing | 2 PDFs | 2 MB |
| Practice | Sample Dashboards | .pbix files, sales data | 55 MB (ZIP) |

**Datasets:** Sales Extract Dataset (55 MB compressed), various analysis data

### Section S09: Modelling (17 MB, 6 modules)
**Focus:** Advanced statistical and time series modelling

| Module | Topic | Resources | Datasets |
|--------|-------|-----------|----------|
| M51 | Regression Analysis | 2 PDFs, jupyter | Housing data |
| M52 | Hypothesis Testing | 2 PDFs, jupyter | Housing data |
| M53 | Regression Models | 2 PDFs, jupyter | Advertising data |
| M54 | Time Series | 2 PDFs, python script | Climate/economic data |
| M55 | AR(p) Models | 2 PDFs, jupyter | Time series data |
| M56 | ARIMA Models | 2 PDFs, jupyter | NY temperature data |

### Module M57: Storytelling (7.8 MB, 1 module)
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
P01-User-Reviews/
├── README.md                      # Project documentation
├── User-Reviews.csv               # 7.7 MB review dataset
├── Analysis-Jupyter.ipynb         # Clustering analysis
├── Project-Report.pdf             # Formal report
└── Visualizations/                # PNG charts and graphs
```
**Technologies:** Python, Pandas, Scikit-learn, Matplotlib
**Key Skills:** Data clustering, dimensionality reduction, pattern recognition

### P02: Heart Attack Prediction (76+ MB)
**Objective:** Supervised learning - medical risk prediction
**Structure:**
```
P02-Heart-Attack/
├── README.md                      # Project guide
├── medical_dataset.csv            # 11 KB medical data
├── mnist_data/                    # 76 MB MNIST digits
├── Prediction-Model.ipynb         # ML model development
├── Project-Report.pdf             # Analysis & results
└── Model-Evaluation/              # Performance metrics
```
**Technologies:** Python, Scikit-learn, TensorFlow, XGBoost
**Key Skills:** Feature engineering, model selection, classification, cross-validation

### P04: Movie Data Analysis (1.5+ MB)
**Objective:** SQL and data analytics - relational database analysis
**Structure:**
```
P04-Movie-Data/
├── README.md                      # Project documentation
├── dvdrental/                     # DVD rental database files
│   ├── dvdrental.sql              # Database restore script
│   └── backup/                    # Database backup
├── queries/                       # SQL analysis scripts
│   ├── inventory-analysis.sql     # Inventory queries
│   └── revenue-analysis.sql       # Financial queries
├── Analysis-Report.pdf            # 1.5 MB comprehensive report
├── Visualizations/                # 15+ PNG screenshots
└── Analysis-Markdown.md           # Detailed documentation
```
**Technologies:** SQL, SQLite, Database design, Data visualization
**Key Skills:** Complex SQL queries, data aggregation, reporting, visualization

### P05: PowerBI COVID-19 Analysis
**Objective:** Business intelligence - pandemic data dashboard
**Structure:**
```
P05-PowerBI-COVID19/
├── README.md                      # Project overview
├── covid_dashboard.pbix           # PowerBI file
├── covid_data.csv                 # COVID-19 statistics
├── Dashboard-Report.pdf           # Analysis report
└── Screenshots/                   # Dashboard visualizations
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
| S08-PowerBI (BI & dashboards) | 146 MB | 49.5% |
| P02-Heart-Attack (Project) | 76 MB | 25.8% |
| PDF Documentation | ~50 MB | 17% |
| S07-SQL (Database & scripts) | 16 MB | 5.4% |
| S09-Modelling | 17 MB | 5.8% |
| CSV Datasets | Variable | ~3-4% |
| PNG Images | ~20 MB | 6.8% |
| Other Modules | ~15 MB | 5% |
| **Total** | **295 MB** | **100%** |

---

## Learning Progression

### Phase 1: Foundation (S02-S03)
**Concepts & Frameworks**
- Data science fundamentals
- Analytics types and methodologies
- CRISP-DM and KDD frameworks

### Phase 2: Technical Skills (S04, S06, S07)
**Core Technical Competencies**
- Supervised learning algorithms
- Statistical analysis and testing
- SQL and database querying

### Phase 3: Advanced Tools (S08-S09)
**Professional & Advanced Topics**
- Business intelligence dashboarding
- Advanced time series modelling
- DAX and data modelling

### Phase 4: Integration & Specialization (M57, Projects)
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
