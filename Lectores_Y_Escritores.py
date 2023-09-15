"""Este código permite que varios hilos actúen como "lectores" que pueden leer el recurso 
compartido al mismo tiempo, pero solo un hilo actúa como "escritor" que puede modificar el recurso. 
Los semáforos mutex y escritura se utilizan para garantizar la exclusión mutua entre lectores y escritores,
y lectores_activos se utiliza para rastrear cuántos lectores están leyendo el recurso en un momento dado."""

import threading
import time

# Recurso compartido (por ejemplo, una base de datos o un archivo)
recurso = "Información inicial"

# Semáforos
mutex = threading.Semaphore(1)  # Para asegurar la exclusión mutua
lectores = threading.Semaphore(0)  # Para rastrear el número de lectores activos
escritura = threading.Semaphore(1)  # Para controlar la escritura

# Contador de lectores activos
lectores_activos = 0

def lector():
    global lectores_activos
    while True:
        mutex.acquire()
        lectores_activos += 1
        if lectores_activos == 1:
            escritura.acquire()
        mutex.release()

        # Leer el recurso
        print(f"Lector leyendo: {recurso}")

        mutex.acquire()
        lectores_activos -= 1
        if lectores_activos == 0:
            escritura.release()
        mutex.release()

        time.sleep(1)  # Simula el proceso de lectura

def escritor():
    while True:
        escritura.acquire()

        # Modificar el recurso
        global recurso
        recurso = "Información actualizada por el escritor"

        escritura.release()

        time.sleep(2)  # Simula el proceso de escritura

if __name__ == "__main__":
    # Crear hilos de lectores
    for _ in range(3):
        threading.Thread(target=lector).start()

    # Crear hilo de escritor
    threading.Thread(target=escritor).start()
