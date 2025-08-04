
# Titanic Data Cleaning & Preprocessing 🧼

This project is a part of an AI/ML internship task focused on cleaning and preparing raw Titanic dataset for machine learning models. The steps include handling missing values, encoding categorical features, standardizing numerical features, and removing outliers.

---

## 🚀 Project Goals

- Understand and clean raw real-world datasets
- Handle null values using appropriate strategies
- Convert categorical data to numerical format
- Normalize and standardize features
- Detect and remove outliers using visualization

---

## 🛠️ Tools & Libraries Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## 📊 Dataset

- Titanic dataset from Kaggle  
  [🔗 Link to dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset)

---

## 📁 Project Files

- `titanic_preprocessing.py` – Main preprocessing script
- `cleaned_titanic.csv` – Final cleaned dataset
- `boxplot.png` – Outlier visualization
- `README.md` – Project explanation

---

## ✅ Steps Performed

1. Loaded and explored the Titanic dataset
2. Filled missing values (`Age`, `Embarked`), dropped `Cabin`
3. Label-encoded `Sex` and one-hot encoded `Embarked`
4. Standardized `Age` and `Fare`
5. Visualized and removed outliers from `Fare`
6. Exported cleaned dataset as `cleaned_titanic.csv`

---

## 📌 How to Run

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
python titanic_preprocessing.py
```

---

## 🧑‍💻 Author

- Bhagavi Bisen  
- [GitHub Profile](https://github.com/bhagavibisen)

---

## 📤 Submission

This repository is submitted as part of the AI & ML Internship task by AICT Pvt. Ltd.
