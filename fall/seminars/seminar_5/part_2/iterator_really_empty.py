class MyIterator:


    def __init__(self, numbers_list):
        self.numbers_list = numbers_list
        self.list_len = len(numbers_list)
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index+1 > self.list_len:
            self.current_index = 0
            raise StopIteration
        else:
            result = self.numbers_list[self.current_index] * 2
            self.current_index += 1
            return result


