# Entrega #3

## Tecnologías

<p align="center">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
  <img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white">
  <img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white">
  <img src="https://img.shields.io/badge/Rabbitmq-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white">
</p>

## Estructura base de los servicios

Para construir los servicios, se tomó como referencia la siguiente estructura, basada en los principios de la arquitectura hexagonal. Esta plantilla sirvió como punto de partida para desarrollar las soluciones, adaptándolas según las necesidades de cada servicio, sin ser una regla estricta.

```bash
/servicio
│── /aplicación          # Capa de aplicación: lógica de negocio y casos de uso
│   ├── /comandos        # Comandos para modificar el estado del sistema
│   ├── /queries         # Consultas para recuperar información
│   ├── handlers.py      # Manejadores que procesan comandos y consultas
│
│── /dominio             # Capa de dominio: entidades y lógica central
│   ├── entidades.py     # Definición de entidades y reglas de negocio
│
│── /infraestructura     # Capa de infraestructura: interacción con tecnologías externas
│
│── /seedwork            # Código reutilizable para los servicios
│   ├── /dominio         # Utilidades comunes para la capa de dominio
│   │   ├── utils.py     # Funciones de soporte para entidades y reglas de negocio
│   │
│   ├── /infraestructura # Utilidades para la infraestructura
│       ├── utils.py     # Herramientas para conectividad, persistencia, etc.
```
## Puntos de sensibilidad
Para la arquitectura propuesta se desean trabajar 3 atributos de calidad clave: Latencia, disponibilidad y modificabilidad. Esto se debe a que la parte más crítica de cara a los clientes es la prestación de los servicios digitales de descarga, filtrado y entrenamiento de ecosistemas digitales para los usuarios Pro y Enterprise. Esto implica que el sistema debe ser confiable y estable, debe entregar una respuesta oportuna, independientemente de lo largo de sus procesos; y finalmente, debe poder ser flexible en el futuro ya que el dominio de negocio debe poder adaptarser para ofrecer un valor agregado más importante a los usuarios. Por tal razón los escenarios de calidad a probar son los siguientes:

* Las peticiones de descarga de imágenes de los usuarios deben ser siempre procesadas, incluso si el componente que compila las imágenes se encuentra fuera de servicio
* Si se está realizando el cambio a otra tecnología o librería, no es necesario modificar la lógica ni los componentes de dominio del sistema ** (Ver consideraciones técnicas)
* Los usuarios de la plataforma de servicios digitales de STA esperan un tiempo de respuesta de confirmación en términos de segundos cuándo hacen solicitudes de descarga

### Consideraciones técnicas
Para esta entrega se realizó la construcción de varios componentes que se ejecutan de forma independiente, siguiendo una estructura de microservicios, tanto en la forma de servicios con exposición de APIs o workers activados por medio de eventos. La idea era seguir una estructura basada en eventos para cada uno y limitar las comunicaciones síncronas únicamente a las consultas a las bases de datos. 

**Para este proyecto se utilizó el message broker RabbitMQ.** Es importante mencionar que, aunque está claro que el objetivo es usar Apache Pulsar como broker de eventos obligatorio para las entregas 4 y 5, se decidió implementar esta tecnología para validar la eficacia de la arquitectura hexagonal construida para STA.

La instancia de RabbitMQ utilizada se desplegó en un entorno virtual expuesto en una Raspberry PI para efectos de prueba y experimentación con tecnologías de Tunneling. Esto significa que no se cuenta con una instancia de RabbitMQ en la nube y por tanto el servicio **no operará de forma automática debido a la temporalidad de las URL del servicio de PITunnel.** Si se requiere probar, se debe modificar el archivo utils.py en el seedwork de infraestructura de los servicios para incluir una URL que admita el protocolo AMPQ en el puerto 5672. **Si es necesario, informar al equipo para aprovisionar una URL válida**

## Despliegue de los diferentes componentes

### compilador_imagenes

#### Configuración e instalaciones

```

cd "Entrega 3"/compilador_imagenes

```

```

pipenv install

```

#### Iniciar el proyecto

```

pipenv run python app.py

```

### NotificacionesDescarga

#### Configuración e instalaciones

```

cd "Entrega 3"/src/NotificacionesDescarga

```

```

pipenv install

```

#### Iniciar el proyecto

```

pipenv run python main.py

```

### publicadorCompilaciones

#### Configuración e instalaciones

```

cd "Entrega 3"/src/publicadorCompilaciones

```

```

pipenv install

```

#### Iniciar el proyecto

```

pipenv run python main.py

```

### serviciosDigitales

#### Configuración e instalaciones

```

cd "Entrega 3"/src/serviciosDigitales

```

```

pipenv install

```

#### Iniciar el proyecto

```

pipenv run python application.py

```
