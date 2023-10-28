#Coustome metaClass inhereting type class(default metaclass)
class Mymeta(type):
    def __new__(cls, name, bases, attrb):
        if name == "MyClass":
            raise NameError
        #overriding __new__ method in type metaclass(by calling super())
        return super().__new__(cls, name, bases, attrb)

print(type(Mymeta))

class MyObject(metaclass=Mymeta):
    pass

#throws NameError as per metaclass above(Mymeta) if class name is MyClass
class MyClass(MyObject):
    pass


class Myclass(MyObject):
    pass

print(type(Myclass))#return 'Mymeta'

#type return instance type

#Creating new class using type(name_of_class, tuple(of_bases_class/Parent_class), attribute_dict{key:value, key1:value1})
Test = type("MyClass", (object, ), {"name": "Ram", "age": 20})

print(type(Test))#return 'type'

#Inhereting object class(manages all class in python).Which take type as metaClass
class Parent(object):
    def __init__(self, name) -> None:
        self.name = name 

print(type(Parent))

class Child(Parent):
    def __init__(self, name) -> None:
        super().__init__(name)

print(type(Child))#return 'type'