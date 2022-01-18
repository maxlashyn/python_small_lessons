from abc import ABC, abstractmethod


class Homo(ABC):
    def __init__(self, age, weight):
        self.age = age
        self.weight = weight

    def can_run(self):
        return True

    @abstractmethod
    def can_eat_meat(self):
        pass

class Rabbit():
    def can_eat_carrot(self):
        return True

class Sapiens(Homo, Rabbit):
    def can_eat_grass(self):
        return True

    def can_eat_meat(self):
        return True

    def can_eat_leaves(self):
        return False


class Parantrop(Homo):
    def can_eat_grass(self):
        return True

    def can_eat_meat(self):
        return False

    def can_eat_leaves(self):
        return True


class Australopitecus(Homo):
    def can_eat_grass(self):
        return True

    def can_eat_meat(self):
        return False

    def can_eat_leaves(self):
        return True

class Erectus(Homo):
    def can_eat_meat(self):
        return True


class Tundra:
    def can_live(self, homo: Homo):
        return homo.can_eat_meat()

    def can_eat_cattor(self, rabbit: Rabbit):
        return rabbit.can_eat_carrot()

tundra = Tundra()

assert tundra.can_live(Erectus(10, 10))
assert not tundra.can_live(Parantrop(10, 10))
assert tundra.can_eat_cattor(Sapiens(0,0))


class Character(ABC):
    pass

class Action(ABC):
    @abstractmethod
    def action(self):
        pass

class SwordsMan(Action):
    def chop(self):
        pass

    def action(self):
        self.chop()

class Nipper(Action):
    def bite(self):
        pass

    def action(self):
        self.bite()

class Human(Character, SwordsMan):
    pass

class Orc(Character, SwordsMan):
    pass

class Werwolf(Character, Nipper):
    pass

class Wolf(Character, Nipper):
    pass

human = Human()
while True:
    if isinstance(human, Action):
        human.action()
