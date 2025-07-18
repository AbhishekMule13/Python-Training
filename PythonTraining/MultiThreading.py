
from time import sleep
from threading import Thread

class a(Thread):
    def run(self):
        for i in range(5):
            print("ram")
            sleep(1)

class b(Thread):
    def run(self):
        for i in range(5):
            print("Sita")
            sleep(1)


t1=a()
t2=b()

t1.start()
t2.start()

t1.join()
t2.join() 

print("DADA")