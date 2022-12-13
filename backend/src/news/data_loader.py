import requests
import json
import sqlite3
from deep_translator import GoogleTranslator 
from news_config import api_key,now,keyword,language,sorting_mode
translator =GoogleTranslator(source='pl', target='en') 


def update():
# or maybe since last update?
    
    try:
        response_API = requests.get('https://newsapi.org/v2/everything?q='+keyword+'&language='+language+'&from='+now+'&sortBy='+sorting_mode+'&apiKey='+api_key)
    except requests.exceptions.RequestException as e:
        print(e)

    data = response_API.text
    parsed_data = json.loads(data)


    with sqlite3.connect("news_db.db") as conn:
        try:
            cur = conn.cursor()
            for article in parsed_data['articles']:
                source=article['source']['name']
                title=translator.translate(article['title'])
                description=translator.translate(article['description'])
                url=article['url']
                image_url=article['urlToImage']
                published=article['publishedAt'].split('T')[0]
                content=translator.translate(article['content'])
                cur.execute(
                    f'SELECT source_id FROM source WHERE source_name = "{source}"'
                )
                data = cur.fetchall()
                if len(data) != 0:
                    msg = "Source already in the database"
                else:
                    cur.execute(f'INSERT INTO source (source_name) values ("{source}")')
                    conn.commit()
                try:
                    
                        cur.execute(
                            f'SELECT source_id FROM source WHERE source_name = "{source}"'
                        )
                        src_id = cur.fetchone()
                        cur.execute(
                            f'SELECT news_id FROM news WHERE news_title ="{title}"  AND source_id={src_id[0]}'
                        )
                        news_data = cur.fetchall()
                        if len(news_data) != 0:
                            msg = "News already in the database"
                        else:

                            cur.execute(
                                "INSERT INTO news (news_title,news_link,news_description,news_content,image_url,source_id,published_at) values (?,?,?,?,?,?,?)",
                                (title,url,description,content,image_url,src_id[0],published),)
                            conn.commit()
                except sqlite3.Error as er:
                    print(er)
                    msg = "cant news to the databse"
        except sqlite3.Error as er:
            print(er)
            msg = "cant add source to the databse"


    conn.close()

