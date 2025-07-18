from time import sleep 


class A:
    def run(self):
        for i in range(5):
            print("Abhi")
            sleep(1)

class B:
    def run(self):
        for  i in range(5):
            print("Ram")
            sleep(1)

t1=A()
t2=B()

t1.run()
t2.run()