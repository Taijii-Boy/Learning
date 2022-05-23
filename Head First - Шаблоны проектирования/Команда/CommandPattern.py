from Commands import *


class SimpleRemoteControl:
    def __init__(self):
        self.slot = None

    def set_command(self, command: Command):
        self.slot = command

    def button_was_pressed(self):
        self.slot.execute()


class RemoteControlTest:

    @staticmethod
    def main():
        remote = SimpleRemoteControl()
        garage_door = GarageDoor()
        light = Light()
        light_on = LightOnCommand(light)
        open_door = GarageDoorOpenCommand(garage_door)

        remote.set_command(light_on)
        remote.button_was_pressed()

        remote.set_command(open_door)
        remote.button_was_pressed()



if __name__ == '__main__':
    test = RemoteControlTest()
    test.main()
