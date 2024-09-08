# Loan Default Prediction

![banner](banner.jpg)

## Table of Contents

-   [Technologies Used](#technologies-used)
-   [Description](#description)
-   [Objectives](#objectives)
-   [Presentation](#presentation)
-   [Notebooks Overview](#notebooks-overview)
-   [Using Docker](#using-docker)
-   [Installation](#installation)
-   [Usage](#usage)
-   [Project Structure](#project-structure)
-   [Collaborators](#collaborators)
-   [License](#license)

---

## Technologies Used

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black) ![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![MLflow](https://img.shields.io/badge/MLflow-%230080FF.svg?style=for-the-badge&logo=mlflow&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

---

## Description
This project is focused on building an app that estimates the probability of default for each client based on their characteristics. Then create a CI/CD pipeline to deploy it with AWS Elastic Container Service

### Objectives
The main objective of this project is build an image and a pipeline with all the necessary tools to achieve the deployment of a predictive app. The specific steps include:

1. **Data Preprocessing**: Filtering and preparing the dataset for analysis.
2. **Model Engineering**: Test at least two classification algorithms.
3. **Model Tracking**: Tracking the metrics and artifacts of the model with MLflow.
4. **App Deployment**: Create a CI/CD pipeline.
---

## Presentation

A **presentation** is available as a **PDF** file in the repo ```Loan_Default_Prediction_MLOPS_Presentation.pdf``` & also as a **Canva/Powerpoint** presentation through the following link: [Presentation Link](https://www.canva.com/design/DAGQGXGl6cY/MxnDDFWOFYTaYfHhl0eRFg/view?utm_content=DAGQGXGl6cY&utm_campaign=designshare&utm_medium=link&utm_source=editor).

---
## Notebooks Overview

1. **¨Exploratory_Data_Analysis.ipynb**:
   - This notebook contains the data exploration, analysis & preprocessing.
2. **¨Loan_Default_Prediciont_Models.ipynb**:
   - This notebook contains the models fitting, evaluation and mlflow setup.
---
## Using Docker
#### 1. Pulling the Docker Image
To pull the Docker image from Docker Hub, run the following command:
```sh
# Pull the docker image
$ docker pull medkallel/loan-default-prediction:latest
```
#### 2. Building the Docker Image
If you prefer to build the Docker image locally, navigate to the project directory and run:

```sh
# Build the docker image
$ docker build -t loan-default-prediction .
```
#### 3. Running the Docker Container
To run the Docker container, use the following command:
```sh
# Run the docker container
$ docker run -p 5000:5000 loan-default-prediction
```
> [!TIP] 
> You can access the app on another device by following the link: ```http://<server-ip>:8501```
---
## Installation

> [!IMPORTANT]
> The project was done on Python 3.11.6

To run this project locally, follow these steps:

1. Clone the repository:
```sh
# Clone the repository
$ git clone https://github.com/Medkallel/Loan-Default-Prediction.git
# Navigate into the directory
$ cd Loan-Default-Prediction
```
2. Install the required dependencies:
```sh
# Install the requirements
$ pip install -r requirements.txt
```
---
## Usage 

1. To use the App, Just run the app.py
```sh
$ python app.py
```
---
## Project structure
```sh
📦 mlops-project/
├── 📁.github/
│   └── 📁workflows/
│       └── aws.yaml
├── 📁Data/
│   ├── 🗃️Loan_Data_Describe.csv # Describe data used to denormalize
│   ├── 🗃️Loan_Data.csv # Initial Dataset
│   └── 🗃️Processed_Loan_Data.csv 
│ 
├── 📁Models/
│   └── 🤖model.pkl
│
├── 📁mlartifacts/ # Contains mlflow artifacts for runs
├── 📁mlruns/ # Contains mlflow runs logs
│ 
├── 📁templates/
│   └── index.html
├── 🐍app.py
├── 📓Exploratory_Data_Analysis.ipynb
├── 📓Loan_Default_Prediction_Models.ipynb
├── 📄requirements.txt
├── 📄.dockerignore
├── 📄.gitignore
├── 📄Dockerfile
├── 📄LICENCE.md
├── 📄README.md
└── 📄Loan_Default_Prediction_MLOPS_Presentation.pdf
```

---


## Collaborators

This project was developed by a collaborative team. Each member played a crucial role in the research, development, and analysis:

- **Mohamed Kallel**
- **Jean Christophe Rigoni**
- **Simon Pierre Rodner**
---



## License
This project is under the **CC BY-NC 4.0 License**. For more information, refer to the license file. <br/>
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
