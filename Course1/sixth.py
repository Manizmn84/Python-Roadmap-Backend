class Person:
    def __getattribute__(self, name):
        if name.startswith("fs") :
            raise AttributeError
        return super().__getattribute__(name)

    def __init__(self):
        self.fun = "funny"

    def __getattr__(self, name):
        return f"We don`t have attribuite with name : {name}"

test = Person()

# print(test.fsun)

class Proxy:
    def __init__(self, obj: object) -> None:
        self._obj = obj
        self._last_accessed = None
        self._access_count = dict()

    def __getattr__(self, attribute_name):
        if not hasattr(self._obj, attribute_name):
            raise Exception('No such attribute.')

        self._access_count[attribute_name] = self._access_count.get(attribute_name, 0) + 1
        self._last_accessed = attribute_name
        return getattr(self._obj, attribute_name)

    def last_accessed_attribute(self) -> str:
        if len(self._access_count) == 0:
            raise Exception('No attribute was accessed.')

        return self._last_accessed

    def count_of_accesses(self, attribute_name: str) -> int:
        return self._access_count.get(attribute_name, 0)

    def was_accessed(self, attribute_name: str) -> bool:
        if attribute_name not in self._access_count:
            return False

        return True


class Radio():
    def __init__(self):
        self._channel = None
        self.is_on = False
        self.volume = 0

    def get_channel(self):
        return self._channel

    def set_channel(self, value):
        self._channel = value

    def power(self):
        self.is_on = not self.is_on

    def __str__(self):
        return f"Radio(channel={self._channel}, is_on={self.is_on}, volume={self.volume})"

radio = Radio()
radio_proxy = Proxy(radio)


# radio_proxy.set_channel(95)
# radio_proxy.power()
# radio_proxy.set_channel(100)
# print(radio_proxy.is_on)                                     # True

# print(radio_proxy.last_accessed_attribute())                 # is_on
# print(radio_proxy.count_of_accesses('set_channel'))          # 2
# print(radio_proxy.was_accessed('power'))                     # True
# print(radio_proxy.count_of_accesses('non_existent_method'))  # 0
# print(radio_proxy.was_accessed('volume'))                    # False

class Reverse:
    def __init__(self , lst: list[int]):
        self._list_number = lst
        self._current_index = len(self._list_number)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self._current_index -= 1
        if self._current_index == -1 :
            raise StopIteration
        
        return self._list_number[self._current_index]
    
# ls = [10, 20, 30]

# print("Reverse iteration")
# for it in Reverse(ls):
#     print(it)

# print("Original list:")
# print(ls)



class Strint(int):
    def __lt__(self, other):
        return self % 10 < other % 10

    def __gt__(self, other):
        return self % 10 > other % 10

    def __le__(self, other):
        return self % 10 <= other % 10

    def __ge__(self, other):
        return self % 10 >= other %  10

    def __eq__(self, other):
        return self % 10 == other % 10

    def __ne__(self, other):
        return self % 10 != other % 10      

    def __add__(self, other):
        return Strint(int(str(self) + str(other)))

    def __sub__(self, other):
        if not str(self).endswith(str(other)) :
            raise ValueError('The subtraction is not valid!')
    
        new_strint = str(self).removesuffix(str(other))
        if new_strint :
            return Strint(int(new_strint))
        return Strint(0) 

    def __len__(self):
        return len(str(self))

    def __call__(self):
        digit_map = {
            '0': '۰',
            '1': '۱',
            '2': '۲',
            '3': '۳',
            '4': '۴',
            '5': '۵',
            '6': '۶',
            '7': '۷',
            '8': '۸',
            '9': '۹'
        }
        return ''.join(digit_map.get(ch, ch) for ch in str(int(self)))


# print(Strint.__name__)


def info_decorator(func):
    def inner_func(*args , **kwargs):
        print(f"Start the operation {func.__name__}")
        c = func(*args , **kwargs)
        print("End the operation")
        return c

    return inner_func

@info_decorator
def addd(a , b) :
    return a + b
@info_decorator
def minuss(a , b):
    return a - b

# print(addd(2,3))


def decorator_builder(validator):
    def first_func(func):
        def second_func(*args, **kwargs):
            if not validator(*args , **kwargs) :
                return "error"
            return func(*args,**kwargs)
        return second_func
    return first_func

def nonnegative_validator(x):
    return x >= 0

@decorator_builder(nonnegative_validator)
def square_root(x):
    return x ** 0.5

print(square_root(4))  # 2.0

print(square_root(-4)) # error