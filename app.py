
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
@app.route('/phase2')
def phase2():
    return render_template('phase2.html')

@app.route('/consent')
def consent():
    return render_template('consent.html')
@app.route('/phase1/login')
def login():
    return render_template('login.html')

@app.route('/phase1/login_cc')
def login_cc():
    return render_template('login_cc.html')

@app.route('/phase1/ap_screen')
def ap_screen():
    return render_template('ap_screen.html')

@app.route('/phase1/cc_screen')
def cc_screen():
    return render_template('cc_screen.html')

@app.route('/phase1/cm_screen')
def cm_screen():
    return render_template('cm_screen.html')

@app.route('/phase2/stage1')
def stage1():
    return render_template('stage1.html')

@app.route('/phase2/stage2')
def stage2():
    return render_template('stage2.html')

@app.route('/phase2/stage3')
def stage3():
    return render_template('stage3.html')

@app.route('/phase2/stage4')
def stage4():
    return render_template('stage4.html')

@app.route('/phase2/stage4/under12')
def under12():
    return render_template('under12.html')

@app.route('/phase2/stage4/over12')
def over12():
    return render_template('over12.html')


if __name__ == '__main__':
    app.run(debug=True)