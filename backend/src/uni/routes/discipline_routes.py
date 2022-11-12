"""Voivodeship routes in the WroclawPortal API.  Used for retrieving, adding, updating, and deleting voivodeships ."""
from flask_restful import Resource, fields, marshal_with
from flask import Response, request
from flask.json import jsonify
from src.uni.dao.discipline_dao import DisciplineDao

# from flask_jwt_extended import jwt_required
from src.uni.models.discipline_model import (
    Discipline,
    DisciplineSchema,
    discipline_schema,
    disciplines_schema,
)

resource_fields = {"discipline_id": fields.String, "discipline_name": fields.String}


class DisciplineIdApi(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument(
    #    "price", type=float, required=True, help="This field cannot be left blank!"
    # )

    def get(self, disc_id):
        """
        Get a single discipline with a unique ID.
        :param disc_id: The unique identifier for a discipline.
        :return: A response object for the GET API request.
        """
        discipline = DisciplineDao.get_discipline_by_id(disc_id=disc_id)

        if discipline is None:
            response = jsonify(
                {
                    "self": f"/disciplines/{disc_id}",
                    "discipline": None,
                    # "log": None,
                    "error": "there is no discipline with this identifier",
                }
            )
            response.status_code = 400
            return response
        else:
            discipline_dict: dict = Discipline(discipline).__dict__
            # comment_dict["time"] = str(comment_dict["time"])

            response = jsonify(
                {
                    "self": f"/disciplines/{disc_id}",
                    "discipline": discipline_dict,
                    # "log": f'/v2/logs/{comment_dict.get("log_id")}',
                }
            )
            # response.status_code = 200
            # return response
            return Response(response, mimetype="application/json", status=200)

        # voivodeship = Voivodeship.objects.get(id=id).to_json()
        # return Response(voivodeship, mimetype="application/json", status=200)

    def put(self, disc_id):
        """
        Update an existing discipline.
        :param disc_id: The unique identifier for a discipline.
        :return: A response object for the PUT API request.
        """
        old_discipline: Discipline = DisciplineDao.get_discipline_by_id(disc_id=disc_id)

        if old_discipline is None:
            response = jsonify(
                {
                    "self": f"/disciplines/{disc_id}",
                    "updated": False,
                    "discipline": None,
                    "error": "there is no existing discipline with this id",
                }
            )
            # response.status_code = 400
            # return response
            return Response(response, mimetype="application/json", status=400)

        discipline_data: dict = request.get_json()
        new_discipline = Discipline(discipline_data)

        if old_discipline != new_discipline:

            is_updated = DisciplineDao.update_discipline(discipline=new_discipline)

            if is_updated:
                updated_discipline: Discipline = DisciplineDao.get_discipline_by_id(
                    disc_id=new_discipline.discipline_id
                )
                updated_discipline_dict: dict = Discipline(updated_discipline).__dict__

                response = jsonify(
                    {
                        "self": f"/disciplines/{disc_id}",
                        "updated": True,
                        "discipline": updated_discipline_dict,
                    }
                )
                # response.status_code = 200
                # return response
                return Response(response, mimetype="application/json", status=200)
            else:
                response = jsonify(
                    {
                        "self": f"/disciplines/{disc_id}",
                        "updated": False,
                        "discipline": None,
                        "error": "the discipline failed to update",
                    }
                )
                # response.status_code = 500
                # return response
                return Response(response, mimetype="application/json", status=500)
        else:
            response = jsonify(
                {
                    "self": f"/disciplines/{disc_id}",
                    "updated": False,
                    "discipline": None,
                    "error": "the discipline submitted is equal to the existing discipline with the same id",
                }
            )
            # response.status_code = 400
            # return response
            return Response(response, mimetype="application/json", status=400)

        # body = request.get_json()
        # Voivodeship.objects.get(id=id).update(**body)
        # return "", 200

    def delete(self, disc_id):
        """
        Delete an existing discipline.
        :param disc_id: The unique identifier for a discipline.
        :return: A response object for the DELETE API request.
        """
        existing_discipline: Discipline = DisciplineDao.get_discipline_by_id(
            disc_id=disc_id
        )

        if existing_discipline is None:
            response = jsonify(
                {
                    "self": f"/disciplines/{disc_id}",
                    "deleted": False,
                    "error": "there is no existing discipline with this id",
                }
            )
            # response.status_code = 400
            # return response
            return Response(response, mimetype="application/json", status=400)

        is_deleted = DisciplineDao.delete_discipline_by_id(disc_id=disc_id)

        if is_deleted:
            response = jsonify(
                {
                    "self": f"/disciplines/{disc_id}",
                    "deleted": True,
                }
            )
            # response.status_code = 204
            # return response
            return Response(response, mimetype="application/json", status=204)
        else:
            response = jsonify(
                {
                    "self": f"/disciplines/{disc_id}",
                    "deleted": False,
                    "error": "failed to delete the discipline",
                }
            )
            # response.status_code = 500
            # return response
            return Response(response, mimetype="application/json", status=500)

        # voivodeship = Voivodeship.objects.get(id=id).delete()
        # return "", 200


class DisciplineNameApi(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument(
    #    "price", type=float, required=True, help="This field cannot be left blank!"
    # )

    # @jwt_required()
    def get(self, name):
        "get discipline by name"
        # voivodeship = Voivodeship.objects.get(name=name).to_json()
        # if voivodeship:
        #     return Response(voivodeship, mimetype="application/json", status=200)
        # return {"message": "Uni not found"}, 404
        discipline = Discipline.objects.get(name=name).to_json()
        return Response(discipline, mimetype="application/json", status=200)

    def put(self, name):
        # data = Uni.parser.parse_args()
        # voivodeship = Voivodeship.objects.get(name=name)
        # if voivodeship is None:
        #    voivodeship = voivodeship(name, data["terc"])
        # else:
        #    voivodeship.terc = data["terc"]
        # voivodeship.save_to_db()

        body = request.get_json()
        Discipline.objects.get(name=name).update(**body)
        return "", 200

    def delete(self, name):
        # voivodeship = Voivodeship.objects.get(name=name)
        # if voivodeship:
        #    voivodeship.delete()
        # return {"message": "Uni deleted"}

        discipline = Discipline.objects.get(name=name).delete()
        return "", 200


class DisciplinesApi(Resource):
    # comments: list = CommentDao.get_comments()
    @marshal_with(resource_fields)
    def get(self):
        """
        Get all the disciplines in the database.
        :return: A response object for the GET API request.
        """
        disciplines: list = DisciplineDao.get_disciplines()

        return disciplines
        """
        if disciplines is None:
            response = jsonify(
                {
                    "self": "/disciplines",
                    "disciplines": None,
                    "error": "an unexpected error occurred retrieving disciplines",
                }
            )
            
            return Response(response, mimetype="application/json", status=500)
        else:
            disc_dicts = [Discipline(disc).__dict__ for disc in disciplines]

            # for voiv_dict in voiv_dicts:
            #    voiv_dict["log"] = f'/v2/logs/{comment_dict.get("log_id")}'

            response = jsonify({"self": "/disciplines", "disciplines": disc_dicts})
            
            return Response(response, mimetype="application/json", status=200)
        """

    # def get(self):
    #    "get voivodeship list"
    #    voivodeships = Voivodeship.objects().to_json()
    #    return Response(voivodeships, mimetype="application/json", status=200)

    def post(self):
        # if Voivodeship.objects.get(name=name):
        #    return {
        #        "message": "A voivodeship with name '{} already exists.".format(name)
        #    }, 400

        # data = Uni.parser.parse_args()

        # uni = UniModel(name, data["price"])

        # try:
        #    uni.save_to_db()
        # except:
        #    return {"message": "An error occured inserting the item"}, 500

        # return uni.json(), 201
        """
        Create a new discipline.
        :return: A response object for the POST API request.
        """
        discipline_data: dict = request.get_json()

        if discipline_data is None:
            response = jsonify(
                {
                    "self": f"/disciplines",
                    "added": False,
                    "discipline": None,
                    "error": "the request body isn't populated",
                }
            )
            response.status_code = 400
            return response
        discipline_to_add = Discipline(discipline_data)

        discipline_added_successfully: bool = DisciplineDao.add_discipline(
            new_disc=discipline_to_add
        )

        if discipline_added_successfully:
            discipline_added = DisciplineDao.get_discipline_by_id(
                discipline_to_add.voiv_id
            )
            discipline_added_dict: dict = Discipline(discipline_added).__dict__

            response = jsonify(
                {
                    "self": "/disciplines",
                    "added": True,
                    "discipline": discipline_added_dict,
                }
            )
            response.status_code = 200
            return response
        else:
            response = jsonify(
                {
                    "self": "/disciplines",
                    "added": False,
                    "discipline": None,
                    "error": "failed to create a new discipline",
                }
            )
            response.status_code = 500
            return response

        # body = request.get_json()
        # voivodeship = Voivodeship(**body).save()
        # id = voivodeship.id
        # return {"id": str(id)}, 200
