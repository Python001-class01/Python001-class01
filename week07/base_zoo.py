from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, animal_type, size, character):
        # TODO:筛选设置规定的字段
        self.animal_type = animal_type
        self.size = size
        self.character = character

    @property
    def ferocious(self):
        if self.size == "中等" and self.animal_type == "食肉" and self.character == "凶猛":
            return True
        return False


class Cat(Animal):
    voice = "喵"

    def __init__(self, name, animal_type, size, character):
        self.name = name
        super().__init__(animal_type, size, character)

    @property
    def is_pet(self):
        if not self.ferocious:
            return True
        else:
            return False


class Zoo(object):
    def __init__(self, name):
        self.name = name
        self.animals = {}
    # def __set__(self, instance, value):
    #     print(f'__set__{instance} {value}')
    #     self.animals.append(value)

    def add_animal(self, animal):
        animal_id = id(animal)
        animal_name = animal.__class__.__name__

        if animal_id in self.animals:
            print(f"{animal_id}{animal_name} exist")
            return
        self.animals[animal_id] = animal

        if not hasattr(self, animal_name):
            setattr(self, animal_name, [animal])
        else:
            getattr(self, animal_name).append(animal)

    @property
    def animal(self):
        return self.animal


# 实例化动物园
z = Zoo('时间动物园')
# 实例化一只猫，属性包括名字、类型、体型、性格
cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
print(cat1.is_pet)
# 增加一只猫到动物园
z.add_animal(cat1)
# 动物园是否有猫这种动物
have_cat = getattr(z, 'Cat')
z.add_animal(cat1)
print(bool(have_cat), len(have_cat))
