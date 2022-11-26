"""courses data access from the database.  Contains SQL queries related to courses."""
from typing import List

# from src.__init__ import db
from main import db
from sqlalchemy import and_

# from sqlalchemy import Integer, String

# from src impor app
from src.uni.dao.basic_dao import BasicDao
from src.uni.models.course_model import Course
from src.uni.models.course_form_model import CourseForm
from src.uni.models.course_language_model import CourseLanguage
from src.uni.models.course_level_model import CourseLevel
from src.uni.models.course_title_model import CourseTitle


class CourseDao:
    # engine = db.get_engine(app=app, bind="app")

    @staticmethod
    def get_courses() -> List[Course]:
        """
        Get a list of all the courses in the database.
        :return: A list containing Course model objects.
        """

        return Course.query.order_by(Course.course_name).all()
        # return db.session.query(StudyDiscipline).all()

    @staticmethod
    def get_courses_by_name(course_name: str) -> List[Course]:
        """
        Get a list of all the courses from the database based on their name.
        :param study_name: Study name
        :return: The result of the database query.
        """
        return (
            Course.query.filter_by(course_name=course_name)
            # .options(defer("profilepic"), defer("profilepic_name"))
            .all()
        )

    @staticmethod
    def get_course_by_id(course_id: str) -> Course:
        """
        Get a single course from the database based on their id.
        :param id: Id which uniquely identifies the course.
        :return: The result of the database query.
        """
        return (
            Course.query.filter_by(course_id=course_id)
            # .options(defer("profilepic"), defer("profilepic_name"))
            .first()
        )

    @staticmethod
    def add_course(course: Course) -> bool:
        """
        Add a course.
        :param course: Object representing a course for the application.
        :return: True if the course is inserted into the database, False otherwise.
        """
        db.session.add(course)
        return BasicDao.safe_commit()

    @staticmethod
    def update_course(course_id: int, course: Course) -> bool:
        """
        Update a course in the database.
        :param course_id: Course id which uniquely identifies the course.
        :param course: Object representing an updated course for the application.
        :return: True if the course is updated in the database, False otherwise.
        """
        db.session.execute(
            """
            UPDATE courses SET
                course_name=:course_name,
            WHERE course_id=:course_id
            """,
            {
                "course_name": course.course_name,
            },
            # bind=UniDao.engine,
        )
        return BasicDao.safe_commit()

    @staticmethod
    def delete_course(course_id: int) -> bool:
        """
        Delete a course from the database based on its id.
        :param course_id: Course id which uniquely identifies the course.
        :return: True if the deletion was successful without error, False otherwise.
        """
        db.session.execute(
            "DELETE FROM courses WHERE course_id=:course_id",
            {"course_id": course_id},
            # bind=UniDao.engine,
        )

        return BasicDao.safe_commit()

        # return Study.query(Study.level).distinct().order_by(Study.level).all()
        # return Course.query.with_entities(Course.level).distinct().all()

    @staticmethod
    def filter_courses(params: dict) -> List[Course]:
        """method to filter courses using parameners from query string"""
        # query = db.session.query(Foo).join(Bar)
        print("params from query")
        print(params)
        print(params["uni_uid"])

        return (
            # db.session.query(Course, courses_disciplines, Discipline)
            Course.query.join(CourseLanguage)
            .join(CourseForm)
            .join(CourseTitle)
            .join(CourseLevel)
            # .join(CourseLanguage, Course.language==CourseLanguage.course_language_id)
            # .join(CourseForm,Course.form==CourseForm.course_form_id)
            # .join(CourseTitle,Course.title==CourseForm.course_form_id)
            .filter(
                and_(
                    Course.main_discipline == params["discipline_name"],
                    Course.level == params["level"],
                    Course.institution == params["uni_uid"],
                )
            )
            # .with_entities(
            #    Course.course_id,
            #    Course.course_name,
            #    Course.main_discipline,
            #    Course.semesters_number,
            #    Course.ects,
            #    CourseForm.course_form_name,
            #    CourseLanguage.course_language_name,
            #    CourseTitle.course_title_name,
            # )
            .all()
        )
        """
        return Course.query.filter(
            Course.course_disciplines.any(
                Discipline.discipline_name == params["discipline_name"]
            )
        ).all()
        """
        """
        return (
            Course.query.join(courses_disciplines)
            .join(Discipline)
            .filter(
                (courses_disciplines.c.course_id_joint == Course.course_id)
                & (
                    courses_disciplines.c.discipline_id_joint
                    == Discipline.discipline_id
                )
            )
            .join(Uni, Uni.uni_uid == Course.institution)
            .filter(
                Uni.city
                == params["city"]
                # Course.level == params["level"],
                # Discipline.discipline_name.like("%"+ params["discipline_name"] + "%"),
            )
            .all()
        )
        """
        # filt = UniFilter(data=params)
        # q = filt.apply()

        # query = db.session.query(Uni).join(Course).join(Discipline)
        filter_dict = {
            "city": {"model": "Uni", "field": "city", "op": "==", "value": ""},
            "discipline_name": {
                "model": "Discipline",
                "field": "discpline_name",
                "op": "ilike",
                "value": "",
            },
            "level": {"model": "Course", "field": "level", "op": "==", "value": ""},
        }
        filter_spec = []
        for key, value in params.items():
            if value and value != "":
                filter_dict[key]["value"] = value
                filter_spec.append(filter_dict[key])
        print("filter_spec")
        print(filter_spec)

        """
        filter_spec = [
            {"model": "Uni", "field": "city", "op": "==", "value": "name_1"},
            {
                "model": "Discipline",
                "field": "discpline_name",
                "op": "ilike",
                "value": 5,
            },
            {"model": "Course", "field": "level", "op": "==", "value": 5},
        ]
        """

        # filtered_query = apply_filters(query, filter_spec)

        # result = filtered_query.all()
