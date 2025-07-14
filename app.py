
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)
queue = []
doctor_notes = []

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/phase1')
def phase1():
    return render_template('phase1.html')

@app.route('/ap_screen')
def ap_screen():
    return render_template('ap_screen.html')  # Make sure this HTML file exists in the templates folder

if __name__ == '__main__':
    app.run(debug=True)