import streamlit as st
import numpy as np
import pandas as pd
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the models and data
model = load_model('rnn_model.h5')
with open('./data/tokenizer.pkl', 'rb') as file:
    tokenizer = pickle.load(file)
with open('./data/item_sim_df.pkl', 'rb') as file:
    item_sim_df = pickle.load(file)
with open('./data/user_item_data.pkl', 'rb') as file:
    user_item_data = pickle.load(file)

# Define sequence length used in the RNN model
sequence_length = 3

# Define functions for recommendations
def recommend_rnn(user_purchases, top_n=5):
    user_sequences = tokenizer.texts_to_sequences(user_purchases)
    user_padded = pad_sequences(user_sequences, maxlen=sequence_length, padding='post')
    prediction = model.predict(user_padded)
    top_items = prediction[0].argsort()[-top_n:][::-1]
    recommendations = [(tokenizer.index_word[item], prediction[0][item]) for item in top_items if item in tokenizer.index_word]
    return recommendations

def get_item_type(item):
    item_type = user_item_data[user_item_data['purchases'] == item]['item_type'].values
    if len(item_type) > 0:
        return item_type[0]
    else:
        return None

def get_item_recommendations(custom_items, top_n=3):
    similarity_scores = item_sim_df[custom_items].mean(axis=1)
    custom_item_types = set(get_item_type(item) for item in custom_items)
    recommendation_scores = similarity_scores[similarity_scores.index.map(get_item_type).isin(custom_item_types)]
    recommendation_scores = recommendation_scores[~recommendation_scores.index.isin(custom_items)]
    return recommendation_scores.sort_values(ascending=False).head(top_n)

def hybrid_recommendations(custom_items, top_n=5, alpha=0.5):
    rnn_recommendations = recommend_rnn(custom_items, top_n)
    rnn_recommendation_dict = {item: score for item, score in rnn_recommendations}
    cosine_recommendations = get_item_recommendations(custom_items, top_n)
    combined_scores = {}
    for item, score in cosine_recommendations.items():
        combined_scores[item] = alpha * score + (1 - alpha) * rnn_recommendation_dict.get(item, 0)
    combined_recommendations = sorted(combined_scores.items(), key=lambda x: x[1], reverse=True)
    return combined_recommendations[:top_n], rnn_recommendations, cosine_recommendations

# Streamlit UI
st.title('Hybrid Recommendation System')

custom_items = st.text_input('Enter items (comma-separated):', '')
custom_items_list = [item.strip() for item in custom_items.split(',') if item.strip()]

if custom_items_list:
    recommendations, rnn_recommendations, cosine_recommendations = hybrid_recommendations(custom_items_list)
    
    st.write(f"**RNN Recommendations for custom input {custom_items_list}:**")
    for item, score in rnn_recommendations:
        st.write(f"Item: {item}, Score: {score}")
    
    st.write(f"**Cosine Similarity Recommendations for custom input {custom_items_list}:**")
    for item, score in cosine_recommendations.items():
        st.write(f"Item: {item}, Score: {score}")
    
    st.write(f"**Hybrid Recommendations for custom input {custom_items_list}:**")
    for item, score in recommendations:
        st.write(f"Item: {item}, Score: {score}")
