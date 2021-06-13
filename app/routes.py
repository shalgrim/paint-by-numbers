from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    grid = [
        [None, 'filled'],
        ['empty', None],
        ['filled', 'filled'],
        ['empty', 'empty'],
        [None, None],
    ]
    return render_template('index.html', grid=grid)
