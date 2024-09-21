from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Route for the main to-do list page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the login page
@app.route('/login')
def login():
    return render_template('login.html')

# Route for creating a new list
@app.route('/new-list')
def new_list():
    # Logic for creating a new list goes here
    return render_template('index.html')  # Redirect to a new list view (index for now)

# Route for saving the list
@app.route('/save-list', methods=['POST'])
def save_list():
    # Logic for saving the list goes here
    return redirect(url_for('index'))

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
