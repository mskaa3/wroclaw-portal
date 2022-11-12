"""Course form data access from the database.
Contains SQL queries related to course form."""

from main import db

# from src import app
from src.uni.dao.basic_dao import BasicDao
from src.uni.models.course_form_model import CourseForm


class CourseFormDao:
    """course form DAO"""

    @staticmethod
    def get_forms() -> list:
        """
        Retrieve all the forms in the database.
        :return: The result of the query.
        """
        return CourseForm.query.order_by(CourseForm.course_form_name).all()

    @staticmethod
    def get_form_by_id(form_id: int) -> CourseForm:
        """
        Retrieve a single form by its unique id
        :param form_id: The unique identifier for a course form.
        :return: The result of the query.
        """
        return CourseForm.query.filter_by(course_form_id=form_id).first()

    @staticmethod
    def add_form(new_form: CourseForm) -> bool:
        """
        Add a course form to the database.
        :param new_form: Object representing a course form.
        :return: True if the form is inserted into the database, False otherwise.
        """
        db.session.add(new_form)
        return BasicDao.safe_commit()

    @staticmethod
    def update_form(form: CourseForm) -> bool:
        """
        Update a course form in the database.
        :param form: Object representing an updated form.
        :return: True if the form is updated in the database, False otherwise.
        """
        db.session.execute(
            """
            UPDATE course_forms SET
                course_form_name=:form_name,
            WHERE course_form_id=:form_id
            """,
            {
                "form_id": form.course_form_id,
                "form_name": form.course_form_name,
            },
        )
        return BasicDao.safe_commit()

    @staticmethod
    def delete_form_by_id(form_id: int) -> bool:
        """
        Delete a course form from the database based on its id.
        :param form_id: ID which uniquely identifies the form.
        :return: True if the deletion was successful without error, False otherwise.
        """
        db.session.execute(
            "DELETE FROM course_forms WHERE course_form_id=:form_id",
            {"form_id": form_id},
        )
        return BasicDao.safe_commit()
