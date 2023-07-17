from flask import Flask, render_template, request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
from datetime import datetime, date

import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

# Testing Parameters
TEST_CONNECTION = False     # ? Set to True to test connection to MongoDB
REAL_DATA = True            # ? Set to False to use sample data


# MongoDB connection
mongodb_uri = os.getenv("MONGODB_URI")
client = MongoClient(mongodb_uri, server_api=ServerApi('1'))

# Select the database and collection
db = client['DTL_db']
collection = db['posts']

# Send a ping to confirm a successful connection
if TEST_CONNECTION:
    try:
        client.admin.command('ping')
        print("✅ Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    # Add a sample document in the collection (don't add if already exists)
    name = 'John Doe'
    if collection.count_documents({'name': name}) == 0:
        collection.insert_one({'name': name})
        print("✅ Added a sample document in the collection.")

    # Retrieve the sample document added
    result = collection.find_one({'name': name})
    print(result)
    print("✅ Retrieved the sample document.")

    # Delete the sample document added
    collection.delete_one({'name': name})
    print("✅ Deleted the sample document.")


def formatData(posts_dict):

    today = date.today()

    for post in posts_dict:
        # Convert date from string to datetime object
        post['date'] = datetime.strptime(post['date'], '%Y-%m-%d')

        # Convert date to string in the format DD MMM YYYY
        post['date_str'] = post['date'].strftime('%d %b %Y')

        # Categorize the post
        if post['date'].date() > today:
            post['category'] = 'Upcoming'
        elif post['date'].date() == today:
            post['category'] = 'Today'
        else:
            post['category'] = 'Completed'

    # Sort posts by date (Newest first)
    posts_dict = sorted(posts_dict, key=lambda k: k['date'])

    return posts_dict


def getPostsData():

    posts_dict = []

    # Get data from MongoDB afterwards
    if REAL_DATA:
        posts_dict = list(collection.find({}))

    # Sample data
    else:
        with open('./static/json/sample_posts.json', 'r') as file:
            data = json.load(file)
            posts_dict = data['posts']

    posts_dict = formatData(posts_dict)

    return posts_dict


@app.route('/')
def index():

    posts_dict = getPostsData()

    return render_template('events.html', posts_dict=posts_dict)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/events')
def events():
    return render_template('events.html')


@app.route('/events/upcoming')
def upcoming():
    posts_dict = getPostsData()
    return render_template('upcoming.html', posts_dict=posts_dict)


@app.route('/events/ongoing')
def ongoing():
    posts_dict = getPostsData()
    return render_template('ongoing.html', posts_dict=posts_dict)


@app.route('/events/completed')
def completed():
    posts_dict = getPostsData()
    return render_template('completed.html', posts_dict=posts_dict)


@app.route('/eventDetail')
def eventDetail():
    title = request.args.get('title')
    date = request.args.get('date')
    des = request.args.get('des')
    image = request.args.get('image')
    host = request.args.get('host')
    return render_template('eventDetails.html', title=title, date=date, des=des, image=image, host=host)


if __name__ == '__main__':
    app.run(debug=True)
