from flask import render_template, request
from app import app

import string

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/resume/')
def resume():
	return render_template('resume.html')

@app.route('/contact/')
def contact():
	return render_template('contact.html')
