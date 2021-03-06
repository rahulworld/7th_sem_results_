import os
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory
import simplejson as json
import codecs


input_file_name = 'results.json'
openFile =  codecs.open(input_file_name, 'r',"utf-8" )
inputFile = json.load(openFile)
subject_wise_results = inputFile['subject_wise_results']
student_wise_results = inputFile['student_wise_results']

ITStudentsFile =  codecs.open('students.json', 'r',"utf-8" )
ITStudentsFileinput = json.load(ITStudentsFile)
IT_subjects = ITStudentsFileinput['subjects']
IT_credits = {}
for x in IT_subjects:
    IT_credits[ x['subject'] ] = x['credit']


CS_input_file_name = 'CS_students_result.json'
CS_openFile =  codecs.open(CS_input_file_name, 'r',"utf-8" )
CS_inputFile = json.load(CS_openFile)
CS_subject_wise_results = CS_inputFile['subject_wise_results']
CS_student_wise_results = CS_inputFile['student_wise_results']



app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    # print student_wise_results
    # subjects = [ x['sub'].replace('_'," ") for x in student_wise_results[0]['grades'] ]
    # print subjects
    return render_template('temp.html',credits=IT_credits,student_wise_results=student_wise_results)


@app.route('/IT')
def studentwiseresults_IT():
    # print student_wise_results
    # subjects = [ x['sub'].replace('_'," ") for x in student_wise_results[0]['grades'] ]
    # print subjects
    # print student_wise_results[0]
    namesList = [x['name'] for x in student_wise_results]
    rollList =  [x['rollno'] for x in student_wise_results]
    return render_template('res1.html',credits=IT_credits,student_wise_results=student_wise_results,namesList=namesList,rollList=rollList)

@app.route('/CS')
def studentwiseresults_CS():
    # print student_wise_results
    subjects = [ x['sub'].replace('_'," ") for x in CS_student_wise_results[0]['grades'] ]
    # print subjects
    # print student_wise_results[0]
    namesList = [x['name'] for x in CS_student_wise_results]
    rollList =  [x['rollno'] for x in CS_student_wise_results]
    return render_template('res1.html',subjects=subjects,student_wise_results=CS_student_wise_results,namesList=namesList,rollList=rollList)




# @app.route('/<path:resource>')
# def serveStaticResource(resource):
#     return send_from_directory('static/', resource)

# @app.route("/IT")
# def test():
#     return "<strong>It's Alive!</strong>"

if __name__ == '__main__':
    app.run(debug=True)
