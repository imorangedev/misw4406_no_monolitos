from flask_jsonpify import jsonify

from seedwork.presentacion.api import crear_blueprint

routing = crear_blueprint('servicios_digitales', '/servicios')

@routing.get('/health')
def health_check():
    return jsonify({'msg': 'Los servicios digitales están activos'}), 200