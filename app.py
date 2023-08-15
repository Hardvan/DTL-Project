from flask import Flask, render_template, request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import os
from dotenv import load_dotenv

# Custom modules
import PostHandler

load_dotenv()


app = Flask(__name__)

# Testing Parameters
TEST_CONNECTION = False     # ? Set to True to test connection to MongoDB
REAL_DATA = False            # ? Set to False to use sample data


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


@app.route('/')
def index():

    posts_dict = PostHandler.getPostsData(collection, REAL_DATA)

    return render_template('dashboard.html', posts_dict=posts_dict)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/events')
def events():
    return render_template('events.html')


@app.route('/events/all_in_one/<category>')
def all_in_one(category):
    posts_dict = PostHandler.getPostsData(collection, REAL_DATA)
    return render_template('all_in_one.html', posts_dict=posts_dict, category=category)


@app.route('/eventDetail')
def eventDetail():
    title = request.args.get('title')
    date = request.args.get('date')
    des = request.args.get('des')
    image = request.args.get('image')
    host = request.args.get('host')
    return render_template('eventDetails.html', title=title, date=date, des=des, image=image, host=host)


# Chatbot functions
def getChatbotResponse(user_input):

    options = {
        "1": "You chose option 1: See upcoming events.",
        "2": "You chose option 2: See completed events.",
        # Add more options here
    }

    default_response = "You have chosen an invalid option. Please try again."

    response = options.get(user_input, default_response)
    return response


@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():

    if request.method == 'POST':
        user_input = request.form['user_input']
        bot_response = getChatbotResponse(user_input)

        return render_template('chatbot.html', user_input=user_input, bot_response=bot_response)

    return render_template('chatbot.html')


if __name__ == '__main__':
    app.run(debug=True)
