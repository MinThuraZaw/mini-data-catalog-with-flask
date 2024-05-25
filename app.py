from flask import Flask, render_template, redirect, request, url_for
import os
import json

app = Flask(__name__)

DATA_FILE = 'data/tables.json'


def read_tables():
    with open(DATA_FILE, 'r') as f:
        tables = json.load(f)
    return tables


def write_tables(tables):
    with open(DATA_FILE, 'w') as f:
        json.dump(tables, f, indent=4)


@app.route('/')
def home():
    tables = read_tables()
    return render_template('home.html', tables=tables)


@app.route('/add_table', methods=['POST'])
def add_table():
    new_table = {
        "table_name": request.form['table_name'],
        "database_name": request.form['database_name'],
        "description": request.form['description']
    }
    tables = read_tables()
    tables.append(new_table)
    write_tables(tables)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
