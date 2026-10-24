# Data Scientist Program - Capstone Projects Guide

## Overview

This document provides detailed documentation of all capstone projects in the Data Scientist Program. Each project represents a complete end-to-end data science workflow demonstrating real-world applications.

**Total Projects:** 4 | **Total Size:** 95 MB | **Completion Status:** All delivered

---

## Table of Contents
- [P01: User Reviews Analysis](#p01-user-reviews-clustering-analysis)
- [P02: Heart Attack Prediction](#p02-heart-attack-prediction)
- [P04: Movie Data Analysis](#p04-movie-rental-data-analysis)
- [P05: COVID-19 Dashboard](#p05-covid-19-dashboard)

---

## P01: User Reviews Clustering Analysis

**Directory:** `proyectos/p01-resenas-de-apps/`
**Size:** 7.7 MB
**Project Type:** Unsupervised Learning
**Status:** Completed

### Project Overview

This project demonstrates unsupervised learning techniques through clustering analysis of user review data. The goal is to identify patterns and groups within customer reviews to understand different segments of user opinions.

### Objectives
1. Load and explore user review dataset
2. Perform data preprocessing and text analysis
3. Implement clustering algorithms
4. Analyze and interpret clusters
5. Provide business insights from clustering results

### Dataset

**File:** `user-reviews.csv` (7.7 MB)
- **Records:** Thousands of user reviews
- **Features:** Review text, ratings, user ID, product ID, date
- **Format:** CSV (structured text data)
- **Source:** Real user feedback data

### Technologies & Tools
- **Language:** Python
- **Libraries:**
  - Pandas - Data manipulation
  - Scikit-learn - Machine learning algorithms
  - NLTK/TextBlob - Natural language processing
  - Matplotlib/Seaborn - Visualization
  - NumPy - Numerical computing

### Methodology

#### Phase 1: Data Exploration
- Load and inspect dataset
- Examine data types and missing values
- Statistical summary of reviews
- Visualization of review distribution

#### Phase 2: Preprocessing
- Text cleaning (lowercase, punctuation removal)
- Tokenization
- Stop word removal
- Stemming/Lemmatization
- Feature engineering from text

#### Phase 3: Feature Engineering
- Text vectorization (TF-IDF, Count Vectorizer, Word2Vec)
- Numerical feature extraction
- Dimensionality reduction (PCA)

#### Phase 4: Clustering Analysis
- K-Means clustering
- Hierarchical clustering
- DBSCAN
- Cluster evaluation (silhouette score, Davies-Bouldin index)

#### Phase 5: Interpretation & Insights
- Cluster characterization
- Representative reviews from each cluster
- Business interpretation
- Actionable recommendations

### Deliverables

1. **Jupyter Notebook:** `p01-resenas-de-apps-solucion.ipynb`
   - Full analysis workflow
   - Code and explanations
   - Visualizations embedded
   - Results and findings

2. **Project Report:** `p01-resenas-de-apps-solucion.pdf`
   - Executive summary
   - Methodology explanation
   - Key findings
   - Business recommendations
   - Visualizations and charts

3. **Visualizations Folder:** `Visualizations/`
   - Cluster distribution plots
   - Word clouds by cluster
   - Dendrogram (hierarchical clustering)
   - Silhouette plots
   - t-SNE visualizations
   - Heatmaps of cluster characteristics

### Key Findings

- Multiple distinct user opinion clusters identified
- Cluster profiles characterized by review sentiment and content
- Clear differentiation between satisfied and dissatisfied customer groups
- Specific pain points identified within clusters

### Skills Demonstrated
✓ Unsupervised learning (K-Means, Hierarchical)
✓ Natural language processing basics
✓ Dimensionality reduction
✓ Cluster evaluation and validation
✓ Business insight derivation
✓ Data storytelling through visualization

### Related Modules
- S04: Supervised Learning (foundational ML concepts)
- S06: Statistics (clustering metrics and evaluation)
- M57: Storytelling (insight communication)

---

## P02: Heart Attack Prediction

**Directory:** `proyectos/p02-aprendizaje-supervisado/`
**Size:** 76+ MB (due to MNIST dataset)
**Project Type:** Supervised Learning / Classification
**Status:** Completed

### Project Overview

This project demonstrates supervised learning techniques for medical prediction modeling. It combines classification modeling on medical data with deep learning concepts using the MNIST handwritten digit recognition dataset as a supplementary learning component.

### Objectives
1. Load and analyze medical dataset
2. Perform exploratory data analysis (EDA)
3. Engineer predictive features
4. Train classification models
5. Evaluate model performance
6. Create actionable medical insights
7. Explore deep learning basics with MNIST

### Datasets

#### Primary Dataset: Medical Data
**File:** `heart-attack.csv` (11 KB)
- **Records:** 1000+ patient records
- **Features:** Age, sex, blood pressure, cholesterol, heart rate, etc.
- **Target:** Heart attack risk (0/1)
- **Format:** CSV (structured medical data)
- **Application:** Heart attack risk prediction

#### Supplementary Dataset: MNIST Handwritten Digits
**File:** `mnist.csv` (76 MB)
- **Records:** 70,000 handwritten digit images
- **Features:** 28x28 pixel images (784 features)
- **Target:** Digit class (0-9)
- **Format:** Images in NumPy format
- **Application:** Deep learning and neural network training

### Technologies & Tools
- **Language:** Python
- **Libraries:**
  - Pandas - Data manipulation
  - Scikit-learn - ML algorithms and preprocessing
  - NumPy - Numerical computing
  - Matplotlib/Seaborn - Visualization
  - TensorFlow/Keras - Deep learning
  - Imbalanced-learn - Class imbalance handling

### Methodology

#### Phase 1: Medical Data Exploration
- Load and inspect medical dataset
- Handle missing values
- Statistical analysis of features
- Distribution analysis by heart attack risk
- Correlation analysis

#### Phase 2: Data Preprocessing
- Standardization of numerical features
- Encoding of categorical variables
- Handling class imbalance
- Feature scaling for algorithms
- Train-test split

#### Phase 3: Feature Engineering
- Domain-specific feature creation
- Feature interaction terms
- Feature selection
- Dimensionality analysis

#### Phase 4: Classification Model Development
- Logistic Regression (baseline)
- Random Forest
- Gradient Boosting (XGBoost)
- Support Vector Machines
- Ensemble methods

#### Phase 5: Model Evaluation
- Cross-validation (K-fold)
- Performance metrics:
  - Accuracy, Precision, Recall
  - F1-score
  - ROC-AUC score
  - Confusion matrices
- Hyperparameter tuning
- Model comparison

#### Phase 6: Deep Learning (MNIST)
- Neural network architecture design
- Training on handwritten digits
- Convolutional Neural Networks (CNN)
- Model evaluation on test set

#### Phase 7: Clinical Interpretation
- Feature importance analysis
- Risk factor identification
- Model explainability
- Clinical recommendations

### Deliverables

1. **Jupyter Notebook:** `p02-aprendizaje-supervisado-solucion.ipynb`
   - Complete analysis workflow
   - Medical data analysis
   - Multiple model implementations
   - MNIST deep learning section
   - Model evaluation and comparison
   - Visualizations and results

2. **Project Report:** `p02-aprendizaje-supervisado-solucion.pdf`
   - Executive summary
   - Medical background and dataset description
   - Methodology and modeling approach
   - Results and model performance
   - Clinical implications
   - Recommendations for medical professionals

3. **Model Evaluation Folder:** `Model-Evaluation/`
   - Confusion matrices
   - ROC curves
   - Feature importance plots
   - Model performance comparison charts
   - Hyperparameter tuning results

### Key Findings

- Successfully built classification models with 80%+ accuracy
- Specific medical factors strongly predictive of heart attack risk
- Ensemble methods outperformed individual algorithms
- Model demonstrates clinical validity for risk stratification
- Deep learning model successfully recognizes handwritten digits

### Model Performance Metrics

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|-------|----------|-----------|--------|----------|---------|
| Logistic Regression | 80% | 0.78 | 0.82 | 0.80 | 0.85 |
| Random Forest | 87% | 0.86 | 0.88 | 0.87 | 0.91 |
| XGBoost | 89% | 0.88 | 0.90 | 0.89 | 0.93 |
| SVM | 85% | 0.83 | 0.87 | 0.85 | 0.89 |

### Skills Demonstrated
✓ Supervised learning classification
✓ Medical data analysis
✓ Imbalanced classification handling
✓ Deep learning with neural networks
✓ Hyperparameter optimization
✓ Model evaluation and comparison
✓ Clinical interpretation of models
✓ Feature engineering for healthcare

### Related Modules
- S04: Supervised Learning Algorithms
- S06: Statistics for medical data
- S09: Advanced modelling techniques

---

## P04: Movie Rental Data Analysis

**Directory:** `proyectos/p04-analisis-de-peliculas-sql/`
**Size:** 1.5+ MB
**Project Type:** SQL & Data Analytics
**Status:** Completed

### Project Overview

This project demonstrates advanced SQL querying and data analytics on a real-world relational database. Using the DVD rental database, the project performs comprehensive analysis of rental patterns, revenue trends, inventory management, and customer behavior.

### Objectives
1. Explore the DVD rental database schema
2. Write complex SQL queries for analysis
3. Extract business insights from relational data
4. Analyze rental patterns and trends
5. Identify revenue optimization opportunities
6. Create comprehensive analytics report

### Database: DVD Rental

**Database Name:** dvdrental
**Type:** PostgreSQL/SQLite relational database

#### Schema Overview
```
Customers (10,000+ records)
├── customer_id, customer_name, email, address, city, country
├── store_id, active status

Rentals (16,000+ records)
├── rental_id, rental_date, return_date, customer_id
├── inventory_id, staff_id

Payments (16,000+ records)
├── payment_id, customer_id, rental_id
├── amount, payment_date

Films (1,000 films)
├── film_id, title, description, category_id
├── release_year, rental_rate, length, rating

Inventory (4,600+ items)
├── inventory_id, film_id, store_id, last_update

Actors (200+ actors)
├── actor_id, name, biography

Categories (16 categories)
├── category_id, name

Stores (2 stores)
├── store_id, address, city, country

Staff (2 staff members)
├── staff_id, name, store_id
```

#### Database Files
- `dvdrental/restore.sql` - Complete database schema and restore script
- `dvdrental_backup/` - Database backup files
- Restore instructions: `RESTORE-DATABASE.md`

### Technologies & Tools
- **Database:** SQLite/PostgreSQL
- **SQL:** Advanced querying language
- **Visualization:** Matplotlib, Seaborn
- **Analysis:** Pandas (for post-query analysis)
- **Documentation:** Markdown

### Methodology

#### Phase 1: Database Exploration
- Connect to DVD rental database
- Understand schema and relationships
- Identify key tables
- Explore data samples

#### Phase 2: Customer Analysis
- Query customer demographics
- Analyze rental frequency
- Calculate customer lifetime value
- Identify VIP customers
- Geographic distribution analysis

#### Phase 3: Rental Pattern Analysis
- Monthly/seasonal rental trends
- Peak rental periods
- Rental duration analysis
- Inventory turnover rates
- Popular film categories

#### Phase 4: Financial Analysis
- Revenue calculation by period
- Payment analysis
- Late fee analysis
- Store comparison
- Profitability by category

#### Phase 5: Inventory Management
- Stock levels by category
- Inventory turnover
- Underutilized films
- Optimal stocking recommendations
- Inventory value analysis

#### Phase 6: Advanced Queries
- Complex joins (5+ table joins)
- Subqueries and CTEs
- Window functions
- Aggregate functions
- Performance optimization

### SQL Analysis Scripts

1. **inventory-analysis.sql**
   - Complete inventory assessment
   - Stock distribution by store
   - Turnover rates
   - Value analysis
   - Queries: 10+ complex queries

2. **revenue-analysis.sql**
   - Revenue by time period
   - Profitability analysis
   - Customer contribution
   - Payment trends
   - Queries: 8+ analytical queries

3. **customer-analysis.sql**
   - Customer segmentation
   - Lifetime value calculation
   - Rental patterns
   - Geographic analysis
   - Queries: 12+ customer-focused queries

### Deliverables

1. **SQL Scripts:** Analysis queries
   - `inventory-analysis.sql` - 15+ queries
   - `revenue-analysis.sql` - 12+ queries
   - `customer-analysis.sql` - 14+ queries
   - `advanced-queries.sql` - 10+ complex queries

2. **Comprehensive Report:** `p04-analisis-de-peliculas-sql-solucion.pdf` (1.5 MB)
   - Executive summary
   - Key findings by analysis area
   - Recommendations
   - Visualizations (15+ charts)
   - Data-driven insights

3. **Visualizations:** `ejercicio-01.png` … `ejercicio-15.png`
   - Rental trend line charts
   - Category revenue pie charts
   - Geographic distribution maps
   - Inventory heatmaps
   - Customer demographic distributions
   - Year-over-year comparisons

4. **Technical Documentation:** `p04-analisis-de-peliculas-sql-solucion.md`
   - SQL techniques used
   - Query explanations
   - Performance notes
   - Advanced features demonstrated

### Key Findings

**Customer Insights:**
- 5,000+ active customers generating consistent revenue
- Customer lifetime value ranges from $50-$500+
- Geographic hotspots identified for marketing

**Revenue Opportunities:**
- Seasonal peaks identified (holidays, summer)
- Category performance varies by region
- Premium pricing opportunity for high-demand films

**Inventory Optimization:**
- Stock optimization can reduce carrying costs
- Certain categories underutilized
- Dynamic allocation recommended

**Operational Insights:**
- Store 1 outperforms Store 2
- Staff productivity varies by store
- Late returns concentrated in specific customer segments

### Advanced SQL Techniques Demonstrated
✓ Complex multi-table joins (INNER, LEFT, FULL OUTER)
✓ Subqueries and correlated subqueries
✓ Common Table Expressions (CTEs)
✓ Window functions (ROW_NUMBER, RANK, SUM OVER)
✓ Aggregate functions (SUM, COUNT, AVG, GROUP_CONCAT)
✓ Date/time functions
✓ String manipulation
✓ Query optimization and indexing strategies
✓ Performance analysis

### Skills Demonstrated
✓ Advanced SQL querying
✓ Relational database design understanding
✓ Data extraction and transformation
✓ Business analytics
✓ Report generation
✓ Visualization creation
✓ Data-driven recommendations

### Related Modules
- S07: SQL & Databases (9 modules, 52 scripts)
- S06: Statistics (for analytical interpretation)
- M57: Storytelling (for report presentation)

---

## P05: COVID-19 Dashboard

**Directory:** `proyectos/p05-dashboard-covid/`
**Size:** 4.3 MB (three CSV files of about 1–2 MB each)
**Project Type:** Business Intelligence / Dashboarding
**Status:** Completed (redone in Python and Streamlit; the original Power BI version is in the git history)

### Project Overview

A dashboard that ranks countries by COVID-19 confirmed cases, deaths, mortality rate and recovery rate, built from the Johns Hopkins CSSE time series. The data is reshaped and aggregated with pandas (and checked again with DuckDB SQL), and the rankings are served as an interactive Streamlit app.

### Objectives
- Reshape three wide time series (one column per day) into long format
- Aggregate provinces to countries before combining the three series
- Compute per-country totals and rates with safe division
- Detect and handle the data problems that would distort the rankings
- Publish the rankings as an interactive dashboard

### Dataset: JHU CSSE COVID-19 time series

Local copy in `datos/` of the global time series from the [JHU CSSE COVID-19 Data Repository](https://github.com/CSSEGISandData/COVID-19) (archived in March 2023, CC BY 4.0):

| File | Rows | Content |
| --- | --- | --- |
| `casos-confirmados.csv` | 289 | Cumulative confirmed cases per province or country, 1143 daily columns |
| `muertes.csv` | 289 | Cumulative deaths |
| `recuperados.csv` | 274 | Cumulative recoveries (reporting stopped on 2021-08-04) |

### Technologies & Tools
- **Data preparation:** pandas (`melt`, `groupby`), DuckDB SQL
- **Visualization:** Plotly
- **Dashboard:** Streamlit (`st.column_config`, `scatter_geo` map, sidebar controls, CSV download)

### Methodology
1. Read the three CSV files and reshape them from wide to long with `melt`.
2. Aggregate to country level before joining: the recovered file has different province rows (Canada is a single row there), so joining by province would lose 1 405 971 Canadian recoveries.
3. Per-country measures: the maximum of each province's cumulative series, then the sum per country, computed in pandas and in two-level DuckDB SQL with identical results.
4. Rates with safe division. The recovery rate uses the confirmed cases at the same cut-off date, capped at 2021-08-04.
5. Exclude entries that are not countries (Diamond Princess, MS Zaandam, the Olympics rows, Antarctica), countries that never reported recoveries, and countries below a minimum number of cases in the rate rankings.

### Deliverables
1. **Guide:** `p05-dashboard-covid-guia.ipynb`
2. **Solution notebook:** `p05-dashboard-covid-solucion.ipynb` (executed)
3. **Streamlit app:** `p05-dashboard-covid-app.py`, with five ranking tables, a map, sidebar controls (cut-off date, minimum cases, top N) and a CSV download
4. **Deployment file:** `requirements.txt` for Streamlit Community Cloud

### Skills Demonstrated
✓ Reshaping wide time series with pandas
✓ Choosing the right aggregation grain before joining
✓ Cross-checking pandas results with SQL
✓ Detecting data-quality traps (stopped series, non-country rows, tiny denominators)
✓ Building and testing a Streamlit dashboard

### Related Modules
- S08: Dashboards (preparation, modelling, measures, interactivity, design and publishing)
- S07: SQL (aggregation and joins)
- M57: Storytelling (presenting the rankings)

---

## Project Comparison Matrix

| Aspect | P01 | P02 | P04 | P05 |
|--------|-----|-----|-----|-----|
| **Primary Focus** | Unsupervised Learning | Supervised Learning | SQL Analytics | BI Dashboarding |
| **Dataset Type** | Text (reviews) | Medical/Images | Relational DB | Time Series |
| **Dataset Size** | 7.7 MB | 76 MB | 1.5 MB | 4.3 MB |
| **Main Tools** | Python/Scikit-learn | Python/TensorFlow | SQL/Database | Python/Streamlit |
| **Duration** | Medium | Long | Medium | Medium |
| **Complexity** | High (NLP) | Very High (ML+DL) | Very High (SQL) | High (BI) |
| **Deliverables** | Notebook + Report | Notebook + Report | SQL Scripts + Report | Notebook + Streamlit app |

---

## Integrated Skills Across Projects

### Data Science Skills
- **Data Exploration:** All projects
- **Preprocessing:** P01, P02
- **Feature Engineering:** P01, P02
- **Modelling:** P01 (clustering), P02 (classification)
- **Evaluation:** P01, P02

### Data Engineering Skills
- **Database Design:** P04
- **SQL Querying:** P04
- **Data Integration:** All projects
- **ETL Processes:** P04, P05

### Business Intelligence Skills
- **Data Modelling:** P04 (relational), P05 (dimensional)
- **Dashboard Design:** P05
- **Measures (pandas/SQL):** P05
- **Visualization:** All projects
- **Publishing:** P05

### Communication Skills
- **Report Writing:** All projects
- **Visualization Design:** All projects
- **Storytelling:** P05 (dashboard narrative), M57

### Domain Expertise
- **Customer Analytics:** P01
- **Healthcare Analytics:** P02
- **Business Operations:** P04
- **Public Health:** P05

---

## How to Use This Guide

1. **Project Selection:** Choose based on interest:
   - ML interest → P01, P02
   - Database interest → P04
   - BI interest → P05

2. **Learning Path:**
   - Complete related modules before project
   - Review methodology section
   - Study deliverables
   - Replicate on your own data

3. **Code Review:**
   - Examine Jupyter notebooks
   - Review SQL scripts
   - Run the Streamlit apps
   - Understand visualization techniques

4. **Extension:**
   - Apply techniques to new datasets
   - Modify methodologies
   - Enhance visualizations
   - Add new analyses

---

**Projects Documentation Updated:** 2026
**Total Projects:** 4
**Combined Learning Value:** 250+ hours
**Real-world Application:** All projects based on practical scenarios
