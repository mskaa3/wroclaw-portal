"""Voivodeship routes in the WroclawPortal API.  Used for retrieving, adding, updating, and deleting voivodeships ."""
from flask_restful import Resource
from flask import Response, request
from flask.json import jsonify
from src.uni.dao.voivodeship_dao import VoivodeshipDao

# from flask_jwt_extended import jwt_required
from src.uni.models.voivodeship_model import Voivodeship


class VoivodeshipIdApi(Resource):
    def get(self, voiv_id):
        """
        Get a single voivodeship with a unique ID.
        :param voiv_id: The unique identifier for a voivodeship.
        :return: A response object for the GET API request.
        """
        voivodeship = VoivodeshipDao.get_voivodeship_by_id(voiv_id=voiv_id)

        if voivodeship is None:
            response = jsonify(
                {
                    "self": f"/voivodeships/{voiv_id}",
                    "voivodeship": None,
                    # "log": None,
                    "error": "there is no voivodeship with this identifier",
                }
            )
            response.status_code = 400
            return response
        else:
            voivodeship_dict: dict = Voivodeship(voivodeship).__dict__
            # comment_dict["time"] = str(comment_dict["time"])

            response = jsonify(
                {
                    "self": f"/voivodeships/{voiv_id}",
                    "voivodeship": voivodeship_dict,
                    # "log": f'/v2/logs/{comment_dict.get("log_id")}',
                }
            )
            # response.status_code = 200
            # return response
            return Response(response, mimetype="application/json", status=200)

        # voivodeship = Voivodeship.objects.get(id=id).to_json()
        # return Response(voivodeship, mimetype="application/json", status=200)

    def put(self, voiv_id):
        """
        Update an existing voivodeship.
        :param voiv_id: The unique identifier for a voivodeship.
        :return: A response object for the PUT API request.
        """
        old_voivodeship: Voivodeship = VoivodeshipDao.get_voivodeship_by_id(
            voiv_id=voiv_id
        )

        if old_voivodeship is None:
            response = jsonify(
                {
                    "self": f"/voivodeships/{voiv_id}",
                    "updated": False,
                    "voivodeship": None,
                    "error": "there is no existing voivodeship with this id",
                }
            )
            # response.status_code = 400
            # return response
            return Response(response, mimetype="application/json", status=400)

        voivodeship_data: dict = request.get_json()
        new_voivodeship = Voivodeship(voivodeship_data)

        if old_voivodeship != new_voivodeship:

            is_updated = VoivodeshipDao.update_voivodeship(voivodeship=new_voivodeship)

            if is_updated:
                updated_voivodeship: Voivodeship = VoivodeshipDao.get_voivodeship_by_id(
                    voiv_id=new_voivodeship.voiv_id
                )
                updated_voivodeship_dict: dict = Voivodeship(
                    updated_voivodeship
                ).__dict__

                response = jsonify(
                    {
                        "self": f"/voivodeships/{voiv_id}",
                        "updated": True,
                        "voivodeship": updated_voivodeship_dict,
                    }
                )
                # response.status_code = 200
                # return response
                return Response(response, mimetype="application/json", status=200)
            else:
                response = jsonify(
                    {
                        "self": f"/voivodeships/{voiv_id}",
                        "updated": False,
                        "voivodeship": None,
                        "error": "the voivodeship failed to update",
                    }
                )
                # response.status_code = 500
                # return response
                return Response(response, mimetype="application/json", status=500)
        else:
            response = jsonify(
                {
                    "self": f"/voivodeships/{voiv_id}",
                    "updated": False,
                    "voivodeship": None,
                    "error": "the voivodeship submitted is equal to the existing voivodeship with the same id",
                }
            )
            # response.status_code = 400
            # return response
            return Response(response, mimetype="application/json", status=400)

        # body = request.get_json()
        # Voivodeship.objects.get(id=id).update(**body)
        # return "", 200

    def delete(self, id):
        """
        Delete an existing voivodeship.
        :param voiv_id: The unique identifier for a voivodeship.
        :return: A response object for the DELETE API request.
        """
        existing_voivodeship: Voivodeship = VoivodeshipDao.get_voivodeship_by_id(
            voiv_id=voiv_id
        )

        if existing_voivodeship is None:
            response = jsonify(
                {
                    "self": f"/voivodeships/{voiv_id}",
                    "deleted": False,
                    "error": "there is no existing voivodeship with this id",
                }
            )
            # response.status_code = 400
            # return response
            return Response(response, mimetype="application/json", status=400)

        is_deleted = VoivodeshipDao.delete_voivodeship_by_id(voiv_id=voiv_id)

        if is_deleted:
            response = jsonify(
                {
                    "self": f"/voivodeships/{voiv_id}",
                    "deleted": True,
                }
            )
            # response.status_code = 204
            # return response
            return Response(response, mimetype="application/json", status=204)
        else:
            response = jsonify(
                {
                    "self": f"/voivodeships/{voiv_id}",
                    "deleted": False,
                    "error": "failed to delete the voivodeship",
                }
            )
            # response.status_code = 500
            # return response
            return Response(response, mimetype="application/json", status=500)

        # voivodeship = Voivodeship.objects.get(id=id).delete()
        # return "", 200


