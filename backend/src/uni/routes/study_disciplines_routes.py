"""Study disciplines routes in the WroclawPortal API.  Used for retrieving, adding, updating, and deleting study disciplines ."""
from flask_restful import Api, Resource, fields, marshal_with, reqparse
from flask import Response, request
from flask.json import jsonify
from src.uni.dao.study_disciplines_dao import StudyDisciplineDao


# from flask_jwt_extended import jwt_required
from src.uni.models.study_discipline_model import (
    StudyDiscipline,
    StudyDisciplineSchema,
    study_discipline_schema,
    study_disciplines_schema,
)

resource_fields = {
    "study_discipline_id": fields.Integer,
    "study_discipline_name": fields.String,
}


class StudyDisciplineIdApi(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument(
    #    "price", type=float, required=True, help="This field cannot be left blank!"
    # )

    def get(self, study_discipline_id):
        """
        Get a single study discipline with a unique ID.
        :param study_discipline_id: The unique identifier for a study discipline.
        :return: A response object for the GET API request.
        """
        study_discipline = StudyDisciplineDao.get_study_discipline_by_id(
            study_discipline_id=study_discipline_id
        )

        if study_discipline is None:
            response = jsonify(
                {
                    "self": f"/study_disciplines/{study_discipline_id}",
                    "study_discipline": None,
                    # "log": None,
                    "error": "there is no study_discipline with this identifier",
                }
            )
            response.status_code = 400
            return response
        else:
            study_disciplines_dict: dict = StudyDiscipline(study_discipline).__dict__
            # comment_dict["time"] = str(comment_dict["time"])

            response = jsonify(
                {
                    "self": f"/study_disciplines/{study_discipline_id}",
                    "study_discipline": study_disciplines_dict,
                    # "log": f'/v2/logs/{comment_dict.get("log_id")}',
                }
            )
            # response.status_code = 200
            # return response
            return Response(response, mimetype="application/json", status=200)

        # voivodeship = Voivodeship.objects.get(id=id).to_json()
        # return Response(voivodeship, mimetype="application/json", status=200)

    def put(self, study_discipline_id):
        """
        Update an existing study discipline.
        :param study_discipline_id: The unique identifier for a study discipline.
        :return: A response object for the PUT API request.
        """
        old_study_discipline: StudyDiscipline = (
            StudyDisciplineDao.get_study_discipline_by_id(
                study_discipline_id=study_discipline_id
            )
        )

        if old_study_discipline is None:
            response = jsonify(
                {
                    "self": f"/study_disciplines/{study_discipline_id}",
                    "updated": False,
                    "study_discipline": None,
                    "error": "there is no existing study_discipline with this id",
                }
            )
            # response.status_code = 400
            # return response
            return Response(response, mimetype="application/json", status=400)

        study_discipline_data: dict = request.get_json()
        new_study_discipline = StudyDiscipline(study_discipline_data)

        if old_study_discipline != new_study_discipline:

            is_updated = StudyDisciplineDao.update_study_discipline(
                study_discipline=new_study_discipline
            )

            if is_updated:
                updated_study_discipline: StudyDiscipline = (
                    StudyDisciplineDao.get_study_discipline_by_id(
                        study_discipline_id=new_study_discipline.study_discipline_id
                    )
                )
                updated_study_discipline_dict: dict = StudyDiscipline(
                    updated_study_discipline
                ).__dict__

                response = jsonify(
                    {
                        "self": f"/study_disciplines/{study_discipline_id}",
                        "updated": True,
                        "study_discipline": updated_study_discipline_dict,
                    }
                )
                # response.status_code = 200
                # return response
                return Response(response, mimetype="application/json", status=200)
            else:
                response = jsonify(
                    {
                        "self": f"/study_disciplines/{study_discipline_id}",
                        "updated": False,
                        "study_discipline": None,
                        "error": "the study_discipline failed to update",
                    }
                )
                # response.status_code = 500
                # return response
                return Response(response, mimetype="application/json", status=500)
        else:
            response = jsonify(
                {
                    "self": f"/study_disciplines/{study_discipline_id}",
                    "updated": False,
                    "study_discipline": None,
                    "error": "the study_discipline submitted is equal to the existing study_discipline with the same id",
                }
            )
            # response.status_code = 400
            # return response
            return Response(response, mimetype="application/json", status=400)

        # body = request.get_json()
        # Voivodeship.objects.get(id=id).update(**body)
        # return "", 200

    def delete(self, study_discipline_id):
        """
        Delete an existing study_discipline.
        :param study_discipline_id: The unique identifier for a study_discipline.
        :return: A response object for the DELETE API request.
        """
        existing_study_discipline: StudyDiscipline = (
            StudyDisciplineDao.get_study_discipline_by_id(
                study_discipline_id=study_discipline_id
            )
        )

        if existing_study_discipline is None:
            response = jsonify(
                {
                    "self": f"/study_disciplines/{study_discipline_id}",
                    "deleted": False,
                    "error": "there is no existing study_disciplines with this id",
                }
            )
            # response.status_code = 400
            # return response
            return Response(response, mimetype="application/json", status=400)

        is_deleted = StudyDisciplineDao.delete_study_discipline(
            study_discipline_id=study_discipline_id
        )

        if is_deleted:
            response = jsonify(
                {
                    "self": f"/study_disciplines/{study_discipline_id}",
                    "deleted": True,
                }
            )
            # response.status_code = 204
            # return response
            return Response(response, mimetype="application/json", status=204)
        else:
            response = jsonify(
                {
                    "self": f"/study_disciplines/{study_discipline_id}",
                    "deleted": False,
                    "error": "failed to delete the study_discipline",
                }
            )
            # response.status_code = 500
            # return response
            return Response(response, mimetype="application/json", status=500)

        # voivodeship = Voivodeship.objects.get(id=id).delete()
        # return "", 200


class StudyDisciplineNameApi(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument(
    #    "price", type=float, required=True, help="This field cannot be left blank!"
    # )

    # @jwt_required()
    def get(self, study_discipline_name):
        "get study discipline by name"
        # voivodeship = Voivodeship.objects.get(name=name).to_json()
        # if voivodeship:
        #     return Response(voivodeship, mimetype="application/json", status=200)
        # return {"message": "Uni not found"}, 404
        study_discipline = StudyDisciplineDao.get_study_discipline_by_name(
            study_discipline_name=study_discipline_name
        ).to_json()
        return Response(study_discipline, mimetype="application/json", status=200)

    def put(self, study_discipline_name):
        # data = Uni.parser.parse_args()
        # voivodeship = Voivodeship.objects.get(name=name)
        # if voivodeship is None:
        #    voivodeship = voivodeship(name, data["terc"])
        # else:
        #    voivodeship.terc = data["terc"]
        # voivodeship.save_to_db()

        body = request.get_json()
        StudyDisciplineDao.get_study_discipline_by_name(
            study_discipline_name=study_discipline_name
        ).update(**body)
        return "", 200

    def delete(self, study_discipline_name):
        # voivodeship = Voivodeship.objects.get(name=name)
        # if voivodeship:
        #    voivodeship.delete()
        # return {"message": "Uni deleted"}

        study_discipline = StudyDisciplineDao.get_study_discipline_by_name(
            study_discipline_name=study_discipline_name
        ).delete()
        return "", 200


class StudyDisciplinesApi(Resource):
    @marshal_with(resource_fields)
    def get(self):
        """
        Get all the study disciplines in the database.
        :return: A response object for the GET API request.
        """
        study_disciplines: list = StudyDisciplineDao.get_study_disciplines()
        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        print(type(study_disciplines))
        print(study_disciplines)
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
        res = study_disciplines_schema.dump(study_disciplines)
        print(res)

        # return study_disciplines_schema.dump(study_disciplines)
        # return jsonify(study_disciplines)
        # return {"a": "1", "b": "2"}
        return study_disciplines

    def post(self):

        """
        Create a new study discipline.
        :return: A response object for the POST API request.
        """
        study_discipline_data: dict = request.get_json()

        if study_discipline_data is None:
            response = jsonify(
                {
                    "self": f"/study_disciplines",
                    "added": False,
                    "study_discipline": None,
                    "error": "the request body isn't populated",
                }
            )
            response.status_code = 400
            return response
        study_discipline_to_add = StudyDiscipline(study_discipline_data)

        study_discipline_added_successfully: bool = (
            StudyDisciplineDao.add_study_discipline(
                new_study_discipline=study_discipline_to_add
            )
        )

        if study_discipline_added_successfully:
            study_discipline_added = StudyDisciplineDao.get_study_discipline_by_id(
                study_discipline_to_add.study_discipline_id
            )
            study_discipline_added_dict: dict = StudyDiscipline(
                study_discipline_added
            ).__dict__

            response = jsonify(
                {
                    "self": "/study_disciplines",
                    "added": True,
                    "study_discipline": study_discipline_added_dict,
                }
            )
            response.status_code = 200
            return response
        else:
            response = jsonify(
                {
                    "self": "/study_disciplines",
                    "added": False,
                    "study_discipline": None,
                    "error": "failed to create a new study discipline",
                }
            )
            response.status_code = 500
            return response

        # body = request.get_json()
        # voivodeship = Voivodeship(**body).save()
        # id = voivodeship.id
        # return {"id": str(id)}, 200
