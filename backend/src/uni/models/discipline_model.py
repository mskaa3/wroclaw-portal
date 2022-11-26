"""discipline  model"""
from main import db, ma
from sqlalchemy import Column, String

from src.uni.models.course_model import courses_disciplines


class Discipline(db.Base):
    "disciplines table schema"
    __tablename__ = "disciplines"

    # discipline_id = Column(Integer, primary_key=True)
    discipline_id = Column(String(10), primary_key=True)
    # discipline_key = Column(String(10), index=True)
    # discipline_name = Column(String(80), index=True, unique=True)
    discipline_name = Column(String(80), index=True)
    # discipline_code = Column(String(10), index=True, unique=True)
    # _courses = relationship(
    #    "Course",
    #    secondary=courses_disciplines,
    #    # backref="courses_to_disciplines_table_backref",
    #    backref="courses_to_disciplines_table_backref",
    # )

    def __init__(self, discipline: dict):
        self.discipline_id = discipline.get("discipline_id")
        self.discipline_name = discipline.get("discipline_name")
        # self.discipline_code = discipline.get("discipline_code")

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
            f"discipline_name: {self.discipline_name},]"
        )


class DisciplineSchema(ma.Schema):
    """schema for Discipline"""

    class Meta:
        model = Discipline
        # sqla_session = db.session
        # load_instance = True
        # fields = ["level"]


discipline_schema = DisciplineSchema()
disciplines_schema = DisciplineSchema(many=True)
