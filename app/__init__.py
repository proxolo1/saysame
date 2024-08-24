

from flask import Flask
from .saysamething import socketio
from .routes import main
def create_app() :
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = "SECRET"

    app.register_blueprint(main)
    socketio.init_app(app)
    return app