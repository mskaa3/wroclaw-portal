"""define database configuration"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from greenlet import getcurrent as _get_ident
from flask_sqlalchemy import SQLAlchemy

# from app import app


class Database:
    """define database configuration"""

    def __init__(self):
        """Create instance of class to be used when defining tables"""
        # tell SQLAlchemy how you'll define tables and models
        self.Base = declarative_base()

    def init_app(self, app):
        """Set up SQLAlchemy to work with Flask Application"""
        # connect database
        self.engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
        # create session factory
        self.sessionmaker = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )
        # set up scoped_session registry
        # #add ability to access scoped session registry (implicitly)
        # self.session = scoped_session(self.sessionmaker, scopefunc=_get_ident)
        self.session = scoped_session(self.sessionmaker)
        # add ability to query against the tables in database
        self.Base.query = self.session.query_property()
        # make sure db is initialize and up to date

        from src.uni.models.uni_model import Uni
        from src.uni.models.voivodeship_model import Voivodeship
        from src.uni.models.uni_kind_model import UniKind
        from src.uni.models.field_of_study_model import FieldOfStudy
        from src.uni.models.discipline_model import Discipline
        from src.uni.models.study_model import Study
        from src.uni.models.study_discipline_model import StudyDiscipline

        # from src.uni.models.studies_study_discipline_model import StudiesStudyDiscipline

        self.Base.metadata.create_all(bind=self.engine)

        # app.teardown_request(self.remove_session)

    # @app.teardown_appcontext
    # def shutdown_session(exception=None):
    #    self.session.remove()
