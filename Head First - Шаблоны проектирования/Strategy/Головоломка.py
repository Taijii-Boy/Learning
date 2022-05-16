from abc import ABC, abstractmethod


class WeaponBehavior(ABC):
    @abstractmethod
    def use_weapon(self):
        pass


class KnifeBehavior(WeaponBehavior):
    def use_weapon(self):
        print('Удар ножом')


class AxeBehavior(WeaponBehavior):
    def use_weapon(self):
        print('Удар топором')


class SwordBehavior(WeaponBehavior):
    def use_weapon(self):
        print('Удар мечом')


class BowAndArrowBehavior(WeaponBehavior):
    def use_weapon(self):
        print('Выстрел из лука')


class Character(ABC):
    def __init__(self):
        self._weapon = WeaponBehavior()

    @property
    def weapon(self):
        return self._weapon

    @weapon.setter
    def weapon(self, new_weapon):
        if not isinstance(new_weapon, WeaponBehavior):
            raise TypeError('Invalid type of weapon...')

        self._weapon = new_weapon

    @abstractmethod
    def fight(self):
        pass


class King(Character):
    def __init__(self):
        self.weapon = SwordBehavior()

    def fight(self):
        print('Я кАроль!')
        self.weapon.use_weapon()


class Queen(Character):
    def __init__(self):
        self.weapon = BowAndArrowBehavior()

    def fight(self):
        print('Я прынцесса!')
        self.weapon.use_weapon()


class Troll(Character):
    def __init__(self):
        self.weapon = AxeBehavior()

    def fight(self):
        print('Я Троллль!')
        self.weapon.use_weapon()


class Knight(Character):
    def __init__(self):
        self.weapon = SwordBehavior()

    def fight(self):
        print('Я рыцарь!')
        self.weapon.use_weapon()


k = King()
k.weapon = AxeBehavior()
k.fight()