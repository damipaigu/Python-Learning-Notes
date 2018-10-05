from sys import argv

script, filename = argv

print(f"We're goning to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C)")
print("If you do want that, hit RETURN.")

input('? ')
# 打开要被写入的文件时，文件名后要加参数'w', 以提供写入权限。
print("Opening the file...")
target = open(filename, 'w')
# truncate()命令， 清空文件内容
print("truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')
# close()命令，保存/关闭文件？
print("And finally, we close it.")
target.close()
