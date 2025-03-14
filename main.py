from flask import Flask, render_template, redirect, url_for
from cloudant.client import Cloudant
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField 
from wtforms.validators import DataRequired 
from forms import NameForm, getInfoTask
from datetime import datetime, timezone 
from task import Task 


#Cloudant credentials here 
# {
#   "apikey": "U6gkibgbshNn9notLjhUIoiULuASTckde0zI-onXSgX3",
#   "host": "d41c36bb-eaf3-4e85-a710-f4b654204838-bluemix.cloudantnosqldb.appdomain.cloud",
#   "iam_apikey_description": "Auto-generated for key crn:v1:bluemix:public:cloudantnosqldb:au-syd:a/cc16129c32434032a8f22d47936b97b6:ed2a5264-5eba-4f44-bbf4-e71f458773d5:resource-key:ddb37acd-39c2-4cc2-8822-ea8aa611b8aa",
#   "iam_apikey_id": "ApiKey-67cd5852-17f7-4338-93a1-086fbc0e2e86",
#   "iam_apikey_name": "to-do-List",
#   "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Manager",
#   "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/cc16129c32434032a8f22d47936b97b6::serviceid:ServiceId-07a46af0-6106-4c8e-bc54-2464913fe9b7",
#   "url": "https://d41c36bb-eaf3-4e85-a710-f4b654204838-bluemix.cloudantnosqldb.appdomain.cloud",
#   "username": "d41c36bb-eaf3-4e85-a710-f4b654204838-bluemix"
# }

#for now we comment out the call to the data base 
cloudant_url="https://d41c36bb-eaf3-4e85-a710-f4b654204838-bluemix.cloudantnosqldb.appdomain.cloud"
cloudant_username="d41c36bb-eaf3-4e85-a710-f4b654204838-bluemix"
cloudant_apikey="U6gkibgbshNn9notLjhUIoiULuASTckde0zI-onXSgX3"

#establishing a conneciton 
client = Cloudant.iam(cloudant_username, cloudant_apikey, connect = True)
database = client["todo_list"]

#flask instance 

app = Flask(__name__)
#crf 
app.config['SECRET_KEY']="secretKey:v"

#print for debuging purposes 
def printData(title, description):
    print(f"The user title: ", {title})
    print(f"The description is ",{description})

#Making todo the main page 
@app.route("/")
def index():
    return redirect(url_for("todo"))

#Page display all the list of things to do 
@app.route("/todo")
def todo():
    tasks = [task for task in database]

    return render_template("display.html", tasks = tasks)

#This changes takes the id as input so it can change its status to done or completed
@app.route('/mark_done/<task_id>')
def mark_done(task_id):
    task = database[task_id]
    if task.exists():
        task["done"] = True
        task.save()
    return redirect(url_for("todo"))

#this one deletes a task from the databases 
@app.route("/delete_task/<task_id>")
def delete_task(task_id):
    task = database[task_id]  
    if task:
        task.delete()  
    return redirect(url_for("todo"))

#Creates a new databases using the form 
@app.route('/newTask', methods=['GET', 'POST'])
def newTask():
    form = getInfoTask()

    if form.validate_on_submit():
        #it measn we get somethign from the input user
        title = form.title.data
        description = form.description.data

        task = Task(task_title = title, description=description)
        taskData = task.to_dict()
        database.create_document(taskData)

        printData(title, description)
        print("Data succesfuly added to database ")
        return redirect(url_for('todo'))
    return render_template("newTask.html", form = form)

#this was an example from youtube video to refresh memroy 
@app.route('/name', methods=['GET', 'POST'])
def name():
    #none first because it will no name after 
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        #here we pass the data provided and then we empty the values. 
        form.name.data = ''
    return render_template("name.html", 
                           name = name,
                           form = form )


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500



