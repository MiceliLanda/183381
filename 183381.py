import queue 
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import time

platillo = queue.Queue(maxsize=5)
filosofos = ['Lalo','Edwin','Gordo','Ventu','Miceli'] 

def Filosofos():
    if not platillo.full():
        filosofo = np.random.choice(filosofos,1)
        filosofos.remove(filosofo)
        platillo.put(filosofo)
        print(f'Filosofo : {filosofo} comiendo.....  Filosofos en cola:  {len(filosofos)}')
        time.sleep(np.random.randint(1,3))
                 
def verficarPlatillo():
    if not platillo.empty():
        cenando = platillo.get()
        platillo.task_done()
        print(f'Filosofo: {cenando} ah terminado de comer\n')        
        time.sleep(np.random.randint(1,3))

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=1) as executor:
        contador = 0
        aux = 5
        print(f'\nFilosofos en Cola: {len(filosofos)} \n')
        while True:
            executor.submit(Filosofos)
            executor.submit(verficarPlatillo)
            contador+=1
            if contador == aux:
                break
    print(f'Todos los Filosofos han terminado de comer')
