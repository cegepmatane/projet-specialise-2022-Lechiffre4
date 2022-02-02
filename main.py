from graphviz import render
import function


from flask import Flask, render_template, jsonify
import numpy as np



application = Flask(__name__)

Films_titles = function.listfilmIMBD("indianajones")

@application.route('/filmlist', methods = ['POST'])
def updatedecimal():
    Films_titles = function.listfilmIMBD()
    return jsonify('',render_template('Listfilms_model.html', x=Films_titles[0]))

@application.route('/')
def homepage():
    return render_template('home.html')

application.run()
