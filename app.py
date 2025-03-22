from flask import Flask, render_template, request, jsonify
from supabase import create_client, Client
import os
import pandas as pd

app = Flask(__name__)

SUPABASE_URL = os.getenv("SUPABASE_URL", "your-supabase-url")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "your-supabase-api-key")

# Create the Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Retrieves data from the form
    name = request.form.get('name')
    email = request.form.get('email')
    age = request.form.get('age')
    likes_cats = request.form.get('like-cats')
    owns_cats = request.form.get('own-cats')
    favorite_activity = request.form.get('favorite-activity')
    favorite_breed = request.form.get('cat-breed')
    disliked_dogs = request.form.getlist('dog-breed')
    comments = request.form.get('suggestion_text')

    # Stores responses in the Supabase database
    data = {
        'name': name,
        'email': email,
        'age': age,
        'likes_cats': likes_cats,
        'owns_cats': owns_cats,
        'favorite_activity': favorite_activity,
        'favorite_breed': favorite_breed,
        'disliked_dogs': disliked_dogs,
        'comments': comments
    }

    # Insert the data into the 'responses' table in Supabase
    response = supabase.table('responses').insert(data).execute()

    # Check for any issues with inserting the data
    if response.status_code != 201:
        return jsonify({"status": "error", "message": response.data}), 400

    return jsonify({"status": "success"})  # Respond to the frontend after submission

@app.route('/average_responses')
def average_responses():
    # Fetch all responses from the Supabase database
    responses = supabase.table('responses').select('*').execute()

    if responses.status_code != 200:
        return jsonify({"status": "error", "message": "Failed to fetch data from the database"}), 400

    # Convert responses to a pandas DataFrame for easier analysis
    df = pd.DataFrame(responses.data)
    
    # Calculate average age (considering age may be optional)
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    average_age = df['age'].mean()
    
    # Calculate the number of people who like cats
    like_cats_count = df[df['likes_cats'] == 'Yes. Good answer.'].shape[0]
    
    # Calculate most popular cat breed (mode)
    most_popular_breed = df['favorite_breed'].mode()[0]
    
    # Calculate disliked dog breeds (count how many users dislike each breed)
    disliked_dogs = df['disliked_dogs'].explode().value_counts().to_dict()

    # Send the calculated averages and statistics back to the frontend as JSON
    return jsonify({
        'average_age': average_age,
        'like_cats_count': like_cats_count,
        'most_popular_breed': most_popular_breed,
        'disliked_dogs': disliked_dogs
    })

if __name__ == '__main__':
    app.run(debug=True)
