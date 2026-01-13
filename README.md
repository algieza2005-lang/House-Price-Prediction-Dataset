# House Price Prediction – Technical Project Report

## 1. Introduction

This repository contains a complete end-to-end **Machine Learning application** for predicting house prices based on property characteristics. The project demonstrates the full lifecycle of a data-driven system, starting from dataset processing and model training, continuing through backend API development using FastAPI, and ending with a simple yet functional web-based user interface.

The main objective of this project is to illustrate how a trained machine learning model can be deployed into a real-world application where users can interactively obtain predictions in real time.

---

## 2. Project Objectives

The objectives of this project are:

1. To process and prepare a structured house price dataset for machine learning tasks.
2. To train a regression-based machine learning model capable of predicting house prices.
3. To deploy the trained model as a RESTful API using FastAPI.
4. To develop a web interface that allows users to input data and receive predictions.
5. To provide technical documentation explaining the system architecture and workflow.

---

## 3. Scope of the System

The system is designed with the following scope and limitations:

* The prediction is based on historical housing data provided in the dataset.
* Input features used by the model:

  * Building area (square meters)
  * Number of bedrooms
  * Number of bathrooms
* Output:

  * Estimated house price (scaled according to the dataset)
* The system does not consider external factors such as location quality, economic conditions, or market trends.

---

## 4. Dataset Description

The dataset used in this project is a structured CSV file containing historical house price information.

### 4.1 Selected Features

The following attributes are used for model training:

| Feature   | Description                   |
| --------- | ----------------------------- |
| Area      | Building area (m²)            |
| Bedrooms  | Number of bedrooms            |
| Bathrooms | Number of bathrooms           |
| Price     | House price (target variable) |

### 4.2 Data Preprocessing

Before training the model, several preprocessing steps are applied:

* Selection of relevant features and target variable
* Handling missing values using mean imputation
* Splitting the dataset into training and testing sets (80% training, 20% testing)

These steps ensure the dataset is clean and suitable for regression modeling.

---

## 5. Machine Learning Methodology

### 5.1 Algorithm Selection

The project uses the **Linear Regression** algorithm, chosen due to:

* Its simplicity and interpretability
* Suitability for numerical regression problems
* Low computational complexity

### 5.2 Model Training

The model training process includes:

1. Loading the dataset
2. Splitting the data into training and testing sets
3. Training the Linear Regression model on the training data
4. Saving the trained model using `joblib`

The trained model is stored as:

```
house_price_model.pkl
```

---

## 6. System Architecture

The system architecture consists of three main components:

1. **Machine Learning Model**
   A trained Linear Regression model responsible for generating predictions.

2. **Backend API (FastAPI)**
   Handles HTTP requests, loads the trained model, performs predictions, and returns results.

3. **Frontend Interface (HTML/CSS)**
   Provides a user-friendly form for input and displays prediction results.

### 6.1 System Workflow

```
User Input → Web Interface → FastAPI Backend → ML Model → Prediction Result → Web Interface
```

---

## 7. API Implementation

### 7.1 Web-Based Prediction Endpoint

* **Endpoint:** `POST /predict`
* Accepts form data from the HTML interface
* Returns rendered HTML with prediction results

### 7.2 JSON API Endpoint

* **Endpoint:** `POST /api/predict`
* Accepts JSON input
* Returns prediction results in JSON format

Example request:

```json
{
  "area": 120,
  "bedrooms": 3,
  "bathrooms": 2
}
```

Example response:

```json
{
  "predicted_price": 350000,
  "predicted_price_rupiah": "Rp 350.000"
}
```

---

## 8. User Interface

The frontend is implemented using HTML and CSS, providing:

* A simple form for user input
* Server-side rendering of prediction results
* Clear visualization of estimated house price

The interface is intentionally kept minimal to focus on system functionality.

---

## 9. Project Structure

```
project-root/
│
├── templates/
│   └── index.html
├── train.py
├── main.py
├── house_price_model.pkl
├── README.md
└── requirements.txt
```

---

## 10. Setup and Execution

### 10.1 Environment Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 10.2 Model Training

```bash
python train.py
```

### 10.3 Running the FastAPI Server

```bash
uvicorn main:app --reload
```

The application will be accessible at:

```
http://127.0.0.1:8000
```

---

## 11. Conclusion

This project demonstrates a complete machine learning workflow, from data preparation and model training to deployment using FastAPI and integration with a web interface. The system serves as a practical example of how machine learning models can be embedded into real applications for real-time predictions.

Future improvements may include:

* Adding model evaluation metrics
* Using more advanced regression algorithms
* Enhancing frontend interactivity
* Deploying the system to a cloud environment

---

## 12. References

* FastAPI Documentation: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
* Reference Paper: [https://www.scirp.org/journal/paperinformation?paperid=132019](https://www.scirp.org/journal/paperinformation?paperid=132019)
