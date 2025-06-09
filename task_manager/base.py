from typing import Generator
from .utils import deco


class Task:
    def __init__(self, description: str, priority: str = "low", status: str = "pending"):
        self._description = description
        self._priority = priority
        self._status = status

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value: str):
        self._priority = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value: str):
        self._status = value

    def __str__(self):
        return f"[{self.status.upper()}] {self.priority.upper()}: {self._description}"

    def __add__(self, other):
        if isinstance(other, Task):
            return Task(f"{self._description} + {other._description}")
        raise TypeError("Can only add Task to Task")

    @deco("yellow")  
    def display(self):
        return str(self)

    

def task_generator(filepath: str) -> Generator[Task, None, None]:
    with open(filepath, 'r') as file:
        for line in file:
            desc, prio, status = line.strip().split('|')
            yield Task(desc, prio, status)
