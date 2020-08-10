"""
1. 定义“动物”、“猫”、“动物园”三个类，动物类不允许被实例化。
2. 动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
3. 猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，猫类继承自动物类。
4. 动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。
"""

from abc import ABCMeta


class Zoo(object):
    """
    Zoo 动物园
    """
    __instance = False
    list_animal = []

    def __new__(cls, *args, **kwargs):
        if cls.__instance:
            return cls.__instance
        cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, name):
        self.name = name

    def add_animal(self, animal):
        if animal not in self.list_animal:
            self.list_animal.append(animal)
        else:
            # return self.list_animal[animal]
            print('已经存在')

    def __getattr__(self, item):
        """
        动物园是否有 item 这种动物
        :param item:动物某子类名
        :return:
        """
        try:
            for animal in self.list_animal:
                if isinstance(animal, eval(item)):
                    return True
        except:
            pass
        return False


class Animal(metaclass=ABCMeta):
    """
    Animal 动物
    """

    def __init__(self, types, shape, character):
        """

        :param types:类型
        :param shape:体型 (假设体型有 大 中 小 三类，分别对应 3 ,2, 1，体型 >= 中等，表示为 非小)
        :param character:性格
        """
        self.types = types
        self.shape = shape
        self.character = character

        if shape != '小' and types == '食肉' and character == '凶猛':
            self.isdanger = True
        else:
            self.isdanger = False


class Cat(Animal):
    """
    Cat 猫
    """

    # __instance_cat = False
    # list_animal = []
    #
    # def __new__(cls, *args, **kwargs):
    #     if cls.__instance_cat:
    #         return cls.__instance_cat
    #     cls.v = object.__new__(cls)
    #     return cls.__instance_cat

    def __init__(self, name, types, shape, character, ispet=True):
        """

        :param name: 名字
        :param types: 类型
        :param shape: 体型
        :param character:性格
        :param ispet: 是否适合做宠物
        :return:
        """
        self.name = name
        self.ispet = ispet
        super().__init__(types, shape, character)

    @property
    def bark(self):
        """
        猫 "叫"
        :return:
        """
        print('tha Cat bark.')


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')
    print('have_cat:', have_cat)
