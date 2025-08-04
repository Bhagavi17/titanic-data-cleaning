# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv('titanic.csv')

# Step 1: Explore basic info
print("Dataset Info:\n")
print(df.info())
print("\nMissing values:\n")
print(df.isnull().sum())
print("\nSummary statistics:\n")
print(df.describe())

# Step 2: Handle Missing Values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop('Cabin', axis=1, inplace=True)

# Step 3: Convert Categorical to Numeric
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})  # Label Encoding

# One-hot encoding for Embarked
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

# Step 4: Feature Scaling (Standardization)
scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

# Step 5: Outlier Detection and Removal
plt.figure(figsize=(12, 6))
sns.boxplot(data=df[['Age', 'Fare']])
plt.title("Boxplots for Age and Fare")
plt.show()

# Remove outliers from 'Fare' column (optional)
Q1 = df['Fare'].quantile(0.25)
Q3 = df['Fare'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['Fare'] >= Q1 - 1.5 * IQR) & (df['Fare'] <= Q3 + 1.5 * IQR)]

# Step 6: Save Cleaned Dataset
df.to_csv('cleaned_titanic.csv', index=False)
print("Data cleaned and saved as 'cleaned_titanic.csv'")
