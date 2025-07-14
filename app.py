
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)
queue = []
doctor_notes = []

@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)