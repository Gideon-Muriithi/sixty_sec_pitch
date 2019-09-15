from flask import render_template
from app import app

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The best Sixty Seconds Pitch Access Website Online'
    
    return render_template('index.html', title = title)