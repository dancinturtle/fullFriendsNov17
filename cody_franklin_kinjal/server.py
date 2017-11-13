from flask import Flask, render_template, redirect, url_for, flash, request
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "RUBYISBETTER<3"

mysql = MySQLConnector(app, 'full_friends')

@app.route('/')
def index():
  friends = mysql.query_db('SELECT * FROM friends')
  return render_template('index.html', friends = friends)

@app.route('/add', methods = ['POST'])
def add():
  full_name = request.form['full_name']
  age = request.form['age']
  errors = []

  if len(full_name) < 1:
    errors.append('Name cannot be blank.')
  
  if len(age) < 1:
    errors.append('Age cannot be blank.')

  query = 'INSERT INTO friends (full_name, age, created_at, updated_at) VALUES (:full_name, :age, NOW(), NOW());'
  data = {
    'full_name': full_name,
    'age': age
  }

  # If there are any errors in the list, then redirect back to the index and display flash messages.
  # If there are no errors then redirect to the welcome/success page.
  if len(errors) > 0:
    # Sort errors alphabeticaly.
    errors.sort()
    # Create a new flash message for each error in the list.
    # In the view we loop through all flash messages to display.
    
    for message in errors:
      flash(message, 'error')
    return redirect(url_for('index'))
  else:
    mysql.query_db(query, data)
    flash("Success! Friend added!", 'success')
    return redirect(url_for('index'))



app.run(debug=True)
