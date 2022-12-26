file_book = open('phonebook.txt')
line_count = sum(1 for line in open('phonebook.txt'))
print(line_count)
file_book.close()