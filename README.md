# ABOUT YOU – Customer Churn Predictor

### An End-to-End MLOps Pipeline for Proactive Customer Retention

This project presents a full-stack MLOps solution to predict customer churn for a fashion e-commerce platform like **ABOUT YOU**. It encompasses data versioning, experiment tracking, model training, and automated deployment through a REST API.

[![Build and Test](https://github.com/pythongurfer/AboutYouChurnPredictor/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/pythongurfer/AboutYouChurnPredictor/actions)
![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Business Context

In e-commerce, customer retention is both more cost-effective and strategically valuable than customer acquisition. This project addresses that challenge by implementing a machine learning pipeline that identifies users at high risk of churn. These insights can support targeted interventions—such as promotional offers or personalized outreach—to help improve customer retention and stabilize revenue.

---

## Project Scope

This project includes the following key components:

- **Data Version Control (DVC)** – Tracks changes in datasets and ensures reproducibility  
- **Experiment Tracking (MLflow)** – Logs all training runs, parameters, and performance metrics  
- **CI/CD Pipeline** – Automated testing and deployment using GitHub Actions  
- **Model Serving** – Production-ready inference API using FastAPI, containerized via Docker  

---
## Visual Overview

### Experiment Tracking with MLflow

![MLflow UI Screenshot](https://raw.githubusercontent.com/pythongurfer/AboutYouChurnPredictor/main/images/mlflow_dashboard.png)

### Live API Demo

![Postman API Screenshot](https://raw.githubusercontent.com/pythongurfer/AboutYouChurnPredictor/main/images/postman_api.png)
