from flask import Flask, render_template, redirect, request, url_for
import os
import json

app = Flask(__name__)

DATA_FILE = 'data/tables.json'


def load_tables():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []


def save_tables(tables):
    with open(DATA_FILE, 'w') as file:
        json.dump(tables, file)


@app.route('/')
def home():
    tables = load_tables()
    return render_template('home.html', tables=tables)


@app.route('/add_table', methods=['POST'])
def add_table():
    new_table_name = request.form['table_name']
    tables = load_tables()
    if new_table_name and new_table_name not in tables:
        tables.append(new_table_name)
        save_tables(tables)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
