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
        self.no_command = NoCommand()
        self.undo_command = NoCommand()

        for slot in range(7):
            self.on_commands[slot] = self.no_command
            self.off_commands[slot] = self.no_command

    def set_command(self, slot: int, on_command: Command, off_command: Command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_was_pressed(self, slot: int):
        self.on_commands[slot].execute()
        self.undo_command = self.on_commands[slot]

    def off_button_was_pressed(self, slot: int):
        self.off_commands[slot].execute()
        self.undo_command = self.off_commands[slot]

    def undo_button_was_pushed(self):
        self.undo_command.undo()

    def to_string(self) -> list:
        string_buffer = []
        string_buffer.append('\n-------Remote Control -------')

        for slot in range(7):
            on_command_text = f'[slot {slot}] {self.on_commands[slot].__class__.__name__} -- '
            off_command_text = f'{self.off_commands[slot].__class__.__name__}'
            string_buffer.append(on_command_text + off_command_text)

        string_buffer.append(f'[undo] {self.undo_command.__class__.__name__}')
        string_buffer.append('-' * 30)
        return string_buffer


class RemoteLoader:
    def main(self):
        remote_control = RemoteControl()
        light = Light('Светильник в гостиной')
        tv = TV('ТВ в гостиной')
        stereo = Stereo('Стерео в гостиной')
        hottub = Hottub()

        light_on_command = LightOnCommand(light)
        tv_on_command = TVOnCommand(tv)
        stereo_on_command = StereoOnWithCDCommand(stereo)
        hottub_on_command = HottubOnCommand(hottub)

        light_off_command = LightOffCommand(light)
        tv_off_command = TVOffCommand(tv)
        stereo_off_command = StereoOffCommand(stereo)
        hottub_off_command = HottubOffCommand(hottub)

        party_on = [light_on_command, tv_on_command, stereo_on_command, hottub_on_command]
        party_off = [light_off_command, tv_off_command, stereo_off_command, hottub_off_command]

        party_on_macro = MacroCommand(party_on)
        party_off_macro = MacroCommand(party_off)

        remote_control.set_command(0, party_on_macro, party_off_macro)

        self.print_slots_information(remote_control)
        print('-------Party on!!!!------')
        remote_control.on_button_was_pressed(0)
        print('-------Party off!!!!------')
        remote_control.off_button_was_pressed(0)


    @staticmethod
    def print_slots_information(remote):
        slots_information = remote.to_string()
        for slot in slots_information:
            print(slot)


if __name__ == '__main__':
    test = RemoteLoader()
    test.main()
