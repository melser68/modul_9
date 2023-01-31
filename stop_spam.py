text = 'Молох'
spam_words = ['лох']


def is_spam_words(text, spam_words, space_around=False):
    text = text.replace(',', '')
    text = text.replace('.', '')
    checking_list = text.split(' ')
    
    if space_around == True:

        for i in checking_list:
            for y in spam_words:
                if i.lower() == y.lower():
                    return True
                    break

    else:
        for w in checking_list:
            w = w.lower()
            for o in spam_words:
                if w.find(o.lower()) != -1:
                    return True
                    break



print(is_spam_words(text, spam_words))
