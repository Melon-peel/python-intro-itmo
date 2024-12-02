class CustomException(Exception):

    def __init__(self, message="Custom exception raised", *args):
        self.message = message
        super().__init__(message, *args)

try:
    raise CustomException
except CustomException as e:
    print(e)