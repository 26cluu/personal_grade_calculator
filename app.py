from flask import Flask, render_template, request, redirect, url_for
import calc
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()

app = Flask(__name__)

cluster = MongoClient(os.getenv('cluster_key'))

db = cluster['grade_calc']
collection = db['grades']

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        assignment_type = request.form['assignment_type']
        correct = request.form['correct']
        total = request.form['total']
        subject = request.form['subject']
        return redirect(url_for('grade_calc', assignment_type=assignment_type, correct=correct, total=total, subject=subject))
    else:
        return render_template('index.html')

@app.route('/calc', methods=['GET'])
def grade_calc():
    assignment_type = request.args.get('assignment_type')
    correct = int(request.args.get('correct'))
    total = int(request.args.get('total'))
    subject = request.args.get('subject')

    
    if subject == 'Spanish':
        percentage = calc.span_calc(assignment_type, correct, total)
    elif subject == 'Physics':
        percentage = calc.physics_calc(assignment_type, correct, total)
    elif subject == 'Math':
        percentage = calc.math_calc(assignment_type, correct, total)
    elif subject == 'Scripture':
        percentage = calc.scripture_calc(assignment_type, correct, total)
    elif subject == 'History':
        percentage = calc.history_calc(assignment_type, correct, total)
    elif subject == 'English':
        percentage = calc.english_calc(assignment_type, correct, total)

    return render_template('calc.html', percentage=percentage)

@app.route('/add', methods = ['GET', 'POST'])
def add_assignment():
    if request.method == 'POST':
        assignment_type = request.form['assignment_type']
        correct = float(request.form['correct'])
        total = float(request.form['total'])
        subject = request.form['subject']
        name = request.form['name']
        post = {'assignment_type': assignment_type, 'correct': correct, 'total': total, 'subject': subject, 'name': name}
        collection.insert_one(post)
        return redirect(url_for('main'))
    else:
        return render_template('add_assignment.html')




if __name__=='__main__':
   configure()
   app.run()


##### ideas
#auto calc grade percentage to get overall grade to goal percentage
#regular grade calc has add assignment button with modal to get name for it
#come up with solution for the extra grading types for spanish class
#floats don't work
#physics done


