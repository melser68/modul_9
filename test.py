import re
text = 'ЛОХ, лох проверка сволочь'
spam_words = ['лох', 'СВОЛОЧЬ']

def replace_spam_words(text, spam_words):
    count = 0
    for y in spam_words:
        if len(re.findall(y, text, re.IGNORECASE)) >0:
            rez = re.findall(y, text, re.IGNORECASE)
            
            for i in rez:
                if count == 0:
                    new_text = re.sub((i), '*'*len(i), text)
                    count +=1
                else:
                    new_text = re.sub((i), '*'*len(i), new_text)
    text = new_text
    return text
            


print(replace_spam_words(text, spam_words))

