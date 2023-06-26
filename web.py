import flask
from flask import request, jsonify
import new_studentgenerator


#create an app
app = flask.Flask(__name__)

#use student generator program as a base
#write a function to create and return a list of student dictionaries
#create 2 routes
# -- return all students
# -- returns student by id


#auto reload server when changes made
app.config["DEBUG"] = True

#load student dictionaries
student_dictionaries = new_studentgenerator.get_student_dictionaries()

@app.route('/', methods = ['GET'])
def index():
    return "<h1> My name is Jemuel Lee</h1>"

#create route to return all student data
@app.route('/api/students/all', methods = ['GET'])
def api_all():
    return jsonify(student_dictionaries)

app.run()
