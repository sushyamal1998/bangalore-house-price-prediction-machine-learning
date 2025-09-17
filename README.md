# Bangalore House price Prediction

This project uses Machine Learning Techniques - Linear Regression, Ridge, Lasso Regression and Neural network model, to predict the house price based on various feature in the location **Bangalore**



## Contents
- <a href="#overview">Overview</a>
- <a href="#dataset">Dataset</a>
- <a href="#technologies--tools">Technologies & Tools</a>
- <a href="#project-structure">Project Structure</a>
- <a href="#data-cleaning--preprocessing">Data Cleaning & Preprocessing</a>
- <a href="#outlier-detection">Outlier Detection</a>
- <a href="#model">Model</a>
- <a href="#results">Results</a>
- <a href="#conclusions">Conclusions</a>

---

<h2><a class="anchor" id="overview"></a>Overview</h2>
Real price prediction is influenced by multiple factors such as location, number of bedrooms, area, and amenities. This project builds a predictive model for Bangalore housing prices using both classical ML algorithms and a simple Neural Network, and compares their performance.

---

<h2><a class="anchor" id="dataset"></a>Dataset</h2>

- **Source** `Bengaluru_House_Data.csv`

- **size of dataset:** 13320 rows and 9 columns
- **Attributes:**
   - area_type
   - availability
   - location
   - size
   - society
   - total_sqft
   - bath
   - balcony
   - price

---

<h2><a class="anchor" id="technologies--tools"></a>Technologies & Tools</h2>

- **Python** (pandas,numpy, scikir-learn)
- **Models:** Linear regression, Ridge, Lasso, Neural Network
- **version control:**Git/GitHub
- **jupyter notebook** for analysis and documentation

---

<h2><a class="anchor" id="project-structure"></a>Project Structure</h2>

```
bangalore-house-price-prediction/
│
├── Data/                         
│   └── Bengaluru_House_Data.csv
│
├── Notebook/                    
│   └── Bengaluru_house_price_predict.ipynb
│
├── templates/                     
│   └── index.html
│
├── app.py                        
├── model.pkl                      
├── requirements.txt               
├── .gitignore                     
└── README.md                      

```

---

<h2><a class="anchor" id="data-cleaning--preprocessing"></a>Data Cleaning & Preprocessing</h2>

- Remove unnecessary columns which are not used to predict the house price<br>
- Converted total_sqrt to numeric<br>
- Fill the missing values of each column<br>
- As location has 1294 unique categorical values. so we reduce the size of this value as when we apply **one_hot_encoding** to transform categorical to numerical then so manny unnecessary columns are created<br>
- Create new features price_sqrt, it helps to remove outlier<br>

---

<h2><a class="anchor" id="outlier-detection"></a>Outlier Detection</h2>

 - **BHK Column:**
  - The `bhk` (bedroom) column has values ranging from **1 to 43**, which seems unusual
  - To detect outliers, we calculated the ratio:  
    ```
    total_sqft / bhk
    ```
    - If this value is **less than 300**, it's likely an outlier and was removed
 - **Price per Square Foot:**
  - The `price_per_sqft` column showed a **very large range** between the minimum and maximum values
  - To remove extreme values, we applied the **location-wise Z-score method**:
    - Outliers were detected and removed based on mean ± standard deviation for each location group    
   
---


<h2><a class="anchor" id="model"></a>Model</h2>

### 1. Linear regression
- Assume linear relation exists between features and target price
### 2. Ridge Regression and Lasso Regression
- Helps to reduce overfitting and handles Multicolinearity
### 3. Neural Network
- I apply this model with 3 hidden layer and 1 output layer with size 128,64,32 and 1. I apply **relu** activation function on hidden layer and **linear** activation function on output layer. I use **mean_squared_loss** and **adam** optimizer fot htis model with **epochs = 25**

---

<h2><a class="anchor" id="results"></a>Results</h2>
- Linear regression gives R2-score 0.8294<br>
- Ridge and Lasso gives R2-score 0.8296 and 0.8222<br>
- Neural Network model give R2-score 0.8445<br>

---

<h2><a class="anchor" id="conclusions"></a>Conclusions</h2>

This project demonstrates how simple regression models and neural network model can be used to estimate property prices in the city Bangalore.
- Simple regression models perform reasonably well (~83% R²).
- Neural Networks slightly outperform classical methods (~84%).
- Feature engineering (price_per_sqft, location grouping) plays a big role in improving model accuracy.

   
     
