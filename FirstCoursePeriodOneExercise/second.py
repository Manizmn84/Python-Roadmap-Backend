def calculator(n: int, m: int, ls: list[int]) -> int:
    list_group = [[ls[i] for i in range(j,j+m) if i < n] for j in range(0,n,m)]
    answer = 0
    # print(list_group)
    list_finall = [sum(group) for group in list_group]
    for _ in range(len(list_finall)):
        if _ % 2 == 0:
            answer += list_finall[_]
        else :
            answer -= list_finall[_]
    return answer
# print(calculator(8, 1, [1, 2, 3, 4, 5, 6, 7, 8]))