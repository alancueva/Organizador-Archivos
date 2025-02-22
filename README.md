# Organizador de Archivos Automático

Este es un programa en Python que organiza archivos en carpetas según su tipo (imágenes, documentos, música, videos, otros).


## Cómo Usar

1. Clona este repositorio.
2. Ejecuta el archivo `main.py`.
3. Selecciona la carpeta que deseas organizar usando la interfaz gráfica.
4. Haz clic en "Organizar Archivos".

## Estructura del Proyecto

- `src/`: Contiene el código fuente.
- `README.md`: Documentación del proyecto.

## Requisitos

- Python 3.13.2
- Tkinter (viene incluido con Python)

## Ejecutable
Convierte el programa en un archivo ejecutable (.exe) usando pyinstaller para que puedas distribuirlo fácilmente.

- pip install pyinstaller
- pyinstaller --onefile --windowed src/main.py