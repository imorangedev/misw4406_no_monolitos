from flask import request
from flask_jsonpify import jsonify

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
        'id_cliente': body['id_cliente'].strip(),
        'tipo': body['tipo'],
        'servicio': body['servicio'],
        'data': str(body['data'])
    }
    response = HandlerServiciosDigitales().handle_consulta_cliente(comando)
    return jsonify(response['response']), response['status_code']

@routing.post('/consultarDescarga')
def consultar_url_descarga():
    body = request.json
    consulta = {
        'id_cliente': body['id_cliente'],
        'tipo': body['tipo'],
        'servicio': body['servicio'],
        'data': body['data']
    }
    response = HandlerServiciosDigitales().handle_consulta_cliente(consulta)

    return jsonify(response['response']), response['status_code']

@routing.post('/registrarCliente')
def registrar_cliente():
    body = request.json
    response = HandlerServiciosDigitales().handle_comando_crear_cliente(body)
    return jsonify(response['response']), response['status_code']

@routing.get('/validarCliente/<tipo>/<id_cliente>')
def consultar_cliente(tipo, id_cliente):
    response = HandlerServiciosDigitales().handle_consulta_cliente(tipo, id_cliente)
    return jsonify(response['response']), response['status_code']

@routing.post('webhooks/solicitudDescarga')
def webhook_solicitud_descarga():
    body = request.json
    response = HandlerServiciosDigitales().handle_solicitud_descarga(body)
    return jsonify(response['response']), response['status_code']

@routing.post('webhooks/consultaDescarga')
def webhook_consulta_descarga():
    body = request.json
    response = HandlerServiciosDigitales().handle_consulta_descarga(body)
    return jsonify(response['response']), response['status_code']