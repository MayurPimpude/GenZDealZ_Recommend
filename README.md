# Hybrid Recommendation System

This repository contains a hybrid recommendation system that combines cosine similarity and a Recurrent Neural Network (RNN) to provide personalized recommendations. The system is implemented using Streamlit for the frontend and TensorFlow/Keras for the RNN.

## Result
RNN Recommendations - 
train accuracy - 82.14%
test accuracy - 57.14%
Initially, implemented an RNN-based recommendation system. However, we found that the RNN recommendations were not as accurate or relevant as expected. The RNN struggled with the sparse nature of the purchase data and often produced less relevant recommendations.

Cosine Similarity Recommendations
In contrast, the cosine similarity-based recommendation system performed significantly better. It provided more accurate and relevant recommendations by leveraging the similarity between items based on user purchase history. This method proved to be more effective for the given dataset and user behavior patterns.

Hybrid Recommendations
To combine the strengths of both approaches, implemented a hybrid recommendation system. This system combines the cosine similarity and RNN recommendations to provide a balanced set of suggestions. Despite the inclusion of RNN recommendations, the cosine similarity method remains the dominant and more reliable recommendation source.



## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Data Preparation](#data-preparation)
- [Streamlit Application](#streamlit-application)

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Clone the Repository

```bash
git clone https://github.com/yourusername/GenZDealZ_Recomendation.git
cd hybrid-recommendation-system

pip install -r requirements.txt

python data.py

## Streamlit Application

The main.py script implements the Streamlit application, which:

Loads the saved models and data files.
Provides a user interface to input a list of items.
Displays recommendations based on the input items using RNN, cosine similarity, and a hybrid approach.
