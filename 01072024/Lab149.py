from abc import ABC, abstractmethod

class ATB(ABC):
    @abstractmethod
    def perform_task1(self):
        pass
    @abstractmethod
    def perform_task2(self):
        pass

class Amit(ATB):
    def perform_task1(self):
        return "Task 1 performed"

    def perform_task2(self):
        return "Task 2 performed"


amit = Amit()
print(amit.perform_task1())
print(amit.perform_task2())
