# Task 1
from abc import abstractmethod
import json
filename = 'homework1'
somedata = """{'name': 'Home', 'lastname': 'Work', 'age': 1}"""


class SerializationInterface:
    @abstractmethod
    def serialization(self):
        pass


class SerializationToBin(metaclass=SerializationInterface):
    def serialization(self, args):
        with open(f'{filename}.bin', 'wb') as f:
            f.write(args)


class SerializationToJson(metaclass=SerializationInterface):
    def serialization(self, args):
        with open(f'{filename}.json', 'w') as f:
            json.dumps(args, f)


# Task 2


class Meta(type):
    def __new__(mcs, class_name, class_parents, class_atrrs):
        class_atrrs['class_number'] = Meta.children_number
        Meta.children_number += 1
        return type(class_name, class_parents, class_atrrs)


Meta.children_number = 0


class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data


assert (Cls1.class_number, Cls2.class_number) == (0, 1)
a, b = Cls1(''), Cls2('')
assert (a.class_number, b.class_number)

print(Meta.children_number)
