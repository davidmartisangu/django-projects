# Proyecto instagram con Django

Este proyecto es una práctica para profundizar el framework web **Django**. A través de este proyecto, estoy explorando las funcionalidades de Django, como el manejo de rutas, vistas, modelos, formularios, autenticación, y mucho más.

## Requisitos

- Python 3.x
- Django (versión recomendada: 3.x o superior)
- pip (gestor de paquetes de Python)
- Virtualenv

## Instalación

1. Clona este repositorio en tu ordenador:

    ```
    git clone https://github.com/tu-usuario/nombre-del-repositorio.git
    cd nombre-del-repositorio
    ```

2. Crea un entorno virtual para aislar las dependencias del proyecto y activalo:

    ```
    python3 -m venv env
    source env/bin/activate
    ```

3. Instala las dependencias necesarias, para ello he creado un archivo "requirementes":

    ```
    pip install -r requirements.txt
    ```

4. Realiza las migraciones de la base de datos:

    ```
    python manage.py migrate
    ```

5. Ejecuta el servidor de desarrollo:

    ```
    python manage.py runserver
    ```

6. Abre tu navegador web y ve a `http://127.0.0.1:8000/` para ver el proyecto en ejecución.

## Funcionalidades

- [x] Configuración básica de un proyecto Django.
- [x] Creación de aplicaciones y modelos.
- [x] Rutas y vistas personalizadas.
- [x] Autenticación de usuarios.
- [x] Formularios y validaciones.

## Contribución

Este proyecto es parte de mi aprendizaje y está abierto a sugerencias y mejoras. Siéntete libre de escribirme o enviar un **Pull Request**.

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.
