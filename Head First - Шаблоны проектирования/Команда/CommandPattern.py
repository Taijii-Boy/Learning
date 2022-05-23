from Commands import *


class SimpleRemoteControl:
    def __init__(self):
        self.slot = None

    def set_command(self, command: Command):
        self.slot = command

    def button_was_pressed(self):
        self.slot.execute()


class SimpleRemoteControlTest:

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


class RemoteControl:
    def __init__(self):
        self.on_commands = {}
        self.off_commands = {}

    def set_command(self, slot: int, on_command: Command, off_command: Command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_was_pressed(self, slot: int):
        self.on_commands[slot].execute()

    def off_button_was_pressed(self, slot: int):
        self.off_commands[slot].execute()

    def to_string(self) -> list:
        string_buffer = []
        string_buffer.append('\n-------Remote Control -------')
        for slot in range(7):
            try:
                string_buffer.append(f'[slot {slot}] {self.on_commands[slot].name} -- {self.off_commands[slot].name}')
            except:
                string_buffer.append(f'[slot {slot}] Слот пустой')
        string_buffer.append('-'*30)
        return string_buffer


class RemoteLoader:
    def main(self):
        remote = RemoteControl()
        living_room_light = Light('Светильник в гостиной')
        kitchen_light = Light('Светильник на кухне')
        ceiling_fun = CeilingFan('Вентилятор в гостиной')
        garage_door = GarageDoor()
        stereo = Stereo('Стерео система в гостиной')

        living_room_light_on = LightOnCommand(living_room_light)
        living_room_light_off = LightOffCommand(living_room_light)
        kitchen_light_on = LightOnCommand(kitchen_light)
        kitchen_light_off = LightOffCommand(kitchen_light)

        ceiling_fun_on = CeilingFanHighCommand(ceiling_fun)
        ceiling_fun_off = CeilingFanOffCommand(ceiling_fun)

        garage_door_up = GarageDoorOpenCommand(garage_door)
        garage_door_down = GarageDoorCloseCommand(garage_door)

        stereo_on_with_cd = StereoOnWithCDCommand(stereo)
        stereo_off = StereoOffCommand(stereo)

        remote.set_command(0, living_room_light_on, living_room_light_off)
        remote.set_command(1, kitchen_light_on, kitchen_light_off)
        remote.set_command(2, ceiling_fun_on, ceiling_fun_off)
        remote.set_command(3, garage_door_up, garage_door_down)
        remote.set_command(4, stereo_on_with_cd, stereo_off)

        slots_information = remote.to_string()
        for slot in slots_information:
            print(slot)

        remote.on_button_was_pressed(0)
        remote.off_button_was_pressed(0)
        remote.on_button_was_pressed(1)
        remote.off_button_was_pressed(1)
        remote.on_button_was_pressed(2)
        remote.off_button_was_pressed(2)
        remote.on_button_was_pressed(3)
        remote.off_button_was_pressed(3)
        remote.on_button_was_pressed(4)
        remote.off_button_was_pressed(4)


if __name__ == '__main__':
    test = RemoteLoader()
    test.main()
