# ABOUT YOU - Customer Churn Predictor 

### An End-to-End MLOps Pipeline to Proactively Identify and Reduce Customer Churn

This project demonstrates a full-stack MLOps approach to predict customer churn for a fashion e-commerce platform like **ABOUT YOU**. It covers everything from data versioning and experiment tracking to automated model deployment via a REST API.

[![Build and Test](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/YOUR_USERNAME/YOUR_REPO/actions)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## The Business Problem

In e-commerce, customer retention is cheaper and more effective than customer acquisition. This project tackles this challenge by building a machine learning system that identifies customers who are at a high risk of churning. By flagging these users proactively, the business can launch targeted retention campaigns (e.g., special offers, personalized outreach) to improve customer loyalty and protect revenue.

---

## Visual Showcase

### System Architecture

This diagram illustrates the complete MLOps workflow, from data ingestion to model prediction.

```mermaid
graph TD
    A[Data Source: customer_data.csv] --> B{DVC: Version Control};
    B --> C[Training Script: train.py];
    C -- Log Experiments --> D(MLflow Tracking Server);
    C -- Register Best Model --> E[MLflow Model Registry];
    E -- Loads Production Model --> F{FastAPI Prediction Service};
    F -- Containerized by --> G([Docker Image]);
    H[API Request] -- JSON features --> F;
    F -- churn: 0/1 --> H;
    I{GitHub Actions} -- on push --> J[Run Pytests];
    J -- on success --> C;



Experiment Tracking with MLflow

<img src="/images/mlflow_dashboard.png" alt="MLflow UI Screenshot" width="800"/>


Live API Demo

<img src="/images/postman_api.png" alt="Postman API Screenshot" width="800"/>

