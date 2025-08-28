import re

class Security:
    def encrypt(self, s: str) -> str:
        if not s:
            return ""

        lst_sub = []
        current = s[0]

        for ch in s[1:]:
            if ch == current[-1]:
                current += ch
            else:
                lst_sub.append(current)
                current = ch
        lst_sub.append(current)

        lst_code = []
        for item in lst_sub:
            weight_str = ""
            w = ord(item[0]) - 96  # وزن کاراکتر (فرض حروف کوچک)
            for i in range(len(item)):
                weight_str += str((i + 1) * w)
            lst_code.append(weight_str)

        return "".join(lst_code)

    def is_social_account_info(self, param: str) -> bool:
        pattern = r'[A-Z][a-zA-Z]+:www\.([a-z0-9]+(?:\.[a-z0-9]+)+)/([A-Za-z0-9_]+)'
        return bool(re.fullmatch(pattern, param))

    def secure(self, info: str) -> str:
        pattern = r'([A-Z][a-zA-Z]+:www\.([a-z0-9]+(?:\.[a-z0-9]+)+)/([A-Za-z0-9_]+))'

        def replacer(match):
            full_match = match.group(1)
            username = match.group(3)
            encrypted_username = self.encrypt(username)
            replaced = full_match.rsplit('/', 1)[0] + '/' + encrypted_username
            return replaced

        return re.sub(pattern, replacer, info)



            

print(Security.encrypt("abcccdd"))
print(Security.is_social_account_info("Instagram:www.instagram.com/javafan"))
print(Security.secure("FirstName:Ali, LastName:Alavi, BirthDate:1990/02/02 Gender:male Instagram:www.instagram.com/aalavi Degree:Master Twitter:www.twiter.com/alaviii imdb:www.imdb.com/alavi"))
# print(ord("c"))