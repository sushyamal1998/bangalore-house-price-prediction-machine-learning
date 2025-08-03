# Bangalore House price Prediction

This project uses Machine Learning Techniques - Linear Regression, Ridge and Lasso Regression, to predict the house price based on various feature in the location **Bangalore**

## Dataset
- **Source:** `Bengaluru_House_Data.csv`
- **size of dataset:** 13320 rows and 9 columns
- **Attributes:**
   - area_ttype
   - availability
   - location
   - size
   - society
   - total_sqft
   - bath
   - balcony
   - price

---
## Preprocessing Steps
- Remove unnecessary columns which are not used to predict the house price
- Converted total_sqrt to numeric
- Fill the missing values of each column
- As location has 1294 unique categorical values. so we reduce the size of this value as when we apply **one_hot_encoding** to transform categorical to numerical then so manny unnecessary columns are created
- Create new features price_sqrt, it helps to remove outlier
   
---
## Features used
After data cleaning and preprocessing
- **location**
- **total_sqft**
- **bath**
- **bhk**
- **price**


## Machine Learning Models

### 1. Linear regression
- Assume linear relation exists between features and target price
### 2. Ridge Regression and Lasso Regression
- Helps to reduce overfitting and handles Multicolinearity
### 3. Neural Network
- Apply to get better performance

---
## Results
- Linear regression gives R2-score 0.8294
- Ridge and Lasso gives R2-score 0.8296 and 0.8222
- Neural Network model give R2-score 0.8445

## Conclusions
This project demonstrates how simple regression models and neural network model can be used to estimate property prices.

   
     
