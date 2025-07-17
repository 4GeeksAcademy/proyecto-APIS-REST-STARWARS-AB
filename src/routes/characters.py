from flask import Flask, jsonify,request,Blueprint
from database.db import db
from models.Characters import Character



api = Blueprint("/api/characters",__name__)



@api.route("/")
def get_all_characters():
   all_characters = Character.query.all()
   if all_characters is None:
      return jsonify("Error no se ha encontrado ningun personaje"),400
   all_characters = list(map(lambda x: x.serialize(),all_characters))
   return jsonify({"all_character" : all_characters}),200

@api.route("<character_id>",methods = ["GET"])
def get_character(character_id):

   
   character = db.session.get(Character,character_id)
   if character is None:
      return jsonify("Error, no se ha encontrado el personaje introducido"),404
    

   return jsonify({"character":character.serialize()}),200

@api.route("/create", methods =["POST"])
def create_charactert():
    body = request.get_json()
    if body is None:
       return jsonify("Error, el cuerpo de la solicitud es null"),400
    if  'name' not in body:
       return jsonify("Error, falta introducir el nombre del personaje"),400
    if 'description' not in body:
       return jsonify("Error, falta por introducir una descripcion del personaje"),400
    if 'planet_id' not in body:
       return jsonify("Error, falta poner el planeta de origen del personaje"),400
    
    new_character = Character()
    new_character.name = body["name"]
    new_character.description = body["description"]
    new_character.planet_id = body["planet_id"]
    db.session.add(new_character)
    db.session.commit()
   
    return jsonify({"planeta": new_character.serialize()}),200

@api.route("/<character_id>",methods = ["DELETE"])
def delete_character_favorite(character_id):
    character = db.session.get(Character,character_id)
    if character is None:
        return jsonify("Error, no se ha encontrado el planeta buscado"),400
    db.session.delete(character)
    db.session.commit()

    return jsonify("Personaje  eliminado correctamente"),200