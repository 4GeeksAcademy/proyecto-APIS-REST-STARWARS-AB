from flask import Flask, jsonify,request,Blueprint
from models.Favorites import Favorite
from models.User import User
from database.db import db

api = Blueprint("/api/user",__name__)

@api.route("/favorites/<int:user_id>",methods = ["GET"])
def get_users_favorites(id_user):
   
   user_favorite = Favorite.query.filter_by(id_user)

   if user_favorite is None:
     return jsonify("Error, usuario no encontrado"),404
   
   response = list(map(lambda favorite: favorite.serialize(),user_favorite))

   
   return jsonify({"all_favorites" : response}),200
    

@api.route("/")
def get_users():
   all_users = User.query.all()
   if all_users is None:
      return jsonify("Error usuarios no encontrados"),404
   
   all_users = list(map(lambda x: x.serialize(),all_users))
   return jsonify({"all_user" : all_users}),200

@api.route("/<user_id>",methods = ["GET"])
def get_user(user_id):
   user = db.session.get(User,user_id)
   if user is None:
      return jsonify("El usuario no existe"),404

   return jsonify({"usuario":user.serialize()}),200


    

@api.route("/create", methods =["POST"])
def create_user():
    body = request.get_json()
    new_user = User()
    new_user.email = body["email"]
    new_user.password = body["password"]
    new_user.nickname = body["nickname"]
    db.session.add(new_user)
    db.session.commit()
   
    return jsonify({"usuario": new_user.serialize()}),200

