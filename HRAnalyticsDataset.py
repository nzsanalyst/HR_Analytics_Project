# %%
import pandas as pd  # Import pandas library

# %%
file_path = "/Users/noor/Desktop/HR Analytics/HR-Employee-Attrition.csv"
df = pd.read_csv(file_path)

# %%
# Removing Duplicates
df = df.drop_duplicates()

# %%
# Removing 'EmployeeCount' and 'Over18' as they are constants
df = df.drop(columns=['EmployeeCount', 'Over18'])

# %%
# Converting 'Age' to integer type
df['Age'] = df['Age'].astype(int)

# %%
# Renaming columns
df = df.rename(columns={'JobInvolvement': 'Job_Engagement', 'YearsAtCompany': 'Years_At_Company'})

# %%
# Removing NaN values
df = df.dropna()

# %%
# Creating a new column 'AgeGroup' based on 'Age'
df['AgeGroup'] = pd.cut(df['Age'], bins=[20, 30, 40, 50, 60, 100], labels=['20-30', '30-40', '40-50', '50-60', '60+'])

# %%
# Checking if there are any negative values in columns
df = df[df['MonthlyIncome'] > 0]
df = df[df['TotalWorkingYears'] >= 0]
df = df[df['WorkLifeBalance'] >= 0]
df = df[df['TrainingTimesLastYear'] >= 0]
df = df[df['TotalWorkingYears'] >= 0]
df = df[df['StockOptionLevel'] >= 0]
df = df[df['PercentSalaryHike'] >= 0]


# %%
#One-Hot Encoding Department Data
df = pd.get_dummies(df, columns=['Department'])


# %%
# Text Cleaning 
df['JobRole'] = df['JobRole'].str.lower().str.replace('[^a-zA-Z0-9]', '')


# %%
print(df.columns)

# %%
# Creating "YearsSinceLastPromotion" Ratio
df['PromotionToManagerRatio'] = df['YearsSinceLastPromotion'] / df['YearsWithCurrManager']

# %%
df.to_csv("/Users/noor/Desktop/HR Analytics/Cleaned_HR_Employee_Attrition.csv", index=False)

# %%
print("Data cleaning completed successfully! :)")


