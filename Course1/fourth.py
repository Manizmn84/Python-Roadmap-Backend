# with open("E:\\UNIVERSITY\\IUST-CE\\Python-Roadmap-Backend\\Course1\\text.txt", "a+") as f :
#     # print(f.tell())
#     # print(f.read())
#     # print(f.tell())
#     # print(f.tell())
#     # for line in f :
#     #     print(line)
#     f.write("\nthis is test for write in the file")
#     print(f.seek(0))
#     print(f.read())

'''first code'''
# def count_executable_lines(path: str) -> int:
#     return sum(1 for line in open(path,"r").readlines() if line.strip() and not line.strip().startswith("#"))

# print(count_executable_lines("E:\\UNIVERSITY\\IUST-CE\\Python-Roadmap-Backend\\Course1\\text.txt"))

'''second code'''
# def calculate_sums(path: str) -> None:
#     rows = parse_csv(path)
#     with open("result.csv","w") as f :
#         for row in rows:
#             total = str(sum(map(int,row)))
#             row.append(total)
#             f.write(",".join(row) + "\n")
# def parse_csv(path: str):
#     with open(path) as csv:
#         for row in csv.readlines():
#             yield row.strip().split(',')

import json

# my_data = {
#     "first_name" : "mani",
#     "last_name" : "zamani",
#     "emai;" : "mani.84.zmn@gmail.com",
#     "phone_number" : "09966304410",
# }
# data_json = json.dumps(my_data,indent=5)
# print(my_data)
# print(data_json)    

# with open("E:\\UNIVERSITY\\IUST-CE\\Python-Roadmap-Backend\\Course1\\data.json","a") as f :
#     json.dump(my_data,f,indent=4)

'''third code'''
# Count = int(input())
# lst_input = [item := input() for _ in range(Count)]
# # lst_input = list(map(json.dumps,lst_input))
# dict_variable = {}
# # print(type(dict_variable))

# for line in lst_input :
#     if line.split()[0] != "print" :
#         dict_variable[json.loads(json.dumps(line.split()[0]))] = json.loads(json.dumps(line.split()[2]))
#     else:
#         print(dict_variable[json.loads(json.dumps(line.split()[1]))])

# lst_variable = list(filter(lambda line : line.split()[0] != "print",lst_input.copy()))
# print(lst_variable)
# print(lst_input)

import json
import sys

n = int(sys.stdin.readline())
variables = {}

for _ in range(n):
    line = sys.stdin.readline().rstrip()

    if ":=" in line:
        var_name, value_str = line.split(" := ", 1)
        value = json.loads(value_str)
        variables[var_name] = value
    else:
        rest = line[len("print "):]

        var_name_end = rest.index('[')
        var_name = rest[:var_name_end]
        id_str = rest[var_name_end+1:-1]

        var_value = variables[var_name]

        if isinstance(var_value, list):
            idx = int(id_str)
            print(var_value[idx])
        else:
            key = json.loads(id_str)
            print(var_value[key])
