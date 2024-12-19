class CustomBaseException(Exception):
    pass

class Divzero(CustomBaseException):
    pass

class Oflow(CustomBaseException):
    pass

class Uflow(CustomBaseException):
    pass

def func():
    raise Uflow

try:
    func()
except Exception as e:
    print(e)
    print("Well handled")