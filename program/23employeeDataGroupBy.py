#A company wants to analyze its employee data to understand demographics, 
# job distribution, and salary trends.
# Analysis
# 1. Departmental Salary Trends: Calculate average salary by department.
# 2. Job Title Distribution: Count the number of employees by job title.
# 3. Age Distribution: Analyze age distribution across departments.
import pandas as pd

data = {
    'EmployeeId': [1,2,3],
    'Name' : ['John', 'Ram', 'Shyam'],
    'Department': ['Sales', 'Marketing', 'IT'],
    'Job Title': ['Manager','Analyst', 'Developer'],
    'Salary': [80000,60000,70000],
    'Age': [35,28,32]
}

dataframe = pd.DataFrame(data)

dep_salary_trends = dataframe.groupby('Department')['Salary'].agg(['mean'])
print("dep_salary_trends")
print(dep_salary_trends)

job_title_distributation = dataframe.groupby('Job Title')['Name'].agg(['count'])
print("job_title_distributation:")
print(job_title_distributation)

age_distributation = dataframe.groupby('Department')['Age'].describe()
print("age_distributation:")
print(age_distributation)
