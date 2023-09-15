"""Este código representa un búfer limitado en el que un productor coloca elementos en el búfer y un 
consumidor los retira. Los semáforos empty y full controlan cuándo se pueden agregar elementos y 
cuándo se pueden retirar elementos del búfer, y el semáforo mutex garantiza la exclusión 
mutua al acceder al búfer compartido."""

import threading
import time

# Tamaño máximo del búfer
BUFFER_SIZE = 3

# Búfer compartido
buffer = []

# Semáforos
mutex = threading.Semaphore(1)  # Semáforo para la exclusión mutua
empty = threading.Semaphore(BUFFER_SIZE)  # Semáforo para elementos vacíos
full = threading.Semaphore(0)  # Semáforo para elementos llenos

def productor():
    for i in range(1, 11):  # Produce 10 elementos
        item = f"Item {i}"
        empty.acquire()  # Espera si el búfer está lleno
        mutex.acquire()  # Accede al búfer de manera exclusiva
        buffer.append(item)  # Agrega el elemento al búfer
        mutex.release()  # Libera el búfer
        full.release()  # Avisa que hay un elemento disponible
        time.sleep(1)  # Simula un proceso de producción

def consumidor():
    for _ in range(10):  # Consume 10 elementos
        full.acquire()  # Espera si el búfer está vacío
        mutex.acquire()  # Accede al búfer de manera exclusiva
        item = buffer.pop(0)  # Consume el primer elemento del búfer
        mutex.release()  # Libera el búfer
        empty.release()  # Avisa que hay espacio disponible en el búfer
        print(f"Consumido: {item}")
        time.sleep(1)  # Simula un proceso de consumo

if __name__ == "__main__":
    productor_thread = threading.Thread(target=productor)
    consumidor_thread = threading.Thread(target=consumidor)

    productor_thread.start()
    consumidor_thread.start()

    productor_thread.join()
    consumidor_thread.join()
