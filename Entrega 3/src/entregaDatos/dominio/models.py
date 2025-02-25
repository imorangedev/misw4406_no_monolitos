""" {"fecha_comando": "2025-02-23 19:28:14.342949", "id_solicitud": "ae288471-6814-40cd-b057-92650c2a95e1", "id_cliente": "12b81dae-fc99-4085-8471-947d7b750101", "correo_cliente": "jdoe@misouniandes.com", "tipo": "Consulta", "servicio": "Descargar", "id_consulta": "5798d00b-52ea-44a5-8600-b52a6ad2955e", "fecha_creacion": "2025-02-23 19:28:14.342949"} """
""" {"fecha_comando": "2025-02-23 19:29:11.412446", "id_solicitud": "1ad59164-97d3-4004-8972-6190423bd1bc", "id_cliente": "12b81dae-fc99-4085-8471-947d7b750101", "tipo": "Comando", "servicio": "Descargar", "imagenes": [1000001, 1000010, 1000100, 1001000, 1010000, 1100000, 1100001, 1100010, 1100100, 1101000, 1110000], "fecha_creacion": "2025-02-23 19:29:11.412446"} """

from pydantic import BaseModel, Field, ValidationError
from abc import ABC
from enum import Enum
from typing import List, Dict, Any, Optional
import json
from seedwork.logger_config import get_logger

class MessageType(str, Enum):
    COMMAND = "Comando"
    QUERY = "Consulta"

class BaseMessage(BaseModel, ABC): 
    fecha_comando: str
    id_solicitud: str
    id_cliente: str
    servicio: str
    fecha_creacion: str
    tipo: str

    def to_dict(self) -> Dict[str, Any]:
        return self.model_dump(exclude_none=True)

class CommandMessage(BaseMessage):
    imagenes: List[Any] = Field(default_factory=list)

class QueryMessage(BaseMessage):
    correo_cliente: str
    id_consulta: str

def message_factory(message: Dict[str, Any]) -> Optional[BaseMessage]:
    logger = get_logger("MESSAGE_FACTORY")
    type_message_key = "tipo"

    if not isinstance(message, dict):
        logger.error(f"Se esperaba un diccionario, pero se recibió: {type(message).__name__}.")
        return None

    if type_message_key not in message:
        logger.error(f"Falta la clave '{type_message_key}'. Mensaje recibido: {message}")
        return None

    try:
        message[type_message_key] = MessageType(message[type_message_key]).value
    except ValueError:
        logger.error(f"Tipo de mensaje desconocido: {message.get(type_message_key, 'N/A')}")
        return None

    message_type = message[type_message_key]

    try:
        if message_type == MessageType.COMMAND.value:
            return CommandMessage(**message)
        elif message_type == MessageType.QUERY.value:
            return QueryMessage(**message)
    except ValidationError as e:
        logger.error(f"Error de validación en mensaje: \n{e.json(indent=4)}")
        return None

    return None
