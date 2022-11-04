"""Universities routes in the WroclawPortal API.  Used for retrieving, adding, updating, and deleting universities."""
from flask_restful import Resource, reqparse, fields, marshal_with
from flask.json import jsonify
from flask import Response, request

# from flask_jwt_extended import jwt_required

from src.uni.dao.uni_dao import UniDao

from src.uni.models.uni_model import (
    Uni,
    UniSchema,
    CitiesSchema,
    uni_schema,
    unis_schema,
    cities_schema,
)

resource_fields = {
    "uni_id": fields.Integer,
    "uni_uid": fields.String,
    "uni_name": fields.String,
    "uni_code": fields.String,
    "uni_kind": fields.Integer,
    "www": fields.String,
    "phone_number": fields.String,
    "uni_email": fields.String,
    "city": fields.String,
    "street": fields.String,
    "building": fields.String,
    "postal_code": fields.String,
    "voivodeship": fields.Integer,
}


class UniIdApi(Resource):
    def get(self, uni_id):
        """
        Get a single uni with a unique ID.
        :param uni_id: The unique identifier for a study.
        :return: A response object for the GET API request.
        """
        uni = UniDao.get_uni_by_id(uni_id=uni_id)

        if uni is None:
            response = jsonify(
                {
                    "self": f"/unis/{uni_id}",
                    "uni": None,
                    # "log": None,
                    "error": "there is no university with this identifier",
                }
            )
            response.status_code = 400
            return response
        else:
            uni_dict: dict = Uni(uni).__dict__
            # comment_dict["time"] = str(comment_dict["time"])

            response = jsonify(
                {
                    "self": f"/unis/{uni_id}",
                    "uni": uni_dict,
                    # "log": f'/v2/logs/{comment_dict.get("log_id")}',
                }
            )
            # response.status_code = 200
            # return response
            return Response(response, mimetype="application/json", status=200)

        # voivodeship = Voivodeship.objects.get(id=id).to_json()
        # return Response(voivodeship, mimetype="application/json", status=200)

    def put(self, uni_id):
        """
        Update an existing university.
        :param uni_id: The unique identifier for a university.
        :return: A response object for the PUT API request.
        """
        old_uni: Uni = UniDao.get_uni_by_id(uni_id=uni_id)

        if old_uni is None:
            response = jsonify(
                {
                    "self": f"/unis/{uni_id}",
                    "updated": False,
                    "uni": None,
                    "error": "there is no existing university with this id",
                }
            )
            # response.status_code = 400
            # return response
            return Response(response, mimetype="application/json", status=400)

        uni_data: dict = request.get_json()
        new_uni = Uni(uni_data)

        if old_uni != new_uni:

            is_updated = UniDao.update_uni(uni=new_uni)

            if is_updated:
                updated_uni: Uni = UniDao.get_uni_by_id(uni_id=new_uni.uni_id)
                updated_uni_dict: dict = Uni(updated_uni).__dict__

                response = jsonify(
                    {
                        "self": f"/unis/{uni_id}",
                        "updated": True,
                        "uni": updated_uni_dict,
                    }
                )
                # response.status_code = 200
                # return response
                return Response(response, mimetype="application/json", status=200)
            else:
                response = jsonify(
                    {
                        "self": f"/unis/{uni_id}",
                        "updated": False,
                        "uni": None,
                        "error": "the university failed to update",
                    }
                )
                # response.status_code = 500
                # return response
                return Response(response, mimetype="application/json", status=500)
        else:
            response = jsonify(
                {
                    "self": f"/unis/{uni_id}",
                    "updated": False,
                    "uni": None,
                    "error": "the university submitted is equal to the existing university with the same id",
                }
            )
            # response.status_code = 400
            # return response
            return Response(response, mimetype="application/json", status=400)

        # body = request.get_json()
        # Voivodeship.objects.get(id=id).update(**body)
        # return "", 200

    def delete(self, uni_id):
        """
        Delete an existing university.
        :param uni_id: The unique identifier for a university.
        :return: A response object for the DELETE API request.
        """
        existing_uni: Uni = UniDao.get_Uni_by_id(uni_id=uni_id)

        if existing_uni is None:
            response = jsonify(
                {
                    "self": f"/unis/{uni_id}",
                    "deleted": False,
                    "error": "there is no existing university with this id",
                }
            )
            # response.status_code = 400
            # return response
            return Response(response, mimetype="application/json", status=400)

        is_deleted = UniDao.delete_uni(uni_id=uni_id)

        if is_deleted:
            response = jsonify(
                {
                    "self": f"/unis/{uni_id}",
                    "deleted": True,
                }
            )
            # response.status_code = 204
            # return response
            return Response(response, mimetype="application/json", status=204)
        else:
            response = jsonify(
                {
                    "self": f"/unis/{uni_id}",
                    "deleted": False,
                    "error": "failed to delete the university",
                }
            )
            # response.status_code = 500
            # return response
            return Response(response, mimetype="application/json", status=500)

        # voivodeship = Voivodeship.objects.get(id=id).delete()
        # return "", 200


