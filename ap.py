from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    data = db.Column(db.Text, nullable=False)

@app.route('/')
def index():
    reports = Report.query.all()
    return render_template('index.html', reports=reports)

@app.route('/add_report', methods=['POST'])
def add_report():
    name = request.form['name']
    data = request.form['data']
    
    new_report = Report(name=name, data=data)
    db.session.add(new_report)
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
