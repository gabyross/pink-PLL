class Animal:
    def introduce_self(self):
        print( "I am a " + self.name)
    def make_asound(self):
        print(self.sound)

a1 = Animal()
a1.name = "dog"
a1.sound = "woof"

a2 = Animal()
a2.name = "cat"
a2.sound = "meow"

a1.introduce_self()
a1.make_asound()
a2.introduce_self()
a2.make_asound()


class Person:
    def__init__(self, n, p, i, animalOwned):
        self.name = n
        self.personality = p
        self.is_Sitting = i
        self.animalOwned = ao

    def.sit_down(self):
        self.is_Sitting = True

    def.stand_up(self):
        self.is_Sitting = False


p1 = Person("Andrix", "friendly", False)
p2 = Person("Gabs", "loving", True)

