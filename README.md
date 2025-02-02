# Entrega 1 - Diseño y arquitectura de dominio

Este repositorio contiene el código para ejecutar la generación de los mapas de contexto a través de la herramienta ContextMapper.


## Estructura
├── Entrega 1 # Imágenes de los mapas de contexto y resultado del Event storming para el AS-IS y el TO-BE de STA. También existe un documento de resumen, el cuál contiene también un glosario del lenguaje ubicuo y descripciones del proceso de diseño

│

├── src-gen # Directorio dónde se generan los mapas de contexto

│

├── src

├─── main 

├─────── cml # Códigos que construyen el diagrama del AS-IS y el TO-BE en formato .cml


## Instrucciones
**Este proyecto fue construido usando Gitpod classic**. En el repositorio se encuentra el archivo .gitpod.yml que permite que GitPod realice la inicialización del proceso de construcción del ambiente de ejecución del proyecto. La forma más directa de hacer la inicialización del ambiente de trabajo es cargar el código en un repositorio de GitHub e instalar la extensión web de GitPod para poder inicializar el proceso automáticamente.

![imagen](https://github.com/user-attachments/assets/4a644194-fc87-4563-846d-d843b42cc215)


En caso de que esto no sea posible, será necesario entonces usar el cliente de GitPod en local para ejecutar el archivo .gitpod.yml, o bien, usar docker con el archivo .gitpod.Dockerfile, el cuál crea el ambiente en Java para ejecutar ContextMapper. Finalmente, será necesario instalar las siguientes extensiones en VSCode:

extensions:
- jebbs.plantuml
- contextmapper.context-mapper-vscode-extension
- vscjava.vscode-java-pack
- asciidoctor.asciidoctor-vscode
