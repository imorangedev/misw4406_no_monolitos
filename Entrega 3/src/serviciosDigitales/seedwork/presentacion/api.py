from flask import Blueprint

def crear_blueprint(identificador: str, prefijo_url: str = None):
    return Blueprint(identificador, __name__, url_prefix= prefijo_url)