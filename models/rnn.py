import pandas as pd
from data import data
from sklearn.model_selection import train_test_split
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

df_exploded = data()

tokenizer = Tokenizer()
tokenizer.fit_on_texts(df_exploded['purchases'].astype(str).tolist() + df_exploded['item_type'].astype(str).tolist())

# Prepare sequences for training
sequence_length = 3
X = []
y = []

for user, group in df_exploded.groupby('user'):
    user_purchases = group['purchases'].astype(str).tolist()
    encoded_purchases = tokenizer.texts_to_sequences(user_purchases)
    encoded_purchases = [item for sublist in encoded_purchases for item in sublist]

    for i in range(len(encoded_purchases) - sequence_length):
        X.append(encoded_purchases[i:i + sequence_length])
        y.append(encoded_purchases[i + sequence_length])

# Convert to numpy arrays
X = pad_sequences(X, maxlen=sequence_length)
y = np.array(y)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

vocab_size = len(tokenizer.word_index) + 1

model = Sequential([
    Embedding(input_dim=vocab_size, output_dim=64, input_length=sequence_length),
    LSTM(64, return_sequences=True),
    LSTM(32),
    Dense(vocab_size, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

model.fit(X_train, y_train, epochs=80, batch_size=32)

loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy * 100:.2f}%")

def recommend_rnn(user_purchases, top_n=5):
    # Convert the user purchases to sequences
    user_sequences = tokenizer.texts_to_sequences(user_purchases)
    user_padded = pad_sequences(user_sequences, maxlen=sequence_length, padding='post')
    
    # Get the model predictions
    prediction = model.predict(user_padded)
    
    # Get the top N items with their scores
    top_items = prediction[0].argsort()[-top_n:][::-1]
    recommendations = [(tokenizer.index_word[item], prediction[0][item]) for item in top_items if item in tokenizer.index_word]
    
    return recommendations

# Custom input array
custom_input_rnn = ['mcd','dominos']
recommendations_rnn = recommend_rnn(custom_input_rnn)

# Print recommendations with their scores
for item, score in recommendations_rnn:
    print(f"Item: {item}, Score: {score}")
