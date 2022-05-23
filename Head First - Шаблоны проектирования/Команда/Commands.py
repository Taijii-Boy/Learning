from Devices import *


class Command(ABC):

    @abstractmethod
    def execute(self):
        pass


class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light
        self.name = light.name

    def execute(self):
        self.light.on()


class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light
        self.name = light.name

    def execute(self):
        self.light.off()


class GarageDoorOpenCommand(Command):
    def __init__(self, door: GarageDoor):
        self.door = door
        self.name = door.name

    def execute(self):
        self.door.up()


class GarageDoorCloseCommand(Command):
    def __init__(self, door: GarageDoor):
        self.door = door
        self.name = door.name

    def execute(self):
        self.door.down()


class CeilingFanHighCommand(Command):
    def __init__(self, fan: CeilingFan):
        self.fan = fan
        self.name = fan.name

    def execute(self):
        self.fan.high()


class CeilingFanMediumCommand(Command):
    def __init__(self, fan: CeilingFan):
        self.fan = fan
        self.name = fan.name

    def execute(self):
        self.fan.medium()


class CeilingFanLowCommand(Command):
    def __init__(self, fan: CeilingFan):
        self.fan = fan
        self.name = fan.name

    def execute(self):
        self.fan.low()


class CeilingFanOffCommand(Command):
    def __init__(self, fan: CeilingFan):
        self.fan = fan
        self.name = fan.name

    def execute(self):
        self.fan.off()



class ApplianceControlOnCommand(Command):
    def __init__(self, control: ApplianceControl):
        self.control = control
        self.name = control.name

    def execute(self):
        self.control.on()


class ApplianceControlOffCommand(Command):
    def __init__(self, control: ApplianceControl):
        self.control = control
        self.name = control.name

    def execute(self):
        self.control.off()


class StereoOnWithCDCommand(Command):
    def __init__(self, stereo: Stereo):
        self.stereo = stereo
        self.name = stereo.name

    def execute(self):
        self.stereo.on()
        self.stereo.set_cd()
        self.stereo.set_volume(11)

class StereoOnWithDVDCommand(Command):
    def __init__(self, stereo: Stereo):
        self.stereo = stereo
        self.name = stereo.name

    def execute(self):
        self.stereo.on()
        self.stereo.set_dvd()
        self.stereo.set_volume(11)


class StereoOffCommand(Command):
    def __init__(self, stereo: Stereo):
        self.stereo = stereo
        self.name = stereo.name

    def execute(self):
        self.stereo.off()


class FausetOpenCommand(Command):
    def __init__(self, fauset: FaucetControl):
        self.fauset = fauset
        self.name = fauset.name

    def execute(self):
        self.fauset.open_value()


class FausetCloseCommand(Command):
    def __init__(self, fauset: FaucetControl):
        self.fauset = fauset
        self.name = fauset.name

    def execute(self):
        self.fauset.close_value()


class HottubOnCommand(Command):
    def __init__(self, hottub: Hottub):
        self.hottub = hottub
        self.name = hottub.name

    def execute(self):
        self.hottub.jets_on()


class HottubOfCommand(Command):
    def __init__(self, hottub: Hottub):
        self.hottub = hottub
        self.name = hottub.name

    def execute(self):
        self.hottub.jets_off()


class TermostateSetCommand(Command):
    def __init__(self, termostate: Termostate):
        self.termostate = termostate
        self.name = termostate.name

    def execute(self):
        self.termostate.set_temperature()


class SecurityArmCommand(Command):
    def __init__(self, security: SecurityControl):
        self.security = security
        self.name = security.name

    def execute(self):
        self.security.arm()


class SecurityDisarmCommand(Command):
    def __init__(self, security: SecurityControl):
        self.security = security
        self.name = security.name

    def execute(self):
        self.security.disarm()


class TVOnCommand(Command):
    def __init__(self, tv: TV):
        self.tv = tv
        self.name = tv.name

    def execute(self):
        self.tv.on()


class TVOffCommand(Command):
    def __init__(self, tv: TV):
        self.tv = tv
        self.name = tv.name

    def execute(self):
        self.tv.off()


class CeilingLightOnCommand(Command):
    def __init__(self, light: CeilingLight):
        self.light = light
        self.name = light.name

    def execute(self):
        self.light.on()


class CeilingLightOffCommand(Command):
    def __init__(self, light: CeilingLight):
        self.light = light
        self.name = light.name

    def execute(self):
        self.light.off()


class CeilingLightDimCommand(Command):
    def __init__(self, light: CeilingLight):
        self.light = light
        self.name = light.name

    def execute(self):
        self.light.dim()


class SprinklerOnCommand(Command):
    def __init__(self, sprinkler: Sprinkler):
        self.sprinkler = sprinkler
        self.name = sprinkler.name

    def execute(self):
        self.sprinkler.water_on()


class SprinklerOffCommand(Command):
    def __init__(self, sprinkler: Sprinkler):
        self.sprinkler = sprinkler
        self.name = sprinkler.name

    def execute(self):
        self.sprinkler.water_off()


class OutdoorLightOnCommand(Command):
    def __init__(self, light: OutdoorLight):
        self.light = light
        self.name = light.name

    def execute(self):
        self.light.on()


class OutdoorLightOffCommand(Command):
    def __init__(self, light: OutdoorLight):
        self.light = light
        self.name = light.name

    def execute(self):
        self.light.off()


class GardenLightOnCommand(Command):
    def __init__(self, light: GardenLight):
        self.light = light
        self.name = light.name

    def execute(self):
        self.light.manual_on()


class GardenLightOffCommand(Command):
    def __init__(self, light: GardenLight):
        self.light = light
        self.name = light.name

    def execute(self):
        self.light.manual_off()
