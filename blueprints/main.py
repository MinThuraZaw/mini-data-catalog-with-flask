from flask import Blueprint, render_template, request, redirect, url_for, jsonify, json
from .db import get_db
from mysql.connector import Error

main_bp = Blueprint('main', __name__)

# DATA_FILE = 'data/tables.json'


# def read_tables():
#     with open(DATA_FILE, 'r') as f:
#         tables = json.load(f)
#     return tables
#
#
# def write_tables(tables):
#     with open(DATA_FILE, 'w') as f:
#         json.dump(tables, f, indent=4)


@main_bp.route('/')
def home():
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tables")
        tables = cursor.fetchall()
        return render_template('home.html', tables=tables)
    except Error as e:
        error_message = f"Error connecting to MySQL: {str(e)}"
        return render_template('home.html', error=error_message)


@main_bp.route('/add_table', methods=['POST'])
def add_table():
    # new_table = {
    #     "table_name": request.form['table_name'],
    #     "database_name": request.form['database_name'],
    #     "description": request.form['description']
    # }
    # tables = read_tables()
    # tables.append(new_table)
    # write_tables(tables)
    # return redirect(url_for('main.home'))

    table_name = request.form['table_name']
    database_name = request.form['database_name']
    description = request.form['description']
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO tables (table_name, database_name, description) VALUES (%s, %s, %s)",
                   (table_name, database_name, description))
    db.commit()
    return redirect(url_for('main.home'))


@main_bp.route('/delete_table', methods=['POST'])
def delete_table():
    # data = request.get_json()
    # table_name = data['table_name']
    # tables = read_tables()
    # tables = [table for table in tables if table['table_name'] != table_name]
    # write_tables(tables)
    # return jsonify({"message": "Table deleted successfully"}), 200

    table_name = request.form['table_name']
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM tables WHERE table_name = %s", (table_name,))
    db.commit()
    return jsonify({'status': 'success'})
