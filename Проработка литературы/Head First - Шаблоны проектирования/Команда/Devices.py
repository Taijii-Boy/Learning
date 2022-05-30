from abc import ABC, abstractmethod
from enum import Enum


class Speed(Enum):
    HIGH = 3
    MEDIUM = 2
    LOW = 1
    OFF = 0


class Device(ABC):
    @abstractmethod
    def __init__(self):
        self.name = None


class Light(Device):
    def __init__(self, name='Светильник'):
        self.name = name

    def on(self):
        print(f'{self.name} включен')

    def off(self):
        print(f'{self.name} выключен')


class GarageDoor(Device):
    def __init__(self, name='Гаражная дверь'):
        self.name = name

    def up(self):
        print(f'{self.name} открывается')

    def down(self):
        print(f'{self.name} закрывается')

    def stop(self):
        print(f'{self.name} остановилась')

    def light_on(self):
        print('Светильник гаража включен')

    def light_off(self):
        print('Светильник гаража выключен')


class ApplianceControl(Device):
    def __init__(self, name='Электрические приборы'):
        self.name = name

    def on(self):
        print(f'{self.name} включились')

    def off(self):
        print(f'{self.name} отключились')


class Stereo(Device):
    def __init__(self, name='Стереосистема'):
        self.name = name

    def on(self):
        print(f'{self.name} включилась')

    def off(self):
        print(f'{self.name} отключилась')

    def set_cd(self):
        print(f'устанавливаем CD')

    def set_dvd(self):
        print(f'устанавливаем DVD')

    def set_radio(self, value):
        print(f'включаем радио {value}')

    def set_volume(self, value):
        print(f'устанавливаем громкость на {value}')


class FaucetControl(Device):
    def __init__(self, name='Кран'):
        self.name = name

    def open_value(self):
        print(f'{self.name} включен')

    def close_value(self):
        print(f'{self.name} отключен')


class Hottub(Device):
    def __init__(self, name='Джакузи'):
        self.name = name

    def jets_on(self):
        print(f'{self.name} включено')

    def jets_off(self):
        print(f'{self.name} отключено')

    def circulate(self):
        pass

    def set_temperature(self):
        pass


class Termostate(Device):
    def __init__(self, name='Термостат'):
        self.name = name

    def set_temperature(self):
        print(f'{self.name}: устанавливается температура')


class SecurityControl(Device):
    def __init__(self, name='Охранная система'):
        self.name = name

    def arm(self):
        print(f'{self.name} включена')

    def disarm(self):
        print(f'{self.name} отключена')


class TV(Device):
    def __init__(self, name='Телевизор'):
        self.name = name

    def on(self):
        print(f'{self.name} включен')

    def off(self):
        print(f'{self.name} отключен')

    def set_input_channel(self):
        pass

    def set_volume(self):
        pass


class CeilingLight(Device):
    def __init__(self, name='Потолочный светильник'):
        self.name = name

    def on(self):
        print(f'{self.name} включен')

    def off(self):
        print(f'{self.name} выключен')

    def dim(self):
        print(f'{self.name}: яркость уменьшена')


class CeilingFan(Device):

    def __init__(self, name='Потолочный вентилятор'):
        self.name = name
        self.speed = Speed.OFF

    def high(self):
        self.speed = Speed.HIGH
        print(f'{self.name} включен на высокой скорости')

    def medium(self):
        self.speed = Speed.MEDIUM
        print(f'{self.name} включен на средней мощности')

    def low(self):
        self.speed = Speed.LOW
        print(f'{self.name} включен на малой мощности')

    def off(self):
        self.speed = Speed.OFF
        print(f'{self.name} выключен')

    def get_speed(self):
        return self.speed


class Sprinkler(Device):
    def __init__(self, name='Поливалка'):
        self.name = name

    def water_on(self):
        print(f'{self.name} включена')

    def water_off(self):
        print(f'{self.name} выключена')


class OutdoorLight(Device):
    def __init__(self, name='Наружный светильник'):
        self.name = name

    def on(self):
        print(f'{self.name} включен')

    def off(self):
        print(f'{self.name} выключен')


class GardenLight(Device):
    def __init__(self, name='Садовый светильник'):
        self.name = name

    def manual_on(self):
        print(f'{self.name} включен')

    def manual_off(self):
        print(f'{self.name} выключен')

    def set_dusk_time(self):
        pass

    def set_down_time(self):
        pass
