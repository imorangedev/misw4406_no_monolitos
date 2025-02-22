from flask import request
from flask_jsonpify import jsonify
from uuid import UUID

from aplicacion.handlers import HandlerServiciosDigitales
from seedwork.presentacion.api import crear_blueprint

routing = crear_blueprint('servicios_digitales', '/servicios')

@routing.get('/health')
def health_check():
    return jsonify({'msg': 'Los servicios digitales están activos'}), 200

@routing.post('/descargarImagenes')
def descargar_imagenes():
    body = request.json
    comando = {
        'id_cliente': UUID(body['id_cliente']),
        'tipo': body['tipo'],
        'servicio': body['servicio'],
        'imagenes': body['imagenes']
    }
    response = HandlerServiciosDigitales().handle_solicitud_descarga(comando)

    return jsonify(response['response']), response['status_code']