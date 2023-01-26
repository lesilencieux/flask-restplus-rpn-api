from flask import Flask
from rpn_api.config import Config

# api = Api()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    from rpn_api.apis import blueprint as api

    app.register_blueprint(api)
    return app