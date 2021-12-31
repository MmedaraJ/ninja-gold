from flask import Flask, redirect, request, session, render_template
from collections import OrderedDict
import random

app = Flask(__name__)
app.secret_key = 'SecretKyy'

@app.route('/')
def display():
    #session.clear()
    if 'score' not in session:
        session['score'] = 0
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    gold_earned = 0
    colour = ''

    if 'index' not in session:
        session['index'] = -1

    if request.form['building'] == 'casino':
        gold_earned = random.randint(0, 50)
        if random.choice([True, False]) == False:
            gold_earned *= -1
            session["index"] += 1
            message = f'Entered a {request.form["building"]} and lost {gold_earned*-1} golds... Ouch...-{session["index"]}'
            colour = 'red'
        else: 
            session["index"] += 1
            message = f'Earned {gold_earned} golds from the {request.form["building"]}-{session["index"]}'
            colour = 'green'
        #session['colour'] = 'red'
    else:   
        if request.form['building'] == 'farm':
            gold_earned = random.randint(10, 20)
        elif request.form['building'] == 'cave':
            gold_earned = random.randint(5, 10)
        elif request.form['building'] == 'house':
            gold_earned = random.randint(2, 5)
        session["index"] += 1
        message = f'Earned {gold_earned} golds from the {request.form["building"]}-{session["index"]}'
        colour = 'green'
        #session['colour'] = 'green'

    if 'message' not in session: 
        session['message'] = OrderedDict()

    session['score'] += gold_earned
    message_dict = session['message']
    message_dict[message] = colour
    session['message'] = message_dict
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)