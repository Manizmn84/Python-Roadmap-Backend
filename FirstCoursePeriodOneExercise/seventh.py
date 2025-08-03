def check_words(text: str) -> dict[str, int]:
    lst = text.split()
    lst = remove_bad_words(lst)
    filter_bad_ch(lst)
    capitalize_words(lst)
    
    dict_answer = {}
    for item in lst:
        dict_answer[item] = dict_answer.get(item, 0) + 1
    return dict_answer


def is_bad_word(word: str) -> bool:
    counter = 0
    for ch in word:
        if not ch.isalpha():
            counter += 1
    return counter >= len(word) / 2


def remove_bad_words(lst: list[str]) -> list[str]:
    return [word for word in lst if not is_bad_word(word)]


def delete_bad_ch(word: str) -> str:
    return ''.join(ch for ch in word if ch.isalpha())


def filter_bad_ch(lst: list[str]) -> None:
    for i in range(len(lst)):
        lst[i] = delete_bad_ch(lst[i])


def capitalize_words(lst: list[str]) -> None:
    for i in range(len(lst)):
        lst[i] = lst[i].capitalize()


print(check_words("""hEllO My FriEnDs!!! thIS is A tEsT For your #p#r#o#b#l#e#m a"""))
