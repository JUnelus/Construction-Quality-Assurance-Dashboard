import pandas as pd
import psycopg2

# Establish connection to PostgreSQL
conn = psycopg2.connect(
    host="localhost",  # Replace with your DB host
    database="ConstructionQA",
    user="postgres",
    password="PostGres924!"
)

# Load data into pandas DataFrames
projects_df = pd.read_sql_query("SELECT * FROM Projects", conn)
quality_metrics_df = pd.read_sql_query("SELECT * FROM QualityMetrics", conn)
risks_df = pd.read_sql_query("SELECT * FROM Risks", conn)

conn.close()

# Merge dataframes on project_id
merged_df = pd.merge(projects_df, quality_metrics_df, on="project_id", how="left")
merged_df = pd.merge(merged_df, risks_df, on="project_id", how="left")

# Prepare the Data for Modeling
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Fill any missing values
merged_df.fillna(0, inplace=True)

# Encode categorical features (risk_level, completion_status)
le = LabelEncoder()
merged_df['risk_level_encoded'] = le.fit_transform(merged_df['risk_level'])
merged_df['completion_status_encoded'] = le.fit_transform(merged_df['completion_status'])

# Define features and target
X = merged_df[['budget', 'defects_found', 'completion_status_encoded']]  # Features
y = merged_df['risk_level_encoded']  # Target (risk level)

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a Machine Learning Model
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Initialize the Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
clf.fit(X_train, y_train)

# Predict on the test data
y_pred = clf.predict(X_test)

# Evaluate the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Evaluate and Interpret the Model
from sklearn.metrics import classification_report

# Determine the unique classes in the test set and corresponding labels
unique_classes = sorted(set(y_test))
target_names = [le.classes_[cls] for cls in unique_classes]

# Print classification report
print(classification_report(y_test, y_pred, target_names=target_names))

# Save the Model and Integrate with Power BI
import joblib

# Save the model
joblib.dump(clf, '../project_risk_model.pkl')