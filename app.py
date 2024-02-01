from flask import Flask, request, abort, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = db.session.execute(f"SELECT * FROM user WHERE username='{username}' AND password='{password}'").fetchone()
        if user is None:
            abort(401, description="Invalid username or password")
        return redirect(url_for('admin'))
    return render_template('login.html')


@app.route('/admin312312321321133113')

def admin():

    return render_template('admin.html')




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False)    