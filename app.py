from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime, timedelta
from werkzeug.security import check_password_hash
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

queue = []
doctor_notes = []

SESSION_TIMEOUT = 300  # 5 minutes in seconds

# -------- ADMIN LOGIN CREDENTIALS (ENCRYPTED PASSWORD) --------
ADMIN_USERNAME = 'primahealth'
# Hash for password: "primahealth25"
ADMIN_PASSWORD_HASH = 'scrypt:32768:8:1$PgHBXxvv2705ES59$b852a704ca8a770eb59e5e79b262c338aaa443687f464e583bedbebc3a8bdac6d8558875870711cc5a52700bf32790e22993e0ed9445b8bc1aaa858d5ed3241b'

# -------- GLOBAL LOGIN + TIMEOUT CHECK --------
@app.before_request
def require_login_and_timeout():
    allowed_routes = ['admin_login', 'admin_auth', 'do_logout', 'static']
    if request.endpoint not in allowed_routes:
        if 'admin_user' not in session:
            return redirect(url_for('admin_login'))

        last_active = session.get('last_active')
        if last_active:
            last_active_time = datetime.strptime(last_active, '%Y-%m-%d %H:%M:%S')
            if datetime.utcnow() - last_active_time > timedelta(seconds=SESSION_TIMEOUT):
                session.clear()
                return redirect(url_for('admin_login'))

        session['last_active'] = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

# ------------------- MAIN ROUTES -------------------
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/phase1')
def phase1():
    return render_template('phase1.html')

@app.route('/phase1/phase1_overview')
def phase1_overview():
    return render_template('phase1_overview.html')

@app.route('/phase2')
def phase2():
    return render_template('phase2.html')

@app.route('/consent')
def consent():
    return render_template('consent.html')

@app.route('/phase1/login_ap')
def login_ap():
    return render_template('login_ap.html')

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

@app.route('/phase2/receipt')
def receipt():
    return render_template('receipt.html')

@app.route('/phase2/stage4/under12')
def under12():
    return render_template('under12.html')

@app.route('/phase2/stage4/over12')
def over12():
    return render_template('over12.html')

# ------------------- LOGIN SYSTEM -------------------
@app.route('/admin_login')
def admin_login():
    return render_template('admin_login.html')

@app.route('/admin_auth', methods=['POST'])
def admin_auth():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == ADMIN_USERNAME and check_password_hash(ADMIN_PASSWORD_HASH, password):
        session['admin_user'] = username
        session['last_active'] = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        return redirect(url_for('index'))
    return render_template('admin_login.html', error='Invalid credentials')

@app.route('/do_logout')
def do_logout():
    session.clear()
    return redirect(url_for('admin_login'))

# -----------------------------------------------------

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5050))  # Render will inject PORT
    app.run(host='0.0.0.0', port=port)