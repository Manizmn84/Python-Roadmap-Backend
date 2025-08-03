import re


def real_numbers(numbers: list[str]) -> list[str]:
    list_answer = []
    for item in numbers :
        if re.match(r"^[-+]?(?:\d+\.\d+|\d+)(?:[eE][-+]?\d+)?$",item):
            list_answer.append("LEGAL")
        else:
            list_answer.append("ILLEGAL")
    return list_answer
print(real_numbers(['1.5e+2', '3.', '1.1.1', '1+e5', ' -123.45 ', '0', '+10E-5', 'abc', '1. ', '.5', '5e', '5e1.0']))