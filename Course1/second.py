'''first code'''

# MaxDifference = 0

# for _ in range(NameCount := int(input())):
#     name = input().lower()
#     MaxDifferenceItem = 0
#     for ch in range(len(name)):
#         if name[ch] not in name[:ch]:
#             MaxDifferenceItem += 1
#     if MaxDifference < MaxDifferenceItem :
#         MaxDifference = MaxDifferenceItem

# print(MaxDifference)

'''second code'''

# k = int(input())

# key = input()

# step = 0

# for _ in range(k):
#     text = input()
#     location = text.find(key[_])
#     if location > len(text) - location : 
#         step += len(text) - location
#     else :
#         step += location

# print(step)

'''third code'''
# print(f"{int(input()):b}".count("1"))

'''fourth code'''
# import re


# def validate_email(email: str) -> bool:
#     return re.match(r'^[a-zA-Z0-9\.\_]+@[a-zA-Z0-9]+\.[a-zA-Z]{3}$',email) is not None


# def validate_phone(number: str) -> bool:
#     return re.match(r'^(09|\+989|00989)[0-9]{9}$',number) is not None
