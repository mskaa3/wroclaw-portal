"""Uni data access from the database.  Contains SQL queries related to unis."""
from typing import List
from src.__init__ import db

# from src impor app
from src.uni.dao.basic_dao import BasicDao
from src.uni.models.uni_model import Uni


class UniDao:
    # engine = db.get_engine(app=app, bind="app")

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
