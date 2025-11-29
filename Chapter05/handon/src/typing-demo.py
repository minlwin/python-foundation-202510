from typing import Protocol

class Runnable(Protocol):
    def run(self) -> None:
        ...

def execute(obj: Runnable):
    obj.run()

class Runner:
    def run(self) -> None:
        print("Runner is Running")

execute(Runner())
