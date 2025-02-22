import os
import tkinter as tk
from tkinter import filedialog, messagebox
from file_organizer import FileOrganizer  

class FileOrganizerApp:

    def __init__(self, root):
        """
        Inicializa la aplicación.
        :param root: Ventana principal de tkinter.
        """
        self.root = root
        #icono = tk.PhotoImage(file="src/icons/icons8-codificación-en-línea-96.ico")
        # self.root.iconbitmap("src/icons/icons8-codificación-en-línea-96.ico")
        #Sself.root.iconphoto(False, icono, icono)
        self.root.geometry("400x200")  # Tamaño de la ventana
        
        self.center_window()
        self.load_icon()
        self.root.resizable(0,0)
        self.root.title("Organizador de Archivos")
        # Ruta fija (cambia esto por la ruta que desees)
        self.destination_directory  = "D:\\"  # Ruta fija para organizar archivos
        seleccionar_name = "Selecciona una carpeta para organizar:"
        # Etiqueta y botón para seleccionar carpeta
        self.label = tk.Label(root, text=seleccionar_name)
        self.label.pack(pady=10)
        self.select_button = tk.Button(root, text="Seleccionar Carpeta", command=self.select_directory)
        self.select_button.pack(pady=10)
        # Botón para organizar archivos
        self.organize_button = tk.Button(root, text="Organizar Archivos", command=self.organize_files, state=tk.DISABLED)
        self.organize_button.pack(pady=10)
        # Ruta de la carpeta de origen seleccionada
        self.source_directory = ""

    # Centrar la ventana en la pantalla
    def center_window(self):
        """
        Centra la ventana en la pantalla.
        """
        # Actualiza la ventana para asegurarse de que se conozcan sus dimensiones
        self.root.update_idletasks()
        # Obtiene las dimensiones de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        # Obtiene las dimensiones de la ventana
        Wventana = self.root.winfo_width()
        Hventana = self.root.winfo_height()
        # Calcula la posición para centrar la ventana
        x = (screen_width // 2) - (Wventana // 2)
        y = (screen_height // 2) - (Hventana // 2)
        # Establece la posición de la ventana
        self.root.geometry(f"+{x}+{y}")

    def load_icon(self):
        """
        Carga el icono de la aplicación.
        """
        # Ruta del archivo de icono
        icon_path = os.path.join(os.path.dirname(__file__), "icons", "icons8-codificación-en-línea-96.ico")
        # Verifica si el archivo de icono existe
        if os.path.exists(icon_path):
            try:
                self.root.iconbitmap(icon_path)  # Carga el icono
            except Exception as e:
                print(f"Error al cargar el icono: {e}")
        else:
            print(f"Advertencia: No se encontró el archivo de icono en {icon_path}")
    #-------------------------------------------------------------------------------------------------------




    def select_directory(self):
        """Abre un diálogo para seleccionar una carpeta."""
        self.source_directory = filedialog.askdirectory()
        if self.source_directory:
            self.label.config(text=f"Carpeta seleccionada: {self.source_directory}")
            self.organize_button.config(state=tk.NORMAL)

    def organize_files(self):
        """Organiza los archivos en la carpeta seleccionada."""

        # Verifica si la carpeta de destino existe
        if not os.path.exists(self.destination_directory):
            messagebox.showerror("Error", f"La carpeta de destino {self.destination_directory} no existe.")
            return

        # Verifica si la carpeta de origen está vacía
        if not os.listdir(self.source_directory):
            messagebox.showwarning("Advertencia", "La carpeta seleccionada está vacía.")
            return

        # Verifica permisos de escritura en la carpeta de destino
        if not self.check_permissions(self.destination_directory):
            return
    
        organizer = FileOrganizer(self.source_directory, self.destination_directory)
        organizer.organizar_file() 
        messagebox.showinfo("Completado", "¡Archivos organizados con éxito!")

        # Bloquea el botón de organizar y habilita el botón de reiniciar
        self.organize_button.config(state=tk.DISABLED)
        self.reset_interface();

    def reset_interface(self):
        """
        Reinicia la interfaz para permitir una nueva acción.
        """
        # Limpia la selección de carpeta
        self.source_directory = ""
        self.label.config(text="Selecciona una carpeta para organizar:")

        # Habilita el botón de seleccionar carpeta y deshabilita los demás
        self.select_button.config(state=tk.NORMAL)
        self.organize_button.config(state=tk.DISABLED)

    def check_permissions(self, directory):
        """Verifica si el programa tiene permisos de escritura en la carpeta."""
        if not os.access(directory, os.W_OK):
            messagebox.showerror("Error", f"No tienes permisos para escribir en {directory}.")
            return False
        return True