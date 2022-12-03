"""Users in the WroclawPortal API.
Used for retrieving, adding, updating, and deleting users ."""
from flask_restful import Resource, fields, marshal_with
from flask import Response, request
from flask.json import jsonify
from src.user.dao.user_dao import UserDao
from src.utils.helpers import generate_hash, verify_hash
from flask_jwt_extended import create_access_token
from src.user.user_model import (
    User,
    UserSchema,
    user_schema,
    users_schema,
)

resource_fields = {
    "user_id": fields.Integer,
    "user_name": fields.String,
    "user_email": fields.String,
    "password": fields.String,
    "avatar": fields.String,
}


class UserIdApi(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument(
    #    "price", type=float, required=True, help="This field cannot be left blank!"
    # )
    @marshal_with(resource_fields)
    def get(self, user_id):
        """
        Get a single user with a unique ID.
        :param user_id: The unique identifier for a user.
        :return: A response object for the GET API request.
        """
        user = UserDao.get_user_by_id(user_id=user_id)
        print(type(user))
        print(user)
        return user
        """
        if thread is None:
            response = jsonify(
                {
                    "self": f"/threads/{thread_id}",
                    "thread": None,
                    # "log": None,
                    "error": "there is no thread with this identifier",
                }
            )
            response.status_code = 400
            return response
        else:
            thread_dict: dict = Thread(thread).__dict__
            # comment_dict["time"] = str(comment_dict["time"])

            response = jsonify(
                {
                    "self": f"/threads/{thread_id}",
                    "thread": thread_dict,
                    # "log": f'/v2/logs/{comment_dict.get("log_id")}',
                }
            )
            # response.status_code = 200
            # return response
            return Response(response, mimetype="application/json", status=200)
        """

    # @marshal_with(resource_fields)
    def put(self, user_id):
        """
        Update an existing user.
        :param user_id: The unique identifier for a user.
        :return: A response object for the PUT API request.
        """
        print("parameter id")
        print(user_id)
        old_user: User = UserDao.get_user_by_id(user_id)

        if old_user is None:
            response = jsonify(
                {
                    "self": f"/users/{user_id}",
                    "updated": False,
                    "user": None,
                    "error": "there is no existing user with this id",
                }
            )
            # response.status_code = 400
            # return response
            return Response(response, mimetype="application/json", status=400)

        user_data: dict = request.get_json()
        print("data from request")
        print(user_data)
        print(type(user_data))
        user_data["user_id"] = user_id
        print("user_data with user_id ")
        print(user_data)
        new_user = User(user_data)
        new_user.user_id = user_id
        print("new user")
        print(new_user)
        if old_user != new_user:

            is_updated = UserDao.update_user(user=new_user)

            if is_updated:
                updated_user: User = UserDao.get_user_by_id(new_user.user_id)
                # updated_user_dict: dict = User(updated_user).__dict__
                updated_user_dict: dict = updated_user.to_dict()
                print("updated user dict")
                print(updated_user_dict)
                return {
                    "self": f"/users/{user_id}",
                    "updated": True,
                    # "user": updated_user_dict,
                    "user": updated_user.json(),
                }

                # response.status_code = 200
                # return response
                # return Response(response, mimetype="application/json", status=200)
                # return updated_user_dict
                # return Response(
                #    updated_user_dict, mimetype="application/json", status=200
                # )
            else:
                response = jsonify(
                    {
                        "self": f"/users/{user_id}",
                        "updated": False,
                        "user": None,
                        "error": "the user failed to update",
                    }
                )
                # response.status_code = 500
                # return response
                return Response(response, mimetype="application/json", status=500)
        else:
            response = jsonify(
                {
                    "self": f"/users/{user_id}",
                    "updated": False,
                    "user": None,
                    "error": "the post submitted is equal to the existing user with the same id",
                }
            )
            # response.status_code = 400
            # return response
            return Response(response, mimetype="application/json", status=400)

        # body = request.get_json()
        # Voivodeship.objects.get(id=id).update(**body)
        # return "", 200

    def delete(self, user_id):
        """
        Delete an existing user.
        :param user_id: The unique identifier for a user.
        :return: A response object for the DELETE API request.
        """
        existing_user: User = UserDao.get_user_by_id(user_id=user_id)

        if existing_user is None:
            response = jsonify(
                {
                    "self": f"/users/{user_id}",
                    "deleted": False,
                    "error": "there is no existing user with this id",
                }
            )
            # response.status_code = 400
            # return response
            return Response(response, mimetype="application/json", status=400)

        is_deleted = UserDao.delete_user_by_id(user_id=user_id)

        if is_deleted:
            response = jsonify(
                {
                    "self": f"/users/{user_id}",
                    "deleted": True,
                }
            )
            # response.status_code = 204
            # return response
            return Response(response, mimetype="application/json", status=204)
        else:
            response = jsonify(
                {
                    "self": f"/users/{user_id}",
                    "deleted": False,
                    "error": "failed to delete the user",
                }
            )
            # response.status_code = 500
            # return response
            return Response(response, mimetype="application/json", status=500)

        # voivodeship = Voivodeship.objects.get(id=id).delete()
        # return "", 200


class UsersApi(Resource):
    # comments: list = CommentDao.get_comments()
    @marshal_with(resource_fields)
    def get(self):
        """
        Get all the users in the database.
        :return: A response object for the GET API request.
        """
        print("in routes///////////////////")
        users: list = UserDao.get_users()

        return users
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
    @marshal_with(resource_fields)
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
        Create a new user.
        :return: A response object for the POST API request.
        """
        user_data: dict = request.get_json()
        print("user_data from request")
        print(user_data)
        print(type(user_data))

        # user_data['password']=User.generate_hash(user_data['password'])

        if user_data is None:
            response = jsonify(
                {
                    "self": f"/users",
                    "added": False,
                    "user": None,
                    "error": "the request body isn't populated",
                }
            )
            response.status_code = 400
            return response

        if UserDao.get_user_by_user_name(user_data["user_name"]):
            return {"message": "User {} already exists".format(user_data["user_name"])}

        user_to_add = User(user_data)

        print("user to add")
        print(user_to_add)
        print(type(user_to_add))

        user_added_successfully: bool = UserDao.add_user(new_user=user_to_add)
        print(user_added_successfully)

        if user_added_successfully:
            user_added = UserDao.get_user_by_id(user_to_add.user_id)
            print("user added type")
            print(type(user_added))
            user_added_dict: dict = user_added.to_dict()

            print("user_added_dict")
            print(user_added_dict)
            response = jsonify(
                {
                    "self": "/users",
                    "added": True,
                    "user": user_added_dict,
                }
            )
            print(response.data)

            # response.status_code = 200
            # response.headers.add("Access-Control-Allow-Origin", "*")
            # return response
            return user_added, 201
            # return Response(response, mimetype="application/json", status=200)
        else:
            response = jsonify(
                {
                    "self": "/users",
                    "added": False,
                    "user": None,
                    "error": "failed to create a new user",
                }
            )
            response.status_code = 500
            return response

        # body = request.get_json()
        # voivodeship = Voivodeship(**body).save()
        # id = voivodeship.id
        # return {"id": str(id)}, 200


class UserAuthApi(Resource):
    # comments: list = CommentDao.get_comments()
    @marshal_with(resource_fields)
    def get(self, user_name):
        """
        Get all the user in the database by unique name.
        :return: A response object for the GET API request.
        """
        print("in routes///////////////////")
        user: User = UserDao.get_user_by_user_name(user_name)
        # ??? what if not found
        return user
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

    login_resource_fields = {
        "user_id": fields.Integer,
        "user_name": fields.String,
        "user_email": fields.String,
        "avatar": fields.String,
        "access_token": fields.String,
    }

    # @marshal_with(login_resource_fields)
    def post(self):
        """
        Authenticate a user by user_name.
        :return: A response object for the POST API request.
        """

        try:
            user_data: dict = request.get_json()
            print("user_data from request")
            print(user_data)
            print(type(user_data))

            user_from_db = UserDao.get_user_by_user_name(user_data["user_name"])
            print(user_from_db)
            if not user_from_db:
                return "such user dne in db"

                # if verify_hash(user_data["password"], user_from_db.password):
            access_token = create_access_token(identity=user_data["user_name"])

            # response 201
            return {
                "message": "Logged in as {}".format(user_from_db.user_name),
                "access_token": access_token,
                "user": user_from_db.json(),
            }
            # return user_from_db, access_token
            # else:
            #    return "401"
        except Exception as e:
            print(e)
            return "422"
        # user_data['password']=User.generate_hash(user_data['password'])
