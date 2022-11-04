"""study_discipline model"""
# from src.__init__ import db, ma
from src import db, ma
from sqlalchemy import Column, Integer, String


class StudyDiscipline(db.Base):
    "study_disciplines table schema"
    __tablename__ = "study_disciplines"

    study_discipline_id = Column(Integer, primary_key=True)
    study_discipline_name = Column(String(80), index=True, unique=True)
    # field_name = Column(String(80), index=True)

    # def __init__(self, study_discipline: dict):
    #    self.study_discipline_name = study_discipline.get("study_discipline_name")
    # self.study_discipline_name = study_discipline.study_discipline_name

    def __init__(self, study_discipline_name):
        #    self.study_discipline_name = study_discipline.get("study_discipline_name")
        self.study_discipline_name = study_discipline_name

    def json(self):
        return {
            "study_discipline_id": self.study_discipline_id,
            "study_discipline_name": self.study_discipline_name,
        }

    def __repr__(self):
        """
        String representation of the study_discipline.
        This representation is meant to be machine readable.
        :return: The study_discipline string.
        """
        return "<StudyDiscipline %r>" % (self.study_discipline_name)

    def __str__(self):
        """
        String representation of the study_discipline.
        This representation is meant to be human readable.
        :return: The study_discipline string.
        """
        return (
            f"StudyDiscipline: [study_discipline_id: {self.study_discipline_id},"
            f"study_discipline_name: {self.study_discipline_name}]"
        )


class StudyDisciplineSchema(ma.Schema):
    class Meta:
        # model = StudyDiscipline
        # sqla_session = db.session
        # load_instance = True
        fields = ("study_disciplines_id", "study_disciplines_name")


study_discipline_schema = StudyDisciplineSchema()
study_disciplines_schema = StudyDisciplineSchema(many=True)
