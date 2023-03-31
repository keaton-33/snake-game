# Class Inheritance #

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale... exhale")

# super() refers to the 'super class' which is Animal and initializes Fish by copying everything from Animal
class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater")

    def swim(self):
        print("just keep swimming")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)

