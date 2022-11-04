"""study_discipines data access from the database.  Contains SQL queries related to study_disciplines."""
from typing import List

# from src.__init__ import db
from src import db

# from src impor app
from src.uni.dao.basic_dao import BasicDao
from src.uni.models.study_discipline_model import StudyDiscipline


class StudyDisciplineDao:
    # engine = db.get_engine(app=app, bind="app")

    @staticmethod
    def get_study_disciplines() -> List[StudyDiscipline]:
        """
        Get a list of all the study_disciplines in the database.
        :return: A list containing StudyDiscipline model objects.
        """
        # return StudyDiscipline.query.filter.all()
        return StudyDiscipline.query.order_by(
            StudyDiscipline.study_discipline_name
        ).all()
        # return db.session.query(StudyDiscipline).all()

    @staticmethod
    def get_study_discipline_by_name(study_discipline_name: str) -> StudyDiscipline:
        """
        Get a single study discipline from the database based on their name.
        :param study_discipline_name: Study discipline name
        :return: The result of the database query.
        """
        return (
            StudyDiscipline.query.filter_by(study_discipline_name=study_discipline_name)
            # .options(defer("profilepic"), defer("profilepic_name"))
            .first()
        )

    @staticmethod
    def get_study_discipline_by_id(study_discipline_id: str) -> StudyDiscipline:
        """
        Get a single study discipline from the database based on their id.
        :param id: Id which uniquely identifies the study discipline.
        :return: The result of the database query.
        """
        return (
            StudyDiscipline.query.filter_by(study_discipline_name=study_discipline_name)
            # .options(defer("profilepic"), defer("profilepic_name"))
            .first()
        )

    @staticmethod
    def add_study_discipline(study_discipline: StudyDiscipline) -> bool:
        """
        Add a study discipline.
        :param study_discipline: Object representing a study discipline for the application.
        :return: True if the study discipline is inserted into the database, False otherwise.
        """
        db.session.add(study_discipline)
        return BasicDao.safe_commit()

    @staticmethod
    def update_study_discipline(
        study_discipline_id: int, study_discipline: StudyDiscipline
    ) -> bool:
        """
        Update a study discipline in the database.
        :param study_discipline_id: Study discipline id which uniquely identifies the study discipline.
        :param study_discipline: Object representing an updated study discipline for the application.
        :return: True if the study discipline is updated in the database, False otherwise.
        """
        db.session.execute(
            """
            UPDATE study_disciplines SET 
                study_discipline_name=:study_discipline_name, 
              
            WHERE study_discipline_id=:study_discipline_id
            """,
            {
                "study_discipline_name": study_discipline.study_discipline_name,
            },
            # bind=UniDao.engine,
        )
        return BasicDao.safe_commit()

    @staticmethod
    def delete_study_discipline(study_discipline_id: int) -> bool:
        """
        Delete a study discipline from the database based on its id.
        :param study_discipline_id: Study discipline id which uniquely identifies the study discipline
        :return: True if the deletion was successful without error, False otherwise.
        """
        db.session.execute(
            "DELETE FROM study_disciplines WHERE study_discipline_id=:study_discipline_id",
            {"study_discipline_id": study_discipline_id},
            # bind=UniDao.engine,
        )

        return BasicDao.safe_commit()
