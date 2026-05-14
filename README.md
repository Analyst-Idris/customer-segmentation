# Customer Segmentation & Behavioral Intelligence System

---

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


<img width="1032" height="1027" alt="Image" src="https://github.com/user-attachments/assets/518d4482-ea1e-49ab-aa6b-1d87a7c83155" />   <img width="580" height="493" alt="Image" src="https://github.com/user-attachments/assets/e8e6127f-a0b4-450c-bca5-6866707c9547" />



---

## Data Cleaning & Feature Engineering

### Cleaning Steps

- Removed duplicates  
- Handled missing values  
- Standardized formats  
- Removed irrelevant columns  

### Engineered Features

- Age → Derived from Year of Birth  
- Total_Children → Kidhome + Teenhome  
- Total_Spending → Combined product categories  
- Customer_Since → Tenure from registration date

### Statistical Exploration

Analyzed distributions for:

- Income
- Total spending
- Website visits
- Purchase frequency
- Recency
- Product category spending

## Correlation Analysis

A correlation matrix was constructed to examine relationships between key business variables.

### Key Insights

- Relationship between income and spending patterns  
- Customer purchase behavior trends  
- Customer engagement patterns across different metrics  
- Impact of discounts on purchasing behavior  
- Relationship between store-based purchasing activities  



<img width="704" height="590" alt="Image" src="https://github.com/user-attachments/assets/088e88d2-ca3c-41ee-952f-615519d7a3fc" />


### Summary

This analysis provides a clearer understanding of how customer features interact and influence segmentation outcomes, supporting more informed business decision-making.


---

## Feature Engineering for Clustering

| Feature | Meaning |
|---|---|
| Age | Demographics |
| Income | Purchasing power |
| Total_Spending | Customer value |
| NumWebPurchases | Online behavior |
| NumStorePurchases | Offline behavior |
| NumWebVisitsMonth | Engagement level |
| Recency | Activity freshness |


---

## Feature Scaling

StandardScaler was applied to normalize feature ranges.

### Why Scaling Matters

- Prevents income dominance  
- Ensures fair distance computation  
- Improves clustering stability  

---

## Machine Learning Approach

### Algorithm Used: K-Means Clustering

K-Means was selected due to its effectiveness in identifying hidden customer groups without labels.

---

## Cluster Optimization (Elbow Method)

The Elbow Method was used to determine optimal cluster count.

### Process

- Multiple K values tested  
- Within-cluster variance measured  
- Optimal balance identified  

### Result

 **Optimal Clusters = 6**

<img width="589" height="453" alt="Image" src="https://github.com/user-attachments/assets/5f055ebe-5422-42ea-8242-5a7682d0d148" />



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

### App Interface

<img width="921" height="811" alt="Image" src="https://github.com/user-attachments/assets/db8b2c1b-bcb4-4e96-8b7c-8a12e725ec91" />


## Live Demo
The model has been deployed as an interactive Streamlit application.

**Live App:** https://customer-segmentation-hkrphruczfq6xrtcyn3kl8.streamlit.app/




---

## Tech Stack

- Python  
- Pandas / NumPy  
- Scikit-learn  
- K-Means Clustering  
- StandardScaler  
- Streamlit  
- Joblib
- Jupyter Notebook
- Visual Studio Code (VS Code)
 

---

## Key Skills Demonstrated

- Exploratory Data Analysis (EDA)
- Data Cleaning & Preprocessing
- Feature Engineering
- Unsupervised Machine Learning
- Customer Analytics
- Model Deployment
- Business Problem Solving
- End-to-End ML Workflow


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



## Conclusion

This project demonstrates how machine learning can transform raw customer data into actionable business intelligence.

It enables businesses to:

- Understand customer behavior  
- Improve marketing strategies  
- Increase retention  
- Optimize customer engagement  
- Make data-driven decisions  

---


## Contact & Collaboration

I am open to **freelance projects, data consulting, and collaboration opportunities** in:

- Data Analysis & Visualization (Excel | SQL | Power BI | Python)
- Machine Learning Solutions (Prediction | Segmentation | Forecasting)
- Dashboard Development & Automation
- Training & Mentorship in Data Skills

---

## Contact

- 📞 Phone: +234 702 506 2857  
- 📧 Email: oladejoidris55@gmail.com  
- 💬 WhatsApp: https://wa.me/2347025062857  

---

## Location

Nigeria (Available for Remote & On-site Work)

---

## Availability

I typically respond within a few hours. 

Open to both short-term and long-term engagements.

---

## Let’s Build Something Impactful

Data tells the story — I help you understand it, translate it into insight, and use it to drive business growth.


