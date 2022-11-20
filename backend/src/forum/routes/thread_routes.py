"""Thread routes in the WroclawPortal API.
Used for retrieving, adding, updating, and deleting threads ."""
from flask_restful import Resource, fields, marshal_with
from flask import Response, request
from flask.json import jsonify
from src.forum.dao.topic_dao import TopicDao
from src.forum.dao.thread_dao import ThreadDao

# from flask_jwt_extended import jwt_required
from src.forum.models.thread_model import (
    Thread,
    ThreadSchema,
    thread_schema,
    threads_schema,
)

resource_fields = {
    "thread_id": fields.Integer,
    "thread_name": fields.String,
    "thread_content": fields.String,
    "thread_created_at": fields.DateTime,
    "thread_creator": fields.Integer,
    "topic": fields.Integer,
    "pinned": fields.String,
}


class ThreadIdApi(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument(
    #    "price", type=float, required=True, help="This field cannot be left blank!"
    # )
    @marshal_with(resource_fields)
    def get(self, thread_id):
        """
        Get a single thread with a unique ID.
        :param thread_id: The unique identifier for a thread.
        :return: A response object for the GET API request.
        """
        thread = ThreadDao.get_thread_by_id(thread_id=thread_id)

        print(thread)
        return thread
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

    def put(self, thread_id):
        """
        Update an existing thread.
        :param thread_id: The unique identifier for a thread.
        :return: A response object for the PUT API request.
        """
        old_thread: Thread = ThreadDao.get_thread_by_id(thread_id=thread_id)

        if old_thread is None:
            response = jsonify(
                {
                    "self": f"/threads/{thread_id}",
                    "updated": False,
                    "thread": None,
                    "error": "there is no existing thread with this id",
                }
            )
            # response.status_code = 400
            # return response
            return Response(response, mimetype="application/json", status=400)

        thread_data: dict = request.get_json()
        new_thread = Thread(thread_data)

        if old_thread != new_thread:

            is_updated = ThreadDao.update_thread(thread=new_thread)

            if is_updated:
                updated_thread: Thread = ThreadDao.get_thread_by_id(
                    thread_id=new_thread.thread_id
                )
                updated_thread_dict: dict = Thread(updated_thread).__dict__

                response = jsonify(
                    {
                        "self": f"/threads/{thread_id}",
                        "updated": True,
                        "thread": updated_thread_dict,
                    }
                )
                # response.status_code = 200
                # return response
                return Response(response, mimetype="application/json", status=200)
            else:
                response = jsonify(
                    {
                        "self": f"/threads/{thread_id}",
                        "updated": False,
                        "thread": None,
                        "error": "the thread failed to update",
                    }
                )
                # response.status_code = 500
                # return response
                return Response(response, mimetype="application/json", status=500)
        else:
            response = jsonify(
                {
                    "self": f"/threads/{thread_id}",
                    "updated": False,
                    "thread": None,
                    "error": "the thread submitted is equal to the existing thread with the same id",
                }
            )
            # response.status_code = 400
            # return response
            return Response(response, mimetype="application/json", status=400)

        # body = request.get_json()
        # Voivodeship.objects.get(id=id).update(**body)
        # return "", 200

    def delete(self, thread_id):
        """
        Delete an existing thread.
        :param thread_id: The unique identifier for a thread.
        :return: A response object for the DELETE API request.
        """
        existing_thread: Thread = ThreadDao.get_thread_by_id(thread_id=thread_id)

        if existing_thread is None:
            response = jsonify(
                {
                    "self": f"/threads/{thread_id}",
                    "deleted": False,
                    "error": "there is no existing thread with this id",
                }
            )
            # response.status_code = 400
            # return response
            return Response(response, mimetype="application/json", status=400)

        is_deleted = ThreadDao.delete_thread_by_id(thread_id=thread_id)

        if is_deleted:
            response = jsonify(
                {
                    "self": f"/threads/{thread_id}",
                    "deleted": True,
                }
            )
            # response.status_code = 204
            # return response
            return Response(response, mimetype="application/json", status=204)
        else:
            response = jsonify(
                {
                    "self": f"/threads/{thread_id}",
                    "deleted": False,
                    "error": "failed to delete the thread",
                }
            )
            # response.status_code = 500
            # return response
            return Response(response, mimetype="application/json", status=500)

        # voivodeship = Voivodeship.objects.get(id=id).delete()
        # return "", 200


class ThreadsApi(Resource):
    # comments: list = CommentDao.get_comments()
    @marshal_with(resource_fields)
    def get(self):
        """
        Get all the threads in the database.
        :return: A response object for the GET API request.
        """
        print("in routes///////////////////")
        threads: list = ThreadDao.get_threads()

        return threads
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
        Create a new thread.
        :return: A response object for the POST API request.
        """
        thread_data: dict = request.get_json()

        if thread_data is None:
            response = jsonify(
                {
                    "self": f"/threads",
                    "added": False,
                    "thread": None,
                    "error": "the request body isn't populated",
                }
            )
            response.status_code = 400
            return response
        thread_to_add = Thread(thread_data)

        thread_added_successfully: bool = ThreadDao.add_thread(new_thread=thread_to_add)

        if thread_added_successfully:
            thread_added = ThreadDao.get_thread_by_id(thread_to_add.thread_id)
            thread_added_dict: dict = Thread(thread_added).__dict__

            response = jsonify(
                {
                    "self": "/threads",
                    "added": True,
                    "thread": thread_added_dict,
                }
            )
            response.status_code = 200
            return response
        else:
            response = jsonify(
                {
                    "self": "/threads",
                    "added": False,
                    "thread": None,
                    "error": "failed to create a new thread",
                }
            )
            response.status_code = 500
            return response

        # body = request.get_json()
        # voivodeship = Voivodeship(**body).save()
        # id = voivodeship.id
        # return {"id": str(id)}, 200


class ThreadsByTopicApi(Resource):

    # def get_posts_count(self, obj):
    #    return PostDao.objects.filter(thread__forum=obj).count()

    thread_last_activity_fields = {
        "thread": fields.Integer,
        # "thread_name": fields.String,
        # "activity_time": fields.DateTime,
        # "pinned": fields.Boolean,
        "post_creator_name": fields.String,
    }

    resource_fields = {
        "thread_id": fields.Integer,
        "thread_name": fields.String,
        "thread_content": fields.String,
        "thread_created_at": fields.String,
        "thread_creator_name": fields.String,
        "post_count": fields.Integer,
        # "last_activity": fields.Nested(thread_last_activity_fields),
        "last_activity": {
            "thread_id": fields.Integer,
            "thread_name": fields.String,
            "post_created_at": fields.String,
            "post_creator_name": fields.String,
            "pinned": fields.String,
        },
    }

    @marshal_with(resource_fields)
    def get(self, topic_id: int):
        """
        Get all the threads by topic in the database.
        :return: A response object for the GET API request.
        """
        print("in routes///////////////////")

        threads: list = ThreadDao.get_threads_by_topic(topic_id)
        print(type(threads))
        print(threads)
        for thread in threads:
            print(thread)

        # res = threads_schema.dump(threads)
        # print(res)
        return threads
