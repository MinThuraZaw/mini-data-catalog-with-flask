from flask import Blueprint, jsonify, request
from .db import get_db
import mysql.connector
from mysql.connector import Error

api_bp = Blueprint('api', __name__)


@api_bp.route('/tables', methods=['GET'])
def get_tables():
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)

        # Get query parameters
        table_name = request.args.get('table_name')
        database_name = request.args.get('database_name')

        # Build the query based on parameters
        query = "SELECT * FROM tables WHERE 1=1"
        params = []

        if table_name:
            query += " AND table_name = %s"
            params.append(table_name)

        if database_name:
            query += " AND database_name = %s"
            params.append(database_name)

        cursor.execute(query, params)
        tables = cursor.fetchall()
        return jsonify(tables)

    except Error as e:
        return jsonify({"error": str(e)}), 500
