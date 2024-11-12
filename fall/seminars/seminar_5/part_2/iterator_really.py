class MyIterator:

    def __init__(self, num_iterable_):
        self.num_iterable_ = num_iterable_
        self.iter_len = len(num_iterable_)
        self.current_index = 0

    def __next__(self):
        if self.current_index+1 > self.iter_len:
            raise StopIteration
        else:
            new_value = self.num_iterable_[self.current_index] * 2
            self.current_index += 1
            return new_value

    def __iter__(self):
        return self

my_iterator = MyIterator([1, 2, 3, 4])
for i in my_iterator:
    print(i)
