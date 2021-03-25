from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

url = "https://api.thecatapi.com/v1/breeds/search"
headers = {'x-api-key': '82cef8ce-039b-47e9-a74f-f6a7053171cd'}

url_img = 'https://api.thecatapi.com/v1/images/search'


@app.route('/')
def home_route():
    """Show form."""

    return render_template('home.html')


@app.route('/new')
def get_data():
    breed = request.args["newish"]
    q = {'name': breed}
    res = requests.get(url, headers=headers, params=q)
    cat = res.json()
    q_img = {'limit': '4', "breed_id": cat[0]['id']}
    # print(cat[0]['id'])
    r_img = requests.get(url_img, headers=headers, params=q_img)
    img = r_img.json()
    

    # Early stage testing nothing here is currently permanent
    
    # make table that 
    print(img[0]['url'])
    print(img[1]['url'])
    print(img[2]['url'])
    print(img[3]['url'])
    # make data bases with data about breed, origin, lifespan, description
    print (cat[0]['name'])
    print(cat[0]['origin'])
    print(cat[0]['life_span'], 'years')
    print(cat[0]['description'])
    return jsonify(cat)

    # see if you can take specific data from the Json and store it in the database as new data 