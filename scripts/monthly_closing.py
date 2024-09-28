import pandas as pd
import psycopg2
from datetime import datetime


# Function to update financial data for monthly closing
def update_monthly_closing(conn):
    # Pull the latest data
    latest_data = pd.read_sql_query("SELECT * FROM MonthlyFinancials", conn)

    # Example: You can perform any necessary updates/calculations here
    latest_data['closing_date'] = datetime.now().date()

    # Write the updated data back to the database (replace, append, etc.)
    latest_data.to_sql('MonthlyFinancials', conn, if_exists='replace', index=False)
    print("Monthly closing data updated successfully!")


# Connect to PostgreSQL and update monthly data
conn = psycopg2.connect(
    host="localhost",  # Replace with your DB host
    database="ConstructionQA",
    user="postgres",
    password="PostGres924!"
)

update_monthly_closing(conn)
conn.close()


# Function to generate monthly report as CSV
def generate_monthly_report(conn):
    monthly_report = pd.read_sql_query("SELECT * FROM MonthlyFinancials", conn)

    # Save the report as a CSV file
    monthly_report.to_csv(f'reports/MonthlyReport_{datetime.now().strftime("%Y_%m_%d")}.csv', index=False)
    print("Monthly report generated!")


generate_monthly_report(conn)