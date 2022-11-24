import sqlite3
from flask import Blueprint, request, jsonify

docs_routes = Blueprint("docs_routes", __name__)


@docs_routes.route("/docs",methods=['GET'])
def docs():
    with sqlite3.connect("docs_db.db") as conn:
        try:
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM categories")
            categories_data = cur.fetchall()
            cur.execute(f"SELECT * FROM documents")
            documents_data = cur.fetchall()
            return jsonify(categories_data, documents_data)
        except sqlite3.Error as er:
            return er
