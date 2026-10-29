#abstract method
#1. Need to implement compulsary in sub classes
#2. No body only definition

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def stop():
        pass
#v1 = Vehicle()   #can't instantiate

class Bike(Vehicle):
    def start(self):
        print("Start method......")
    def stop(self):
        print("Stop method......")

b1 = Bike()
b1.start()
b1.stop()