"""Voivodeship routes in the WroclawPortal API.  Used for retrieving, adding, updating, and deleting voivodeships ."""
from flask_restful import Resource, fields, marshal_with
from flask import Response, request
from flask.json import jsonify
from src.uni.dao.level_dao import CourseLevelDao

# from flask_jwt_extended import jwt_required
from src.uni.models.course_level_model import (
    CourseLevel,
    CourseLevelSchema,
    course_level_schema,
    course_levels_schema,
)

resource_fields = {
    "course_level_id": fields.Integer,
    "course_level_name": fields.String,
}


class CourseLevelIdApi(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument(
    #    "price", type=float, required=True, help="This field cannot be left blank!"
    # )

    def get(self, level_id):
        """
        Get a single level with a unique ID.
        :param level_id: The unique identifier for a level.
        :return: A response object for the GET API request.
        """
        level = CourseLevelDao.get_level_by_id(level_id=level_id)

        if level is None:
            response = jsonify(
                {
                    "self": f"/levels/{level_id}",
                    "level": None,
                    # "log": None,
                    "error": "there is no level with this identifier",
                }
            )
            response.status_code = 400
            return response
        else:
            level_dict: dict = CourseLevel(level).__dict__
            # comment_dict["time"] = str(comment_dict["time"])

            response = jsonify(
                {
                    "self": f"/levels/{level_id}",
                    "level": level_dict,
                    # "log": f'/v2/logs/{comment_dict.get("log_id")}',
                }
            )
            # response.status_code = 200
            # return response
            return Response(response, mimetype="application/json", status=200)

        # voivodeship = Voivodeship.objects.get(id=id).to_json()
        # return Response(voivodeship, mimetype="application/json", status=200)

    def put(self, level_id):
        """
        Update an existing level.
        :param level_id: The unique identifier for a level.
        :return: A response object for the PUT API request.
        """
        old_level: CourseLevel = CourseLevelDao.get_level_by_id(level_id=level_id)

        if old_level is None:
            response = jsonify(
                {
                    "self": f"/levels/{level_id}",
                    "updated": False,
                    "level": None,
                    "error": "there is no existing level with this id",
                }
            )
            # response.status_code = 400
            # return response
            return Response(response, mimetype="application/json", status=400)

        level_data: dict = request.get_json()
        new_level = CourseLevel(level_data)

        if old_level != new_level:

            is_updated = CourseLevelDao.update_level(level=new_level)

            if is_updated:
                updated_level: CourseLevel = CourseLevelDao.get_level_by_id(
                    level_id=new_level.course_level_id
                )
                updated_level_dict: dict = CourseLevel(updated_level).__dict__

                response = jsonify(
                    {
                        "self": f"/levels/{level_id}",
                        "updated": True,
                        "level": updated_level_dict,
                    }
                )
                # response.status_code = 200
                # return response
                return Response(response, mimetype="application/json", status=200)
            else:
                response = jsonify(
                    {
                        "self": f"/levels/{level_id}",
                        "updated": False,
                        "level": None,
                        "error": "the level failed to update",
                    }
                )
                # response.status_code = 500
                # return response
                return Response(response, mimetype="application/json", status=500)
        else:
            response = jsonify(
                {
                    "self": f"/levels/{level_id}",
                    "updated": False,
                    "level": None,
                    "error": "the level submitted is equal to the existing level with the same id",
                }
            )
            # response.status_code = 400
            # return response
            return Response(response, mimetype="application/json", status=400)

        # body = request.get_json()
        # Voivodeship.objects.get(id=id).update(**body)
        # return "", 200

    def delete(self, level_id):
        """
        Delete an existing level.
        :param level_id: The unique identifier for a level.
        :return: A response object for the DELETE API request.
        """
        existing_level: CourseLevel = CourseLevelDao.get_level_by_id(level_id=level_id)

        if existing_level is None:
            response = jsonify(
                {
                    "self": f"/levels/{level_id}",
                    "deleted": False,
                    "error": "there is no existing level with this id",
                }
            )
            # response.status_code = 400
            # return response
            return Response(response, mimetype="application/json", status=400)

        is_deleted = CourseLevelDao.delete_level_by_id(level_id=level_id)

        if is_deleted:
            response = jsonify(
                {
                    "self": f"/levels/{level_id}",
                    "deleted": True,
                }
            )
            # response.status_code = 204
            # return response
            return Response(response, mimetype="application/json", status=204)
        else:
            response = jsonify(
                {
                    "self": f"/levels/{level_id}",
                    "deleted": False,
                    "error": "failed to delete the levele",
                }
            )
            # response.status_code = 500
            # return response
            return Response(response, mimetype="application/json", status=500)

        # voivodeship = Voivodeship.objects.get(id=id).delete()
        # return "", 200


class CourseLevelNameApi(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument(
    #    "price", type=float, required=True, help="This field cannot be left blank!"
    # )

    # @jwt_required()
    def get(self, name):
        "get level by name"
        # voivodeship = Voivodeship.objects.get(name=name).to_json()
        # if voivodeship:
        #     return Response(voivodeship, mimetype="application/json", status=200)
        # return {"message": "Uni not found"}, 404
        level = CourseLevel.objects.get(name=name).to_json()
        return Response(level, mimetype="application/json", status=200)

    def put(self, name):
        # data = Uni.parser.parse_args()
        # voivodeship = Voivodeship.objects.get(name=name)
        # if voivodeship is None:
        #    voivodeship = voivodeship(name, data["terc"])
        # else:
        #    voivodeship.terc = data["terc"]
        # voivodeship.save_to_db()

        body = request.get_json()
        CourseLevel.objects.get(name=name).update(**body)
        return "", 200

    def delete(self, name):
        # voivodeship = Voivodeship.objects.get(name=name)
        # if voivodeship:
        #    voivodeship.delete()
        # return {"message": "Uni deleted"}

        level = CourseLevel.objects.get(name=name).delete()
        return "", 200


class CourseLevelsApi(Resource):
    # comments: list = CommentDao.get_comments()
    @marshal_with(resource_fields)
    def get(self):
        """
        Get all the levels in the database.
        :return: A response object for the GET API request.
        """
        levels: list = CourseLevelDao.get_levels()

        # res = course_levels_schema.dump(levels)
        # print(res)

        return levels
        """
        if levels is None:
            response = jsonify(
                {
                    "self": "/levels",
                    "levels": None,
                    "error": "an unexpected error occurred retrieving levels",
                }
            )

            return Response(response, mimetype="application/json", status=500)
        else:
            level_dicts = [CourseLevel(level).__dict__ for level in levels]

            # for voiv_dict in voiv_dicts:
            #    voiv_dict["log"] = f'/v2/logs/{comment_dict.get("log_id")}'

            response = jsonify({"self": "/levels", "levels": level_dicts})

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
        Create a new level.
        :return: A response object for the POST API request.
        """
        level_data: dict = request.get_json()

        if level_data is None:
            response = jsonify(
                {
                    "self": f"/levels",
                    "added": False,
                    "level": None,
                    "error": "the request body isn't populated",
                }
            )
            response.status_code = 400
            return response
        level_to_add = CourseLevel(level_data)

        level_added_successfully: bool = CourseLevelDao.add_level(
            new_level=level_to_add
        )

        if level_added_successfully:
            level_added = CourseLevelDao.get_level_by_id(level_to_add.course_level_id)
            level_added_dict: dict = CourseLevel(level_added).__dict__

            response = jsonify(
                {
                    "self": "/levels",
                    "added": True,
                    "level": level_added_dict,
                }
            )
            response.status_code = 200
            return response
        else:
            response = jsonify(
                {
                    "self": "/levels",
                    "added": False,
                    "levele": None,
                    "error": "failed to create a new level",
                }
            )
            response.status_code = 500
            return response

        # body = request.get_json()
        # voivodeship = Voivodeship(**body).save()
        # id = voivodeship.id
        # return {"id": str(id)}, 200
