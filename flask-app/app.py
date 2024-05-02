# app.py

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In a real application, you would use a proper database for user management.
# Here, we use a simple dictionary to store user credentials.
users = {'admin': 'password', 'user2': 'password2'}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home', methods=['POST'])
def home():
    username = request.form['username']
    password = request.form['password']

    # Check if the username and password match
    if username in users and users[username] == password:
        return render_template('home.html', username=username)
    else:
        return "Invalid login. Please try again."

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
