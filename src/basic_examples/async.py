# Comentario: 
#   Este archivo utiliza AsyncIO para gestionar tareas asíncronas.
#   La función 'task' simula una tarea con retardo mediante asyncio.sleep.
#   La función 'main' agrupa múltiples tareas concurrentes utilizando asyncio.gather.
#   Finalmente, asyncio.run se encarga de iniciar y cerrar el event loop.
#
# Comment:
#   This file uses AsyncIO to manage asynchronous tasks.
#   The 'task' function simulates a task with delay using asyncio.sleep.
#   The 'main' function gathers multiple concurrent tasks with asyncio.gather.
#   Finally, asyncio.run starts and properly closes the event loop.

import asyncio

async def task(name: str, seconds: float) -> None:
    # Comentario: Imprime el inicio de la tarea, espera 'seconds' segundos y luego imprime la finalización.
    # Comment: Print the start of the task, wait for 'seconds' seconds and then print its completion.
    print(f"Starting: {name}")
    await asyncio.sleep(seconds)  # await pausa la ejecución de la corutina hasta que se complete el sleep
    print(f"Complete: {name}")

async def main():
    # Comentario: Se crean 10 tareas de 'task' y se ejecutan en forma concurrente.
    # Comment: Create 10 'task' routines and execute them concurrently.
    await asyncio.gather(*[task(f"Coroutine {i}", 2) for i in range(10)])

# Comentario: asyncio.run inicia el event loop, ejecuta 'main' y se encarga del cierre del loop.
# Comment: asyncio.run starts the event loop, executes 'main', and properly shuts down the loop.
asyncio.run(main())
