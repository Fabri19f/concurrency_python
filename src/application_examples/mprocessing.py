# Comentario:
#   Este archivo aplica procesamiento paralelo para modificar el brillo de imágenes.
#   Utiliza la biblioteca PIL para manejar imágenes y ajusta el brillo utilizando ImageEnhance.
#   Se crea una tarea por imagen encontrada en el directorio de origen.
#   Se advierte que la creación de muchos procesos puede impactar en la optimización del sistema,
#   por lo que este ejemplo es meramente ilustrativo y didáctico.
#   Sugerencia: Para una implementación más óptima, considere utilizar un pool de procesos (por ejemplo, multiprocessing.Pool).
#
# Comment:
#   This file applies parallel processing to adjust image brightness.
#   The PIL library is used to handle images and adjust brightness using ImageEnhance.
#   A task is created for each image found in the source directory.
#   Note that creating many processes can impact system performance,
#   so this example is purely illustrative and educational.
#   Suggestion: For a more optimal implementation, consider using a process pool (e.g., multiprocessing.Pool).
from interfaces import Task, TaskFactory
from managers import ProcessManager
from typing import List, Tuple
from PIL import Image, ImageEnhance
import os

class ProcessImage(Task):
    def __init__(
        self,
        name: str,
        source_path: str,
        destination_path: str,
        brightness_factor: float,
    ):
        # Comentario: Se inicializa la tarea asignando nombre y parámetros específicos para el procesamiento de la imagen.
        # Comment: The task is initialized by assigning a name and specific parameters for image processing.
        super().__init__(name)
        self.source_path = source_path
        self.destination_path = destination_path
        self.brightness_factor = brightness_factor

    def run(self) -> None:
        # Comentario:
        #   Este método abre la imagen desde el source_path, utiliza ImageEnhance para modificar el brillo y guarda el resultado.
        # Comment:
        #   This method opens the image from source_path, uses ImageEnhance to adjust brightness, and saves the result.
        image = Image.open(self.source_path)
        ImageEnhance.Brightness(image).enhance(self.brightness_factor).save(
            self.destination_path
        )

class ImageTaskFactory(TaskFactory):
    def __init__(
        self,
        source_directory: str,
        destination_directory: str,
        allowed_extensions: Tuple[str],
    ):
        # Comentario:
        #   El constructor recibe los directorios de origen y destino, y las extensiones de archivo permitidas.
        # Comment:
        #   The constructor receives the source and destination directories along with allowed file extensions.
        self.source_directory = source_directory
        self.destination_directory = destination_directory
        self.allowed_extensions = allowed_extensions

    def create_tasks(self, name_prefix: str) -> List[Task]:
        # Comentario:
        #   Se recorren los archivos en el directorio de origen y se crea una tarea para cada imagen cuya extensión esté permitida.
        # Comment:
        #   The source directory is scanned and a task is created for every image with an allowed extension.
        files: List[Task] = []

        path_files = [
            (
                os.path.join(self.source_directory, f),
                os.path.join(self.destination_directory, f),
            )
            for f in os.listdir(self.source_directory)
            if os.path.isfile(os.path.join(self.source_directory, f))
            and f.endswith(self.allowed_extensions)
        ]

        for i, (source_path, destination_path) in enumerate(path_files):
            files.append(
                ProcessImage(
                    name=f"{name_prefix}-{i}",
                    source_path=source_path,
                    destination_path=destination_path,
                    brightness_factor=0.5,
                )
            )
        return files


if __name__ == "__main__":
    # Comentario: Se instancia el ImageTaskFactory, se crean las tareas de imagen y se gestionan con ProcessManager.
    # Comment: Instantiate ImageTaskFactory, create image tasks and manage them with ProcessManager.
    tasks = ImageTaskFactory(
        source_directory="images/input",
        destination_directory="images/output",
        allowed_extensions=(".jpg",)
    ).create_tasks(name_prefix="Task")

    manager = ProcessManager()
    for task in tasks:
        manager.add_task(task)
    manager.run()
