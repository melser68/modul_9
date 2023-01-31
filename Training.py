import re
from pprint import pprint
text = 'Guido van Rossum began working on Python in the late 1980s,' 
'as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
word = 'Python'
def find_word(text, word):
    rez_dict = {}
    rez = re.search(word, text)
    try:
        rez_dict['result'] = True
        rez_dict['first index'] = rez.span()[0]
        rez_dict['last index'] = rez.span()[1]
        rez_dict['search string'] = word
        rez_dict['string'] = text
        
    except:
        rez_dict['result'] = 'False'
        rez_dict['first index'] = None
        rez_dict['last index'] = None
        rez_dict['search string'] = word
        rez_dict['string'] = text
    return rez_dict
    

print(find_word(text, word))
