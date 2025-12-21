🛍️ Customer Shopping Behavior Analysis

A Data Science Project Using Python, SQL, EDA, and Feature Engineering





📌 Project Overview

Retail businesses are undergoing continuous changes in customer preferences, buying behavior, and product interactions. This project aims to analyze customer shopping behavior using real-world data to uncover purchasing trends, demographic insights, seasonal patterns, and revenue-driving factors.

The goal of this project is to:

    1. Understand customer demographics
    
    2. Identify key purchase drivers

    3. Explore category and season-wise trends
    
    4. Study the impact of discounts, reviews, and product interests
    
    5. Generate insights for business decision-making
    
    6. Prepare the dataset for machine learning modeling
    
This project demonstrates clean data preparation, in-depth EDA, feature engineering, SQL integration, visualization, and insights.




📂 Dataset Description

The dataset contains customer-level transaction records, including:

    1. Demographics: Age, Gender, Location
    
    2. Shopping Behavior: Category, Frequency of Purchases, Previous Purchases
    
    3. Transaction Details: Purchase Amount, Discount Applied, Shipping Type
    
    4. Behavioral Factors: Review Rating, Subscription Status
    
    5. Season & Preferred Channel: Helps in understanding timing and platform preferences

This dataset allows both behavioral analysis and predictive modeling.



🧹 Data Preparation & Cleaning

All inconsistencies in the dataset were cleaned, missing values handled, and columns standardized.

✔ Missing Value Treatment

1. Review ratings with missing values were filled using category-wise median values, ensuring no distortion in product-specific trends.

✔ Column Standardization

1. All column names were converted to clean, consistent, snake_case format.

2. Redundant or duplicate fields were removed after validation.

✔ Outlier Checks

1. Purchase amounts and review scores were examined for extreme values.

2. Irregularities caused by data entry issues were handled appropriately.



🛠️ Feature Engineering


To expand the analytical value of the dataset, new features were created.


✔ Age Grouping


    Customers were segmented into four groups:
    Young Adult, Adult, Middle-aged, Senior — enabling demographic-based trend analysis.

✔ Purchase Frequency (in Days)


    Purchase frequency text such as “Weekly”, “Monthly”, “Quarterly”, etc., was converted into numerical day counts. This allows frequency-based comparisons and modeling.


✔ Redundant Feature Elimination


    Two columns — "discount applied" and "promo code used" — were found to contain identical values. The duplicate column was removed to avoid confusion and multicollinearity



These engineered features enhance customer segmentation, predictive capabilities, and visualization clarity


.
