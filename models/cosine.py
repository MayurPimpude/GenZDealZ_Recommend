import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from data import data
# Load the provided CSV file
# file_path = 'recommendation.csv'
# data = pd.read_csv(file_path)
data = data()
# Filter relevant columns
user_item_data = data[['user', 'purchases', 'item_type']]

# Create a set of all unique items
all_items = list(set(user_item_data['purchases']))

# Create a user-item matrix
user_item_matrix = pd.DataFrame(0, index=user_item_data['user'].unique(), columns=all_items)

# Fill the user-item matrix
for index, row in user_item_data.iterrows():
    user_item_matrix.loc[row['user'], row['purchases']] = 1

# Compute the cosine similarity between users
user_similarities = cosine_similarity(user_item_matrix)

# Create a DataFrame for similarities
user_sim_df = pd.DataFrame(user_similarities, index=user_item_matrix.index, columns=user_item_matrix.index)

# Function to get item types
def get_item_type(item):
    return user_item_data[user_item_data['purchases'] == item]['item_type'].values[0]

def get_recommendations(user_id, top_n=3):
    # Get similarity scores for the target user
    similarity_scores = user_sim_df[user_id]

    # Get the target user's purchases
    target_user_purchases = set(user_item_matrix.loc[user_id][user_item_matrix.loc[user_id] == 1].index)

    # Get the types of items the user has purchased
    target_user_item_types = set(get_item_type(item) for item in target_user_purchases)

    # Calculate weighted scores for all items based on similar users' purchases
    recommendation_scores = user_item_matrix.T.dot(similarity_scores).sort_values(ascending=False)

    # Filter recommendations by item type
    recommendation_scores = recommendation_scores[recommendation_scores.index.map(get_item_type).isin(target_user_item_types)]

    # Remove items the target user has already purchased
    recommendation_scores = recommendation_scores[~recommendation_scores.index.isin(target_user_purchases)]

    # Return top N recommended items with scores
    return recommendation_scores.head(top_n)

def recommend_for_custom_input(custom_items, top_n=3):
    # Create a temporary user vector for the custom items
    temp_user_vector = pd.Series(0, index=all_items)
    temp_user_vector[custom_items] = 1

    # Get the types of items in the custom input
    custom_item_types = set(get_item_type(item) for item in custom_items)

    # Calculate similarity of the custom input with existing users
    custom_user_sim = cosine_similarity([temp_user_vector], user_item_matrix)[0]

    # Calculate weighted scores for all items based on the custom input similarity
    recommendation_scores = user_item_matrix.T.dot(custom_user_sim).sort_values(ascending=False)

    # Filter recommendations by item type
    recommendation_scores = recommendation_scores[recommendation_scores.index.map(get_item_type).isin(custom_item_types)]
    
    # Remove items already in the custom input
    recommendation_scores = recommendation_scores[~recommendation_scores.index.isin(custom_items)]
    
    # Return top N recommended items with scores
    return recommendation_scores.head(top_n)

# Example usage
custom_items = ['ola']
recommendations = recommend_for_custom_input(custom_items)
print(f"Recommendations for custom input {custom_items}:\n{recommendations}")
