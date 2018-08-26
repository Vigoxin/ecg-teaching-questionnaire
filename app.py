# Imports
import os
# import shelve
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# set up basedir
basedir = os.path.abspath(os.path.dirname(__file__))

# set up flask app
app = Flask(__name__)

# configure sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'data.sqlite'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.create_all()

# Data
from confucius_quotes import quotes
pd = {
	'quotes': quotes
}

questions = [
	{'subject': 'Presentation', 'description': 'Being able to present ECGs in a slick manner (both for exams, and for when a consultant/senior puts you on the spot)'},
	{'subject': 'Practice', 'description': 'Getting lots of practice at interpreting/presenting ECGs, getting better at pattern recognition'},
	{'subject': 'Management', 'description': '<em>Management</em> of different arrhythmias and ECG pathologies'},
	{'subject': 'Understanding', 'description': 'Getting a deeper understanding of what is happening in the heart during different arrhythmias'},
	{'subject': 'First principles', 'description': 'Understanding the basis of the ECG, why each wave/deflection looks the way it does, i.e. the basics of ECG from first principles'},
	{'subject': 'Other', 'description': ''}
]

# Models
class Response(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	presentation = db.Column(db.Integer)
	practice = db.Column(db.Integer)
	management = db.Column(db.Integer)
	understanding = db.Column(db.Integer)
	first_principles = db.Column(db.Integer)
	other = db.Column(db.Integer)
	other_text = db.Column(db.Text)
	comments = db.Column(db.Text)

	def __init__(self, presentation, practice, management, understanding, first_principles, other, other_text, comments):
		self.presentation = presentation
		self.practice = practice
		self.management = management
		self.understanding = understanding
		self.first_principles = first_principles
		self.other = other
		self.other_text = other_text
		self.comments = comments

	def __repr__(self):
		return 'This is response {}'.format(self.id)




# Routes
@app.route('/')
def index():
	return render_template('index.html', questions=questions, lenq=len(questions), pd=pd)

@app.route('/response', methods=['GET', 'POST'])
def response():
	args = dict(request.args)
	for key in args:
		args[key] = args[key][0]
	values = list(args.values())
	response_to_add = Response(*values)
	db.session.add(response_to_add)
	db.session.commit()
	# with shelve.open('shelf') as shelf:
	# 	data = shelf['data']
	# 	data.append(values)
	# 	shelf['data'] = data
	# with open('text_data.txt', 'a') as file:
	# 	to_add = values
	# 	to_add = ','.join([str(el) for el in to_add]) + '\n'
	# 	file.write(to_add)
	return render_template('thankyou.html', pd=pd, args=args)


# Main
if __name__ == '__main__':
	app.run(debug=True)