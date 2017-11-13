from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
#from dateutil.parser import parse as parse_date
import datetime
import re



NAME_Regex = re.compile(r'^[a-zA-Z ]+$')
AGE_Regex =re.compile(r'^(\d?[1-9]|[1-9]0)$')
now = datetime.datetime.now()

app = Flask(__name__)
app.secret_key = "passwordhere"
mysql = MySQLConnector(app,'friendsTwo')

@app.route('/')
def index():
    query = "SELECT * FROM friends" 
    friends = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html', all_friends=friends) # pass data to our template


@app.route('/friends', methods=['POST'])
def create():
	name = False
	age = False
	f_since = False
	if not NAME_Regex.match(request.form['name']):
		flash("Name has to contain only letters.")
	else:
		name = True

	if not AGE_Regex.match(request.form['age']):
		flash ("Age has to be numerical")
	else:
		age = True
	'''if request.form['friends_since'] > now:
		flash ("The date is in the future")
	else:
		f_since = True
	'''
	if name and age: #and f_since:
		query = "INSERT INTO friends (name, age, friends_since) VALUES (:name, :age, :friends_since)"
		data = {
			"name": request.form['name'],
			'age': request.form['age'],
			'friends_since': request.form['friends_since']
		}
		mysql.query_db(query,data)

	return redirect('/')


'''@app.route("/friends/<friend_id>")
def show(friend_id):
	query = "SELECT * FROM friends WHERE id= :specific_id"
	data = {"specific_id": friend_id}
	friends = mysql.query_db(query,data)
	return render_template("index.html", one_friend=friends[0])
'''

'''@app.route("/update/<friend_id>")
def updateForm(friend_id):
	query = "SELECT * FROM friends WHERE id= :specific_id"
	data = {"specific_id": friend_id}
	friend = mysql.query_db(query, data)
	fname = friend[0]['first_name']
	lname = friend[0]['last_name']
	occu = friend[0]['occupation']

	return render_template("update.html", firstName = fname, lastName = lname, occup = occu, ident = data['specific_id'])
'''

#@app.route("/update_friend/<friend_id>",methods=['POST'])
#def update(friend_id):
#	query = "UPDATE friends SET first_name = :first_name, last_name= :last_name, occupation = :occupation WHERE id = :id"
#	data = {
#		'first_name': request.form['first_name'],
#		'last_name': request.form['last_name'],
#		'occupation': request.form['occupation'],
#		'id': friend_id
#	}
#	mysql.query_db(query,data)
#	return redirect('/')


@app.route("/removefriend/<friend_id>", methods=['POST'])
def delete(friend_id):
	query = "DELETE from friends WHERE id= :id"
	data = {'id': friend_id}
	mysql.query_db(query,data)
	return redirect("/")

app.run(debug=True)
