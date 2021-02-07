from flask import render_template
from app import app

user = {'username': 'Arun', 'lastname': 'Chithambaram'}


@app.route('/')
@app.route('/index')
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/polls')
def polls():
    polls = [
        {
            'question': 'What\'s the difference between "Climate" & "Weather"?',
            'options': ['Nothing', 'Everything', 'Something']
        },
        {
            'question': 'What\'s the difference between "Everything" & "Something"?',
            'options': ['What', 'is', 'this', '??']
        }
    ]
    return render_template('polls.html', title='Polls', user=user, polls=polls)
