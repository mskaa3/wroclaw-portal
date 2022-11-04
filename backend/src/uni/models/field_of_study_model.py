"""fields_of_study model"""
from src import db
from sqlalchemy import Column, Integer, String


class FieldOfStudy(db.Base):
    "fields_of_study table schema"
    __tablename__ = "fields_of_study"

    field_id = Column(Integer, primary_key=True)
    # field_name = Column(String(80), index=True, unique=True)
    field_name = Column(String(80), index=True)

    def __init__(self, field: dict):
        self.field_name = field.get("field_name")

    # def json(self):
    #  return {'name':self.name,...}
    def __repr__(self):
        """
        String representation of the field of study.
        This representation is meant to be machine readable.
        :return: The field of study string.
        """
        return "<FieldOfStudy %r>" % (self.field_name)

    def __str__(self):
        """
        String representation of the field of study.
        This representation is meant to be human readable.
        :return: The field of study string.
        """
        return (
            f"FieldOfStudy: [field_id: {self.field_id}, field_name: {self.field_name}]"
        )
