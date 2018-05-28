class Animal(object):
    owner = 'Jack'
    def __init__(self,name):
        self._name = name
    def make_sound(self):
        pass
    @classmethod
    def get_owner(cls):
        return cls.owner
    
    def age(self,value):
        if isinstance(value,int):
            self._age = value
        else:
            raise ValueError 
    @staticmethod
    def order_animal_food():
        print('ording...')
        print('ok')

class Cat(Animal):
    
    def make_sound(self):
        print(self._name +' is making miu miu miu' )


Animal.order_animal_food()

animals = [Cat('kitty'),Cat('caicaizi')]
for animal in animals:
    animal.make_sound()

    print(animal.get_owner())

    animal.age = 3
    print(animal.age)

