# 🚀 CleanCraft

### Intelligent Data Cleaning & Preprocessing Platform for Machine Learning

PreprocessIQ is an AI-powered data preprocessing and cleaning platform that transforms messy datasets into clean, machine-learning-ready datasets through an interactive step-by-step workflow.

Users can upload datasets or provide dataset links, monitor the cleaning process through a real-time terminal interface, receive intelligent cleaning recommendations, make custom decisions, and download the cleaned dataset.

---

## 🌟 Key Features

✅ Upload CSV / Excel datasets  
✅ Dataset URL support  
✅ Real-time terminal-style cleaning logs  
✅ AI-powered cleaning recommendations  
✅ Interactive user decisions during preprocessing  
✅ Missing value handling  
✅ Duplicate detection & removal  
✅ Outlier detection  
✅ Data standardization  
✅ Date formatting correction  
✅ Feature scaling for ML readiness  
✅ Before vs After comparison dashboard  
✅ Download cleaned dataset  
✅ Cleaning report generation

---

## 🎯 Project Goal

The objective of PreprocessIQ is to automate and simplify the process of data preprocessing for Machine Learning workflows.

Instead of manually cleaning datasets using scripts or notebooks, users can simply upload a dataset and let the system:

1. Detect problems
2. Suggest intelligent solutions
3. Ask for user confirmation
4. Clean the dataset step-by-step
5. Return a clean downloadable dataset

This project bridges the gap between **Data Science, AI/ML, and Web Development**.

---

## ⚙️ How PreprocessIQ Works

PreprocessIQ follows an intelligent step-by-step preprocessing workflow to clean datasets efficiently.

### Workflow

```text
Upload Dataset / Paste Dataset URL
                ↓
        Dataset Analysis
                ↓
      Problem Detection Engine
                ↓
       AI Recommendation Engine
                ↓
     User Decision & Confirmation
                ↓
     Step-by-Step Data Cleaning
                ↓
     Before vs After Comparison
                ↓
      Download Clean Dataset
```

---

## 🖥️ Interactive Cleaning Process

Unlike traditional data cleaning tools, PreprocessIQ provides a **real-time terminal experience** where users can monitor every step of preprocessing.

Example terminal workflow:

```text
> Dataset uploaded successfully

> Scanning dataset...

✓ Dataset Shape: (10,240 rows, 18 columns)

✓ Missing values detected:
Age → 142 missing values
Salary → 51 missing values

━━━━━━━━━━━━━━━━━━
AI Recommendation
━━━━━━━━━━━━━━━━━━

Column: Age

Suggested Method:
Median Imputation

Reason:
Data contains outliers and skewed distribution.

Choose Action:

[1] Use AI Recommendation
[2] Mean
[3] Median
[4] Remove Rows
```

After selection:

```text
✓ Median imputation applied successfully
```

Next step:

```text
Duplicate rows detected: 37

AI Recommendation:
Remove duplicate rows

Reason:
Exact duplicate records found.

Proceed?

[Accept Suggestion]
[Choose Manually]
```

---

## 🧠 AI Recommendation Engine

PreprocessIQ intelligently suggests cleaning methods based on dataset characteristics.

### Examples

| Problem Detected | AI Suggestion |
|------------------|---------------|
| Skewed numerical data | Median imputation |
| Symmetric numerical data | Mean imputation |
| Excessive missing values | Drop column |
| Duplicate rows | Remove duplicates |
| Inconsistent categorical values | Standardization |
| Extreme values | Outlier treatment |

The user always remains in control and can either:

- Accept AI recommendations
- Choose custom preprocessing methods

---

## 🛠️ Tech Stack

PreprocessIQ is built using modern technologies for web development, data preprocessing, and machine learning readiness.

### Frontend

The frontend is responsible for user interaction and interface design.

| Technology | Purpose |
|------------|---------|
| HTML5 | Website structure |
| CSS3 | Styling & responsive design |
| JavaScript | Dynamic interactions |
| AJAX / Fetch API | Real-time terminal updates |

---

### Backend

The backend handles file processing, preprocessing logic, and AI recommendations.

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Flask | Backend framework |
| Jinja2 | HTML templating |

---

### Data Processing & Machine Learning Libraries

| Library | Purpose |
|---------|---------|
| Pandas | Data cleaning & manipulation |
| NumPy | Numerical operations |
| Scikit-learn | Feature scaling & preprocessing |
| SciPy | Statistical analysis |
| Missingno | Missing value visualization |

---

### Visualization Libraries

| Library | Purpose |
|---------|---------|
| Matplotlib | Data visualization |
| Plotly | Interactive charts |

