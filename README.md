# 🚀 Brand Performance & Inventory Optimization Analysis | Flowing Fluidz

**Flowing Fluidz** is a retail liquor distribution company, that is trying to analyze its sales and purchases for the year 2024.

## 📌 Overview

This project presents an end-to-end data analytics workflow for **Flowing Fluidz**, focused on optimizing inventory management, vendor performance, pricing strategies, and profitability within a retail/wholesale business environment.

The analysis combines:

- SQL-based data engineering
- Python-driven exploratory data analysis (EDA)
- Statistical hypothesis testing
- Business intelligence and visualization
- Actionable business recommendations

The project is designed to simulate a real-world business analytics engagement where data is transformed into strategic insights for operational and financial decision-making.

---

## 🧩 Business Problem

Effective inventory and sales management are critical for optimizing profitability in the retail and wholesale industry. The primary objectives of this analysis were to:

1. Identify underperforming brands requiring promotional or pricing adjustments
2. Analyze the impact of bulk purchasing on unit costs
3. Assess inventory turnover efficiency
4. Compare profitability between high-performing and low-performing brands
5. Evaluate the effectiveness of discounts and promotional pricing

---

## 📈 Key Insights

### 1. Promotional & Pricing Opportunities
- Identified **198 low-sales but high-margin brands**
- Detected **highly price-sensitive brands** that may benefit from discounts and promotional strategies

### 2. Vendor Dependency Risk
- Top 10 vendors contribute approximately **65.69%** of total purchases
- Indicates significant supplier concentration risk

### 3. Bulk Purchasing Advantage
- Large orders reduce unit purchase costs by nearly **72%**
- Demonstrates strong economies of scale

### 4. Inventory Turnover Issues
- Identified slow-moving inventory worth approximately **$9.5M**
- Highlights opportunities for inventory optimization

### 5. Profitability Analysis
- Low-performing brands exhibit significantly higher profit margins than top-selling brands
- Suggests pricing inefficiencies and market penetration challenges

### 6. Statistical Validation
Performed hypothesis testing to validate profit margin differences between top and low-performing brands.

- Null Hypothesis rejected
- Confirms statistically significant profitability differences between brand groups

---

## 📑 Project Structure

```bash
main/
│
├── Data/                               # Raw CSV datasets
├── Logs/                               # Execution logs
│
├── A1_ingestion_db.ipynb               # Database ingestion notebook
├── A2_EDA.ipynb                        # Exploratory Data Analysis notebook
├── A3_vendor_analysis.ipynb            # Final business analysis notebook
│
├── script1_ingestion_db.py             # CSV → MySQL ingestion script
├── script2_get_vendor_summary.py       # SQL aggregation & feature engineering
│
└── Report-Flowing_Fluidz.pdf           # Final business report
```

## ⚙️ Tech Stack

### Languages
- Python
- SQL

### Libraries
- pandas
- numpy
- matplotlib
- seaborn
- scipy
- sqlalchemy
- pymysql

### Database
- MySQL

### Tools
- Jupyter Notebook
- VS Code

## 📊 Workflow

### Step 1: Data Ingestion
```script1_ingestion_db.py```
- Reads CSV files from the ```Data/``` directory
- Creates MySQL tables dynamically
- Stores ingestion logs

### Step 2: Data Aggregation & Cleaning
```script2_get_vendor_summary.py```

Creates a consolidated analytical table named: ```vendor_sales_summary```

**Operations Performed**
- SQL joins across:
    - purchases
    - sales
    - purchase_prices
    - vendor_invoice
- KPI generation:
    - Gross Profit
    - Profit Margin
    - Stock Turnover
    - Sales-to-Purchase Ratio
- Missing value handling
- Infinite value handling for MySQL compatibility

### Step 3: Exploratory Data Analysis
```A2_EDA.ipynb```

**Performed**
- Distribution analysis
- Outlier detection
- Correlation analysis
- Data filtering
- KPI exploration

### Step 4: Business Analysis
```A3_vendor_analysis.ipynb```

**Focused on solving core business problems using:**

- Pricing analysis
- Vendor dependency analysis
- Inventory turnover analysis
- Profitability segmentation
- Confidence intervals
- Hypothesis testing

### Step 5: Statistical Analysis

**Hypothesis Testing**

Null Hypothesis (H₀)

    There is no significant difference in profit margins between top-performing and low-performing brands.

Alternative Hypothesis (H₁)

    A significant difference exists in profit margins between the two groups.

**Result**

    The null hypothesis was rejected using a two-sample t-test, confirming statistically significant differences in profitability structures.

### Sample KPIs Generated
- Gross Profit
- Profit Margin (%)
- Stock Turnover Ratio
- Sales-to-Purchase Ratio
- Vendor Purchase Contribution
- Unsold Inventory Capital

## **Business Recommendations**
- Re-evaluate pricing strategies for low-sales brands
- Diversify vendor partnerships to reduce supply chain risk
- Utilize bulk purchasing advantages strategically
- Optimize slow-moving inventory
- Improve marketing and distribution for high-margin brands

## 🏃‍♂️ How to Run

### 1. Clone Repository
```bash
git clone https://github.com/adaksourin-SA/Brand-Performance-Inventory-Optimization-Analysis.git
```

### 2. Install Dependencies
```pip install -r requirements.txt```

### 3. Extract data.zip
Go to ```Data/``` and extract data.zip to get all CSVs

### 4. Configure MySQL
Update database credentials inside:

```create_engine("mysql+pymysql://username:password@localhost/database")```

### 5. Run Data Ingestion

```python script1_ingestion_db.py```

### 6. Generate Vendor Summary Table

```python script2_get_vendor_summary.py```

### 7. Open Analysis Notebook

```A3_vendor_analysis.ipynb```

## Final Report
The complete business report is included in: ```Report-Flowing_Fluidz.pdf```

**It contains:**

- Executive summary
- EDA insights
- Correlation analysis
- Statistical testing
- Visualizations
- Final business recommendations

## ✍ Author
**Sourin Adak**\
Data Analytics | SQL | Python | Statistical Analysis | Business Intelligence







