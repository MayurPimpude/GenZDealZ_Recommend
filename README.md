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
- [Data Preparation](#data-preparation)
- [Streamlit Application](#streamlit-application)

## Installation

### Prerequisites

- Python 3.9+
- pip (Python package installer)

### Clone the Repository
```bash
git clone https://github.com/MayurPimpude/GenZDealZ_Recomendation.git

cd hybrid-recommendation-system

pip install -r requirements.txt

cd models

python data.py
```
## Streamlit Application

The main.py script implements the Streamlit application, which:

Loads the saved models and data files.
Provides a user interface to input a list of items.
Displays recommendations based on the input items using RNN, cosine similarity, and a hybrid approach.

## Data Preparation

The dataset used in this project was created by combining multiple sources of user purchase history. The additional information added to the dataset includes item types, which categorize each item into broader categories such as 'e-commerce', 'fashion', 'food', etc.

Why Extra Information Was Added
1. Item Types: By including item types, the recommendation system can make more informed suggestions by considering the categories of items a user has shown interest in. This helps in filtering recommendations to    ensure they align with the user's interests.
2. Enhanced Recommendations: The additional information helps improve the accuracy and relevance of the recommendations, particularly when using cosine similarity. It allows the system to provide recommendations     that are not only similar in terms of user behavior but also in terms of item categories.

## Streamlit Application

Run the Streamlit application using the following command:

streamlit run app.py
Interacting with the Application
Open your web browser and navigate to the URL provided by Streamlit (usually http://localhost:8501).

The application will display recommendations generated by the RNN, cosine similarity, and the hybrid approach.
