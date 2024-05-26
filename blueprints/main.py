from flask import Blueprint, render_template, request, redirect, url_for, jsonify, json

main_bp = Blueprint('main', __name__)

DATA_FILE = 'data/tables.json'


def read_tables():
    with open(DATA_FILE, 'r') as f:
        tables = json.load(f)
    return tables


def write_tables(tables):
    with open(DATA_FILE, 'w') as f:
        json.dump(tables, f, indent=4)


@main_bp.route('/')
def home():
    tables = read_tables()
    return render_template('home.html', tables=tables)


@main_bp.route('/add_table', methods=['POST'])
def add_table():
    new_table = {
        "table_name": request.form['table_name'],
        "database_name": request.form['database_name'],
        "description": request.form['description']
    }
    tables = read_tables()
    tables.append(new_table)
    write_tables(tables)
    return redirect(url_for('main.home'))


@main_bp.route('/delete_table', methods=['POST'])
def delete_table():
    data = request.get_json()
    table_name = data['table_name']
    tables = read_tables()
    tables = [table for table in tables if table['table_name'] != table_name]
    write_tables(tables)
    return jsonify({"message": "Table deleted successfully"}), 200
