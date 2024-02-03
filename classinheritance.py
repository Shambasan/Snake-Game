
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")

class Fish(Animal):
   def __init__(self):
       super().__init__()

   def breathe(self):
       super().breathe()
       print("Doing this in under water")
   def swim(self):
        print("moving under water")

naame = Fish()
#naame.swim()
# by using fish we class from the main class this is inheritance
naame.breathe()

# slicing

piano_keys = ["a","b","c","d","e","f","g"]

print(piano_keys[2:5])
print(piano_keys[2:])
print(piano_keys[:5])
print(piano_keys[:: -1])
