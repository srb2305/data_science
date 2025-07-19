# Overview
# A teacher wants to analyze student grades to identify trends and patterns.

# Dataset
# | Student ID | Name | Grade |
# | --- | --- | --- |
# | 1 | John | 85 |
# | 2 | Mary | 90 |
# | 3 | David | 78 |
# | ... | ... | ... |

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Student ID': [1, 2, 3, 4],
    'Name': ['John', 'Mary', 'David', 'Alice'],
    'Grade': [85, 90, 78, 88]
}
df = pd.DataFrame(data)
grade_mean = df['Grade'].mean()
print("Mean Grade:", grade_mean) # 85.25

plt.bar(df['Name'], df['Grade'], color='yellow')
plt.title('Student Grades')
plt.xlabel('Student Name')  
plt.ylabel('Grade')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Student Grades Analysis