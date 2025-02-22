from flask import Flask
from waitress import serve

from api.blueprints import routing
from infraestructura.database import initialize_database

def create_app():
    app = Flask('__main__')
    app.config.from_object("config.Config")
    app.register_blueprint(routing)
    initialize_database(app)
    return app

app = create_app()

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=3000)