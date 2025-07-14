from flask import Flask,jsonify,request,Blueprint
from database.db import db
from models.Favorites import Favorite

api = Blueprint("/api/favorites",__name__)



@api.route("/planets/<int:planet_id>", methods =["POST"])
def create_favorite_planet(id_planet):
    body = request.get_json()
    new_favorite = Favorite
    new_favorite.planet_id = body[id_planet]
    db.session.add(new_favorite)

    return jsonify("Se ha añadido correctamente el personaje favorito")



@api.route("/character/<int:character_id>", methods =["POST"])
def create_favorite_character(id_character):
    body = request.get_json()
    new_favorite_character = Favorite
    new_favorite_character.character_id = body[id_character]
    db.session.add(new_favorite_character)

    return jsonify("planeta favorito creado correctamente")



@api.route("/planet/<int:planet_id",methods = ["DELETE"])
def delete_planet_favorite(planet_id):
    planet = db.session.get(Favorite,planet_id)
    if planet is None:
        return jsonify("Error, no se ha encontrado el planeta buscado"),404
    db.session.delete(planet)
    db.session.commit()

    return jsonify("Planeta favorito eliminado correctamente"),200




@api.route("/character/<int:character_id>",methods = ["DELETE"])
def delete_character_favorite(character_id):

    character = db.session.get(Favorite,character_id)
    if character is None:
        return jsonify("Error al bbuscar el personaje"),404
    db.session.delete(character)
    db.session.commit()

    return jsonify("Usuario eliminado correctamente"),200