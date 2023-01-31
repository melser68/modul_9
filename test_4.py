import re
text = 'The main search http://github.com There'


def find_all_links(text):
    result = []
    iterator = re.finditer(r"(https://|http://)\w+(.)\w+", text)
    for match in iterator:
        result.append(match.group())
    return result


print(find_all_links(text))
