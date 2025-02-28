from flask import Flask, jsonify
from sys import argv

from aplicacion.comandos.image_compiler import ImageCompiler

# app = Flask(__name__)

# def config_app(db_url):
#     app.config["SQLALCHEMY_DATABASE_URI"] = db_url
#     with app.app_context():
#         db.init_app(app)
#         db.create_all()

# if __name__ == '__main__':
#     db_url = f"sqlite:///microservice_test.db"
#     config_app(db_url)
#     app.run(host="0.0.0.0", port=3002, debug=True)

if __name__ == '__main__':
    list_image = [1, 2, 4, 7]
    image_compiler = ImageCompiler(list_image)
    image_compiler.handle(list_image)