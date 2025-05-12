# 🍽️ Food Recipe Assistant

This is a Flask web application that helps users find food recipes by name. It displays the ingredients and instructions from a local JSON file and, if the recipe isn't available, it fetches a related cooking video from YouTube.

---

## 🚀 Features

- Get food details (ingredients + instructions) from a local JSON file.
- Automatically fetch a YouTube video tutorial if recipe is missing.
- Simple web interface to input food names and receive results.
- Easily extendable with more food items in the `food_data.json`.

---

## 📁 Project Structure

├── app.py # Main Flask application
├── food_data.json # Local food data (ingredients & instructions)
├── templates/
│ └── index.html # Frontend HTML template
├── .env # Environment variables (optional)
└── README.md # Project documentation
