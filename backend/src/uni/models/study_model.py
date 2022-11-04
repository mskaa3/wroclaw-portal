"""uni table shema"""

# from src.__init__ import db, ma
from src import db, ma
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from src.uni.models.study_discipline_model import StudyDiscipline


studies_study_disciplines = Table(
    "studies_study_disciplines",
    db.Base.metadata,
    Column("study_id_joint", Integer, ForeignKey("studies.study_id")),
    Column(
        "study_discipline_id_joint",
        Integer,
        ForeignKey("study_disciplines.study_discipline_id"),
    ),
)


class Study(db.Base):
    "studies table schema"
    __tablename__ = "studies"

    study_id = Column(Integer, primary_key=True)
    study_uid = Column(String(30))
    course_id = Column(String(20))
    study_name = Column(String(64), index=True)
    # study_name = Column(String(64), index=True)
    level = Column(String(20))
    profile = Column(String(20))
    title = Column(String(30))
    forms = Column(String(64))
    main_discipline = Column(String(64))
    # disciplines = Column(String(120))
    institutions = Column(String(64))
    # institutions = Column(Integer)
    disciplines = relationship(
        "StudyDiscipline", secondary=studies_study_disciplines, backref="studies"
    )
    """
    def __init__(
        self,
        study_uid,
        course_id,
        study_name,
        level,
        profile,
        title,
        forms,
        main_discipline,
        institutions,
    ):
        self.study_uid = study_uid
        self.course_id = course_id
        self.study_name = study_name
        self.level = level
        self.profile = profile
        self.title = title
        self.forms = forms
        self.main_discipline = main_discipline
        self.institutions = institutions
    """

    def __init__(self, study: dict):
        self.study_uid = study.get("study_uid")
        self.course_id = study.get("course_id")
        self.study_name = study.get("study_name")
        self.level = study.get("level")
        self.profile = study.get("profile")
        self.title = study.get("title")
        self.forms = study.get("forms")
        self.main_discipline = study.get("main_discipline")
        # self.disciplines = study.get("disciplines")
        self.institutions = study.get("institutions")

    # def json(self):
    #  return {'name':self.name,"study_disciplines"=[study_discipline.json() for study_discipline in self.study_disciplines.all()]}

    def __repr__(self):
        """
        String representation of the study.
        This representation is meant to be machine readable.
        :return: The study string.
        """
        return f"<Study {self.study_name}"

    def __str__(self):
        """
        String representation of the study.
        This representation is meant to be human readable.
        :return: The study string.
        """
        return (
            f"Study: [study_id: {self.study_id},study_uid: {self.study_uid},"
            f"course_id: {self.course_id},study_name: {self.study_name},"
            f"level:{self.level},profile:{self:profile},title: {self.title},"
            f"forms: {self.forms},main_discipline: {self.main_discipline},"
            # f"disciplines: {self.disciplines},"
            f"institutions:{self.institutions}]"
        )


class StudySchema(ma.Schema):
    class Meta:
        model = Study
        # sqla_session = db.session
        # load_instance = True
        """
        fields = (
            "study_id",
            "study_uid",
            "course_id",
            "study_name",
            "level",
            "profile",
            "title",
            "forms",
            "main_discipline",
            "institutions",
        )
        """


study_schema = StudySchema()
studies_schema = StudySchema(many=True)


class LevelsSchema(ma.Schema):
    class Meta:
        model = Study
        # sqla_session = db.session
        # load_instance = True
        # fields = ["level"]


levels_schema = LevelsSchema(many=True)
