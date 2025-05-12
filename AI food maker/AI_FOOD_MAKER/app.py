from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

def load_food_data():
    with open("food_data.json", "r") as file:
        return json.load(file)
    
# API Keys (Replace with your own keys)
YOUTUBE_API_KEY = "AIzaSyDgMZCkzjV6_CndpglPs8Ki6FJD2MsOrlw"

# Fetch YouTube recipe video
def get_youtube_video(query):
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}+recipe&type=video&key={YOUTUBE_API_KEY}"
    response = requests.get(url)
    data = response.json()
    if "items" in data and data["items"]:
        return f"https://www.youtube.com/watch?v={data['items'][0]['id']['videoId']}"
    return "No video found."

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/get_food_details', methods=['POST'])
def get_food_details():
    food_name = request.form.get("food_name").lower()
    
    # Load food data from JSON
    food_data = load_food_data()

    if food_name in food_data:
        ingredients = ", ".join(food_data[food_name]["ingredients"])
        instructions = food_data[food_name]["instructions"]
    else:
        ingredients = "Unknown ingredients"
        instructions = "Sorry, I don't have this recipe yet!---But we have video for you" 

    youtube_link = get_youtube_video(food_name)

    return jsonify({
        "ingredients": ingredients,
        "instructions": instructions,
        "youtube_link": youtube_link
    })

if __name__ == '__main__':
    app.run(debug=True,port="7860",host='0.0.0.0')
