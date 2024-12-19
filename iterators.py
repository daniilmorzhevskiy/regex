def hello():
    pass

"""async def hello():
    pass

print(type(hello()))""" #<class 'coroutine'>

"""my_list = [1, 2, 3]

for elem in my_list:
    print(elem) #_iter_(), _next_()


my_iter = iter(my_list)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

print(type(my_iter)) #class 'list_iterator'>

try:
    print(next(my_iter))  # This will raise StopIteration
except StopIteration:
    print("Reached the end of the iterator")"""


class CountUpTo:
    def __init__(self, max):
        self.max = max
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.max:
            result = self.num
            self.num += 1
            return result
        else:
            raise StopIteration

counter = CountUpTo(3)
for num in counter:     # Python calls method ``__next__()`` during each iteration
    print(num)