---

## 📦 Python Packages Used

Install required dependencies:

```bash
pip install flask pandas numpy scikit-learn matplotlib plotly scipy missingno openpyxl
```

Or install using:

```bash
pip install -r requirements.txt
```

---

## 💡 Why Flask?

PreprocessIQ uses **Flask** because it provides:

- Lightweight backend architecture  
- Easy integration with HTML/CSS frontend  
- Simple API handling  
- Faster development cycle  
- Beginner-friendly structure  
- Easy deployment on Render

---

## 📂 Project Structure

PreprocessIQ follows a modular and scalable folder structure for maintainability and professional development.

```text
PreprocessIQ/
│
├── static/
│   │
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   ├── terminal.js
│   │   ├── upload.js
│   │   └── dashboard.js
│   │
│   └── images/
│
├── templates/
│   │
│   ├── index.html
│   ├── upload.html
│   ├── processing.html
│   ├── result.html
│   └── error.html
│
├── uploads/
│   └── uploaded_files
│
├── cleaned_data/
│   └── cleaned_datasets
│
├── reports/
│   └── preprocessing_reports
│
├── visualizations/
│   ├── missing_values.png
│   ├── outliers.png
│   └── comparison_chart.png
│
├── src/
│   │
│   ├── cleaner.py
│   ├── validator.py
│   ├── recommender.py
│   ├── outlier_handler.py
│   ├── duplicate_handler.py
│   ├── standardizer.py
│   ├── visualizer.py
│   ├── exporter.py
│   └── logger.py
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

---

## 📁 Folder Explanation

### `static/`
Contains all frontend assets.

- `css/` → website styling  
- `js/` → frontend functionality  
- `images/` → logos, screenshots, icons

---

### `templates/`
Contains HTML pages rendered by Flask.

| File | Purpose |
|------|----------|
| `index.html` | Homepage |
| `upload.html` | Dataset upload page |
| `processing.html` | Live terminal processing |
| `result.html` | Final cleaned dataset results |
| `error.html` | Error handling page |

---

### `uploads/`
Temporarily stores uploaded datasets.

Example:

```text
customer_data.csv
sales_data.xlsx
```

---

### `cleaned_data/`
Stores cleaned datasets for download.

Example:

```text
cleaned_customer_data.csv
processed_sales.xlsx
```

---

### `reports/`
Stores generated cleaning reports.

Example:

```text
report_customer_data.pdf
```

---

### `src/`
Contains the core backend logic.

| File | Purpose |
|------|---------|
| `cleaner.py` | Main cleaning pipeline |
| `validator.py` | Dataset validation |
| `recommender.py` | AI suggestion engine |
| `outlier_handler.py` | Outlier processing |
| `duplicate_handler.py` | Duplicate removal |
| `standardizer.py` | Category standardization |
| `visualizer.py` | Graph generation |
| `exporter.py` | Download handling |
| `logger.py` | Terminal logs |

---

## 🏗️ Project Architecture

```text
Frontend (HTML/CSS/JS)
            ↓
        Flask Server
            ↓
     Data Cleaning Engine
            ↓
   AI Recommendation System
            ↓
   Interactive User Decisions
            ↓
 Clean Dataset + Report Export
```

---

## ✨ Features

PreprocessIQ provides an intelligent and interactive data preprocessing experience for Machine Learning workflows.

---

### 📤 Dataset Upload System

Users can either:

- Upload datasets directly
- Paste dataset URLs

### Supported File Formats

```text
.csv
.xlsx
.xls
```

Example supported sources:

- Local system upload
- GitHub raw dataset links
- Public dataset URLs

---

### 🔍 Intelligent Dataset Analysis

After uploading, PreprocessIQ automatically scans the dataset and detects issues.

The system analyzes:

✅ Dataset shape  
✅ Missing values  
✅ Duplicate rows  
✅ Incorrect data types  
✅ Inconsistent categories  
✅ Invalid date formats  
✅ Outliers  
✅ Feature distributions

Example output:

```text
Dataset Shape: (10,240 rows, 18 columns)

Problems Found:
✓ Missing values: 142
✓ Duplicate rows: 37
✓ Invalid dates: 8
✓ Inconsistent categories: 5
```

---

### 🖥️ Live Terminal Processing

PreprocessIQ displays all cleaning steps in a terminal-style interface in real time.

Example:

```text
> Dataset uploaded successfully

> Running data analysis...

