from dotenv import load_dotenv
from flask import Flask
from sys import argv
from waitress import serve

from api.blueprints import routing

load_dotenv('.env')

def create_app():
    app = Flask('__main__')
    app.config.from_object("config.Config")
    app.register_blueprint(routing)
    return app

app = create_app()

if __name__ == '__main__':
    if argv[1] == 'dev':
        app.run("0.0.0.0", 3000, True)
    else:
        serve(app, host="0.0.0.0", port=3000)