from flask import Blueprint, jsonify, request
from .db import get_db
import mysql.connector
from mysql.connector import Error

api_bp = Blueprint('api', __name__)


def fetch_tables(query, params):
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute(query, params)
        tables = cursor.fetchall()
        return jsonify(tables)
    except Error as e:
        return jsonify({"error": str(e)}), 500


@api_bp.route('/tables', methods=['GET'])
def get_tables():
    table_name = request.args.get('table_name')
    database_name = request.args.get('database_name')
    description = request.args.get('description')
    created_at = request.args.get('created_at')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    query = "SELECT * FROM tables WHERE 1=1"
    params = []

    if table_name:
        query += " AND table_name = %s"
        params.append(table_name)

    if database_name:
        query += " AND database_name = %s"
        params.append(database_name)

    if description:
        query += " AND description LIKE %s"
        params.append(f"%{description}%")

    if created_at:
        query += " AND DATE(created_at) = %s"
        params.append(created_at)

    query += " LIMIT %s OFFSET %s"
    params.extend([per_page, (page - 1) * per_page])

    return fetch_tables(query, params)


@api_bp.route('/tables/<int:table_id>', methods=['GET'])
def get_table(table_id):
    query = "SELECT * FROM tables WHERE id = %s"
    return fetch_tables(query, [table_id])


@api_bp.route('/tables/by_description', methods=['GET'])
def get_tables_by_description():
    description = request.args.get('description')
    if not description:
        return jsonify({"error": "Description is required"}), 400

    query = "SELECT * FROM tables WHERE description LIKE %s"
    params = [f"%{description}%"]

    return fetch_tables(query, params)


@api_bp.route('/tables/by_date', methods=['GET'])
def get_tables_by_date():
    created_at = request.args.get('created_at')
    if not created_at:
        return jsonify({"error": "Date is required"}), 400

    query = "SELECT * FROM tables WHERE DATE(created_at) = %s"
    params = [created_at]

    return fetch_tables(query, params)