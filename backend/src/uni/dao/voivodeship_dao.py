"""Voivodeship data access from the database.
Contains SQL queries related to voivodeship."""

from src import db

# from src import app
from src.uni.dao.basic_dao import BasicDao
from src.uni.models.voivodeship_model import Voivodeship


class VoivodeshipDao:
    """voivodeship DAO"""

    @staticmethod
    def get_voivodeships() -> list:
        """
        Retrieve all the voivodeships in the database.
        :return: The result of the query.
        """
        return Voivodeship.query.order_by(Voivodeship.voiv_name).all()

    @staticmethod
    def get_voivodeship_by_id(voiv_id: int) -> Voivodeship:
        """
        Retrieve a single voivodeship by its unique id
        :param voiv_id: The unique identifier for a voivodeship.
        :return: The result of the query.
        """
        return Voivodeship.query.filter_by(voiv_id=voiv_id).first()

    @staticmethod
    def get_voivodeship_by_terc(terc: int) -> list:
        """
        Retrieve the voivodeship on a specific terc.
        :param terc: Unique identifier for a voivodeship.
        :return: The result of the query.
        """
        return Voivodeship.query.filter_by(terc=terc).first()

    @staticmethod
    def add_voivodeship(new_voivodeship: Voivodeship) -> bool:
        """
        Add a voivodeship to the database.
        :param new_voiv: Object representing a voivodeship.
        :return: True if the voivodeship is inserted into the database, False otherwise.
        """
        db.session.add(new_voivodeship)
        return BasicDao.safe_commit()

    @staticmethod
    def update_voivodeship(voivodeship: Voivodeship) -> bool:
        """
        Update a voivodeship in the database.
        :param voivodeship: Object representing an updated voivodeship.
        :return: True if the voivodeship is updated in the database, False otherwise.
        """
        db.session.execute(
            """
            UPDATE voivodeships SET
                voiv_name=:voiv_name,
                terc=:terc
            WHERE voiv_id=:voiv_id
            """,
            {
                "voiv_id": voivodeship.voiv_id,
                "voiv_name": voivodeship.voiv_name,
                "terc": voivodeship.terc,
            },
        )
        return BasicDao.safe_commit()

    @staticmethod
    def delete_voivodeship_by_id(voiv_id: int) -> bool:
        """
        Delete a voivodeship from the database based on its id.
        :param voiv_id: ID which uniquely identifies the voivodeship.
        :return: True if the deletion was successful without error, False otherwise.
        """
        db.session.execute(
            "DELETE FROM voivodeships WHERE voiv_id=:voiv_id",
            {"voiv_id": voiv_id},
        )
        return BasicDao.safe_commit()

    @staticmethod
    def delete_voivodeship_by_terc(terc: int) -> bool:
        """
        Delete voivodeship from the database based on the terc.
        :param terc: Terc which uniquely identifies the voivodeship.
        :return: True if the deletions were successful without error, False otherwise.
        """
        db.session.execute(
            "DELETE FROM voivodeships WHERE terc=:terc",
            {"terc": terc},
        )
        return BasicDao.safe_commit()
