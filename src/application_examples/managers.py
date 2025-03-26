# Comentario:
#   Este archivo implementa dos gestores de workers: uno para procesos y otro para hilos.
#   Cada clase extiende WorkerManager y define el método _worker para crear instancias
#   de Process o Thread respectivamente.
#
# Comment:
#   This file implements two worker managers: one for processes and one for threads.
#   Each class extends WorkerManager and defines the _worker method to create instances 
#   of Process or Thread respectively.

from interfaces import WorkerManager
from multiprocessing import Process
from threading import Thread

class ProcessManager(WorkerManager):
    def _worker(self, target: callable) -> Process:
        # Comentario: Crea un proceso que ejecutará la función target.
        # Comment: Creates a process that will execute the target function.
        return Process(target=target)

class ThreadManager(WorkerManager):
    def _worker(self, target: callable) -> Thread:
        # Comentario: Crea un hilo que ejecutará la función target.
        # Comment: Creates a thread that will execute the target function.
        return Thread(target=target)
