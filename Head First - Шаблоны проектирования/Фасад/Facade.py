class Tuner:
    def __init__(self, amplifier):
        self.amplifier = amplifier
        self.name = 'Тюнер'

    def on(self):
        print(f'{self.name} включен')

    def off(self):
        print(f'{self.name} выключен')

    def set_am(self, am):
        pass

    def set_fm(self, fm):
        pass

    def set_frequency(self, freq):
        pass

    def to_string(self):
        pass


class Amplifier:
    def __init__(self):
        self.tuner = None
        self.dvd_player = None
        self.cd_player = None
        self.name = 'Усилитель'

    def on(self):
        print(f'{self.name} включен')

    def off(self):
        print(f'{self.name} выключен')

    def set_cd(self):
        pass

    def set_streaming_player(self, player):
        if isinstance(player, CDPlayer):
            self.cd_player = player
        elif isinstance(player, DVDPlayer):
            self.dvd_player = player
        else:
            raise ValueError('Неправильный какой-то плеер')

    def set_dvd(self):
        pass

    def set_stereo_sound(self):
        pass

    def set_surround_sound(self):
        pass

    def set_tuner(self, tuner: Tuner):
        self.tuner = tuner

    def set_volume(self, volume):
        pass

    def to_string(self):
        pass


class Screen:
    def __init__(self):
        self.name = 'Экран'

    def up(self):
        print(f'{self.name} открылся')

    def down(self):
        print(f'{self.name} закрылся')


class PopcornPopper:
    def __init__(self):
        self.name = 'Машинка для попкорна'

    def on(self):
        print(f'{self.name} включилась')

    def off(self):
        print(f'{self.name} выключилась')

    def pop(self):
        print('Взяли попкорн')

    def to_string(self):
        pass


class CDPlayer:
    def __init__(self, amplifier):
        self.name = 'CD-плеер'
        self.amplifier = amplifier

    def on(self):
        print(f'{self.name} включен')

    def off(self):
        print(f'{self.name} выключен')

    def eject(self):
        print('Извлекаем диск')

    def pause(self):
        print('Ставим на паузу')

    def play(self, movie: str):
        print(f'Проигрываем {movie}')

    def stop(self):
        print('Заканчиваем проигрывание CD')

    def to_string(self):
        pass


class DVDPlayer:
    def __init__(self, amplifier):
        self.name = 'DVD-плеер'
        self.amplifier = amplifier

    def on(self):
        print(f'{self.name} включен')

    def off(self):
        print(f'{self.name} выключен')

    def eject(self):
        print('Извлекаем диск')

    def pause(self):
        print('Ставим на паузу')

    def play(self, movie):
        print(f'Проигрываем {movie}')

    def stop(self):
        print('Заканчиваем проигрывание DVD')

    def set_surround_audio(self):
        pass

    def set_two_channel_audio(self):
        pass

    def to_string(self):
        pass


class TheaterLights:
    def __init__(self):
        self.name = 'Освещение'

    def on(self):
        print(f'{self.name} включено')

    def off(self):
        print(f'{self.name} выключено')

    def dim(self, amount):
        print(f'Меняем яркость на {amount}')


class Projector:
    def __init__(self):
        self.name = 'Проектор'
        self.dvd_player = None

    def on(self):
        print(f'{self.name} включен')

    def off(self):
        print(f'{self.name} выключен')

    def set_player(self, player):
        self.dvd_player = player

    def tv_mode(self):
        pass

    def wide_screen_mode(self):
        pass

    def to_string(self):
        pass


class HomeTheaterFacade:
    def __init__(self, amp: Amplifier, tuner: Tuner, player, projector: Projector,
                 screen: Screen, lights: TheaterLights, popper: PopcornPopper):
        self.amp = amp
        self.tuner = tuner
        self.player = player
        self.projector = projector
        self.screen = screen
        self.lights = lights
        self.popper = popper

    def watch_movie(self, movie: str):
        print('Готовимся к просмотру:')
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wide_screen_mode()
        self.amp.on()
        self.amp.set_streaming_player(self.player)
        self.amp.set_surround_sound()
        self.player.on()
        self.player.play(movie)

    def end_movie(self):
        print('Заканчиваем просмотр кинца')
        self.popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.player.stop()
        self.player.off()


class HomeTheaterTest:
    def main(self):
        amp = Amplifier()
        tuner = Tuner(amp)
        dvd = DVDPlayer(amp)
        screen = Screen()
        pop = PopcornPopper()
        projector = Projector()
        light = TheaterLights()
        facade = HomeTheaterFacade(amp, tuner, dvd, projector, screen, light, pop)

        facade.watch_movie('Зорро')
        facade.end_movie()


if __name__ == '__main__':
    test = HomeTheaterTest()
    test.main()