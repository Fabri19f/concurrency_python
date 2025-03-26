# Comentario:
#   Este archivo ejemplifica la ejecución en paralelo mediante multiprocesamiento.
#   Se muestran dos métodos:
#    1. Creación manual de procesos, donde se instancia y se arranca un Process para cada tarea.
#    2. Uso de un Pool, que permite gestionar de forma más controlada el número de procesos.
#
# Comment:
#   This file exemplifies parallel execution using multiprocessing.
#   Two approaches are shown:
#    1. Manual creation of processes, where each task is run in its own Process.
#    2. Use of a Pool, which allows to control the number of processes more efficiently.

from multiprocessing import Process, Pool
from typing import List, Tuple
from time import sleep

def task(name: str, seconds: float) -> None:
    # Comentario:
    #   La función 'task' simula una tarea que imprime mensajes antes y después de un retardo.
    # Comment:
    #   The 'task' function simulates a task that prints messages before and after a delay.
    print(f"Starting: {name}")
    sleep(seconds)
    print(f"Complete: {name}")

if __name__ == "__main__":
    processes: List[Process] = []

    # Comentario: Creación manual de procesos: se inicia un proceso para cada tarea.
    # Comment: Manual creation of processes: a process is started for each task.
    for i in range(5):
        process = Process(target=task, args=(f"Process {i}", 2))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    print("All task complete.")

    print("\n --- Using a pool ---")

    task_args: List[Tuple[str, int]] = []

    # Comentario: Se preparan argumentos para ejecutar tareas en paralelo usando un Pool de procesos.
    # Comment: Prepare arguments to execute tasks in parallel using a Pool.
    for i in range(10):
        task_args.append((f"Pool Process {i}", 2))

    # Comentario: Un Pool gestiona un número fijo de procesos para optimizar el uso del sistema.
    # Comment: A Pool manages a fixed number of processes to optimize system resource usage.
    with Pool(processes=5) as pool:
        pool.starmap(task, task_args)

    print("All task complete.")
