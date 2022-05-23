from Devices import *


class Command(ABC):

    @abstractmethod
    def execute(self):
        pass


class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()


class GarageDoorOpenCommand(Command):
    def __init__(self, door: GarageDoor):
        self.door = door

    def execute(self):
        self.door.up()
