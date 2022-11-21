class Animal:
    def __init__(self, type_animal, name):
        self.type_animal = type_animal
        self.name = name

    def info_name(self):
        print(f"Я {self.type_animal} по имени {self.name}")


class Cat(Animal):
    def __init__(self, name, age, size):
        super().__init__("кошка", name)
        self.name = name
        self.age = age
        self.size = size

    def info(self):
        print(f'Я кошка, мне {self.age}' + " года")

    def sound(self):
        print("meow")


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__("Собака", name)
        self.name = name
        self.age = age

    def info(self):
        print(f'Я собака мне {self.age}')

    def sound(self):
        print("гав")

    def __belt(self):
        print(f'Размер ошейника {self.size}')


cat = Cat("Bazilio", 3)
dog = Dog("Balto", 4)
for animal in (cat, dog):
    animal.info_name()
    animal.sound()
    animal.info()
