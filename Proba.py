from re import sub
dict_phone = tuple()
file_book = open('test.txt')
line_count = sum(1 for line in open('test.txt', 'r+'))
new = ''
if line_count > 0:
    for i in file_book:
        if i.find('Serhii'):
            print(i,'11')
            list = i.split(',')
            print(list,'22')

        new += ('').join(list)
        print(new, '33')
