# name = input()

# print("Hello ",name,"!")

# firstNumber = float(input())
# secondNumber = float(input())
# Answer = int(firstNumber + secondNumber)
# print(Answer)

# Degree = int(input())

# if Degree > 100 :
#     print("Steam")
# elif Degree < 0 :
#     print("Ice")
# else:
#     print("Water")



# MultiplicationTableSize = int(input())

# for row in range(1,MultiplicationTableSize + 1):
#     for col in range(1,MultiplicationTableSize + 1):
#         print(row * col,end=" ")
#     print()

# if name := input().lower() == "mani" :
#     print("hello mani") 

# name := input()
 

try:
    n = int(input())
    m = n/ 0
except Exception as error:
    print(error)
