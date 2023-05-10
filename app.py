from flask import Flask, render_template
import json

app = Flask(__name__)

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
    with open('data.json') as json_file:
        data = json.load(json_file)
    data = calculate_gpa_and_cgpa(data)
    return render_template('index.html', data=data)



if __name__ == '__main__':
    app.run(debug=True)
