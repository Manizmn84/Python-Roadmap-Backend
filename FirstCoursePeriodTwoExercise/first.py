import math
from typing import Callable


def get_func(ls: list[str]) -> list[Callable]:
    '''
        'square', 'circle', 'rectangle', 'triangle'
    '''    
    list_callable = []
    for shape in ls :
        if shape == "square" :
            list_callable.append(lambda x : x * x)
        elif shape == "circle" :
            list_callable.append(lambda x : x * x * math.pi)
        elif shape == "rectangle" :
            list_callable.append(lambda x, y : x * y )
        elif shape == "triangle" :
            list_callable.append(lambda x , y : x * y * 0.5)
    return list_callable
