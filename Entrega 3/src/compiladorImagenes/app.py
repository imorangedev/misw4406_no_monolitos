from flask import Flask, jsonify
from sys import argv

from src.blueprints.routes import blueprint
from src.models.model import db

app = Flask(__name__)
app.register_blueprint(blueprint)

def config_app(db_url):
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    with app.app_context():
        db.init_app(app)
        db.create_all()

if __name__ == '__main__':
    # config_app(argv[1])
    # print(config_app(argv[1]))
    db_url = f"sqlite:///microservice_test.db"
    config_app(db_url)
    app.run(host="0.0.0.0", port=3002, debug=True)