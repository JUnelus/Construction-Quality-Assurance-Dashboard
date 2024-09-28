# Construction Quality Assurance Dashboard with Risk Prediction and Automation

## Overview

This project demonstrates a comprehensive approach to **Construction Quality Assurance** by using **Power BI** for data visualization, a **Machine Learning model** to predict project risks, and **automated workflows** to streamline monthly closing procedures. The project leverages a **PostgreSQL** database for data management and **Python** for predictive analytics and process automation.

---

## Features

### 1. **Power BI Dashboard**
   - **Project Overview**: Displays KPIs such as total number of projects, budget utilization, project completion status, and more.
   - **Quality Metrics**: Tracks defects found during inspections, passed inspections over time, and project risk levels.
   - **Risk Analysis**: Visualizes project risk categories (Financial, Operational, Compliance) and highlights high-risk projects.
   ![img.png](img.png)

### 2. **Machine Learning Risk Prediction (Python)**
   - **Model**: A machine learning model is built using historical project data to predict the risk level of future projects.
   - **Data**: Historical data on project budgets, quality metrics, and previous risk levels is used to train a **Random Forest Classifier**.
   - **Prediction**: The model predicts whether a new project will have **low**, **medium**, or **high** risk based on features like defects found, budget adherence, and completion status.

### 3. **Automated Monthly Closing Procedures (Python)**
   - **Data Update**: Automates the process of updating monthly financial and operational data in PostgreSQL.
   - **Report Generation**: Automatically generates monthly reports and saves them in CSV format.
   - **Task Scheduling**: Automates the script execution using **Task Scheduler** (Windows) or **cron jobs** (Linux/macOS).

---

## Technologies Used

### 1. **Backend (Database and Data Processing)**
   - **PostgreSQL**: Relational database used to store and manage construction project data.
   - **Python**: Used for machine learning, data analysis, and process automation.

### 2. **Data Visualization**
   - **Power BI**: For creating interactive dashboards and visualizing key metrics.

### 3. **Automation**
   - **Power Automate (Optional)**: To streamline data updates and report generation workflows.
   - **Task Scheduler/Cron Jobs**: For automating Python scripts that update data and generate reports on a schedule.

---

## Project Setup

### 1. **Database Setup (PostgreSQL)**

1. Install PostgreSQL and create the `ConstructionQA` database.
2. Run the provided SQL script to create the `Projects`, `QualityMetrics`, and `Risks` tables.
3. Populate the database with the sample data:
   - `Projects`: Stores project details (name, budget, completion status).
   - `QualityMetrics`: Tracks inspection data and defects found.
   - `Risks`: Categorizes risks and defines mitigation plans.

### 2. **Power BI Dashboard Setup**

1. Open **Power BI Desktop** and connect to the PostgreSQL database.
2. Import the tables (`Projects`, `QualityMetrics`, `Risks`) and create visuals.
3. Build the following dashboard components:
   - KPIs (Total Projects, Passed Inspections, Budget Utilization)
   - Project Completion Status Chart
   - Risk Breakdown Donut Chart
   - Quality Metrics Analysis Charts (Defects by Project, Passed Inspections Over Time)

### 3. **Machine Learning Model Setup (Python)**

1. Install the required Python libraries:
   ```bash
   pip install pandas scikit-learn psycopg2
