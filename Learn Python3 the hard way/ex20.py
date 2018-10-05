from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())
''' seek 表示的是offset，代表read/write pointer 在文件中的字节位置，0代表文件第一个
字节之前，1代表第二个字节之前。。。
无论读取还是写入都在此位置开始进行。
忘了的话把0改成1，2，3运行看结果的rewind之后的输出。
seek中还可以加第二个可选参数，0：absolute file positioning；
1：relative to the current position; 2: relative to the file's end.'''

# readline() 加的参数表示读取的字节数，参数为空表示读取整行；
# readline(1) 读取光标所在位置后的一个字节。读取后光标会移动到读取的字符之后。

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file: \n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

''' my own test
readline 读取当前位置的一行内容
readlines 读取文件内包含的所有行，以行为单位一块输出为一个list。
'''
print('*' * 15)
rewind(current_file)
single_line = current_file.readline()
lines = current_file.readlines()
print(f"The current line is: {single_line}")
print(f'The whole file {lines}')
