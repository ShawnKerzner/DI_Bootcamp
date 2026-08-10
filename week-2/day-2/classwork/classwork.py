class Animal():
    def __init__(self, type, number_legs, sound):
        self.type = type
        self.number_legs = number_legs
        self.sound = sound


class Dog(Animal):
    def __init__(self, type, number_legs, sound, fetch_ball):
        super().__init__(type, number_legs, sound)
        # Or : Animal.__init__(self,type, number_legs, sound)
        self.fetch_ball = fetch_ball


rex = Dog('dog', 4, "wouaf", True)
print('This animal is a:', rex.type)
# >> This animal is a dog

print('This dog has', rex.number_legs, ' legs')
# >> This dog has 4 legs

print('This dog makes the sound ', rex.sound)
# >> This dog makes the sound wouaf

print('Does this dog fetchs balls ? ', rex.fetch_ball)
# >> Does this dog fetchs balls ? True


class Circle:
    def __init__(self, diameter):
        self.diameter = diameter

    def grow(self, factor=2):
        """grows the circle's diameter by factor"""
        self.diameter = self.diameter * factor


class NewCircle(Circle):
    def grow(self, factor=2):
        """grows the area by factor..."""
        self.diameter = (self.diameter * factor * 2)


nc = NewCircle(1)
print(nc.diameter)

nc.grow()

print(nc.diameter)


class MyClass(object):
    def func(self):
        print("I'm being called from the Parent class")


class ChildClass(MyClass):
    def func(self):
        print("I'm actually being called from the Child class")
        print("But...")
        # Calling the `func()` method from the Parent class.
        super(ChildClass, self).func()


my_instance_2 = ChildClass()
my_instance_2.func()


class Door():
    def __init__(self, is_opened=False):
        self.is_opened = is_opened

    def open_door(self):
        self.is_opened = True

    def closed_door(self):
        self.is_opened = False


class BlockedDoor(Door):

    def open_door(self):
        raise Exception("Door cannot be opened")

    def closed_door(self):
        raise Exception("Door cannot be closed")


my_door = BlockedDoor()
my_door.open_door()