class UniNameApi(Resource):

    # @jwt_required()
    def get(self, uni_name):
        "get university by name"
        # voivodeship = Voivodeship.objects.get(name=name).to_json()
        # if voivodeship:
        #     return Response(voivodeship, mimetype="application/json", status=200)
        # return {"message": "Uni not found"}, 404
        uni = UniDao.get_uni_by_name(uni_name=uni_name).to_json()
        return Response(uni, mimetype="application/json", status=200)

    def put(self, uni_name):

        body = request.get_json()
        UniDao.get_uni_by_name(uni_name=uni_name).update(**body)
        return "", 200

    def delete(self, uni_name):

        uni = UniDao.get_uni_by_name(uni_name=uni_name).delete()
        return "", 200


class UnisApi(Resource):
    @marshal_with(resource_fields)
    def get(self):
        """
        Get all the universities in the database.
        :return: A response object for the GET API request.
        """
        unis: list = UniDao.get_unis()

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
        res = unis_schema.dump(unis)
        print(res)

        return unis

    def post(self):

        """
        Create a new university.
        :return: A response object for the POST API request.
        """
        uni_data: dict = request.get_json()

        if uni_data is None:
            response = jsonify(
                {
                    "self": f"/unis",
                    "added": False,
                    "uni": None,
                    "error": "the request body isn't populated",
                }
            )
            response.status_code = 400
            return response
        uni_to_add = Uni(uni_data)

        uni_added_successfully: bool = UniDao.add_uni(new_uni=uni_to_add)

        if uni_added_successfully:
            uni_added = UniDao.get_uni_by_id(uni_to_add.uni_id)
            uni_added_dict: dict = Uni(Uni_added).__dict__

            response = jsonify(
                {
                    "self": "/unis",
                    "added": True,
                    "uni": uni_added_dict,
                }
            )
            response.status_code = 200
            return response
        else:
            response = jsonify(
                {
                    "self": "/unis",
                    "added": False,
                    "uni": None,
                    "error": "failed to create a new university",
                }
            )
            response.status_code = 500
            return response


class CitiesApi(Resource):
    city_fields = {
        "city": fields.String,
    }

    @marshal_with(city_fields)
    def get(self):
        """
        Get all the cities of unis in the database.
        :return: A response object for the GET API request.
        """
        cities: list = UniDao.get_cities()
        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        print(cities)
        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        res = cities_schema.dump(cities)
        print(res)

        return cities

    """
        parser = reqparse.RequestParser()
        parser.add_argument(
            "price", type=float, required=True, help="This field cannot be left blank!"
        )

        # @jwt_required()
        def get(self, name):
            uni = Uni.find_by_name(name)
            if uni:
                return uni.json()
            return {"message": "Uni not found"}, 404

        def post(self, name):
            if Uni.find_by_name(name):
                return {"message": "An uni with name '{} already exists.".format(name)}, 400

            data = Uni.parser.parse_args()

            uni = Uni(name, data["price"])

            try:
                uni.save_to_db()
            except:
                return {"message": "An error occured inserting the item"}, 500

            return uni.json(), 201

        def delete(self, name):
            uni = Uni.find_by_name(name)
            if uni:
                uni.delete_from_db()
            return {"message": "Uni deleted"}

        def put(self, name):
            data = Uni.parser.parse_args()

            uni = Uni.find_by_name(name)

            if uni is None:
                uni = Uni(name, data["price"])
            else:
                uni.price = data["price"]

            uni.save_to_db()

            return uni.json()


    class UniList(Resource):
        def get(self):
            return {"unis": list(map(lambda x: x.json(), Uni.query.all()))}
            # return {'unis': [uni.json() for uni in UniModel.query.all()]}"""


"""
@unis.route("/", methods=["POST"])
    # @jwt_required()
    def add_unis():
        # current_user = get_jwt_identity()

        if request.method == "POST":

            body = request.get_json().get("body", "")
            url = request.get_json().get("url", "")

            # if not validators.url(url):
            #    return jsonify({"error": "Enter a valid url"}), HTTP_400_BAD_REQUEST

            if UniModel.query.filter_by(url=url).first():
                return jsonify({"error": "URL already exists"}), HTTP_409_CONFLICT

            bookmark = Bookmark(url=url, body=body, user_id=current_user)
            db.session.add(bookmark)
            db.session.commit()

            return (
                jsonify(
                    {
                        "id": bookmark.id,
                        "url": bookmark.url,
                        "short_url": bookmark.short_url,
                        "visit": bookmark.visits,
                        "body": bookmark.body,
                        "created_at": bookmark.created_at,
                        "updated_at": bookmark.updated_at,
                    }
                ),
                HTTP_201_CREATED,
            )

        else:
            page = request.args.get("page", 1, type=int)
            per_page = request.args.get("per_page", 5, type=int)

            bookmarks = Bookmark.query.filter_by(user_id=current_user).paginate(
                page=page, per_page=per_page
            )

            data = []

            for bookmark in bookmarks.items:
                data.append(
                    {
                        "id": bookmark.id,
                        "url": bookmark.url,
                        "short_url": bookmark.short_url,
                        "visit": bookmark.visits,
                        "body": bookmark.body,
                        "created_at": bookmark.created_at,
                        "updated_at": bookmark.updated_at,
                    }
                )

            meta = {
                "page": bookmarks.page,
                "pages": bookmarks.pages,
                "total_count": bookmarks.total,
                "prev_page": bookmarks.prev_num,
                "next_page": bookmarks.next_num,
                "has_next": bookmarks.has_next,
                "has_prev": bookmarks.has_prev,
            }

            return jsonify({"data": data, "meta": meta}), HTTP_200_OK
            
"""
