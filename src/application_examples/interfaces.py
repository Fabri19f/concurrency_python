# Comentario:
#   Este archivo define las interfaces y clases abstractas que se utilizarán para crear tareas (Task),
#   fábricas de tareas (TaskFactory) y gestores de trabajadores (WorkerManager).
#   Se utilizan decoradores como @abstractmethod para definir contratos en clases base.
#
# Comment:
#   This file defines interfaces and abstract classes used to create tasks (Task),
#   task factories (TaskFactory), and worker managers (WorkerManager).
#   Decorators such as @abstractmethod are used to enforce contracts in base classes.

from abc import ABC, abstractmethod
from typing import List, Union
from multiprocessing import Process
from threading import Thread

class Task(ABC):
    def __init__(self, name: str):
        # Comentario: Inicializa el nombre de la tarea, que sirve para identificarla.
        # Comment: Initializes the task name, used for identification.
        self.name = name

    @abstractmethod
    def run(self) -> None:
        # Comentario: Método abstracto que debe implementarse para definir la ejecución de la tarea.
        # Comment: Abstract method to define how the task is executed; must be implemented in subclasses.
        pass

    def __repr__(self) -> str:
        # Comentario: Representación textual de la tarea para facilitar su depuración.
        # Comment: Textual representation of the task to ease debugging.
        return f"<Task: {self.name}>"

class TaskFactory(ABC):
    @abstractmethod
    def create_tasks(self, name_prefix: str) -> List[Task]:
        # Comentario: Método abstracto que crea y retorna una lista de tareas.
        # Comment: Abstract method to create and return a list of tasks.
        pass

class WorkerManager(ABC):
    def __init__(self):
        # Comentario: Lista de workers (procesos o hilos) que ejecutarán las tareas.
        # Comment: List of workers (processes or threads) that will execute the tasks.
        self._workers: List[Union[Process, Thread]] = []
        
    @abstractmethod
    def _worker(self, target: callable) -> Union[Process, Thread]:
        # Comentario: Método abstracto para crear un worker con el target (función a ejecutar).
        # Comment: Abstract method to create a worker with the given target function.
        pass

    def add_task(self, task: Task) -> None:
        # Comentario: Asocia la función 'run' de la tarea a un worker y lo añade a la lista.
        # Comment: Associates the task's run function to a worker and adds it to the list.
        self._workers.append(
            self._worker(task.run)
        )

    def start_all(self) -> None:
        # Comentario: Inicia todos los workers, arrancando la ejecución de cada tarea.
        # Comment: Starts all workers, launching the execution of each task.
        for worker in self._workers:
            try:
                worker.start()
            except Exception as e:
                print(f"Error starting worker: {e}", flush=True)

    def wait_all(self) -> None:
        # Comentario: Espera a que todos los workers finalicen.
        # Comment: Waits for all workers to complete.
        for worker in self._workers:
            try:
                worker.join()
            except Exception as e:
                print(f"Error joining worker: {e}", flush=True)

    def run(self) -> None:
        # Comentario: Método que inicia y espera la finalización de todas las tareas.
        # Comment: Method that starts and waits for the completion of all tasks.
        self.start_all()
        self.wait_all()
