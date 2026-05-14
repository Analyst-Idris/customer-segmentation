# Customer Segmentation & Behavioral Intelligence System

---

## Project Banner

<img width="1024" height="572" alt="Image" src="https://github.com/user-attachments/assets/0d154550-58ae-4639-ac18-5749cd5e5e86" />
---

## Project Overview

This project focuses on building a Machine Learning-powered customer segmentation system that helps businesses better understand customer purchasing behavior, improve marketing efficiency, and support data-driven decision-making.

The solution uses customer demographic and behavioral data to group customers into meaningful business segments using the K-Means clustering algorithm.

The final model was deployed as an interactive Streamlit web application for real-time customer segmentation.

---

## Business Problem

A retail company operating both online and physical stores struggled with generalized marketing campaigns and inconsistent customer engagement.

### Key Challenges

- Marketing campaigns targeted all customers equally  
- High-value customers were not clearly identified  
- Customer retention rates were declining  
- Website visitors did not always convert into buyers  
- Some high-spending customers showed reduced engagement  
- Lack of visibility into customer behavior patterns  

As acquisition costs increased, the business needed a data-driven segmentation system to improve targeting, retention, and customer understanding.

---

## Project Objective

- Segment customers based on behavior and purchasing patterns  
- Identify high-value and at-risk customers  
- Improve marketing personalization  
- Enhance customer retention strategies  
- Enable data-driven decision-making  
- Deploy model for real-time prediction  

---

# Dataset Overview

The dataset contains customer demographic, purchasing, and engagement information.

## Original Dataset Features

| Feature | Description |
|---|---|
| ID | Unique customer identifier |
| Year_Birth | Customer birth year |
| Education | Education level |
| Marital_Status | Customer marital status |
| Income | Annual income |
| Kidhome | Number of children at home |
| Teenhome | Number of teenagers at home |
| Dt_Customer | Date customer joined |
| Recency | Days since last purchase |
| MntWines | Spending on wine products |
| MntFruits | Spending on fruits |
| MntMeatProducts | Spending on meat products |
| MntFishProducts | Spending on fish products |
| MntSweetProducts | Spending on sweets |
| MntGoldProds | Spending on gold products |
| NumDealsPurchases | Purchases made with discounts |
| NumWebPurchases | Online purchases |
| NumCatalogPurchases | Catalog purchases |
| NumStorePurchases | Physical store purchases |
| NumWebVisitsMonth | Monthly website visits |
| AcceptedCmp1-5 | Marketing campaign responses |
| Response | Last campaign response |
| Complain | Customer complaint indicator |
| Age | Customer age |
| Total_Children | Total number of children |
| Total_Spending | Total spending across products |
| Customer_Since | Customer relationship duration |


---

## Data Exploration & Quality Assessment

### Data Quality Checks

- Missing value analysis  
- Duplicate removal  
- Data type validation  
- Outlier investigation  

### Visualization Placeholder

<img width="589" height="453" alt="Image" src="https://github.com/user-attachments/assets/1eeb1300-8989-4fd5-8dfa-55cf39cb3796" />



---

## Customer Segments Identified

| Cluster | Segment Name | Description |
|---|---|---|
| 0 | Price-Sensitive Occasional Customers | Low spending, discount-driven buyers |
| 1 | Stable Loyal Customers | Consistent mid-value customers |
| 2 | At-Risk Premium Customers | Previously high-value but declining |
| 3 | Dormant Low-Value Customers | Inactive or low engagement users |
| 4 | VIP Champions | High-income, high-spending customers |
| 5 | Omni-Channel Enthusiasts | Multi-channel active customers |

---

## PCA Visualization (Dimensionality Reduction)

PCA was used to reduce dimensionality for visualization.

### Purpose

- Reduce complexity  
- Enable 2D visualization  
- Improve cluster interpretability  

###  Visualization Placeholder

<img width="565" height="453" alt="Image" src="https://github.com/user-attachments/assets/2433c9c2-0df9-4462-8799-906de4d103d1" />



---

## Business Impact

- Improved customer targeting  
- Better retention strategy design  
- Identification of high-value customers  
- Reduced marketing waste  
- Enhanced personalization strategies  

---

## Streamlit Deployment

The model was deployed as an interactive web application.

### App Features

- Input customer data  
- Real-time segmentation prediction  
- Instant cluster classification  

### App Screenshot Placeholder

<img width="921" height="811" alt="Image" src="https://github.com/user-attachments/assets/db8b2c1b-bcb4-4e96-8b7c-8a12e725ec91" />




---

## 🧰 Tech Stack

- Python  
- Pandas / NumPy  
- Scikit-learn  
- K-Means Clustering  
- StandardScaler  
- Streamlit  
- Joblib  

---

## Key Skills Demonstrated

- Data Cleaning & Preprocessing  
- Feature Engineering  
- Exploratory Data Analysis  
- Unsupervised Machine Learning  
- Customer Segmentation  
- Model Deployment  
- Business Intelligence  

---

## Conclusion

This project demonstrates how machine learning can transform raw customer data into actionable business intelligence.

It enables businesses to:

- Understand customer behavior  
- Improve marketing strategies  
- Increase retention  
- Optimize customer engagement  
- Make data-driven decisions  

---

## Repository Structure

Customer-Segmentation/
│

├── data/

├── models/

├── app/

├── notebooks/

├── visuals/

└── README.md

