"""Thread data access from the database.
Contains SQL queries related to topic."""

from main import db
from typing import List

from src.uni.dao.basic_dao import BasicDao
from src.forum.models.thread_model import Thread
from src.user.user_model import User


class ThreadDao:
    """thread DAO"""

    @staticmethod
    def get_threads() -> List[Thread]:
        """
        Retrieve all the threads in the database.
        :return: The result of the query.
        """

        return Thread.query.order_by(Thread.thread_name).all()

    @staticmethod
    def get_thread_by_id(thread_id: str) -> Thread:
        """
        Retrieve a single thread by its unique id
        :param thread_id: The unique identifier for a thread.
        :return: The result of the query.
        """
        res = Thread.query.filter_by(thread_id=thread_id).first()
        print(res)

        return Thread.query.filter_by(thread_id=thread_id).first()

    @staticmethod
    def get_thread_by_name(thread_name: str) -> Thread:
        """
        Retrieve the thread on a specific name.
        :param thread_name: Name for a thread.
        :return: The result of the query.
        """
        return Thread.query.filter_by(thread_name=thread_name).first()

    @staticmethod
    def add_thread(new_thread: Thread) -> bool:
        """
        Add a thread to the database.
        :param new_thread: Object representing a thread.
        :return: True if the thread is inserted into the database, False otherwise.
        """
        db.session.add(new_thread)
        return BasicDao.safe_commit()

    @staticmethod
    def update_thread(thread: Thread) -> bool:
        """
        Update a thread in the database.
        :param thread: Object representing an updated thread.
        :return: True if the thread is updated in the database, False otherwise.
        """
        db.session.execute(
            """
            UPDATE threads SET
                thread_name=:thread_name,
            WHERE thread_id=:thread_id
            """,
            {
                "thread_id": thread.thread_id,
                "thread_name": thread.thread_name,
            },
        )
        return BasicDao.safe_commit()

    @staticmethod
    def delete_thread_by_id(thread_id: str) -> bool:
        """
        Delete a thread from the database based on its id.
        :param thread_id: ID which uniquely identifies the thread.
        :return: True if the deletion was successful without error, False otherwise.
        """
        db.session.execute(
            "DELETE FROM threads WHERE thread_id=:thread_id",
            {"thread_id": thread_id},
        )
        return BasicDao.safe_commit()

    @staticmethod
    def get_threads_count(self, topic_id: int):
        return Thread.query.filter_by(topic_id=topic_id).count()

    @staticmethod
    def get_threads_by_topic(topic_id: int) -> list:
        """
        Retrieve all the threads of one topic in the database by topic id.
        :param topic_id: The unique identifier for a topic.
        :return: The result of the query.
        """
        result = (
            db.session.execute(
                f"WITH threadpost AS "
                f"(SELECT topic, thread_id, count(post_id) AS post_count "
                f"FROM threads JOIN posts ON thread_id=thread GROUP BY thread_id) "
                f"SELECT g.*, u1.user_name AS thread_creator_name, u2.user_name AS post_creator_name, post_count "
                f"FROM "
                f"(SELECT p.*, thread_name, thread_created_at, thread_creator, thread_content,pinned,topic "
                f"FROM "
                f"(SELECT post_id, post_created_at, post_creator, thread AS thread_id, "
                f"row_number() OVER (PARTITION BY thread ORDER BY post_created_at DESC) AS rn "
                f"FROM posts) AS p "
                f"JOIN threads ON threads.thread_id=p.thread_id where rn=1) AS g "
                f"JOIN threadpost ON threadpost.thread_id=g.thread_id "
                f"JOIN users AS u1 ON u1.user_id=g.thread_creator "
                f"JOIN users AS u2 ON u2.user_id=g.post_creator "
                f"WHERE g.topic={topic_id} "
                f"ORDER BY post_created_at DESC"
            )
            .mappings()
            .all()
        )

        # res = (
        #    db.session.query(Thread, User)
        #    .filter_by(topic=topic_id)
        #    .join(User, Thread.thread_creator == User.user_id)
        #    .add_columns(Thread.thread_id, Thread.thread_name, User.user_name)
        # .order_by(Thread.thread_created_at)
        #    .all()
        # )
        print(result)
        # for r in res:
        #    print(r)
        #    print(r.Thread.thread_id)

        return result
