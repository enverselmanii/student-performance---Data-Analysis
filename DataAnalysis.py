"""
Student Performance Analysis with Pandas
--------------------------------------
Author: Enver Selmani

This script demonstrates practical usage of Pandas on a real-world–like dataset:
- DataFrame creation
- Feature engineering
- Filtering & boolean masking
- GroupBy operations & aggregations
- Data cleaning and sorting

"""

import pandas as pd

# -------------------------------
# 1. Dataset creation
# -------------------------------
data = {
    "Student": ["Ardi", "Besa", "Driton", "Elira", "Florian", "Genta"],
    "Gender": ["M", "F", "M", "F", "M", "F"],
    "Math": [85, 78, 92, 88, 70, 95],
    "Python": [80, 82, 90, 91, 65, 98],
    "Statistics": [78, 75, 88, 90, 60, 92],
    "Hours_Studied": [12, 10, 15, 14, 8, 16]
}

df = pd.DataFrame(data)
print("Initial DataFrame:\n", df, "\n")

# -------------------------------
# 2. Feature Engineering
# -------------------------------
# Calculate the average grade for each student
df["Average"] = df[["Math", "Python", "Statistics"]].mean(axis=1)

# Mark students as passed if average grade is >= 80
df["Passed"] = df["Average"] >= 80

print("After feature engineering:\n", df, "\n")

# -------------------------------
# 3. Filtering & Boolean Masking
# -------------------------------
# Students who did not pass
failed_students = df[df["Passed"] == False]
print("Students who did not pass:\n", failed_students, "\n")

# Students who studied less than 10 hours
low_study_hours = df[df["Hours_Studied"] < 10]
print("Students with less than 10 study hours:\n", low_study_hours, "\n")

# -------------------------------
# 4. GroupBy & Aggregations
# -------------------------------
# Average grades by gender
avg_by_gender = df.groupby("Gender")[["Math", "Python", "Statistics"]].mean()
print("Average grades by gender:\n", avg_by_gender, "\n")

# Number of students who passed by gender
passed_count = df.groupby("Gender")["Passed"].sum()
print("Number of students who passed by gender:\n", passed_count, "\n")

# -------------------------------
# 5. Data selection using .loc
# -------------------------------
# Students with Math score greater than 80 (selecting only name and Math score)
high_math = df.loc[df["Math"] > 80, ["Student", "Math"]]
print("Students with Math > 80:\n", high_math, "\n")

# -------------------------------
# 6. Data Cleaning
# -------------------------------
# Remove the student with the lowest average score
df = df.drop(df["Average"].idxmin())

# Sort students from highest to lowest average score
df = df.sort_values(by="Average", ascending=False)

# Reset index after cleaning
df = df.reset_index(drop=True)
print("Cleaned & sorted DataFrame:\n", df, "\n")

# -------------------------------
# 7. Advanced filtering
# -------------------------------
# Students whose name contains 'F' and have an average score below 85
bonus_filter = df.loc[(df["Student"].str.contains("F")) & (df["Average"] < 85)]
print("Bonus filter result:\n", bonus_filter)


import matplotlib.pyplot as plt


avg_gender = df.groupby("Gender")["Average"].mean()


plt.figure()
avg_gender.plot(kind="bar")
plt.title("Average Score by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Score")
plt.show()