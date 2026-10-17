# EBAC Data Scientist Program - Complete Module Guide

## Table of Contents
- [Section 2: Data Science Fundamentals](#section-2-data-science-fundamentals)
- [Section 3: Methodology](#section-3-methodology)
- [Section 4: Supervised Learning](#section-4-supervised-learning)
- [Section 6: Statistics](#section-6-statistics)
- [Section 7: SQL & Databases](#section-7-sql--databases)
- [Section 8: PowerBI & Business Intelligence](#section-8-powerbi--business-intelligence)
- [Section 9: Advanced Modelling](#section-9-advanced-modelling)
- [Module 57: Storytelling with Data](#module-57-storytelling-with-data)

---

## Section 2: Ciencia de Datos (Data Science Fundamentals)

**Directory:** `S02-Ciencia-de-datos/`
**Size:** 1.8 MB | **Modules:** 4 | **Duration:** Introductory

### Purpose
Establish foundational understanding of data science concepts, terminology, and applications.

### Modules

#### M11: History and Definitions of Data Science
- **Topics:**
  - Definition and scope of data science
  - Historical evolution of data science
  - Core concepts and terminology
- **Resources:**
  - Theory PDF: `M11-Data-Science-Definition.pdf`
  - Markdown guide: `M11-Instructions.md`
- **Learning Outcome:** Understand data science as discipline

#### M12: Types of Analytics
- **Topics:**
  - Descriptive analytics
  - Predictive analytics
  - Prescriptive analytics
  - Diagnostic analytics
- **Resources:**
  - Class material: `M12-Analytics-Types.pdf`
  - Exercises: `M12-Exercises.md`
- **Learning Outcome:** Differentiate analytics types

#### M13: Solution-Based Approaches
- **Topics:**
  - Problem-solving frameworks
  - Solution design methodologies
  - Business impact consideration
- **Resources:**
  - PDF guide: `M13-Solutions.pdf`
- **Learning Outcome:** Apply data science to business problems

#### M14: Analytics Applications & Case Studies
- **Topics:**
  - Real-world analytics applications
  - Industry case studies
  - Spotify analytics example
- **Resources:**
  - Case study: `M14-Spotify-Case-Study.pdf`
  - Dataset: `spotify_data.csv`
- **Learning Outcome:** Connect theory to real applications

---

## Section 3: Metodología (Data Science Methodologies)

**Directory:** `S03-Metodología/`
**Size:** 2.6 MB | **Modules:** 4 | **Duration:** Intermediate

### Purpose
Master established data science frameworks and project methodologies.

### Modules

#### M15: Data Science Methodology
- **Topics:**
  - Scientific method application
  - Hypothesis formulation
  - Experiment design
  - Validation approaches
- **Resources:**
  - `M15-Methodology.pdf`
  - `M15-Framework-Guide.md`
- **Prerequisites:** M11-M14
- **Learning Outcome:** Design data science projects methodically

#### M16: KDD and CRISP-DM Frameworks
- **Topics:**
  - Knowledge Discovery in Databases (KDD)
  - CRISP-DM (Cross Industry Standard Process)
  - Framework comparison
  - Implementation steps
- **Resources:**
  - `M16-KDD-CRISP-DM.pdf` (comprehensive guide)
  - `M16-Framework-Details.md`
  - Visual diagrams and flowcharts
- **Learning Outcome:** Apply industry-standard frameworks

#### M17: TDSP (Team Data Science Process)
- **Topics:**
  - Microsoft TDSP framework
  - Team-based project structure
  - Lifecycle phases
  - Deliverables at each stage
- **Resources:**
  - `M17-TDSP-Framework.pdf`
  - Process documentation
- **Learning Outcome:** Plan team data science projects

#### M18: Data Mining with Orange
- **Topics:**
  - Visual data mining concepts
  - Orange software introduction
  - Workflow design
  - Classification and clustering with Orange
- **Resources:**
  - `M18-Orange-Introduction.pdf`
  - Orange workflow files: `workflow_1.ows`, `workflow_2.ows`
  - Tutorial: `M18-Orange-Tutorial.md`
- **Tools:** Orange ML platform
- **Learning Outcome:** Use visual data mining tools

---

## Section 4: Aprendizaje Supervisado (Supervised Learning)

**Directory:** `S04-Aprendizaje-supervisado/`
**Size:** 6.7 MB | **Modules:** 7 | **Duration:** Intermediate-Advanced

### Purpose
Master machine learning algorithms for classification and regression tasks.

### Modules

#### M19: Simple Linear Regression
- **Topics:**
  - Regression fundamentals
  - Ordinary Least Squares (OLS)
  - Model interpretation
  - Assumption validation
- **Resources:**
  - `M19-Linear-Regression.pdf` (theory)
  - `M19-Exercises.pdf`
  - `M19-Analysis.ipynb` (Jupyter notebook)
- **Dataset:** `gdp_data.csv`
- **Tools:** Python, Scikit-learn, Pandas, Matplotlib
- **Learning Outcome:** Implement and interpret linear regression

#### M20: Regularized Regression
- **Topics:**
  - Ridge regression (L2 regularization)
  - Lasso regression (L1 regularization)
  - Elastic Net
  - Hyperparameter tuning
- **Resources:**
  - `M20-Regularization.pdf`
  - `M20-Exercise-Guide.md`
- **Prerequisites:** M19
- **Learning Outcome:** Apply regularization techniques

#### M21: K-Nearest Neighbors (KNN)
- **Topics:**
  - KNN algorithm mechanics
  - Distance metrics
  - Hyperparameter selection (k value)
  - Classification and regression with KNN
- **Resources:**
  - `M21-KNN.pdf` (comprehensive guide)
  - `M21-Implementation.md`
- **Tools:** Scikit-learn
- **Learning Outcome:** Implement KNN classifier/regressor

#### M22: Support Vector Machines (SVM)
- **Topics:**
  - SVM theory and math
  - Kernel methods
  - Linear and non-linear SVM
  - Multi-class classification
- **Resources:**
  - `M22-SVM.pdf`
  - `M22-Practical-Guide.md`
- **Tools:** Scikit-learn
- **Learning Outcome:** Apply SVM to classification problems

#### M24: Ensemble Methods
- **Topics:**
  - Bagging and Bootstrap Aggregating
  - Random Forests
  - Boosting concepts
  - Gradient Boosting
- **Resources:**
  - `M24-Ensemble-Methods.pdf` (3 files)
  - Python script: `M24-preprocess.py`
  - Exercises and examples
- **Tools:** Scikit-learn, XGBoost
- **Learning Outcome:** Build ensemble models

#### M25: Logistic Regression
- **Topics:**
  - Logistic function and odds ratios
  - Binary classification
  - Multi-class classification
  - Model evaluation for classification
- **Resources:**
  - `M25-Logistic-Regression.pdf`
  - Python script: `M25-preprocess.py`
  - Practical examples
- **Tools:** Scikit-learn
- **Prerequisites:** M19 (recommended)
- **Learning Outcome:** Implement logistic regression classifier

---

## Section 6: Estadística (Statistics)

**Directory:** `S06-Estadística/`
**Size:** 2.8 MB | **Modules:** 3 | **Duration:** Intermediate

### Purpose
Master statistical analysis and hypothesis testing for data-driven decisions.

### Modules

#### M31: Descriptive Statistics
- **Topics:**
  - Measures of central tendency
  - Measures of dispersion
  - Distribution analysis
  - Data summarization
- **Resources:**
  - `M31-Descriptive-Stats.pdf` (2 files)
  - Markdown guide: `M31-Guide.md`
- **Learning Outcome:** Summarize data statistically

#### M32: Inferential Statistics & Hypothesis Testing
- **Topics:**
  - Probability distributions
  - Confidence intervals
  - Hypothesis testing (t-tests, chi-square)
  - P-values and significance
  - Type I and Type II errors
- **Resources:**
  - `M32-Inferential-Stats.pdf` (3 files)
  - Jupyter notebook: `M32-Hypothesis-Testing.ipynb`
- **Dataset:** Marketing campaign data
- **Tools:** SciPy, Statsmodels
- **Prerequisites:** M31 (recommended)
- **Learning Outcome:** Conduct hypothesis tests

#### M33: Advanced Statistics & Regression Analysis
- **Topics:**
  - Multiple regression
  - ANOVA (Analysis of Variance)
  - Regression diagnostics
  - Model validation
- **Resources:**
  - `M33-Advanced-Stats.pdf` (2 files)
  - Jupyter notebook: `M33-Regression-Analysis.ipynb`
- **Dataset:** Housing price data
- **Tools:** Statsmodels, Scipy
- **Prerequisites:** M32
- **Learning Outcome:** Conduct advanced statistical analysis

---

## Section 7: SQL (Database & Queries)

**Directory:** `S07-SQL/`
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
- `dvdrental.sql` - Database schema and restore script
- 16 tables including: customers, films, actors, rentals, payments
- ~3000+ records
**Use Cases:** Inventory management, rental analysis, customer queries

---

## Section 8: PowerBI (Business Intelligence)

**Directory:** `S08-PowerBI/`
**Size:** 146 MB | **Modules:** 7 + Practice | **Duration:** Advanced

### Purpose
Master business intelligence dashboarding and data visualization with Microsoft PowerBI.

### Modules

#### M45: Data Preparation
- **Topics:**
  - Data cleaning in PowerBI
  - Data transformation
  - Data quality checks
  - Power Query editor
- **Resources:**
  - `M45-Data-Prep.pdf` (2 files)
  - `M45-Sample.pbix` (PowerBI file)
  - Practical exercises
- **Dataset:** Sales data sample
- **Tools:** Microsoft PowerBI
- **Learning Outcome:** Prepare data for visualization

#### M46: Data Modelling
- **Topics:**
  - Star schema design
  - Fact and dimension tables
  - Relationships
  - Cardinality configuration
- **Resources:**
  - `M46-Modelling.pdf` (3 files)
  - `M46-Sample.pbix` (PowerBI file with models)
- **Prerequisites:** M45
- **Learning Outcome:** Design data models

#### M47: Conditional Formatting
- **Topics:**
  - Background color formatting
  - Font color rules
  - Data bars
  - Icon sets
- **Resources:**
  - `M47-Formatting.pdf` (2 files)
  - `M47-Example.pbix`
- **Learning Outcome:** Apply conditional formatting

#### M48: DAX (Data Analysis Expressions)
- **Topics:**
  - DAX functions and syntax
  - Calculated columns
  - Measures
  - Time intelligence functions
  - Context and evaluation
- **Resources:**
  - `M48-DAX.pdf` (3 files - comprehensive)
  - `M48-Examples.pbix` (DAX formulas)
  - Formula library
- **Prerequisites:** M46
- **Learning Outcome:** Write DAX formulas

#### M49: Dynamic Objects
- **Topics:**
  - Dynamic titles and labels
  - Conditional visibility
  - Bookmarks and navigation
  - Drill-through pages
  - Parameters and slicers
- **Resources:**
  - `M49-Dynamic.pdf` (2 files)
  - `M49-Interactive.pbix`
- **Learning Outcome:** Create interactive dashboards

#### M50: Dashboard Design
- **Topics:**
  - Visual hierarchy
  - Color theory
  - Layout principles
  - User experience
  - Design best practices
- **Resources:**
  - `M50-Design.pdf` (3 files)
  - `M50-Dashboard.pbix` (example dashboard)
  - Design guidelines
- **Prerequisites:** M47-M49 (recommended)
- **Learning Outcome:** Design professional dashboards

#### M51: Publishing & Distribution
- **Topics:**
  - PowerBI Service
  - App publishing
  - Sharing and permissions
  - Row-level security (RLS)
  - Refresh scheduling
- **Resources:**
  - `M51-Publishing.pdf` (2 files)
  - Deployment guides
- **Learning Outcome:** Publish dashboards

### Practice & Datasets
- **Sales Dataset:** 55 MB (wetransfer_sales-extract-dataset_2022-06-07_2023.zip)
  - Contains comprehensive sales data
  - Multiple tables and dimensions
  - Real-world complexity
- **Sample Dashboards:** Multiple .pbix files with examples
- **Practice Exercises:** Guided dashboard creation

---

## Section 9: Advanced Modelling (Advanced Analytics)

**Directory:** `S09-Modelling/`
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
  - `M51-Regression.pdf` (2 files)
  - Jupyter notebook: `M51-Analysis.ipynb`
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
  - `M52-Hypothesis.pdf` (2 files)
  - Jupyter notebook: `M52-Testing.ipynb`
- **Dataset:** Housing data
- **Prerequisites:** M31-M33
- **Learning Outcome:** Conduct rigorous hypothesis tests

#### M53: Regression Models for Prediction
- **Topics:**
  - Model performance metrics
  - Cross-validation
  - Regularization
  - Feature selection
  - Comparison of models
- **Resources:**
  - `M53-Predictive.pdf` (2 files)
  - Jupyter notebook: `M53-Models.ipynb`
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
  - `M54-TimeSeries.pdf` (2 files)
  - Python script: `M54-TimeSeriesAnalysis.py`
- **Tools:** Statsmodels, Pandas
- **Learning Outcome:** Analyze time series data

#### M55: AR(p) Models (AutoRegressive)
- **Topics:**
  - AR model fundamentals
  - ACF and PACF
  - Order selection
  - Model fitting and forecasting
- **Resources:**
  - `M55-ARIMA-Part1.pdf` (2 files)
  - Jupyter notebook: `M55-AR-Models.ipynb`
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
  - `M56-ARIMA-Part2.pdf` (2 files)
  - Jupyter notebook: `M56-ARIMA-Models.ipynb`
- **Dataset:** New York temperature data
- **Tools:** Statsmodels
- **Prerequisites:** M54-M55
- **Learning Outcome:** Build and forecast with ARIMA models

---

## Module 57: Storytelling with Data

**Directory:** `M57-Storytelling/`
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
- Theory PDF: `M57-Storytelling-Essentials.pdf` (2 files)
- Practical Jupyter notebook: `M57-Examples.ipynb`
  - Real data examples
  - Visualization techniques
  - Storytelling patterns
- UN Economic Activity Dataset: `un_economic_data.csv`
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
S08 (PowerBI)
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
- S08 (PowerBI)
- Project P05

**Full Stack Path:**
- All sections S02-S09
- M57 (Storytelling)
- All projects

---

## Time Estimates by Module

| Module | Scope | Estimated Hours |
|--------|-------|-----------------|
| M11-M14 | Data Science Fundamentals | 8-12 |
| M15-M18 | Methodology | 12-16 |
| M19-M25 | Supervised Learning | 40-60 |
| M31-M33 | Statistics | 20-30 |
| M35-M43 | SQL | 30-50 |
| M45-M51 | PowerBI | 40-60 |
| M51-M56 | Advanced Modelling | 40-60 |
| M57 | Storytelling | 8-12 |
| P01-P05 | Projects | 60-100 |
| **Total** | **Full Program** | **250-400 hours** |

---

**Module Guide Updated:** 2026
**Total Modules:** 56+ across 8 sections
**Capstone Projects:** 4
**Datasets:** 12+
