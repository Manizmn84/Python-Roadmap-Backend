# import requests

# url = "https://quera.org/college/3078/chapter/9356/lesson/31131/"
# params = {"comments_page": 1, "comments_filter": "ALL"}

# response = requests.get(url, params=params)

# # نمایش URL نهایی با پارامترها
# print(response.url)
# # تبدیل پاسخ به فرمت JSON
# print(response.text[:100])

import requests


def find_category(url: str) -> str:
    response = requests.get(url)
    if response.status_code != 200 :
        return "Bad Request"
    data = response.json()
    if data is None :
        return "I can't recognize it"
    
    dict_answer = {cat : sum(1 for dic in data if dic["category"] == cat) for cat in [dic["category"] for dic in data]}
    tuple_answer = dict_answer.items()
    tuple_answer.sort(lambda item : item[1])

    if len(tuple_answer) == 1 :
        return tuple_answer[0][0]
    if tuple_answer[0][1] == tuple_answer[1][1] :
        return "I can't recognize it"
    return tuple_answer[0][0]
    