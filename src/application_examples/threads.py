# Comentario:
#   Este archivo muestra cómo usar hilos (threads) para la ejecución concurrente de tareas.
#   Se definen clases que heredan de una clase abstracta 'Task', y se utiliza un ThreadManager para ejecutar cada tarea en un hilo.
#   Se explica el uso de 'super()' para invocar el inicializador de la clase base.
#
# Comment:
#   This file demonstrates how to use threads for concurrent task execution.
#   Classes inheriting from the abstract 'Task' are defined, and a ThreadManager is used to run each task in a separate thread.
#   The use of 'super()' is explained to invoke the base class initializer.
from interfaces import Task, TaskFactory
from managers import ThreadManager
from time import sleep
from typing import List
from datetime import datetime

class SendMessage(Task):
    def __init__(self, name: str, message: str, delay: int = 2):
        # Comentario: Llama al constructor de la clase base Task para inicializar 'name'.
        # Comment: Call the base class Task constructor to initialize 'name'.
        super().__init__(name)
        self.message = message
        self.delay = delay

    def run(self) -> None:
        # Comentario:
        #   Este método se encarga de ejecutar la tarea.
        #   Se muestra cómo imprimir la fecha actual, usar un retardo con sleep y completar el trabajo.
        # Comment:
        #   This method runs the task.
        #   It shows how to print the current date-time, use a delay with sleep, and finish the work.
        print(
            f"[{datetime.now().isoformat()}] {self.name} - Starting: {self.message}",
            flush=True,
        )
        sleep(self.delay)
        print(
            f"[{datetime.now().isoformat()}] {self.name} - Complete: {self.message}",
            flush=True,
        )

class MessageTaskFactory(TaskFactory):
    def __init__(self, messages: List[str]):
        self.messages = messages

    def create_tasks(self, name_prefix: str) -> List[Task]:
        # Comentario: Se crea y retorna una lista de tareas. Cada tarea recibe un nombre único y se asigna el mensaje correspondiente.
        # Comment: Creates and returns a list of tasks, each with a unique name and the assigned message.
        return [
            SendMessage(name=f"{name_prefix}-{i+1}", message=msg)
            for i, msg in enumerate(self.messages)
        ]

if __name__ == "__main__":
    # Comentario: Se generan tareas utilizando la fábrica actualizada y se gestionan mediante ThreadManager.
    # Comment: Tasks are generated using the updated factory and managed with ThreadManager.
    tasks = MessageTaskFactory(
        messages=["Message 1", "Message 2", "Message 3"]
    ).create_tasks(name_prefix="Example")

    manager = ThreadManager()

    for task in tasks:
        manager.add_task(task)

    manager.run()
