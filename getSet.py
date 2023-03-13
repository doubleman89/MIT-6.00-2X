class Name(object):
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self,instance,owner):
        return instance.__dict__[self._name]
    
    def __set__(self,instance, value):
        instance.__dict__[self._name] = value 

class Person(object):
    first_name = Name()
    second_name = Name()

    def __init__(self,first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name