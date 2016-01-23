#!/usr/bin/env python

from flask import Flask, request, session, url_for, redirect, abort, render_template, jsonify, Response
import random

app = Flask(__name__)
app.secret_key = "f3oiewfophewrihu9ipfoinjfdewmkdcfewrhjgf79834hyf98ewnjmcw"

@app.route('/')
def index():
    formAB = 'A'
    if 'formAB' in session:
        formAB = session['formAB']
    else:
        # randomise the session and present form A or B
        formAB = random.choice(('A', 'B'))
        session['formAB'] = formAB
    
    if formAB == 'A':
        out_template = 'calcA.html'
    elif formAB == 'B':
        out_template = 'calcB.html'
    return render_template(out_template)            

@app.route('/donate', methods=['GET', 'POST'])
@app.route('/donate/<int:amount>')
def donate(amount=0):
    session['p_amount'] = amount
    return render_template('donate.html')

@app.route('/api/details', methods=['POST'])
def donate_details():
    res = {}
    return jsonify(**res)

@app.route('/api/payment', methods=['POST'])
def donate_payment():
    res = {}
    return jsonify(**res)

@app.route('/api/confirm', methods=['POST'])
def donate_confirm():
    res = {}
    return jsonify(**res)

@app.route('/api/finish', methods=['POST'])
def donate_finish():
    res = {}
    session.clear()
    return jsonify(**res)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

