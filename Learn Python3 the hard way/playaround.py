file = 'test.txt'

open_file = open(file)

print('-' * 15)
print(open_file.readline())

open_file.seek(0)
print('-' * 15)
print(open_file.readline(1))
print(open_file.readline(2))
print(open_file.readline(4))
open_file.close()
