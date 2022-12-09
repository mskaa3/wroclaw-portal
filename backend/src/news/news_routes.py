import sqlite3
from flask import Blueprint, request, jsonify
from .data_loader import update
number=15
news_routes = Blueprint("news_routes", __name__)


@news_routes.route("/news", methods=["GET"])
def news():
    
    
    with sqlite3.connect("news_db.db") as conn:
        try:
            
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM source")
            source_data = cur.fetchall()
            cur.execute(f"SELECT * FROM news ORDER BY date(published_at) DESC")
            documents_data = cur.fetchall()
            documents_list = []
            for elem in documents_data:
                elem_dict = {
                        "id": elem[0],
                        "title": elem[1],
                        "url": elem[2],
                        "description": elem[3],
                        "content": elem[4],
                        "image": elem[5],
                        "source": elem[6],
                        "date": elem[7]
                    }
                
                documents_list.append(elem_dict)
            part=documents_list[:number]
            
        except sqlite3.Error as er:
             print(er)
    # 
    conn.close()
    return jsonify(source_data,part)

