# pylint: disable=all
from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import json

load_dotenv()
mongo_connection_string = os.getenv("MONGO_CONNECTION_STRING")
print(f"MongoDB Connection String: {mongo_connection_string}")

app = Flask(__name__)
client = MongoClient(mongo_connection_string)

db = client["test"]



def calculate_gpa_and_cgpa(data):
    total_weighted_grades = 0
    total_credits = 0
    for semester in data['semesters']:
        weighted_grades = sum(course['credits'] * course['grade'] for course in semester['courses'])
        credits = sum(course['credits'] for course in semester['courses'])
        semester['gpa'] = round(weighted_grades / credits, 2) if credits != 0 else 0
        total_weighted_grades += weighted_grades
        total_credits += credits
    data['student']['cgpa'] = round(total_weighted_grades / total_credits, 2) if total_credits != 0 else 0
    return data


@app.route('/')
def home():
    data = db.test.find_one()  # Fetch the first document from your collection
    data = calculate_gpa_and_cgpa(data)
    return render_template('index.html', data=data)


# @app.route('/')
# def home():
#     with open('data.json') as json_file:
#         data = json.load(json_file)
#     data = calculate_gpa_and_cgpa(data)
#     return render_template('index.html', data=data)



if __name__ == '__main__':
    app.run(debug=True)
