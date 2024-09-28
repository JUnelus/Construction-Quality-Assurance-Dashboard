import os
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Function to update financial data for monthly closing
def update_monthly_closing(engine):
    # Pull the latest data
    latest_data = pd.read_sql_query("SELECT * FROM MonthlyFinancials", engine)

    # Example: You can perform any necessary updates/calculations here
    latest_data['closing_date'] = datetime.now().date()

    # Write the updated data back to the database (replace, append, etc.)
    latest_data.to_sql('MonthlyFinancials', engine, if_exists='replace', index=False)
    print("Monthly closing data updated successfully!")


# Create an SQLAlchemy engine
db_url = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}/{os.getenv('POSTGRES_DB')}"
engine = create_engine(db_url)

update_monthly_closing(engine)


# Function to generate monthly report as CSV
def generate_monthly_report(engine):
    monthly_report = pd.read_sql_query("SELECT * FROM MonthlyFinancials", engine)

    # Save the report as a CSV file
    monthly_report.to_csv(f'reports/MonthlyReport_{datetime.now().strftime("%Y_%m_%d")}.csv', index=False)
    print("Monthly report generated!")


generate_monthly_report(engine)
