import os
import shutil
from datetime import datetime

class FileOrganizer :

    def __init__(self, source_directory, destination_directory):
        """
        Inicializa el organizador de archivos.
        :param source_directory: Carpeta de origen (donde están los archivos desorganizados).
        :param destination_directory: Carpeta de destino (donde se organizarán los archivos).
        """
        self.source_directory = source_directory
        self.destination_directory = destination_directory
        self.log_file = os.path.join(destination_directory, "organizer_log.txt")
        self.create_folders()

    def create_folders(self):
        """Crea las carpetas para organizar los archivos."""
        folders = ["Imagenes","Videos","Documento","Musica","Otros"]
        for folder in folders:
            folders_path = os.path.join(self.destination_directory, folder)
            if not os.path.exists(folders_path):
                os.makedirs(folders_path)

    def organizar_file(self):
        """Organiza los archivos en las carpetas correspondientes."""
        try :

            for filename in os.listdir(self.source_directory):
                file_path = os.path.join(self.source_directory,filename)
                # Ignorar carpetas, archivos ocultos y el archivo de log
                if os.path.isdir(file_path) or filename.startswith(".") or filename == "Thumbs.db" or filename == "organizer_log.txt":
                    continue       
                if filename.lower().endswith((".png",".jpg",".jpeg",".gif")):
                    dest_folder = "Imagenes"
                elif filename.lower().endswith((".pdf", ".docx", ".txt")):
                    dest_folder = "Documento"
                elif filename.lower().endswith((".mp3", ".wav")):
                    dest_folder = "Musica"
                elif filename.lower().endswith((".mp4", ".mkv", ".avi")):
                    dest_folder = "Videos"
                # elif filename.lower().endswith((".zip", ".rar", ".7z")):
                #     dest_folder = "comprimidos"
                # elif filename.lower().endswith((".exe", ".msi")):
                #     dest_folder = "ejecutables"
                else:
                    dest_folder = "Otros"
                shutil.move(file_path, os.path.join(self.destination_directory, dest_folder, filename))
                self.log(f"Movido: {filename} -> {os.path.join(self.destination_directory, dest_folder)}")

            self.log("Organización completada con éxito.")        
        except Exception as e:
            self.log(f"Error: {str(e)}")
    
    def log(self, message):
        """Registra mensajes en el archivo de log."""
        with open(self.log_file, "a") as f:
            f.write(f"[{datetime.now()}] {message}\n")