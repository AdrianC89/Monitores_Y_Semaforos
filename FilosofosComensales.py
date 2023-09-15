"""En este código, cada filósofo (hilo) intenta adquirir dos cubiertos adyacentes antes de comer
y luego libera los cubiertos cuando ha terminado. Los semáforos se utilizan para controlar el
acceso a los cubiertos y evitar que dos filósofos tomen el mismo cubierto al mismo tiempo.
Este ejemplo simple ilustra cómo se resuelve el problema de los filósofos comensales para evitar el interbloqueo."""

import threading

N = 5  # Número de filósofos
cubiertos = [threading.Semaphore(1) for _ in range(N)]

def filosofo(filosofo_id):
    while True:
        # Filósofo piensa
        print(f"Filósofo {filosofo_id} está pensando.")
        # Filósofo intenta tomar palillos
        cubiertos[filosofo_id].acquire()
        cubiertos[(filosofo_id + 1) % N].acquire()

        # Filósofo come
        print(f"Filósofo {filosofo_id} está comiendo.")

        # Filósofo suelta los palillos
        cubiertos[filosofo_id].release()
        cubiertos[(filosofo_id + 1) % N].release()

if __name__ == "__main__":
    filosofos = []
    for i in range(N):
        filosofo_thread = threading.Thread(target=filosofo, args=(i,))
        filosofos.append(filosofo_thread)

    for thread in filosofos:
        thread.start()

    for thread in filosofos:
        thread.join()