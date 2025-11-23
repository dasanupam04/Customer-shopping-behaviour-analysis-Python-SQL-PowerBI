import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("X:\\Data Science Project\\Customer Trends\\customer_shopping_behavior.csv")
print(df)
print(df.columns)
print(df.info)
print(df.describe)

# Renaming columns according to snake casing for better readability and documentation
df['Review Rating' ] = df.groupby('Category') ['Review Rating'].transform(lambda x: x.fillna(x.median()))
print(df.isnull().sum())

# Renaming columns according to snake casing for better readability and documentation
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')
df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})
print(df.columns)

# create a new column age_group
labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels = labels)
print(df[['age','age_group']].head(10))

# create new column purchase_frequency_days
frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}
df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)
print(df[['purchase_frequency_days','frequency_of_purchases']].head(10))

print(df[['discount_applied','promo_code_used']].head(10))

print((df['discount_applied'] == df['promo_code_used']).all())


# Dropping promo code used column
df = df.drop('promo_code_used', axis=1)
print(df.columns)















