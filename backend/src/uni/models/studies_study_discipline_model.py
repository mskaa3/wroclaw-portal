"""studies_study_discipline model"""
from src import db
from sqlalchemy import Column, Integer


class StudiesStudyDiscipline1(db.Base):
    "studies_study_disciplines table schema"
    __tablename__ = "studies_study_disciplines"

    study_id_joint = Column(Integer)
    study_discipline_id_joint = Column(Integer)

    def __init__(self, studies_study_discipline: dict):
        self.study_id_joint = studies_study_discipline.get("study_id_joint")

        self.study_discipline_id_joint = studies_study_discipline.get(
            "study_discipline_id_joint"
        )

    # def json(self):
    #  return {'name':self.name,...}
    def __repr__(self):
        """
        String representation of the joint table.
        This representation is meant to be machine readable.
        :return: The joint table string.
        """
        return "<StudiesStudyDiscipline %r>" % (self.study_discipline_id_joint)

    def __str__(self):
        """
        String representation of the joint table.
        This representation is meant to be human readable.
        :return: The joint table string.
        """
        return f"StudiesStudyDiscipline: [study_discipline_id_joint: {self.study_discipline_id_joint}, study_discipline_id_joint: {self.study_discipline_id_joint}]"
