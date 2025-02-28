from flask_sqlalchemy import SQLAlchemy
from enum import Enum
from datetime import datetime

db = SQLAlchemy()

class Pedido(db.Model):
    __tablename__ = 'pedidos'

    id = db.Column(db.String, primary_key=True)
    url_imagen = db.Column(db.String, server_default="{}")
    fechaCompilacion = db.Column(db.DateTime, nullable=False, default=datetime.now())