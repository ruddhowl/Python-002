import abc # Abstract Base Class

class Zoo(object):
    def __init__(self, name):
        self.animals = {}
        self.name = name

    def add_animal(self, animal):
        for ani in self.animals:
            if ani == animal:
                return None
        self.animals[animal.__class__] = animal

class Animal(metaclass = abc.ABCMeta):
    shapes = {'small' : 1, 'medium' : 2, 'big' : 3}
    kind = None
    shape = None
    character = None
    
    def __init__(self, name, kind, shape, character):
        self.name = name
        self.kind = kind
        self.shape = shape
        self.character = character

    @property
    def is_ferocious(self):
        if self.shapes[self.shape] >= self.shapes['medium'] and self.kind == '食肉' and self.character == '凶猛':
            return True
        else:
            return False

class Cat(Animal):
    __sound = 'meow'


class Dog(Animal):
    __sound = 'wang'

if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
    print(f'{have_cat}')
 