class VoivodeshipsApi(Resource):
    def get(self):
        """
        Get all the voivodeships in the database.
        :return: A response object for the GET API request.
        """
        voivodeships: list = VoivodeshipDao.get_voivodeships()

        if voivodeships is None:
            response = jsonify(
                {
                    "self": "/voivodeships",
                    "voivodeships": None,
                    "error": "an unexpected error occurred retrieving voivodeships",
                }
            )
            # response.status_code = 500
            # return response
            return Response(response, mimetype="application/json", status=500)
        else:
            voiv_dicts = [Voivodeship(voiv).__dict__ for voiv in voivodeships]

            # for voiv_dict in voiv_dicts:
            #    voiv_dict["log"] = f'/v2/logs/{comment_dict.get("log_id")}'

            response = jsonify({"self": "/voivodeships", "voivodeships": voiv_dicts})
            # response.status_code = 200
            # return response
            return Response(response, mimetype="application/json", status=200)

            # return {"voivodeships": list(map(lambda x: x.json(), Voivodeship.query.all()))}
            # return {'unis': [uni.json() for uni in UniModel.query.all()]}

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
        Create a new voivodeship.
        :return: A response object for the POST API request.
        """
        voivodeship_data: dict = request.get_json()

        if voivodeship_data is None:
            response = jsonify(
                {
                    "self": f"/voivodeships",
                    "added": False,
                    "voivodeship": None,
                    "error": "the request body isn't populated",
                }
            )
            response.status_code = 400
            return response
        voivodeship_to_add = Voivodeship(voivodeship_data)

        voivodeship_added_successfully: bool = VoivodeshipDao.add_voivodeship(
            new_voiv=voivodeship_to_add
        )

        if voivodeship_added_successfully:
            voivodeship_added = VoivodeshipDao.get_voivodeship_by_id(
                voivodeship_to_add.voiv_id
            )
            voivodeship_added_dict: dict = Voivodeship(voivodeship_added).__dict__

            response = jsonify(
                {
                    "self": "/voivodeships",
                    "added": True,
                    "voivodeship": voivodeship_added_dict,
                }
            )
            response.status_code = 200
            return response
        else:
            response = jsonify(
                {
                    "self": "/voivodeships",
                    "added": False,
                    "voivodeship": None,
                    "error": "failed to create a new voivodeship",
                }
            )
            response.status_code = 500
            return response

        # body = request.get_json()
        # voivodeship = Voivodeship(**body).save()
        # id = voivodeship.id
        # return {"id": str(id)}, 200


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
