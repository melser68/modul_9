import re
text = 'Irma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com abc111@test.com.net +380(67)111-777-777+380(67)777-77-787'

def find_all_phones(text):
    
    result = re.findall(r"[+][0-9]{3}[()][0-9]{2}[)][0-9]{3}[-][0-9]{1,2}[-][0-9]{2,3}", text)
    count =0
    for i in result: 
              
        if len(i) > 17:
            new_i = i[0:17]
            result[count] = new_i
            
            count+=1
        else:
            count +=1
    result = (',').join(result)

    return result

print(find_all_phones(text))