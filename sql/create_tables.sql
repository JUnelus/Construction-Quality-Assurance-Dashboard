-- Create the database
CREATE DATABASE ConstructionQA;

-- Table for project information
CREATE TABLE Projects (
    project_id SERIAL PRIMARY KEY,
    project_name VARCHAR(100),
    project_manager VARCHAR(100),
    budget DECIMAL(15, 2),
    start_date DATE,
    end_date DATE,
    completion_status VARCHAR(50) -- 'On Track', 'Delayed', 'Completed'
);

-- Table for quality metrics
CREATE TABLE QualityMetrics (
    metric_id SERIAL PRIMARY KEY,
    project_id INT REFERENCES Projects(project_id),
    inspection_date DATE,
    defects_found INT,
    passed_inspection BOOLEAN
);

-- Table for risk assessment
CREATE TABLE Risks (
    risk_id SERIAL PRIMARY KEY,
    project_id INT REFERENCES Projects(project_id),
    risk_category VARCHAR(50), -- 'Financial', 'Operational', 'Compliance'
    risk_level VARCHAR(20),     -- 'Low', 'Medium', 'High'
    identified_date DATE,
    mitigation_plan TEXT
);

-- Insert sample data into Projects
INSERT INTO Projects (project_name, project_manager, budget, start_date, end_date, completion_status)
VALUES
('Project A', 'John Doe', 1000000, '2023-01-01', '2023-12-31', 'On Track'),
('Project B', 'Jane Smith', 2000000, '2023-02-01', '2024-01-31', 'Delayed'),
('Project C', 'Bob Johnson', 1500000, '2023-03-01', '2023-11-30', 'Completed');

-- Insert sample data into QualityMetrics
INSERT INTO QualityMetrics (project_id, inspection_date, defects_found, passed_inspection)
VALUES
(1, '2023-06-15', 2, TRUE),
(1, '2023-07-20', 0, TRUE),
(2, '2023-08-05', 5, FALSE),
(3, '2023-09-12', 1, TRUE);

-- Insert sample data into Risks
INSERT INTO Risks (project_id, risk_category, risk_level, identified_date, mitigation_plan)
VALUES
(1, 'Financial', 'Low', '2023-02-10', 'Monitor project spending regularly'),
(2, 'Operational', 'High', '2023-05-12', 'Increase workforce to meet deadlines'),
(3, 'Compliance', 'Medium', '2023-04-22', 'Ensure safety compliance checks weekly');
