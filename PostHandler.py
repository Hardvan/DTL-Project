import json
from datetime import datetime, date


def formatData(posts_dict):

    today = date.today()

    for post in posts_dict:
        # Convert date from string to datetime object
        post['date'] = datetime.strptime(post['date'], '%Y-%m-%d')

        # Convert date to string in the format DD MMM YYYY
        post['date_str'] = post['date'].strftime('%d %b %Y')

        # Categorize the post\
        if post['date'].date() > today:
            post['category'] = 'Upcoming'
        elif post['date'].date() == today:
            post['category'] = 'Ongoing'
        else:
            post['category'] = 'Completed'

    # Sort posts by date (Newest first)
    posts_dict = sorted(posts_dict, key=lambda k: k['date'])

    return posts_dict


def getPostsData(collection, REAL_DATA):

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


def getPostsDataClubs(collection, REAL_DATA):

    posts_dict = []

    # Get data from MongoDB afterwards
    if REAL_DATA:
        posts_dict = list(collection.find({}))

    # Sample data
    else:
        with open('./static/json/clubs.json', 'r') as file:
            data = json.load(file)
            posts_dict = data['posts']

    return posts_dict


def getLocationData(collection, REAL_DATA):

    location_dict = []

    # Get data from MongoDB afterwards
    if REAL_DATA:
        location_dict = list(collection.find({}))

    # Sample data
    else:
        with open('./static/json/locations.json') as file:
            location_dict = json.load(file)

    return location_dict
