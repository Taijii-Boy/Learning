from Devices import *


class Command(ABC):

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


class GarageDoorOpenCommand(Command):
    def __init__(self, door: GarageDoor):
        self.door = door

    def execute(self):
        self.door.up()

    def undo(self):
        self.door.down()


class GarageDoorCloseCommand(Command):
    def __init__(self, door: GarageDoor):
        self.door = door

    def execute(self):
        self.door.down()

    def undo(self):
        self.door.up()


class CeilingFanHighCommand(Command):
    def __init__(self, fan: CeilingFan):
        self.fan = fan

    def execute(self):
        self.fan.high()

    def undo(self):
        pass


class CeilingFanMediumCommand(Command):
    def __init__(self, fan: CeilingFan):
        self.fan = fan

    def execute(self):
        self.fan.medium()

    def undo(self):
        pass


class CeilingFanLowCommand(Command):
    def __init__(self, fan: CeilingFan):
        self.fan = fan

    def execute(self):
        self.fan.low()

    def undo(self):
        pass


class CeilingFanOffCommand(Command):
    def __init__(self, fan: CeilingFan):
        self.fan = fan

    def execute(self):
        self.fan.off()

    def undo(self):
        pass


class ApplianceControlOnCommand(Command):
    def __init__(self, control: ApplianceControl):
        self.control = control

    def execute(self):
        self.control.on()

    def undo(self):
        self.control.off()


class ApplianceControlOffCommand(Command):
    def __init__(self, control: ApplianceControl):
        self.control = control

    def execute(self):
        self.control.off()

    def undo(self):
        self.control.on()


class StereoOnWithCDCommand(Command):
    def __init__(self, stereo: Stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.on()
        self.stereo.set_cd()
        self.stereo.set_volume(11)

    def undo(self):
        pass


class StereoOnWithDVDCommand(Command):
    def __init__(self, stereo: Stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.on()
        self.stereo.set_dvd()
        self.stereo.set_volume(11)

    def undo(self):
        pass


class StereoOffCommand(Command):
    def __init__(self, stereo: Stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.off()

    def undo(self):
        self.stereo.on()


class FausetOpenCommand(Command):
    def __init__(self, fauset: FaucetControl):
        self.fauset = fauset

    def execute(self):
        self.fauset.open_value()

    def undo(self):
        self.fauset.close_value()


class FausetCloseCommand(Command):
    def __init__(self, fauset: FaucetControl):
        self.fauset = fauset

    def execute(self):
        self.fauset.close_value()

    def undo(self):
        self.fauset.open_value()


class HottubOnCommand(Command):
    def __init__(self, hottub: Hottub):
        self.hottub = hottub

    def execute(self):
        self.hottub.jets_on()

    def undo(self):
        self.hottub.jets_off()


class HottubOfCommand(Command):
    def __init__(self, hottub: Hottub):
        self.hottub = hottub

    def execute(self):
        self.hottub.jets_off()

    def undo(self):
        self.hottub.jets_on()


class TermostateSetCommand(Command):
    def __init__(self, termostate: Termostate):
        self.termostate = termostate

    def execute(self):
        self.termostate.set_temperature()

    def undo(self):
        pass


class SecurityArmCommand(Command):
    def __init__(self, security: SecurityControl):
        self.security = security

    def execute(self):
        self.security.arm()

    def undo(self):
        self.security.disarm()


class SecurityDisarmCommand(Command):
    def __init__(self, security: SecurityControl):
        self.security = security

    def execute(self):
        self.security.disarm()

    def undo(self):
        self.security.arm()


class TVOnCommand(Command):
    def __init__(self, tv: TV):
        self.tv = tv

    def execute(self):
        self.tv.on()

    def undo(self):
        self.tv.off()


class TVOffCommand(Command):
    def __init__(self, tv: TV):
        self.tv = tv

    def execute(self):
        self.tv.off()

    def undo(self):
        self.tv.on()


class CeilingLightOnCommand(Command):
    def __init__(self, light: CeilingLight):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class CeilingLightOffCommand(Command):
    def __init__(self, light: CeilingLight):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


class CeilingLightDimCommand(Command):
    def __init__(self, light: CeilingLight):
        self.light = light

    def execute(self):
        self.light.dim()

    def undo(self):
        pass


class SprinklerOnCommand(Command):
    def __init__(self, sprinkler: Sprinkler):
        self.sprinkler = sprinkler

    def execute(self):
        self.sprinkler.water_on()

    def undo(self):
        self.sprinkler.water_off()


class SprinklerOffCommand(Command):
    def __init__(self, sprinkler: Sprinkler):
        self.sprinkler = sprinkler

    def execute(self):
        self.sprinkler.water_off()

    def undo(self):
        self.sprinkler.water_on()


class OutdoorLightOnCommand(Command):
    def __init__(self, light: OutdoorLight):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class OutdoorLightOffCommand(Command):
    def __init__(self, light: OutdoorLight):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


class GardenLightOnCommand(Command):
    def __init__(self, light: GardenLight):
        self.light = light

    def execute(self):
        self.light.manual_on()

    def undo(self):
        self.light.manual_off()


class GardenLightOffCommand(Command):
    def __init__(self, light: GardenLight):
        self.light = light

    def execute(self):
        self.light.manual_off()

    def undo(self):
        self.light.manual_on()


class NoCommand(Command):
    def execute(self):
        pass

    def undo(self):
        pass
