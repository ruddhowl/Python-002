import abc # Abstract Base Class

class Animal(metaclass = abc.ABCMeta):
    def __init__(self):
        typie = 'ani'
        shape = 'medium'
        character = 'soft'
        isferocious =False

class Cat(Animal):
    def __init__(self):
        pass
    sound = 'miaomiaomiao'

class Dog(Animal):
    sound = 'wangwangwang'

