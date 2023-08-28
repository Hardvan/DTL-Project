from flask import Flask, render_template, request, redirect, url_for
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from gtts import gTTS
import io
import base64

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

    # category = upcoming/ongoing/completed

    posts_dict = PostHandler.getPostsData(collection, REAL_DATA)
    return render_template('all_in_one.html', posts_dict=posts_dict, category=category)


@app.route('/eventDetail')
def eventDetail():

    # Get the event details from the URL

    title = request.args.get('title')
    date = request.args.get('date')
    des = request.args.get('des')
    image = request.args.get('image')
    host = request.args.get('host')

    return render_template('eventDetails.html', title=title, date=date, des=des, image=image, host=host)


# Chatbot functions
def getSpeech(result_text):

    language = 'en'
    speech = gTTS(text=result_text, lang=language, slow=False)

    # On local machine
    # speech.save("speech.mp3")
    # os.system("start speech.mp3")

    # Save the speech to memory as bytes
    speech_file = io.BytesIO()
    speech.write_to_fp(speech_file)
    speech_bytes = speech_file.getvalue()
    speech_base64 = base64.b64encode(speech_bytes).decode('utf-8')

    return speech_base64


def getChatbotResponse(user_input):

    # Default values
    response_text = "Sorry, I don't understand. Please try again."
    redirect_link = None

    if user_input == "See upcoming events":
        response_text = "You chose option 1: See upcoming events."
        redirect_link = url_for('all_in_one', category='upcoming')
        redirect_text = "View upcoming events"
    elif user_input == "See completed events":
        response_text = "You chose option 2: See completed events."
        redirect_link = url_for('all_in_one', category='completed')
        redirect_text = "View completed events"
    elif user_input == "Visit the events page":
        response_text = "You chose option 3: Visit the events page."
        redirect_link = url_for('events')
        redirect_text = "Visit the events page"

    audio_text = f"{response_text} Click the link below to proceed to your chosen option."

    response_audio = getSpeech(audio_text)

    return response_text, redirect_link, redirect_text, response_audio


@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():

    # Question : Options dictionary
    questionnaire = {"What would you like to do?": ["See upcoming events",
                                                    "See completed events",
                                                    "Visit the events page"]}

    hello = "Hello, I am the DTL Chatbot of RVCE. How can I help you today?"
    speech_base64 = getSpeech(hello)

    if request.method == 'POST':
        user_input = request.form['user_input']
        response_text, redirect_link, redirect_text, response_audio = getChatbotResponse(
            user_input)

        return render_template('chatbot.html', questionnaire=questionnaire,
                               user_input=user_input, response_text=response_text,
                               redirect_link=redirect_link, redirect_text=redirect_text,
                               response_audio=response_audio)

    return render_template('chatbot.html', questionnaire=questionnaire, speech_base64=speech_base64)


if __name__ == '__main__':
    app.run(debug=True)
