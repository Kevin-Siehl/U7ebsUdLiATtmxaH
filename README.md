This project involved predicting customer happiness based on results from a survey.

# Customer Satisfaction Prediction & Feature Importance Analysis

This project builds a predictive machine learning pipeline to determine overall customer happiness based on a 6-question survey. Because the primary business goal is to proactively flag and mitigate customer dissatisfaction, the pipeline is heavily optimized to maximize **Recall** for unhappy customers—ensuring few unhappy customers go unnoticed.

Additionally, this repository utilizes **Recursive Feature Elimination (RFE)** and **Recursive Feature Elimination with Cross-Validation (RFECV)** to rank which service factors impact customer satisfaction the most, driving actionable business recommendations.

---

## 🚀 Key Highlights & Results

* **Metric Optimized:** Recall (Targeting Unhappy Customers to minimize False Positives).
* **Ensemble Boost:** Combining individual classifiers into a **Voting Ensemble** boosted individual recall scores (ranging from 72%–78%) up to an outstanding **86%**.
* **Core Driver:** Sensitivity testing revealed that **Order Delivery Time (Question 1)** behaves as a critical switch; dropping to a score of 1 out of 5 mathematically guarantees a predicted "Unhappy" status across the entire dataset.

---

## 🛠️ The Dataset & Survey Questions

The dataset consists of 126 customer responses. Features are rated on a Likert scale from 1 (Most Dissatisfied) to 5 (Most Satisfied):

1. **Q1:** My Order Was Delivered on Time
2. **Q2:** The Contents of My Order Were as Expected
3. **Q3:** I Ordered Everything I Wanted
4. **Q4:** I Paid a Good Price for My Order
5. **Q5:** I Am Satisfied with My Courier
6. **Q6:** The App Makes Ordering Easy

---

## 🧠 Model Pipeline & Architecture

### 1. Hyperparameter Optimization
Four scikit-learn classification algorithms were tuned using `GridSearchCV` to maximize recall for the unhappy class:
* **SGD Classifier** (Base Recall: 78%)
* **Decision Tree Classifier** (Base Recall: 76%)
* **SVC Classifier** (Base Recall: 72%)
* **NuSVC Classifier** (Base Recall: 72%)

### 2. Voting Ensemble
A hard/soft voting meta-classifier combining all four optimized models to achieve a final **Recall of 86%** on predicting unhappy customers.

### 3. Feature Selection & Relevancy Matrix
* **RFECV (Optimizing Recall):** The SGD Classifier isolated **Q5** and **Q6** as the only critical variables needed to maintain baseline high recall. The Decision Tree isolated all features *except* Q2 and Q4.
* **RFE (Optimizing Accuracy):** RFE ranked all 6 features linearly by general predictive power. Averaging the rankings highlights **Q5 (Courier)**, **Q1 (On-time)**, and **Q6 (App Ease)** as the top 3 core drivers of accuracy.

| Algorithm / Test         | Q1 (On-Time)     | Q2 (Contents)    | Q3 (Assortment)  | Q4 (Price)       | Q5 (Courier)    | Q6 (App)        |
| :----------------------: | :--------------: | :--------------: | :-------------:  | :--------------: | :-------------: | :-------------: |
| **RFECV - SGD**          | Dropped (Rank 1) | Dropped (Rank 4) | Dropped (Rank 3) | Dropped (Rank 2) | **Kept (True)** | **Kept (True)** |
| **RFECV - DecisTree**    | **Kept (True)**  | Dropped (Rank 2) | **Kept (True)**  | Dropped (Rank 1) | **Kept (True)** | **Kept (True)** |
| **RFE Rank - SGD**       | Rank 3           | Rank 6           | Rank 5           | Rank 4           | Rank 2          | Rank 1          |
| **RFE Rank - DecisTree** | Rank 2           | Rank 6           | Rank 3           | Rank 5           | Rank 1          | Rank 4          |
| **Average RFE Rank**     |    **2.5**       |      6.0         |      4.0         |      4.5         |    **1.5**      |    **2.5**      |

*(Note: In RFE ranking, lower numbers denote higher importance).*

---

## 🧪 Sensitivity Analysis (Hypothetical Data Testing)
To stress-test the model, 12 hypothetical variants of the dataset were created by holding 5 questions at baseline and pushing one target question to its maximum (5/5) or minimum (1/5) extreme. 
* **Q1 Extremes:** Generating a "Bad-1" (1/5 on On-Time Delivery) caused the Voting Ensemble to predict **100% Unhappy** customer sentiment across the entire batch, revealing it as an absolute bottleneck for retention.

---

## 📊 Business Recommendations

Based on the combined results of the RFE, RFECV, and Voting Ensemble testing, operations should focus immediate resources on three areas:

1.  **On-Time Delivery (Q1 - Critical Priority):** Late orders completely ruin the customer experience regardless of other factors. **Action:** Implement automated partial refunds if orders pass a strict lateness threshold to soften the negative impact.
2.  **Courier Satisfaction (Q5):** The physical touchpoint matters heavily to retention accuracy. **Action:** Deploy courtesy and customer service training for delivery personnel.
3.  **App Interface Improvements (Q6):** UI frustration directly taints overall brand sentiment. **Action:** Audit the app checkout workflow for bottlenecks, and establish a real-time support hotline or clearer instruction layouts as a short-term patch.

---

## 💻 Getting Started / Installation

### Prerequisites
Make sure you have Python 3.8+ and Jupyter Notebook installed.

### Installation
1. Clone this repository:
   ```bash
   git clone [https://github.com/Kevin-Siehl/U7ebsUdLiATtmxaH.git](https://github.com/Kevin-Siehl/U7ebsUdLiATtmxaH.git)
   cd U7ebsUdLiATtmxaH
