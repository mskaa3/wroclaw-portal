"""Uni kind data from the database.  Contains SQL queries related to uni kinds."""
from typing import List

from src.uni.models.uni_kind_model import UniKind
from main import db

from src.uni.dao.basic_dao import BasicDao


class UniKindDao:
    """dao for uni_kinds table"""

    @staticmethod
    def get_kinds() -> List[UniKind]:
        """
        Get a list of all the uni kinds in the database.
        :return: A list containing UniKind model objects.
        """
        return UniKind.query.all()

    @staticmethod
    def get_kind_by_id(kind_id: str) -> UniKind:
        """
        Get a single uni kind from the database based on their id.
        :param kind_id: Id which uniquely identifies the uni kind.
        :return: The result of the database query.
        """
        return UniKind.query.filter_by(kind_id=kind_id).first()

    @staticmethod
    def add_kind(kind: UniKind) -> bool:
        """
        Add a uni kind.
        :param kind: Object representing a uni kind for the application.
        :return: True if the uni kind is inserted into the database, False otherwise.
        """
        db.session.add(kind)
        return BasicDao.safe_commit()

    @staticmethod
    def update_kind(kind_id: int, kind: UniKind) -> bool:
        """
        Update a uni kind in the database.
        :param kind_id: Uni kind id which uniquely identifies the uni kind.
        :param kind: Object representing an updated uni kind for the application.
        :return: True if the uni kind is updated in the database, False otherwise.
        """
        db.session.execute(
            """
            UPDATE uni_kinds SET
                kind_name=:kind,
            WHERE kind_id=:kind_id
            """,
            {
                "kind_name": kind.kind_name,
            },
        )
        return BasicDao.safe_commit()

    @staticmethod
    def delete_kind(kind_id: int) -> bool:
        """
        Delete a uni kind from the database based on its id.
        :param kind_id: Uni kind id which uniquely identifies the uni kind
        :return: True if the deletion was successful without error, False otherwise.
        """
        db.session.execute(
            "DELETE FROM uni_kinds WHERE kind_id=:kind_id",
            {"kind_id": kind_id},
        )

        return BasicDao.safe_commit()
