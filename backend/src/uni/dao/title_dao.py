"""Course title data access from the database.
Contains SQL queries related to course title."""
from typing import List
from main import db

from src.uni.dao.basic_dao import BasicDao
from src.uni.models.course_title_model import CourseTitle


class CourseTitleDao:
    """course title DAO"""

    @staticmethod
    def get_titles() -> List[CourseTitle]:
        """
        Retrieve all the titles in the database.
        :return: The result of the query.
        """
        return CourseTitle.query.order_by(CourseTitle.course_title_name).all()

    @staticmethod
    def get_title_by_id(title_id: int) -> CourseTitle:
        """
        Retrieve a single title by its unique id
        :param title_id: The unique identifier for a course title.
        :return: The result of the query.
        """
        return CourseTitle.query.filter_by(course_title_id=title_id).first()

    @staticmethod
    def get_title_by_name(title_name: str) -> CourseTitle:
        """
        Retrieve the course title on a specific name.
        :param title_name: Name for a course title.
        :return: The result of the query.
        """
        return CourseTitle.query.filter_by(course_title_name=title_name).first()

    @staticmethod
    def add_title(new_title: CourseTitle) -> bool:
        """
        Add a course title to the database.
        :param new_title: Object representing a course title.
        :return: True if the title is inserted into the database, False otherwise.
        """
        db.session.add(new_title)
        return BasicDao.safe_commit()

    @staticmethod
    def update_title(title: CourseTitle) -> bool:
        """
        Update a course title in the database.
        :param title: Object representing an updated title.
        :return: True if the title is updated in the database, False otherwise.
        """
        db.session.execute(
            """
            UPDATE course_titles SET
                course_title_name=:title_name,
            WHERE course_title_id=:title_id
            """,
            {
                "course_title_id": title.course_title_id,
                "course_title_name": title.course_title_name,
            },
        )
        return BasicDao.safe_commit()

    @staticmethod
    def delete_title_by_id(title_id: int) -> bool:
        """
        Delete a course title from the database based on its id.
        :param title_id: ID which uniquely identifies the title.
        :return: True if the deletion was successful without error, False otherwise.
        """
        db.session.execute(
            "DELETE FROM course_titles WHERE course_title_id=:title_id",
            {"course_title_id": title_id},
        )
        return BasicDao.safe_commit()
