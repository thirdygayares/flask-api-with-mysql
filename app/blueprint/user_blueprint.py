from flask import abort, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_smorest import Blueprint
from app.repository.user_repository import UserRepository
from app.schema.user_schema import UserSchema

user_blp = Blueprint('users','users', url_prefix='/users', description="Operation for users")

@user_blp.route("/", methods=['POST'])
@user_blp.arguments(UserSchema)
@user_blp.response(201, UserSchema)
@jwt_required()
def create_user(data):
   user = UserRepository.create_user(data)
   return user

@user_blp.route("/<string:user_id>", methods=['GET'])
@user_blp.response(200, UserSchema)
def get_user_by_id(user_id):
   user = UserRepository.get_user_by_uuid(user_id)
   if not user:
      return jsonify({"message":"not found"}), 404
   return user

@user_blp.route("/", methods=['GET'])
@user_blp.response(200, UserSchema(many=True))
def get_all_users():
   user = UserRepository.get_all()
   return user


@user_blp.route("/<string:user_id>", methods=['PUT'])
@user_blp.arguments(UserSchema)
@user_blp.response(200, UserSchema)
def update_user(data, user_id):
   user = UserRepository.get_user_by_uuid(user_id)

   if not user:
       abort(404, description="User not found")
   updated_user = UserRepository.update_user(user, data)

   return updated_user

@user_blp.route("/<string:user_id>", methods=["DELETE"])
@user_blp.response(204)
def delete_user(user_id):
   user = UserRepository.get_user_by_uuid(user_id)

   if not user:
      abort(404, description="User Not Found")
   UserRepository.delete_user(user)
   return ''









