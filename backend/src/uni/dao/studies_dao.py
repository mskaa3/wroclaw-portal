"""studies data access from the database.  Contains SQL queries related to studies."""
from typing import List

# from src.__init__ import db
from src import db

# from sqlalchemy import Integer, String

# from src impor app
from src.uni.dao.basic_dao import BasicDao
from src.uni.models.study_model import Study


class StudiesDao:
    # engine = db.get_engine(app=app, bind="app")

    @staticmethod
    def get_studies() -> List[Study]:
        """
        Get a list of all the studies in the database.
        :return: A list containing Study model objects.
        """

        return Study.query.order_by(Study.study_name).all()
        # return db.session.query(StudyDiscipline).all()

    @staticmethod
    def get_studies_by_name(study_name: str) -> List[Study]:
        """
        Get a list of all the studies from the database based on their name.
        :param study_name: Study name
        :return: The result of the database query.
        """
        return (
            Study.query.filter_by(study_name=study_name)
            # .options(defer("profilepic"), defer("profilepic_name"))
            .all()
        )

    @staticmethod
    def get_study_by_id(study_id: str) -> Study:
        """
        Get a single study from the database based on their id.
        :param id: Id which uniquely identifies the study.
        :return: The result of the database query.
        """
        return (
            Study.query.filter_by(study_name=study_name)
            # .options(defer("profilepic"), defer("profilepic_name"))
            .first()
        )

    @staticmethod
    def add_study(study: Study) -> bool:
        """
        Add a study.
        :param study: Object representing a study for the application.
        :return: True if the study is inserted into the database, False otherwise.
        """
        db.session.add(study)
        return BasicDao.safe_commit()

    @staticmethod
    def update_study(study_id: int, study: Study) -> bool:
        """
        Update a study in the database.
        :param study_id: Study id which uniquely identifies the study.
        :param study: Object representing an updated study for the application.
        :return: True if the study is updated in the database, False otherwise.
        """
        db.session.execute(
            """
            UPDATE studies SET 
                study_name=:study_name, 
              
            WHERE study_id=:study_id
            """,
            {
                "study_name": study.study_name,
            },
            # bind=UniDao.engine,
        )
        return BasicDao.safe_commit()

    @staticmethod
    def delete_study(study_id: int) -> bool:
        """
        Delete a study from the database based on its id.
        :param study_id: Study id which uniquely identifies the study.
        :return: True if the deletion was successful without error, False otherwise.
        """
        db.session.execute(
            "DELETE FROM studies WHERE study_id=:study_id",
            {"study_id": study_id},
            # bind=UniDao.engine,
        )

        return BasicDao.safe_commit()

    @staticmethod
    def get_levels() -> List[str]:
        """
        Get a list of all the levels of study in the database.
        :return: A list containing all levels.
        """
        # return StudyDiscipline.query.filter.all()
        # return Study.query(Study.level).distinct().order_by(Study.level).all()
        return Study.query.with_entities(Study.level).distinct().all()
