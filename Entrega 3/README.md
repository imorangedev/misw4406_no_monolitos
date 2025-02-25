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

## Proyectos

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

## Consideraciones técnicas
