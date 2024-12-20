# ml-model-for-descriptor-evaluation
Overview

This repository demonstrates the process of building and evaluating a machine learning model using descriptor-based data. The goal is to predict solubility (logS) using various descriptors provided in the dataset.

Features

-Data preparation and splitting for training/testing.
-Linear regression model implementation.
-Model evaluation using metrics such as Mean Squared Error (MSE) and R-squared.
-Comparison of model performance with potential for adding additional models.

Repository Structure

[Main Script](src/main.py) Contains the main Python scripts.

Dataset

The dataset is sourced from:
[Delaney Solubility](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv) 

Description

-Target Variable: logS (Solubility)
-Features: Various molecular descriptors

Future Extensions

-Adding Random Forest or other models for comparison.
-Visualizing model predictions and residuals.

License

-This project is licensed under the MIT License. See the LICENSE file for details.

