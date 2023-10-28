import logging

logging.basicConfig(level=logging.INFO)

class Descriptor:
    
    def __get__(self, instance, owner):
        value = instance.name
        logging.info("Accessing %r giving %r", "age",value)
        return value
    
    def __set__(self, instance, value):
        logging.info("Updating %r to %r", 'age', value)
        instance._vlaue = value

class MyClass:
    des = Descriptor()

    def __init__(self) -> None:
        pass
    

