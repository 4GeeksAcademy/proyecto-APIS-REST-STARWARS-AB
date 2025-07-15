from flask import Flask,jsonify,request,Blueprint
from database.db import db
from models.User import Favorite

api = Blueprint("/api/favorites",__name__)
# NO FUNCIONA PREGUNTAR HORACIO
@api.route("/planets/<int:planet_id>/<int:id>", methods=["POST"])
def create_favorite_planet(planet_id, id):
    body = request.get_json()
    new_favorite_planet = Favorite
    new_favorite_planet.planet_id = body[planet_id]
    new_favorite_planet.user_id = id
    db.session.add(new_favorite_planet)
    db.session.commit()
    return jsonify("Se ha añadido correctamente el planeta favorito"),200




# NO FUNCIONA PREGUNTAR HORACIO
@api.route("/characters/<int:character_id>/<int:id>", methods =["POST"])
def create_favorite_character(id_character,id):
    body = request.get_json()
    new_favorite_character = Favorite
    new_favorite_character.character_id = body[id_character]
    new_favorite_character.user_id = id
    db.session.add(new_favorite_character)
    db.session.commit()


    return jsonify("planeta favorito creado correctamente"),200



@api.route("/planets/<int:planet_id>",methods = ["DELETE"])
def delete_planet_favorite(planet_id):
    planet = db.session.get(Favorite,planet_id)
    if planet is None:
        return jsonify("Error, no se ha encontrado el planeta buscado"),404
    db.session.delete(planet)
    db.session.commit()

    return jsonify("Planeta favorito eliminado correctamente"),200




@api.route("/characters/<int:character_id>",methods = ["DELETE"])
def delete_character_favorite(character_id):

    character = db.session.get(Favorite,character_id)
    if character is None:
        return jsonify("Error al buscar el personaje"),404
    db.session.delete(character)
    db.session.commit()

    return jsonify("Personaje eliminado correctamente"),200