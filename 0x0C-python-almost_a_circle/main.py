import math

class Pos:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, value):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("A positive number is expected")
        instance.__dict__[self._name] =  value