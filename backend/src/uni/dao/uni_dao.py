"""Uni data access from the database.  Contains SQL queries related to unis."""
from typing import List
from sqlalchemy import and_

from main import db

from src.uni.models.course_model import courses_disciplines
from src.uni.dao.basic_dao import BasicDao
from src.uni.models.uni_model import Uni
from src.uni.models.course_model import Course
from src.uni.models.discipline_model import Discipline


class UniDao:
    """DAO for unis table"""

    @staticmethod
    def get_unis() -> List[Uni]:
        """
        Get a list of all the uniss in the database.
        :return: A list containing Uni model objects.
        """
        return Uni.query.all()

    @staticmethod
    def get_uni_by_name(uni_name: str) -> Uni:
        """
        Get a single uni from the database based on their name.
        :param uni_name: Uni name which uniquely identifies the uni.
        :return: The result of the database query.
        """
        return (
            Uni.query.filter_by(uni_name=uni_name)
            # .options(defer("profilepic"), defer("profilepic_name"))
            .first()
        )

    @staticmethod
    def get_uni_by_id(uni_id: str) -> Uni:
        """
        Get a single uni from the database based on their id.
        :param id: Email which uniquely identifies the uni.
        :return: The result of the database query.
        """
        return (
            Uni.query.filter_by(uni_id=uni_id)
            # .options(defer("profilepic"), defer("profilepic_name"))
            .first()
        )

    @staticmethod
    def get_uni_by_uid(uni_uid: str) -> Uni:
        """
        Get a single uni from the database based on their id.
        :param id: Email which uniquely identifies the uni.
        :return: The result of the database query.
        """
        # res=Uni.join(UniKind)
        # res=db.session.query(*Uni.__table__.columns,*UniKind.__table__.columns).select_from(Uni).join(UniKind).filter(Uni.uni_uid==uni_uid).first()

        return (
            Uni.query.filter_by(uni_uid=uni_uid)
            # .options(defer("profilepic"), defer("profilepic_name"))
            .first()
        )

    @staticmethod
    def add_uni(uni: Uni) -> bool:
        """
        Add a uni.
        :param uni: Object representing a uni for the application.
        :return: True if the uni is inserted into the database, False otherwise.
        """
        db.session.add(uni)
        return BasicDao.safe_commit()

    @staticmethod
    def update_uni(uni_id: int, uni: Uni) -> bool:
        """
        Update a uni in the database.
        :param uni_id: Uni id which uniquely identifies the uni.
        :param uni: Object representing an updated uni for the application.
        :return: True if the uni is updated in the database, False otherwise.
        """
        db.session.execute(
            """
            UPDATE unis SET
                uni_name=:uni_name,
                uni_code=:uni_code,
                kind=:kind,
                www=:www,
                phone_number=:phone_number,
                uni_email=:uni_email,
                city=:city,
                street=:street,
                building=:building,
                postal_code=:postal_code
            WHERE uni_id=:uni_id
            """,
            {
                "uni_name": uni.uni_name,
                "uni_code": uni.uni_code,
                "kind": uni.kind,
                "www": uni.www,
                "phone_number": uni.phoneNumber,
                "uni_email": uni.uni_email,
                "city": uni.city,
                "street": uni.street,
                "building": uni.building,
                "postal_code": uni.postal_code,
            },
            # bind=UniDao.engine,
        )
        return BasicDao.safe_commit()

    @staticmethod
    def delete_uni(uni_id: int) -> bool:
        """
        Delete a uni from the database based on its id.
        :param uni_id: Uni id which uniquely identifies the uni
        :return: True if the deletion was successful without error, False otherwise.
        """
        db.session.execute(
            "DELETE FROM unis WHERE uni_id=:uni_id",
            {"uni_id": uni_id},
            # bind=UniDao.engine,
        )

        return BasicDao.safe_commit()

    @staticmethod
    def get_cities() -> List[str]:
        """
        Get a list of all the cities in the database.
        :return: A list containing cities.
        """
        return Uni.query.with_entities(Uni.city).distinct().order_by(Uni.city).all()

    @staticmethod
    def filter_unis(params: dict) -> List[Uni]:
        # query = db.session.query(Foo).join(Bar)
        print("params from query")
        print(params)
        print(params["discipline_name"])

        return (
            # db.session.query(Course, courses_disciplines, Discipline)
            Course.query.join(
                courses_disciplines,
                courses_disciplines.c.course_id_joint == Course.course_id,
            )
            .join(
                Discipline,
                courses_disciplines.c.discipline_id_joint == Discipline.discipline_id,
            )
            .join(Uni, Uni.uni_uid == Course.institution)
            .filter(
                # Course.main_discipline == params["discipline_name"]
                # Course.course_disciplines.any(
                and_(
                    # Discipline.discipline_id == params["discipline_name"],
                    Course.main_discipline == params["discipline_name"],
                    Course.level == params["level"],
                    Uni.city == params["city"],
                )
            )
            .with_entities(
                Uni.uni_name,
                Uni.uni_uid,
                Course.course_id,
                Course.course_name,
                Course.level,
                Course.main_discipline,
                Discipline.discipline_id,
                Discipline.discipline_name,
            )
            .group_by(Uni.uni_uid)
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
