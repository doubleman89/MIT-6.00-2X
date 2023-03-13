# Using the generator pattern (an iterable)
class first_n(object):


    def __init__(self, n):
        self.n = n
        self.num = 0
        print("new object has been created")


    def __iter__(self):
        return self


    # Python 3 compatibility
    def __next__(self):
        return self.next()


    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num+1
            return cur
        raise StopIteration()


  # a generator that yields items instead of returning a list
def firstn(n):
    num = 0
    while num < n:
        yield num
        print(num)
        num += 1

sum_of_first_n = sum(firstn(5))
print(sum_of_first_n)

sum_of_first_n = sum(first_n(5))
print(sum_of_first_n)