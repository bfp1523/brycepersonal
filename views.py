from flask import render_template, request
from app import app

import string

@app.route('/')
def home():
	return render_template('home.html')