# Comentario:
#   Este archivo demuestra la ejecución concurrente usando hilos.
#   Se define una función 'task' que simula una operación con retardo; luego se crean múltiples hilos
#   que ejecutan dicha función, uno por cada iteración.
#
# Comment:
#   This file demonstrates concurrent execution using threads.
#   A 'task' function is defined to simulate an operation with delay; multiple threads are created
#   to execute that function, one for each iteration.

from threading import Thread
from typing import List
from time import sleep

def task(name: str, seconds: float) -> None:
    # Comentario:
    #   La función 'task' imprime el inicio, espera 'seconds' segundos y luego imprime el fin de la tarea.
    #   Es un ejemplo básico de una función que simula un trabajo que consume tiempo.
    # Comment:
    #   The 'task' function prints a start message, waits for 'seconds' seconds, and then prints a completion message.
    #   It is a basic example of a time-consuming operation.
    print(f"Starting: {name}")
    sleep(seconds)
    print(f"Complete: {name}")

threads: List[Thread] = []

for i in range(10):
    # Comentario: Se crea y arranca un hilo para cada tarea.
    # Comment: Create and start a thread for each task.
    thread = Thread(target=task, args=(f"Thread {i}", i))
    thread.start()
    threads.append(thread)

for thread in threads:
    # Comentario: Se espera a que todos los hilos finalicen su ejecución.
    # Comment: Wait for all threads to finish.
    thread.join()
