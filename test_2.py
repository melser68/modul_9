import re
a = input("Enter email  ")
pattern = r"^[a-zA-Z0-9]{1,100}[@][a-z]{2,6}\.[a-z]{2,4}"
number_re = re.compile(pattern)
if number_re.findall(a):
    print ("Email of correct:")
    print (a)
else:
    print ("Error:")
    print (a)
