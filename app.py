import os

from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Name %r>' % self.name



class task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(80))
    task = db.Column(db.String(120), unique=True)

    def __init__(self, task):
        self.task = task
        self.date = str(time.time())

    def __repr__(self):
        return '<Name %r>' % self.name





@app.route('/in')
def hello_world():
    return render_template('in.html')

@app.route('/all')
def all():
    return render_template('all.html')

@app.route('/project')
def project():
    return render_template('project.html')









@app.route('/robots.txt')
def robots():
    res = app.make_response('User-agent: *\nAllow: /')
    res.mimetype = 'text/plain'
    return res

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
