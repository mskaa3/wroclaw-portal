"""Course level data access from the database.
Contains SQL queries related to course level."""

from main import db

from src.uni.dao.basic_dao import BasicDao
from src.uni.models.course_level_model import CourseLevel


class CourseLevelDao:
    """course level DAO"""

    @staticmethod
    def get_levels() -> list:
        """
        Retrieve all the levels in the database.
        :return: The result of the query.
        """
        return CourseLevel.query.order_by(CourseLevel.course_level_name).all()

    @staticmethod
    def get_level_by_id(level_id: int) -> CourseLevel:
        """
        Retrieve a single level by its unique id
        :param level_id: The unique identifier for a course level.
        :return: The result of the query.
        """
        return CourseLevel.query.filter_by(course_level_id=level_id).first()

    @staticmethod
    def get_level_by_name(level_name: str) -> CourseLevel:
        """
        Retrieve the course level on a specific name.
        :param level_name: Name for a course level.
        :return: The result of the query.
        """
        return CourseLevel.query.filter_by(course_level_name=level_name).first()

    @staticmethod
    def add_level(new_level: CourseLevel) -> bool:
        """
        Add a course levelto the database.
        :param new_level: Object representing a course level.
        :return: True if the level is inserted into the database, False otherwise.
        """
        db.session.add(new_level)
        return BasicDao.safe_commit()

    @staticmethod
    def update_level(level: CourseLevel) -> bool:
        """
        Update a course level in the database.
        :param level: Object representing an updated level.
        :return: True if the level is updated in the database, False otherwise.
        """
        db.session.execute(
            """
            UPDATE course_levels SET
                course_level_name=:level_name,
            WHERE course_level_id=:level_id
            """,
            {
                "level_id": level.course_level_id,
                "level_name": level.course_level_name,
            },
        )
        return BasicDao.safe_commit()

    @staticmethod
    def delete_level_by_id(level_id: int) -> bool:
        """
        Delete a course level from the database based on its id.
        :param level_id: ID which uniquely identifies the level.
        :return: True if the deletion was successful without error, False otherwise.
        """
        db.session.execute(
            "DELETE FROM course_levels WHERE course_level_id=:level_id",
            {"level_id": level_id},
        )
        return BasicDao.safe_commit()
