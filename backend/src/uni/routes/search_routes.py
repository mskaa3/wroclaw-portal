"""Voivodeship routes in the WroclawPortal API.  Used for retrieving, adding, updating, and deleting voivodeships ."""
from flask_restful import Api, Resource, fields, marshal_with, reqparse
from flask import Response, request
from flask.json import jsonify
from src.uni.dao.studies_dao import StudiesDao


# from flask_jwt_extended import jwt_required
from src.uni.models.study_model import (
    Study,
    StudySchema,
    LevelsSchema,
    study_schema,
    studies_schema,
    levels_schema,
)

resource_fields = {
    "study_id": fields.Integer,
    "study_uid": fields.String,
    "study_name": fields.String,
    "course_id": fields.String,
    "level": fields.String,
    "profile": fields.String,
    "title": fields.String,
    "forms": fields.String,
    "main_discipline": fields.String,
    "institutions": fields.String,
}


class StudyIdApi(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument(
    #    "price", type=float, required=True, help="This field cannot be left blank!"
    # )

    def get(self, study_id):
        """
        Get a single study with a unique ID.
        :param study_id: The unique identifier for a study.
        :return: A response object for the GET API request.
        """
        study = StudiesDao.get_study_by_id(study_id=study_id)

        if study is None:
            response = jsonify(
                {
                    "self": f"/studies/{study_id}",
                    "study": None,
                    # "log": None,
                    "error": "there is no study with this identifier",
                }
            )
            response.status_code = 400
            return response
        else:
            study_dict: dict = Study(study).__dict__
            # comment_dict["time"] = str(comment_dict["time"])

            response = jsonify(
                {
                    "self": f"/studies/{study_id}",
                    "study": study_dict,
                    # "log": f'/v2/logs/{comment_dict.get("log_id")}',
                }
            )
            # response.status_code = 200
            # return response
            return Response(response, mimetype="application/json", status=200)

        # voivodeship = Voivodeship.objects.get(id=id).to_json()
        # return Response(voivodeship, mimetype="application/json", status=200)

    def put(self, study_id):
        """
        Update an existing study.
        :param study_id: The unique identifier for a study.
        :return: A response object for the PUT API request.
        """
        old_study: Study = StudiesDao.get_study_by_id(study_id=study_id)

        if old_study is None:
            response = jsonify(
                {
                    "self": f"/studies/{study_id}",
                    "updated": False,
                    "study": None,
                    "error": "there is no existing study with this id",
                }
            )
            # response.status_code = 400
            # return response
            return Response(response, mimetype="application/json", status=400)

        study_data: dict = request.get_json()
        new_study = Study(study_data)

        if old_study != new_study:

            is_updated = StudiesDao.update_study(study=new_study)

            if is_updated:
                updated_study: Study = StudiesDao.get_study_by_id(
                    study_id=new_study.study_id
                )
                updated_study_dict: dict = Study(updated_study).__dict__

                response = jsonify(
                    {
                        "self": f"/studies/{study_id}",
                        "updated": True,
                        "study": updated_study_dict,
                    }
                )
                # response.status_code = 200
                # return response
                return Response(response, mimetype="application/json", status=200)
            else:
                response = jsonify(
                    {
                        "self": f"/studies/{study_id}",
                        "updated": False,
                        "study": None,
                        "error": "the study failed to update",
                    }
                )
                # response.status_code = 500
                # return response
                return Response(response, mimetype="application/json", status=500)
        else:
            response = jsonify(
                {
                    "self": f"/studies/{study_id}",
                    "updated": False,
                    "study": None,
                    "error": "the study submitted is equal to the existing study with the same id",
                }
            )
            # response.status_code = 400
            # return response
            return Response(response, mimetype="application/json", status=400)

        # body = request.get_json()
        # Voivodeship.objects.get(id=id).update(**body)
        # return "", 200

    def delete(self, study_id):
        """
        Delete an existing study.
        :param study_id: The unique identifier for a study.
        :return: A response object for the DELETE API request.
        """
        existing_study: Study = StudiesDao.get_study_by_id(study_id=study_id)

        if existing_study is None:
            response = jsonify(
                {
                    "self": f"/studies/{study_id}",
                    "deleted": False,
                    "error": "there is no existing study with this id",
                }
            )
            # response.status_code = 400
            # return response
            return Response(response, mimetype="application/json", status=400)

        is_deleted = StudiesDao.delete_study(study_id=study_id)

        if is_deleted:
            response = jsonify(
                {
                    "self": f"/studies/{study_id}",
                    "deleted": True,
                }
            )
            # response.status_code = 204
            # return response
            return Response(response, mimetype="application/json", status=204)
        else:
            response = jsonify(
                {
                    "self": f"/studies/{study_id}",
                    "deleted": False,
                    "error": "failed to delete the study",
                }
            )
            # response.status_code = 500
            # return response
            return Response(response, mimetype="application/json", status=500)

        # voivodeship = Voivodeship.objects.get(id=id).delete()
        # return "", 200


class StudyNameApi(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument(
    #    "price", type=float, required=True, help="This field cannot be left blank!"
    # )

    # @jwt_required()
    def get(self, study_name):
        "get studies by name"
        # voivodeship = Voivodeship.objects.get(name=name).to_json()
        # if voivodeship:
        #     return Response(voivodeship, mimetype="application/json", status=200)
        # return {"message": "Uni not found"}, 404
        studies = StudiesDao.get_studies_by_name(study_name=study_name).to_json()
        return Response(studies, mimetype="application/json", status=200)

    def put(self, study_name):

        body = request.get_json()
        StudiesDao.get_studies_by_name(study_name=study_name).update(**body)
        return "", 200

    def delete(self, study_name):

        studies = StudiesDao.get_studies_by_name(study_name=study_name).delete()
        return "", 200


class StudiesApi(Resource):
    @marshal_with(resource_fields)
    def get(self):
        """
        Get all the studies in the database.
        :return: A response object for the GET API request.
        """
        stud: list = StudiesDao.get_studies()
        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        print(type(stud))
        print(stud)
        """
        if study_disciplines is None:
            response = jsonify(
                {
                    "self": "/study_disciplines",
                    "study_disciplines": None,
                    "error": "an unexpected error occurred retrieving study_disciplines",
                }
            )
            # response.status_code = 500
            # return response
            return Response(response, mimetype="application/json", status=500)
        else:
            study_disciplines_dicts = [
                StudyDiscipline(study_disc).__dict__ for study_disc in study_disciplines
            ]

            # for voiv_dict in voiv_dicts:
            #    voiv_dict["log"] = f'/v2/logs/{comment_dict.get("log_id")}'

            response = jsonify(
                {
                    "self": "/study_disciplines",
                    "study_disciplines": study_disciplines_dicts,
                }
            )
            # response.status_code = 200
            # return response
            return Response(response, mimetype="application/json", status=200)
        """
        res = studies_schema.dump(stud)
        print(res)

        # return study_disciplines_schema.dump(study_disciplines)
        # return jsonify(study_disciplines)
        # return {"a": "1", "b": "2"}
        return stud

    def post(self):

        """
        Create a new study.
        :return: A response object for the POST API request.
        """
        study_data: dict = request.get_json()

        if study_data is None:
            response = jsonify(
                {
                    "self": f"/studies",
                    "added": False,
                    "study": None,
                    "error": "the request body isn't populated",
                }
            )
            response.status_code = 400
            return response
        study_to_add = Study(study_data)

        study_added_successfully: bool = StudiesDao.add_study(new_study=study_to_add)

        if study_added_successfully:
            study_added = StudiesDao.get_study_by_id(study_to_add.study_id)
            study_added_dict: dict = Study(study_added).__dict__

            response = jsonify(
                {
                    "self": "/studies",
                    "added": True,
                    "studye": study_added_dict,
                }
            )
            response.status_code = 200
            return response
        else:
            response = jsonify(
                {
                    "self": "/studies",
                    "added": False,
                    "study": None,
                    "error": "failed to create a new study",
                }
            )
            response.status_code = 500
            return response


class StudyLevelsApi(Resource):
    level_fields = {
        "level": fields.String,
    }

    @marshal_with(level_fields)
    def get(self):
        """
        Get all the levels of study in the database.
        :return: A response object for the GET API request.
        """
        levels: list = StudiesDao.get_levels()
        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        print(type(levels))
        print(levels)

        res = levels_schema.dump(levels)
        print(res)

        return levels
