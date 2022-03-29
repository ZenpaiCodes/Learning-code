# OOP Types
# Intatiate is to call a class to create an object.
class BigObject:  # Class  -  blueprint for objects
    pass


object1 = BigObject()  # instanciate - create object from class
object2 = BigObject()
object3 = BigObject()  # 4 objects created from class BigObject
object4 = BigObject()
print(type(object1))  # <class '__main__.BigObject'>

print(type(None))  # <class 'NoneType'>
print(type(True))  # <class 'bool'>
print(type(False))  # <class 'bool'>
print(type(1))  # <class 'int'>
print(type(1.1))  # <class 'float'>
print(type(""))  # <class 'str'>
print(type([]))  # <class 'list'>
print(type({}))  # <class 'dict'>
print(type(()))  # <class 'tuple'>
print(type(set()))  # <class 'set'>
print(type(range(5)))  # <class 'range'>
print(type(BigObject()))  # <class '__main__.BigObject'>
