from flask import Blueprint
from flask_restplus import Api
from .rpn_api import rpn_api
blueprint = Blueprint('api',__name__)
api = Api(blueprint,version='1.0',description='This is a RPN API')
api.add_namespace(rpn_api)
