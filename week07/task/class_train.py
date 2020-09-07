import abc # Abstract Base Class

class Zoo(object):
    def __init__(self, name):
        self.animals = {}
        self.name = name

    def add_animal(self, animal): # 不怎么会，先放着
        for ani in self.animals:
            if ani == animal:
                return None
        self.animals[animal.__class__] = animal

class Animal(metaclass = abc.ABCMeta):
    sizes = {'小' : 1, '中' : 2, '大' : 3}
    kind = None
    size = None
    character = None
    
    def __init__(self, kind, size, character):
        self.kind = kind
        self.size = size
        self.character = character

    @property
    def is_ferocious(self):
        if self.sizes[self.size] >= self.sizes['中'] and self.kind == '食肉' and self.character == '凶猛':
            return True
        else:
            return False

class Cat(Animal):
    sound = 'meow'
    def __init__(self, name, kind, size, character):
        self.name = name    
        super().__init__(kind, size, character)

    @property
    def is_pet(self):
        if self.is_ferocious is not '凶猛':
            return True
        return False

class Dog(Animal):
    sound = 'wang'
    def __init__(self, name, kind, size, character):
        self.name = name    
        super().__init__(kind, size, character)

    @property
    def is_pet(self):
        if self.is_ferocious is not '凶猛':
            return True
        return False

if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    print(f'猫的叫声：{Cat.sound}，猫的名字：{cat1.name}，猫的体型：{cat1.size}，猫的性格：{cat1.character}，是否适合作为宠物：{cat1.is_pet}')
    # 增加一只猫到动物园
    # z.add_animal(cat1)
    # 动物园是否有猫这种动物
    # have_cat = hasattr(z, 'Cat')
    # print(f'{have_cat}')
 