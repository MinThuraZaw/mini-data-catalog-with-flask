from flask import Flask, render_template, redirect, request, url_for, jsonify
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


@app.route('/delete_table', methods=['POST'])
def delete_table():
    data = request.get_json()
    table_name = data['table_name']
    tables = read_tables()
    tables = [table for table in tables if table['table_name'] != table_name]
    write_tables(tables)
    return jsonify({"message": "Table deleted successfully"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
