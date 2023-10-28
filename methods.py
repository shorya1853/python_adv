class MyClass(object):
    attri = "apple"
    __slots__ = ("version", "lis")

    def __init__(self, version, *argw):
        self.version = version
        self.lis = list(argw)

    def printer(self) -> str:
        return self.lis
    
    def __repr__(self):
        return f"This is repr func return {self.version}"
    
    def __str__(self):
        return f"This is str func return {self.version}"
    
    def __add__(self, value):
        res = self.version + value
        return res
    
    def __len__(self):
        return len(self.lis)
    
    def __contains__(self, item):
        return item in self.lis
    
    def __delitem__(self, index: int) -> None:
        if self.__contains__:
            self.lis.pop(index)
            return "element deleted!"
        return "element not found"


    @staticmethod
    def update_ver(newUP: int) -> int:
        return newUP
    
    @classmethod
    def myMehtod(cls, num: int):
        version: int = num
        return cls(version)
    

if __name__ == "__main__":
    obj = MyClass(2, 2, 3, 3, 3)
    obj.version = 10
    print(obj.version)
    print(obj.attri)
    obj1 = MyClass(4)
    obj1.attri = 'banana'
    print(obj1.attri)
    obj2 = MyClass(2, 2,2,2,)
    print(obj2.attri)