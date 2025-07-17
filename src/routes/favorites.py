from flask import Flask,jsonify,request,Blueprint
from database.db import db
from models.User import Favorite, User

api = Blueprint("/api/favorites",__name__)
# NO FUNCIONA PREGUNTAR HORACIO
@api.route("/planets/<int:planet_id>/<int:id>", methods=["POST"])
def create_favorite_planet(planet_id, id):
  
    new_favorite_planet = Favorite()
    new_favorite_planet.planet_id =planet_id
    new_favorite_planet.user_id = id
  
    db.session.add(new_favorite_planet)
    db.session.commit()
    return jsonify("Se ha añadido correctamente el planeta favorito"),200





@api.route("/characters/<int:character_id>/<int:id>", methods =["POST"])
def create_favorite_character(id_character,id):
 
    new_favorite_character = Favorite()
    new_favorite_character.character_id =id_character
    new_favorite_character.user_id = id
    db.session.add(new_favorite_character)
    db.session.commit()


    return jsonify("planeta favorito creado correctamente"),200



@api.route("/planets/<int:planet_id>/<int:id>",methods = ["DELETE"])
def delete_planet_favorite(planet_id,id):
    # user_id = db.session.get(User,id)
    
    planet_favorite_delete = Favorite.query.filter_by(planet_id = planet_id,user_id = id).first()
    if not planet_favorite_delete:
        return jsonify("Error,favorito no encontrado"),404
    db.session.delete(planet_favorite_delete)
    db.session.commit()
    return jsonify("Planeta favorito eliminado correctamente"),200


@api.route("/characters/<int:character_id>/<int:id>",methods = ["DELETE"])
def delete_character_favorite(character_id,id):
    
    character_favorite_delete = Favorite.query.filter_by(character_id = character_id,user_id = id).first()
    if not character_favorite_delete:
        return jsonify("Error, character no encontrado")
    db.session.delete(character_favorite_delete)
    db.session.commit()
    return jsonify("Personaje favorito eliminado correctamente"),200