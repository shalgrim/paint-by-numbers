from app import app
from app.forms import DataForm
from flask import render_template, redirect, url_for, session


def make_empty_grid(rules):
    width = len(rules['columns'])
    height = len(rules['rows'])
    grid = []

    for _ in range(height):
        grid.append([None] * width)

    return grid


def get_rules(data):

    lines = data.splitlines()
    rules = {'rows': [], 'columns': []}

    for i, line in enumerate(lines):
        if line.startswith('='):
            index = i+1
            break
        rules['rows'].append([int(s) for s in line.split()])

    for line in lines[index:]:
        rules['columns'].append([int(s) for s in line.split()])

    return rules


def make_sample_grid(rules):
    grid = [
        [None, 'filled'],
        ['empty', None],
        ['filled', 'filled'],
        ['empty', 'empty'],
        [None, None],
        ['empty', 'filled']
    ]
    return grid


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = DataForm()
    if form.validate_on_submit():
        session['rules'] = get_rules(form.data.data)
        return redirect(url_for('grid'))
    return render_template('index.html', form=form)


@app.route('/grid')
def grid():
    starting_grid = make_empty_grid(session['rules'])
    return render_template('grid.html', grid=starting_grid)
