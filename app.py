#source rest/bin/activate
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

DocPracs = db.Table('DocPracs',
    db.Column('D_id', db.Integer, db.ForeignKey('doctor.D_id')),
    db.Column('P_id', db.Integer, db.ForeignKey('practice.P_id'))

)

class Doctor(db.Model):
    D_id = db.Column(db.Integer, primary_key=True)
    D_name = db.Column(db.String(200), nullable=False)
    experience = db.Column(db.Integer)
    practices = db.relationship('Practice', secondary = 'DocPracs', backref='doctor', lazy='dynamic')

    def __repr__(self):
        return '<Doctor %r>' % self.D_name


class Practice(db.Model):
    P_id = db.Column(db.Integer, primary_key=True)
    P_name = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200))


@app.route('/', methods=['POST', 'GET'])
def index():
    db.create_all()
    return "hello world2"
'''
@app.route('/Doctors', methods=['POST', 'GET'])
def index1():
    all_doctors = Doctor.query.all();
    return jsonify(all_doctors)
'''
@app.route('/Doctors', methods=['POST', 'GET'])
def viewDocs():
    if request.method == 'POST':
        f= int(request.form['f'])
        t= int(request.form['t'])
        docs = Doctor.query.all()[f:t]
        return render_template('ViewDocs.html', docs=docs, disp = 1)
    else:
        return render_template('ViewDocs.html', disp = 0)

@app.route('/Practices', methods=['POST', 'GET'])
def viewPracs():
    if request.method == 'POST':
        f= int(request.form['f'])
        t= int(request.form['t'])
        pracs = Practice.query.all()[f:t]
        return render_template('ViewPracs.html', pracs=pracs, disp = 1)
    else:
        return render_template('ViewPracs.html', disp = 0)


'''
@app.route('/')
def index():
    db.create_all()
    if True:
        #task_content = request.form['content']
         = Doctor1(D_name="Dilip")

        try:
            db.session.add(new_task)
            db.session.commit()
            return "Success" #redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        pass
        """tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)"""
'''

if __name__ == "__main__":
    app.run(debug=True)