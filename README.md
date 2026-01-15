# 📊 Customer Churn Prediction — Production-Ready ML System

## 🔹 Overview

This repository contains an **end-to-end, production-ready Customer Churn Prediction System** designed to help organizations anticipate customer attrition and implement proactive retention strategies.

The project integrates rigorous data science practices with modern MLOps and cloud deployment principles, transforming raw telecom customer data into a scalable, deployable, and business-actionable machine learning solution.
---

## 🎯 Project Objectives

The primary goals of this project are to:

* Accurately predict the likelihood of customer churn.
* Identify key behavioral and service-related drivers of churn.
* Build a reproducible machine learning pipeline.
* Deliver a containerized and cloud-deployable application suitable for real-world use.

---

## 🧩 End-to-End Methodology

The system follows a structured ML lifecycle:

1. **Data Acquisition** — Telecom customer churn dataset.
2. **Exploratory Data Analysis (EDA)** — Statistical and visual analysis to uncover trends, correlations, and risk patterns.
3. **Data Preprocessing** — Handling missing values, encoding categorical variables, and normalizing features.
4. **Feature Engineering** — Creating meaningful predictors to enhance model performance.
5. **Model Development** — Training multiple supervised classification models.
6. **Model Evaluation** — Performance assessment using Precision, Recall, F1-Score, and ROC-AUC.
7. **Model Selection & Serialization** — Persisting the best model using Joblib
8. **Containerization** — Packaging the application with Docker for portability and consistency.
9. **Cloud Deployment** — Hosting the application on **AWS ECS** for scalability and reliability.


## Software and Tools Requirement

1. [GitHub Account](https://github.com)
2. [VS Code IDE](https://code.visualstudio.com)
3. [Kaggle Account](https://kaggle.com)
4. [Jupyter Notebook](https://jupyter.org/)
5. [FastAPI](https://fastapi.tiangolo.com/)

## Create a New Environment

```bash
py -3.12 -m venv venv

---
```

## 🤖 Machine Learning Models Evaluated

* Logistic Regression
* Random Forest Classifier
* Gradient Boosting Classifier
* XGBoost Classifier 

The final model was selected based on optimal balance between predictive performance and operational efficiency.

---

## 🛠️ Technologies & Skills Utilized

**Core Technologies:**

* **Python**
* **Pandas, NumPy** — Data manipulation and numerical computation
* **Scikit-Learn** — Model development and evaluation
* **Matplotlib, Seaborn** — Data visualization

**MLOps & Cloud:**

* **Docker** — Application containerization
* **AWS ECS** — Cloud-based deployment and orchestration
* **Joblib  — Model serialization and storage

**Data Science Practices:**

* Feature Engineering
* Data Cleaning & Transformation
* Model Validation & Cross-Validation
* Performance Monitoring

---

## 🐳 Local Deployment with Docker

### Build the Docker image:

```bash
docker build -t churn-prediction-app .
```

### Run the application container:

```bash
docker run -p 8000:8000 churn-prediction-api
```

Access the service locally at: `http://localhost:8000`

---

## ☁️ Deployment on AWS ECS

Recommended deployment steps:

1. Build and tag the Docker image.
2. Push the image to **AWS ECR (Elastic Container Registry)**.
3. Create an **ECS Task Definition** using the container image.
4. Launch the service via **ECS Cluster** with a load balancer.
5. Monitor performance through AWS CloudWatch.

---

## 📊 Business Value

This system enables organizations to:

* Reduce customer churn through early risk detection.
* Optimize marketing and retention budgets.
* Deliver personalized customer engagement strategies.
* Improve long-term customer lifetime value (CLV).

---

## 🤝 Contributions

Contributions, improvements, and feature enhancements are welcome. Please fork the repository and submit a pull request.

---

## 📬 Contact

For questions, collaboration, or feedback, feel free to connect via LinkedIn or open an issue in this repository.

⭐ If you find this project valuable, please consider starring the repository.
