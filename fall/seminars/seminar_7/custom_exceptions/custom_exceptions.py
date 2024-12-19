class CustomIndexError(Exception):
    pass



# ----------


# не по Лутцу
class PrintableExceptionInit(Exception):

    def __init__(self, message="Custom exception raised", error_code=404, *args):
        self.message = message
        # это позиционные аргументы! название не важно
        super().__init__(message, error_code, *args)
        # по сути, __init__ обеспечивает наличие строкового представления при print(exception_object)



# по Лутцу
class PrintableException(Exception):

    def __str__(self):
        return "Printable Exception raised"

# оптимальный вариант

class PrintableExceptionCombined(Exception):

    def __init__(self, message="Custom exception raised", error_code=404):
        self.message = message
        self.error_code = error_code

    def __str__(self):
        # некоторые так делают, но имхо, это странно
        # return repr(PrintableExceptionCombined(self.message, self.error_code))
        return str((self.message, self.error_code))
        # return str(tuple(vars(self).values()))


print(PrintableExceptionCombined())

