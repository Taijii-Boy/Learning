from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def __init__(self):
        self.name = None


class Light(Device):
    def __init__(self):
        self.name = 'Светильник'

    def on(self):
        print(f'{self.name} включен')

    def off(self):
        print(f'{self.name} выключен')


class GarageDoor(Device):
    def __init__(self):
        self.name = 'Гаражная дверь'

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
    def __init__(self):
        self.name = 'Электрические приборы'

    def on(self):
        print(f'{self.name} включились')

    def off(self):
        print(f'{self.name} отключились')


class Stereo(Device):
    def __init__(self):
        self.name = 'Стереосистема'

    def on(self):
        print(f'{self.name} включилась')

    def off(self):
        print(f'{self.name} отключилась')

    def set_cd(self):
        pass

    def set_dvd(self):
        pass

    def set_radio(self):
        pass

    def set_volume(self):
        pass


class FaucetControl(Device):
    def __init__(self):
        self.name = 'Кран'

    def open_value(self):
        print(f'{self.name} включен')

    def close_value(self):
        print(f'{self.name} отключен')


class Hottub(Device):
    def __init__(self):
        self.name = 'Джакузи'

    def jets_on(self):
        print(f'{self.name} включено')

    def jets_off(self):
        print(f'{self.name} отключено')

    def circulate(self):
        pass

    def set_temperature(self):
        pass


class Termostate(Device):
    def __init__(self):
        self.name = 'Термостат'

    def set_temperature(self):
        print(f'{self.name}: устанавливается температура')


class SecurityControl(Device):
    def __init__(self):
        self.name = 'Охранная система'

    def arm(self):
        print(f'{self.name} включена')

    def disarm(self):
        print(f'{self.name} отключена')


class TV(Device):
    def __init__(self):
        self.name = 'Телевизор'

    def on(self):
        print(f'{self.name} включен')

    def off(self):
        print(f'{self.name} отключен')

    def set_input_channel(self):
        pass

    def set_volume(self):
        pass


class CeilingLight(Device):
    def __init__(self):
        self.name = 'Потолочный светильник'

    def on(self):
        print(f'{self.name} включен')

    def off(self):
        print(f'{self.name} выключен')

    def dim(self):
        print(f'{self.name}: яркость уменьшена')


class CeilingFan(Device):
    def __init__(self):
        self.name = 'Потолочный вентилятор'

    def high(self):
        print(f'{self.name} включен на полную')

    def medium(self):
        print(f'{self.name} включен на средней мощности')

    def low(self):
        print(f'{self.name} включен на малой мощности')

    def off(self):
        print(f'{self.name} выключен')

    def get_speed(self):
        pass


class Sprinkler(Device):
    def __init__(self):
        self.name = 'Поливалка'

    def water_on(self):
        print(f'{self.name} включена')

    def water_off(self):
        print(f'{self.name} выключена')


class OutdoorLight(Device):
    def __init__(self):
        self.name = 'Наружный светильник'

    def on(self):
        print(f'{self.name} включен')

    def off(self):
        print(f'{self.name} выключен')


class GardenLight(Device):
    def __init__(self):
        self.name = 'Садовый светильник '

    def manual_on(self):
        print(f'{self.name} включен')

    def manual_off(self):
        print(f'{self.name} выключен')

    def set_dusk_time(self):
        pass

    def set_down_time(self):
        pass
