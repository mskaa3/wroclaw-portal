"routes related to voivodeships"
from flask_restful import Resource, reqparse

# from flask_jwt_extended import jwt_required
from src.uni.models.uni_model import Uni


class UnisApi(Resource):
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
        # return {'unis': [uni.json() for uni in UniModel.query.all()]}


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
