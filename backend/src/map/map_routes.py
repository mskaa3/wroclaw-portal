import requests
import os
import json
from flask import Blueprint


map_routes = Blueprint("map_routes", __name__)


@map_routes.route("/map", methods=["GET"])
def map_pins():
  f = open('googleMapPins.json')
  data = json.load(f)
  print(data)
  return data