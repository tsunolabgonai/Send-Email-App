from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emails.db'  # SQLiteデータベースのURI
db = SQLAlchemy(app)

class Email(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   address = db.Column(db.String(100), unique=True, nullable=False)

class Group(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), unique=True, nullable=False)

class EmailGroup(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   address_id = db.Column(db.Integer, nullable=False)
   gorup_id = db.Column(db.Integer, nullable=False)

@app.route('/', methods=['GET'])
def index():
   emails = Email.query.all()
   groups = Group.query.all()
   return render_template('index.html', emails=emails, groups=groups)

@app.route('/email', methods=['POST'])
def email():
   if request.method == 'POST':
      email_address = request.form['email']
      if email_address:
         new_email = Email(address=email_address)
         db.session.add(new_email)
         db.session.commit()
   emails = Email.query.all()
   groups = Group.query.all()
   return render_template('index.html', emails=emails, groups=groups)

@app.route('/group', methods=['POST'])
def group_add():
   if request.method == 'POST':
      group = request.form['group']
      if group:
         new_group = Group(name=group)
         db.session.add(new_group)
         db.session.commit()
   emails = Email.query.all()
   groups = Group.query.all()
   return render_template('index.html', emails=emails, groups=groups)

@app.route('/input_email_group', methods=['POST'])
def put_email_in_group ():
   
   

@app.route('/delete', methods=['GET', 'POST'])
def delete():
   if request.method == 'POST':
      selected_email = request.form.get('selected_email')
      if selected_email:
         email_to_delete = Email.query.filter_by(address=selected_email).first()
         if email_to_delete:
            db.session.delete(email_to_delete)
            db.session.commit()
   allEmail = Email.query.all()
   return render_template('delete.html', allEmail=allEmail)

if __name__ == '__main__':
   with app.app_context():
       db.create_all()
   app.run(debug=True)
