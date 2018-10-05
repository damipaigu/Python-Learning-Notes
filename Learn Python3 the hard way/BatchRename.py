import os.path, time, sys, glob#, collections.deque as deque

# class BatchRename(Template):
#     delimiter = '%'

# receive the directory path:
try:
    dir_path = input('Where are the files located?')
except FileNotFoundError:
    dir_path =input('No such file or directory. \n Please try again: ')

os.chdir(dir_path)
name_list = glob.glob('*.csv')
print(name_list)
sorted_name_list = []
match_list  = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
for i, letter in enumerate(match_list):
    for j, name in enumerate(name_list):
        if letter in name:
            sorted_name_list.append(name)
            continue

print(sorted_name_list)

name = input('Enter the rename style ($d-date $n-seqnum $f-format):  ')


# t = BatchRename(name)
# date = time.strftime('%d%b%y')
# for i, filename in enumerate()
