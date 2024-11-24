from animal import Animal

class Dog(Animal):
    def __init__(self, species, legs, fur, breed):
        super().__init__(species, legs, fur)
        self.breed = breed

    def walk(self):
        return f"The {self.breed} has {self.legs} legs."

    def eat(self):
        return f"The {self.breed} is eating food."

    def sleep(self):
        return f"The {self.breed} is sleeping."

    def fur(self):
        return f"The {self.breed} has {self.fur} fur!"

