from flask import Flask, render_template, request, jsonify
import pandas as pd
import json

app = Flask(__name__)

# In-memory list to store form responses (you can replace this with a database)
responses = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get data from the form
    name = request.form.get('name')
    email = request.form.get('email')
    age = request.form.get('age')
    likes_cats = request.form.get('like-cats')
    owns_cats = request.form.get('own-cats')
    favorite_activity = request.form.get('favorite-activity')
    favorite_breed = request.form.get('cat-breed')
    disliked_dogs = request.form.getlist('dog-breed')
    comments = request.form.get('suggestion_text')

    # Store the response
    response = {
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
    
    responses.append(response)  # Add the response to the list

    return jsonify({"status": "success"})  # Respond to the frontend after submission

@app.route('/average_responses')
def average_responses():
    # Convert the responses list to a DataFrame for easier analysis
    df = pd.DataFrame(responses)
    
    # Calculate average age (considering age may be optional)
    average_age = df['age'].apply(pd.to_numeric, errors='coerce').mean()
    
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
