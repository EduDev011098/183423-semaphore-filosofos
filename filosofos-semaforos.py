import threading
import time

class TenedorFilosofo(threading.Thread):
    def __init__(self, tenedores, filosofosNum):
        threading.Thread.__init__(self)
        self.tenedores = tenedores
        self.filosofosNum = filosofosNum
        self.datoTemporal =  self.filosofosNum  % 5
   
    def hilosFilosofos(self):
        while True:
            print("Filosofo", self.filosofosNum, "empezando a comer")
            time.sleep(2)
            print("Filosofo ", self.filosofosNum, "tomo el tenedor izquierdo")
            self.tenedores[self.filosofosNum].acquire()
            time.sleep(2)
            self.tenedores[self.filosofosNum].release()
            print("Filosofo ", self.filosofosNum, "tomo el tenedor derecho")
            self.tenedores[self.datoTemporal].acquire()
            time.sleep(2)
            print("Filosofo", self.filosofosNum, "comiendo")
            self.tenedores[self.datoTemporal].release()
            print("Filosofo ", self.filosofosNum, "dejo tenedor derecho")
            time.sleep(2)
            print("Filosofo ", self.filosofosNum, "dejo tenedor izquierdo")

            break  

    def run(self):
        self.hilosFilosofos()

tenedorArray = [1,1,1,1,1]

for i in range(5):
    tenedorArray[i] = threading.BoundedSemaphore(1)

for i in range(5):
    total = TenedorFilosofo(tenedorArray, i)
    total.start() 
    total.join()