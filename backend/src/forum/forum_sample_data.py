"""download data needed to fill uni db"""
import sqlite3
from urllib.error import URLError
from sqlalchemy.inspection import inspect

from collections import defaultdict

# import dpath.util

from src.utils.validators import validate_string
from src.utils.helpers import get_json_from_url
from src.utils.helpers import sql_data_to_dict

# get column names from table
# columns = [column.name for column in inspect(model).c]


FORUM_DATA_URL = "http://localhoat/forum"

TOPIC_DATA_URL = FORUM_DATA_URL + "/topics"

TOPICS_QUERY = "insert into topics(topic_name,description,slug) values(?,?,?)"
USERS_QUERY = "insert into users(user_name,user_email,password) values(?,?,?)"
THREADS_QUERY = "insert into threads(thread_name,thread_content,thread_created_at,thread_last_activity,topic,thread_creator,pinned) values(?,?,?,?,?,?,?)"

POSTS_QUERY = "insert into posts(post_content,post_created_at,post_updated_at,thread,post_creator) values(?,?,?,?,?)"


INSTITUTION_DATA_STATUS_FILTER = "1"  # Działająca - Operating
INSTITUTION_DATA_COUNTRY_FILTER = "Polska"
INSTITUTION_DATA_KIND_FILTER = 16  # Federation


topics_sample_data = [
    ("Topic 1", "Description of topic 1", "topic-1"),
    ("Topic 2", "Description of topic 2", "topic-2"),
    ("Topic 3", "Description of topic 3", "topic-3"),
    ("Topic 4", "Description of topic 4", "topic-4"),
]
users_sample_data = [
    ("User 1", "user1@gmail.com", "user1"),
    ("User 2", "user2@gmail.com", "user2"),
    ("User 3", "user3@gmail.com", "user3"),
]
threads_sample_data = [
    ("Thread 1", "Content of thread 1", "2022-10-14", "2022-11-11", 1, 1, "false")
]
posts_sample_data = [
    ("Post 1 content", "2022-10-16", None, 1, 2),
    ("Post 2 content", "2022-11-11", None, 1, 3),
]


# *************************************************************************************
# @app.before_first_request
def fill_forum_tables(db):
    """function to initial fill database forum tables"""

    conn = sqlite3.connect(db, detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()

    cursor.executemany(TOPICS_QUERY, topics_sample_data)
    # conn.commit()
    print("topics table filled ======================================")

    cursor.executemany(USERS_QUERY, users_sample_data)
    # conn.commit()
    print("users table filled +++++++++++++++++++++++++++++++++++++++++")

    cursor.executemany(THREADS_QUERY, threads_sample_data)
    # conn.commit()
    print("threads table filled ======================================")

    cursor.executemany(POSTS_QUERY, posts_sample_data)
    conn.commit()
    print("posts table filled ======================================")

    conn.close()
