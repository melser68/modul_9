list_phones = ['+0658759411', '818765347','818765344', '8867658976', '657658976']
dict_country_phones = {'UA': [], 'JP': [], 'TW': [],'SG': []}


def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    for i in list_phones:
        san_phone = sanitize_phone_number(i)
        if san_phone.startswith('81') == True:
            dict_country_phones.get('JP').append(san_phone)
        elif san_phone.startswith('65') == True:
            dict_country_phones.get('SG').append(san_phone)
        elif san_phone.startswith('886') == True:
            dict_country_phones.get('TW').append(san_phone)
        else:
            dict_country_phones.get('UA').append(san_phone)
            
    print(dict_country_phones)

get_phone_numbers_for_countries(list_phones)