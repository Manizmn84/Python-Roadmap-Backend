'''first code'''
# lst = []
# number = -1
# while number != 0:
#     number = int(input())
#     lst.append(number)

# del lst[len(lst)-1]

# lst.reverse()

# for num in lst :
#   print(num)

'''second code'''
# text = input()
# lst = []
# for item in text :
#     if item == "=" and len(lst) > 0:
#         lst.pop()
#     elif item != "=":
#         lst.append(item)
# print("".join(lst))

'''third code'''
# n, m = map(int, input().split())
# k = int(input())

# location = [list(map(int,input().split())) for _ in range(k)]

# # print(location)

# board = [list(0 for _ in range(m)) for _ in range(n)]

# # print(board)

# def print_board(board):
#     for i in range(len(board)):
#         for j in range(len(board[0])) :
#             print(board[i][j],end=" ")
#         print()

# for loc in location :
#     board[loc[0]-1][loc[1]-1] = "*"

# for i in range(n) :
#     for j in range(m) :
#         if board[i][j] != "*" :
#             if  i - 1 >=0 and board[i - 1][j] == "*":
#                 board[i][j] += 1
#             if i + 1 <= n - 1 and board[i + 1][j] == "*" :
#                 board[i][j] += 1
#             if j - 1 >= 0 and board[i][j - 1] == "*" :
#                 board[i][j] += 1
#             if j + 1 <= m - 1 and board[i][j + 1] == "*" :
#                 board[i][j] += 1
#             if  i - 1 >= 0 and j - 1 >= 0 and board[i - 1][j - 1] == "*":
#                 board[i][j] += 1
#             if i - 1 >= 0 and j + 1 <= m - 1 and board[i - 1][j + 1] == "*" :
#                 board[i][j] += 1
#             if i + 1 <= n - 1 and j - 1 >= 0 and board[i + 1][j - 1] == "*" :
#                 board[i][j] +=1
#             if i + 1 <= n - 1 and j + 1 <= m - 1 and board[i + 1][j + 1] == "*" :
#                 board[i][j] +=1  

# print_board(board)
     
'''fourth code'''

# print(*sorted([num for index, num in enumerate(list(map(int,input().split()))) if (index + 1) % 6 == 0 and num % 6 == 0]))

'''fifth code'''
# def calc(lst: list) -> tuple:
#     average = sum(lst)/len(lst)
#     mid = 0
#     lst.sort()
#     if len(lst) % 2 == 0 :
#         mid = (lst[len(lst) // 2] + lst[(len(lst) // 2) - 1]) / 2
#     else :
#         mid = lst[len(lst) // 2]
#     MaxNumber = max(lst)
#     return (average , mid , MaxNumber)
# print(calc([2, 20, 30, 29]))

'''sixth code'''
# Count = int(input())
# dic = dict()
# for item in range(Count):
#     name = input().split()[0]
#     dic[name] = dic.get(name,0) + 1
# print(max(dic.values()))

'''seventh code'''
# def check_registration_rules(**kwargs: str) -> list[str]:
#     IsValid = []
#     for username , password in kwargs.items():
#         if len(password ) < 6 :
#             continue
#         elif len(username) < 4 :
#             continue
#         elif username  == "quera" or username == "codecup" :
#             continue
#         elif password.isdigit() :
#             continue
#         else :
#             IsValid.append(username)
#     return IsValid
# print(check_registration_rules(username='password', sadegh='He3@lsa'))

'''eighth code'''
# all_users = {}
# all_albums = {}


# def add_user(username: str, age: int, city: str, albums: list, all_users: dict) -> None:
#     all_users[username] = {
#         "username" : username,
#         "age" : age,
#         "city" : city,
#         "albums" : albums
#     }


# def add_album(name: str, artist: str, genre: str, tracks: int, all_albums: dict) -> None:
#     all_albums[name] = {
#         "name" : name,
#         "artist" : artist,
#         "genre" : genre,
#         "tracks" : tracks
#     }

# # add_user("SAliB", 19, "Tehran", ["tekunbede", "barf", "gavazn"], all_users)
# # add_user("Saeid", 22, "Esfehan", ["eclipse", "barf", "gavazn"], all_users)
# # add_album("eclipse", "malmsteen", "classic", 10, all_albums)
# # add_album("barf", "beeptunes", "pop", 22, all_albums)
# # add_album("tekunbede", "beeptunes", "pop", 14, all_albums)
# # add_album("gavazn", "sorena", "persian", 18, all_albums)
# # add_user("Ali", 12, "Bushehr", ["bidad", "blaze"], all_users)
# # add_album("bidad", "shajarian", "classic", 10, all_albums)
# # add_album("blaze", "ghorbani", "pop", 9, all_albums)
# def query_user_artist(username: str, artist: str, all_users: dict, all_albums: dict) -> int:
#     return sum(all_albums[album]["tracks"] for album in all_users[username]["albums"] if all_albums[album]["artist"] == artist)

# print(all_users)
# print()
# print(all_albums)
# # print(query_user_artist("Ali", "ghorbani", all_users, all_albums))


# def query_user_genre(username: str, genre: str, all_users: dict, all_albums: dict) -> int:
#     return sum(all_albums[album]["tracks"] for album in all_users[username]["albums"] if all_albums[album]["genre"] == genre)

# # print(query_user_genre("Ali", "classic", all_users, all_albums))

# def query_age_artist(age: int, artist: str, all_users: dict, all_albums: dict) -> int:
#     return sum(all_albums[album]["tracks"] for user in all_users.values() if user["age"] == age for album in user["albums"] if all_albums[album]["artist"] == artist )
# # print(query_age_artist(12, "shajarian", all_users, all_albums))

# def query_age_genre(age: int, genre: str, all_users: dict, all_albums: dict) -> int:
#     return sum(all_albums[album]["tracks"] for user in all_users.values() if user["age"] == age for album in user["albums"] if all_albums[album]["genre"] == genre )
# # print(query_age_genre(12, "pop", all_users, all_albums))

# def query_city_artist(city: str, artist: str, all_users: dict, all_albums: dict) -> int:
#     return sum(all_albums[album]["tracks"] for user in all_users.values() if user["city"] == city for album in user["albums"] if all_albums[album]["artist"] == artist)
# # print(query_city_artist("Bushehr", "ghorbani", all_users, all_albums))


# def query_city_genre(city: str, genre: str, all_users: dict, all_albums: dict) -> int:
#     return sum(all_albums[album]["tracks"] for user in all_users.values() if user["city"] == city for album in user["albums"] if all_albums[album]["genre"] == genre)
# # print(query_city_genre("Bushehr", "pop", all_users, all_albums))

'''nineth'''
# from typing import Generator

# def divs(n: int) -> Generator[int, None, None]:
#     for item in range(1,n + 1) :
#         if n % item == 0 :
#             yield item
