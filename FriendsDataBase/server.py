from flask import Flask, request, redirect, render_template, flash
from mysqlconnect import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
	query = "SELECT * FROM friends"
	friends = mysql.query_db("SELECT * FROM friends")
	return render_template('index.html', all_friends = friends)

@app.route('/friends', methods=['POST'])
def add():
	query = "INSERT INTO friends(first_name,age,created_at) VALUES(:first_name,:age,NOW())"

	data = {
			'first_name': request.form['first_name'],
			'age': request.form['age']
			
	}

	mysql.query_db(query,data)
	return redirect('/')

app.run(debug=True)