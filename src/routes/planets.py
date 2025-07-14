from flask import Flask, jsonify,request,Blueprint
from database.db import db
from models.Planets import Planet
api = Blueprint("/api/planets",__name__)

@api.route("/")
def get_planets():
    return jsonify("Todos los planetas")

@api.route("/")
def get_planets():
   all_planets = Planet.query.all()
   if all_planets is None:
      return jsonify("Error, no se han encontrado planetas"),404
   all_planets = list(map(lambda x: x.serialize(),all_planets))
   return jsonify({"all_planets" : all_planets}),200

@api.route("/<planet_id>",methods = ["GET"])
def get_planet(planet_id):
   planet = db.session.get(Planet,planet_id)
   if planet is None:
      return jsonify("Error, no se ha encontrado el planeta")

   return jsonify({"planet":planet.serialize()}),200

@api.route("/", methods =["POST"])
def create_planet():
    body = request.get_json()
    if body is None:
       return jsonify("Error, el cuerpo de la solicitud es null"),400
    if  'name' is not body:
       return jsonify("Error, falta introducir el nombre del planeta"),400
    if 'description' is not body:
       return jsonify("Error, falta por introducir una descripcion del planeta"),400
    if 'rotation' is not body:
       return jsonify("Error, falta poner la rotacion del planeta"),400
    new_planet = Planet()
    new_planet.name = body["name"]
    new_planet.description = body["description"]
    new_planet.rotation = body["rotation"]
    db.session.add(new_planet)
    db.session.commit()
   
    return jsonify({"planeta": new_planet.serialize()}),200

@api.route("/<int:planet_id",methods = ["DELETE"])
def delete_planet_favorite(planet_id):
    planet = db.session.get(Planet,planet_id)
    if planet is None:
        return jsonify("Error, no se ha encontrado el planeta buscado"),404
    db.session.delete(planet)
    db.session.commit()

    return jsonify("Planeta favorito eliminado correctamente"),200