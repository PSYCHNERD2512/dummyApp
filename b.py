from flask import Flask, render_template
import datetime
import requests
import random

# Unsplash API details
UNSPLASH_ACCESS_KEY = "E26GBCuswAtWEn-amZJ_h_yJI_xRRld5ICryr8p1DVw"

app = Flask(__name__)

# Function to get a random background image from Unsplash
def get_random_unsplash_image():
    url = f"https://api.unsplash.com/photos/random?query=dark+Motivation&client_id={UNSPLASH_ACCESS_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        image_url = data['urls']['regular']
        return image_url
    else:
        return None

# ZenQuotes API for random motivational quotes
def get_random_quote():
    url = "https://zenquotes.io/api/random"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']
        return f"{quote} - {author}"
    else:
        return "Keep going, you're doing great!"

# Function to calculate days left until New Year
def days_until_new_year():
    today = datetime.date.today()
    new_year = datetime.date(today.year + 1, 1, 1)
    delta = new_year - today
    return delta.days

@app.route('/')
def home():
    days_left = days_until_new_year()
    quote = get_random_quote()
    background_image_url = get_random_unsplash_image()

    return render_template('index.html', days_left=days_left, quote=quote, background_image_url=background_image_url)

if __name__ == '__main__':
    app.run(debug=True)