✓ Missing values detected
✓ Outliers identified
✓ Duplicate records found
✓ Data standardization initiated
```

This improves transparency by allowing users to monitor the entire preprocessing pipeline.

---

### 🧠 AI Recommendation Engine

PreprocessIQ intelligently recommends preprocessing methods based on dataset characteristics.

Example:

```text
Column: Salary

Suggested Method:
Median Imputation

Reason:
Column contains skewed values and outliers.
```

The recommendation engine uses statistical logic to suggest:

| Problem | Suggested Solution |
|----------|-------------------|
| Skewed data | Median |
| Symmetric data | Mean |
| Excessive missing data | Drop column |
| Duplicate rows | Remove duplicates |
| Inconsistent labels | Standardization |

---

### 👤 Interactive User Decisions

Users are not forced to follow automated cleaning.

Instead, they can:

- Accept AI recommendation
- Select a custom cleaning method
- Skip a preprocessing step

Example:

```text
Missing values found in Age column.

Choose Action:

[Accept Recommendation]
[Use Mean]
[Use Median]
[Drop Rows]
[Skip]
```

This makes preprocessing flexible and user-controlled.

---

### 🧹 Automated Data Cleaning

PreprocessIQ supports multiple preprocessing techniques.

#### Missing Value Handling

Methods:

- Mean Imputation
- Median Imputation
- Mode Imputation
- Forward Fill
- Backward Fill
- Remove Rows
- Remove Column

---

#### Duplicate Removal

Detects and removes:

- Exact duplicate rows
- Redundant records

---

#### Data Standardization

Converts inconsistent categories into standardized formats.

Example:

```text
Before:
Male
male
M
FEMALE

After:
Male
Female
```

---

#### Date Format Correction

Standardizes inconsistent date formats.

Example:

```text
Before:
12/04/2025
April 12, 2025
2025-04-12

After:
2025-04-12
```

---

#### Outlier Detection

Supports:

- IQR Method
- Z-Score Method

Used to identify abnormal values affecting ML performance.

---

#### Feature Scaling

Machine-learning-ready preprocessing:

- StandardScaler
- MinMaxScaler

---

### 📊 Before vs After Dashboard

PreprocessIQ visually compares dataset quality before and after cleaning.

Example:

| Metric | Before | After |
|--------|--------|--------|
| Missing Values | 142 | 0 |
| Duplicates | 37 | 0 |
| Invalid Dates | 8 | 0 |

---

### 📥 Download Clean Dataset

Users can download:

✅ Cleaned dataset  
✅ Preprocessing report

Supported export formats:

```text
.csv
.xlsx
```

---

### 📄 Cleaning Report Generation

PreprocessIQ generates a detailed preprocessing report containing:

- Dataset summary
- Issues detected
- Cleaning methods used
- AI recommendations
- Before vs After statistics

This helps users understand the cleaning process and improves reproducibility.

---

## ⚡ Installation & Setup

Follow the steps below to run PreprocessIQ locally.

---

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/PreprocessIQ.git
```

Move into the project directory:

```bash
cd PreprocessIQ
```

---

## 2️⃣ Create Virtual Environment

Create a Python virtual environment.

### Windows

```bash
python -m venv venv
```

Activate virtual environment:

```bash
venv\Scripts\activate
```

---

### Mac / Linux

```bash
python3 -m venv venv
```

Activate virtual environment:

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

Install all required packages.

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install flask pandas numpy scikit-learn matplotlib plotly scipy missingno openpyxl
```

---

## 4️⃣ Run the Flask Server

Start the application.

```bash
python app.py
```

If successful, you will see:

```text
* Running on http://127.0.0.1:5000
```

---

## 5️⃣ Open in Browser

Open your browser and visit:

```text
http://127.0.0.1:5000
```

PreprocessIQ should now be running locally.

---

## 📋 Requirements

### Software Required

| Software | Version |
|----------|----------|
| Python | 3.10+ |
| Flask | Latest |
| Git | Recommended |

---

## 📦 requirements.txt

Example:

```text
flask
pandas
numpy
matplotlib
plotly
scikit-learn
scipy
missingno
openpyxl
gunicorn
```

---

## 🚀 Running in Development Mode

For development:

### Windows

```bash
set FLASK_ENV=development
flask run
```

### Mac/Linux

```bash
export FLASK_ENV=development
flask run
```

This enables:

✅ Auto reload  
✅ Easier debugging  
✅ Faster development workflow

---

## 🛠️ Common Errors & Fixes

### Error: Module Not Found

Solution:

```bash
pip install -r requirements.txt
```

---

### Error: Flask Not Recognized

Solution:

```bash
pip install flask
```

---

### Error: Port Already In Use

Run Flask on another port:

```bash
flask run --port=5001
```

---
