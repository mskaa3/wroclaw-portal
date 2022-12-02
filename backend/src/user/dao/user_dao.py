"""User data access from the database.
Contains SQL queries related to user."""

from main import db
from typing import List

from src.uni.dao.basic_dao import BasicDao
from src.user.user_model import User


class UserDao:
    """user DAO"""

    @staticmethod
    def get_users() -> List[User]:
        """
        Retrieve all the users in the database.
        :return: The result of the query.
        """

        return User.query.order_by(User.user_name).all()

    @staticmethod
    def get_user_by_id(user_id: int) -> User:
        """
        Retrieve a single user by its unique id
        :param user_id: The unique identifier for a user.
        :return: The result of the query.
        """
        # res = Post.query.filter_by(post_id=post_id).first()
        # print(res)

        return User.query.filter_by(user_id=user_id).first()

    @staticmethod
    def get_user_by_user_name(user_name: str) -> User:
        """
        Retrieve a users by its user name
        :param user_name: The unique identifier for a user.
        :return: The result of the query.
        """

        return User.query.filter_by(user_name=user_name).first()

    @staticmethod
    def add_user(new_user: User) -> bool:
        """
        Add a user to the database.
        :param new_user: Object representing a user.
        :return: True if the user is inserted into the database, False otherwise.
        """
        db.session.add(new_user)
        return BasicDao.safe_commit()

    @staticmethod
    def update_user(user: User) -> bool:
        """
        Update a user in the database.
        :param user: Object representing an updated user.
        :return: True if the user is updated in the database, False otherwise.
        """
        db.session.execute(
            """
            UPDATE users SET
                user_name=:user_name,
                user_email=:user_email,
                password=:password,
                avatar=:avatar
            WHERE user_id=:user_id
            """,
            {
                "user_id": user.user_id,
                "user_name": user.user_name,
                "user_email": user.user_email,
                "password": user.password,
                "avatar": user.avatar,
            },
        )

        return BasicDao.safe_commit()

    @staticmethod
    def delete_user_by_id(user_id: int) -> bool:
        """
        Delete a user from the database based on its id.
        :param user_id: ID which uniquely identifies the user.
        :return: True if the deletion was successful without error, False otherwise.
        """
        db.session.execute(
            "DELETE FROM users WHERE user_id=:user_id",
            {"user_id": user_id},
        )
        return BasicDao.safe_commit()
