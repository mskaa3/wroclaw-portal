"""Course language data access from the database.
Contains SQL queries related to course language."""
from typing import List
from main import db

# from src import app
from src.uni.dao.basic_dao import BasicDao
from src.uni.models.course_language_model import CourseLanguage


class CourseLanguageDao:
    """course language DAO"""

    @staticmethod
    def get_languages() -> List[CourseLanguage]:
        """
        Retrieve all the languages in the database.
        :return: The result of the query.
        """
        return CourseLanguage.query.order_by(CourseLanguage.course_language_name).all()

    @staticmethod
    def get_language_by_id(lang_id: int) -> CourseLanguage:
        """
        Retrieve a single language by its unique id
        :param lang_id: The unique identifier for a course lnguage.
        :return: The result of the query.
        """
        return CourseLanguage.query.filter_by(course_language_id=lang_id).first()

    @staticmethod
    def add_language(new_lang: CourseLanguage) -> bool:
        """
        Add a course language to the database.
        :param new_lang: Object representing a course language.
        :return: True if the language is inserted into the database, False otherwise.
        """
        db.session.add(new_lang)
        return BasicDao.safe_commit()

    @staticmethod
    def update_language(lang: CourseLanguage) -> bool:
        """
        Update a course language in the database.
        :param language: Object representing an updated language.
        :return: True if the language is updated in the database, False otherwise.
        """
        db.session.execute(
            """
            UPDATE course_languages SET
                course_language_name=:lang_name,
            WHERE course_language_id=:lang_id
            """,
            {
                "course_langusge_id": lang.course_language_id,
                "course_language_name": lang.course_language_name,
            },
        )
        return BasicDao.safe_commit()

    @staticmethod
    def delete_language_by_id(lang_id: int) -> bool:
        """
        Delete a course language from the database based on its id.
        :param lang_id: ID which uniquely identifies the language.
        :return: True if the deletion was successful without error, False otherwise.
        """
        db.session.execute(
            "DELETE FROM course_languages WHERE course_language_id=:lang_id",
            {"course_language_id": lang_id},
        )
        return BasicDao.safe_commit()
