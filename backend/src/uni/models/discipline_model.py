"""discipline  model"""
from src import db
from sqlalchemy import Column, Integer, String


class Discipline(db.Base):
    "disciplines table schema"
    __tablename__ = "disciplines"

    discipline_id = Column(Integer, primary_key=True)
    discipline_key = Column(String(10), index=True, unique=True)
    # discipline_key = Column(String(10), index=True)
    # discipline_name = Column(String(80), index=True, unique=True)
    discipline_name = Column(String(80), index=True)

    def __init__(self, discipline: dict):
        self.discipline_id = discipline.get("discipline_id")
        self.discipline_key = discipline.get("discipline_key")
        self.discipline_name = discipline.get("discipline_name")

    # def json(self):
    #  return {'name':self.name,...}
    def __repr__(self):
        """
        String representation of the discipline.
        This representation is meant to be machine readable.
        :return: The discipline string.
        """
        return f"<Discipline {self.discipline_name}"

    def __str__(self):
        """
        String representation of the discipline.
        This representation is meant to be human readable.
        :return: The discipline string.
        """
        return (
            f"Discipline: [discipline_id: {self.discipline_id}, "
            f"discipline_name: {self.discipline_key},"
            f"discipline_name: {self.discipline_name}]"
        )
