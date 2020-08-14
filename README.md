# CancerPrediction
Cancer Prediction Web Application

# Predicting-cancer-type
Classifying the tumors and non-tumor gene expressions into **34 different types**: *33 cancer types + 1 normal sample type*.

1. [Installation](#installation)
2. [How to Run](#how-to-run)
3. [References](#references)

## Installation
Based on the data from the paper by [**Mostavi, et al.**], newly splitted data for the model can be downloaded [**here**](https://drive.google.com/drive/folders/1EgHyGOZzRiZlv1AZxW4fB2E3H8UpfBiV?usp=sharing).
```
git clone git@github.com:comedi-team3/CancerPrediction_Model.git
cd CancerPrediction_Model
```

## How to Run
1. Start server using **docker-compose**
```
$ docker-compose build
$ docker-compose up
```
2. Access webpage
```
http://0.0.0.0:5000
```
3. The input data for prediction is simply an individual samples of the input data. The samples can be downloaded [**here**](https://drive.google.com/drive/folders/1v7r8RlWGj3XwzJcHIyz0tVDIvwcdxJg7?usp=sharing).

## References
- Mostavi, Milad, et al. [**Convolutional neural network models for cancer type prediction based on gene expression**](https://link.springer.com/content/pdf/10.1186/s12920-020-0677-2.pdf). BMC Medical Genomics 13 (2020): 1-13.
