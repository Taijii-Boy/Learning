from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def register_observer(self):
        pass

    @abstractmethod
    def remove_observer(self):
        pass

    @abstractmethod
    def notify_observer(self):
        pass


class Observer(ABC):
    @abstractmethod
    def update(self):
        pass


class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass


class WeatherData(Subject):
    def __init__(self):
        self.temperature = None
        self.humidity = None
        self.pressure = None
        self.observers = []

    @staticmethod
    def check_observer(observer):
        if not isinstance(observer, Observer):
            raise Exception('Прибор не поддерживается')
        return True

    def register_observer(self, observer):
        if self.check_observer(observer):
            self.observers.append(observer)

    def remove_observer(self, observer):
        if self.check_observer(observer):
            self.observers.remove(observer)

    def measures_changed(self):
        self.notify_observer()

    def notify_observer(self):
        for observer in self.observers:
            observer.update()

    def set_measurements(self, temp, hum, pres):
        self.temperature = temp
        self.humidity = hum
        self.pressure = pres
        self.measures_changed()


class CurrentConditionDisplay(Observer, DisplayElement):
    def __init__(self, wd_object: WeatherData):

        if not isinstance(wd_object, WeatherData):
            raise Exception('Неверный формат weather data')

        self.wd = wd_object
        self.wd.register_observer(self)
        self.temperature = self.wd.temperature
        self.humidity = self.wd.humidity
        self.pressure = self.wd.pressure

    def update(self):
        self.temperature = self.wd.temperature
        self.humidity = self.wd.humidity
        self.pressure = self.wd.pressure
        self.display()

    def display(self):
        print('==================')
        print('Current conditions:')
        print(f'Temperature: {self.temperature}\nHumidity: {self.humidity}\nPressure: {self.pressure}')


class ForecastDisplay(Observer, DisplayElement):
    def update(self):
        pass

    def display(self):
        pass


class StatisticsDisplay(Observer, DisplayElement):
    def update(self):
        pass

    def display(self):
        pass


if __name__ == '__main__':
    wd = WeatherData()
    current_display = CurrentConditionDisplay(wd)

    wd.set_measurements(31, 80, 740)
    wd.set_measurements(32, 80, 740)
    wd.set_measurements(32, 81, 740)
