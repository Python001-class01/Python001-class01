'''
具体要求：
定义“动物”、“猫”、“动物园”三个类，动物类不允许被实例化。
动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，
是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，猫类继承自动物类。
动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。
'''
from abc import ABC, abstractmethod

class Zoo:

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = {}

    def add_animal(self, instanceb):
        if instanceb in self.animals:
            print("cat1 is here")
        else:
            self.animals[instanceb]=1

    def __getattr__(self,someclass):
        print("gggggggg------------")
        try:
            for i in self.animals:
                if isinstance(i,eval(someclass)):
                    return True
        except:
            pass
        return False

class Animals(ABC):

    @abstractmethod
    def __init__(self, type, size, character):
        self.type = type
        self.size = size
        self.character = character

    @property
    def is_danger_animal(self):
        if self.size != '小' and self.type == '食肉' \
           and self.character == '凶猛':
            return True
        return False

class Cat(Animals):
    call = 'miaomiao'
    is_suitable_pet=True

    def __init__(self, name, type, size, character):
        super().__init__(type, size, character)
        self.name = name
       
if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')

    # 增加一只猫到动物园
    z.add_animal(cat1)
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    print(99999999999999999)
    have_cat = getattr(z, 'Cat')
    have_cat2 = getattr(z, 'Dog')
    print(have_cat)


'''
PS E:\pythoncode202005> & d:/ProgramData/Anaconda3/python.exe f:/geek/Python001-class01/week07/zoo.py
cat1 is here
99999999999999999
gggggggg------------
gggggggg------------
True

'''