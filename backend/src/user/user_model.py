"""users table schema"""
from main import db, ma
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class User(db.Base):
    "users table schema"
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(100), nullable=False)
    user_email = Column(String(64), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    # created_on=Column(DateTime(timezone=True), server_default=func.now())
    # last_login=Column(DateTime(timezone=True), onupdate=func.now())

    def __init__(self, user: dict):
        # self.uni_id = uni.get("uni_id")
        self.user_name = user.get("user_name")
        self.user_email = user.get("user_email")
        self.password = user.get("password")

    # def json(self):
    #  return {'name':self.name,...}
    def __repr__(self):
        """
        String representation of the user.
        This representation is meant to be machine readable.
        :return: The user string.
        """
        return f"<User {self.user_name}"

    def __str__(self):
        """
        String representation of the user.
        This representation is meant to be human readable.
        :return: The user string.
        """
        return (
            f"User: [user_id: {self.user_id},user_name: {self.user_name},"
            f"user_email:{self.user_email},password:{self.password}]"
        )


"""
    @classmethod
    def find_by_name(cls, name):
        "find uni by name"
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        "find ini by id"
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
"""


# def json(self):
#    return {"name":self.name,...}


class UserSchema(ma.Schema):
    """schema for User"""

    class Meta:
        model = User
        # sqla_session = db.session
        # load_instance = True


user_schema = UserSchema()
users_schema = UserSchema(many=True)
