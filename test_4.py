import pathlib
path = pathlib.Path(r'C:\11.txt')

fh = open(path, 'r')
list_employee = list()
fh.seek(0)
result = fh.readlines()
for i in result:
    list_employee.append(i[:-1])
fh.close()

print(list_employee)