"routes related to unicersity page"
from flask_restful import Resource, reqparse
from flask import Response, request

# from flask_jwt_extended import jwt_required
from src.uni.models.voivodeship_model import Voivodeship


class VoivodeshipIdApi(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument(
    #    "price", type=float, required=True, help="This field cannot be left blank!"
    # )

    def get(self, id):
        "get voivodeship by id"
        voivodeship = Voivodeship.objects.get(id=id).to_json()
        return Response(voivodeship, mimetype="application/json", status=200)

    def put(self, id):
        body = request.get_json()
        Voivodeship.objects.get(id=id).update(**body)
        return "", 200

    def delete(self, id):
        voivodeship = Voivodeship.objects.get(id=id).delete()
        return "", 200


class VoivodeshipNameApi(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument(
    #    "price", type=float, required=True, help="This field cannot be left blank!"
    # )

    # @jwt_required()
    def get(self, name):
        "get voivodeship by name"
        # voivodeship = Voivodeship.objects.get(name=name).to_json()
        # if voivodeship:
        #     return Response(voivodeship, mimetype="application/json", status=200)
        # return {"message": "Uni not found"}, 404
        voivodeship = Voivodeship.objects.get(name=name).to_json()
        return Response(voivodeship, mimetype="application/json", status=200)

    def put(self, name):
        # data = Uni.parser.parse_args()
        # voivodeship = Voivodeship.objects.get(name=name)
        # if voivodeship is None:
        #    voivodeship = voivodeship(name, data["terc"])
        # else:
        #    voivodeship.terc = data["terc"]
        # voivodeship.save_to_db()

        body = request.get_json()
        Voivodeship.objects.get(name=name).update(**body)
        return "", 200

    def delete(self, name):
        # voivodeship = Voivodeship.objects.get(name=name)
        # if voivodeship:
        #    voivodeship.delete()
        # return {"message": "Uni deleted"}

        voivodeship = Voivodeship.objects.get(name=name).delete()
        return "", 200


class VoivodeshipsApi(Resource):
    def get(self):
        "get voivodeship list"
        return {"voivodeships": list(map(lambda x: x.json(), Voivodeship.query.all()))}
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
        "add voivodeship"
        body = request.get_json()
        voivodeship = Voivodeship(**body).save()
        id = voivodeship.id
        return {"id": str(id)}, 200


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
