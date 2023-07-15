from flask import Flask, render_template, request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
from datetime import datetime

import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)


# MongoDB connection
mongodb_uri = os.getenv("MONGODB_URI")
client = MongoClient(mongodb_uri, server_api=ServerApi('1'))

# Select the database and collection
db = client['DTL_db']
collection = db['posts']

# Send a ping to confirm a successful connection
test = True  # ! Set to False to skip test
if test:
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

    for post in posts_dict:
        # Convert date from string to datetime object
        post['date'] = datetime.strptime(post['date'], '%Y-%m-%d')

        # Convert date to string in the format DD MMM YYYY
        post['date_str'] = post['date'].strftime('%d %b %Y')

    return posts_dict


@app.route('/')
def index():

    with open('./static/json/sample_posts.json', 'r') as file:
        data = json.load(file)
        posts_dict = data['posts']

    posts_dict = formatData(posts_dict)

    return render_template('index.html', posts_dict=posts_dict)


if __name__ == '__main__':
    app.run(debug=True)
