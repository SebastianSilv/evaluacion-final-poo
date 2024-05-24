# Evaluacion Final - Programacion Orientada a Objetos

Este repositorio contiene el proyecto desarrollado por Juan Sebastian Silva Caicedo y Juan Camilo Figueroa Suarez para la evaluacion final de la asignatura Herramientas Computacionales.

## Descripcion del proyecto

El proyecto consiste en una aplicacion de consola en Python que permite realizar las siguientes operaciones:

1. Generar la representacion en byte de un caracter.
2. Generar la representacion en byte de una palabra.
3. Generar la representacion ASCII de un byte.

## Uso

1. Clona este repositorio en tu maquina local.
2. Navega hasta el directorio del proyecto.
3. Ejecuta el archivo `main.py` utilizando Python.
4. Sigue las instrucciones en pantalla para seleccionar una opcion del menu.

## Desarrollo

El proyecto fue desarrollado en una sola rama (`main`) siguiendo los requisitos de la evaluacion. Se implementaron las siguientes funciones:

- `char_to_bytes(char)`: Convierte un caracter a su representacion en bytes.
- `word_to_bytes(word)`: Convierte una palabra a su representacion en bytes.
- `bytes_to_ascii(byte_str)`: Convierte una representacion en bytes a su caracter ASCII.

Ademas, se creo un menu principal en la funcion `main()` para permitir al usuario seleccionar la operacion deseada.

## Archivo `.gitignore`

El archivo `.gitignore` excluye los siguientes patrones del control de versiones de Git:

Archivos compilados
*.pyc
*.pyo
pycache/
Archivos de entorno virtual
venv/
env/
Archivos de editor de texto
*.swp
*.swo
Archivos de sistema
.DS_Store
Thumbs.db

## Comandos utilizados en Git

- `git init`: Inicializar un nuevo repositorio Git.
- `git add .`: Agregar todos los archivos al area de staging.
- `git commit -m "Mensaje del commit"`: Crear un nuevo commit con los cambios.
- `git push origin main`: Subir los cambios de la rama `main` al repositorio remoto.
- `git pull origin main`: Obtener los cambios mas recientes de la rama `main` del repositorio remoto.
