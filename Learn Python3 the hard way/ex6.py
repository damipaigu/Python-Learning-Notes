# 变量赋值时即可在变量前加字母f表示格式：变量内容中包含了另外的变量
types_of_people = 10
x = f"There are {types_of_people} types of people."
binary = "binary"
do_not = "do_not"
y = f"Those who know {binary} and those who {do_not}."

# print variable 直接在print中放入变量名即可
print(x)
print(y)

# 在打印的文字中加入变量，要给变量名加大括号
print(f"I said: {x}")
print(f"I also said: {y}")

# 想在打印文字中加入变量，但变量的内容要运行时决定，使用.format()
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))


w = "This is the left side of ..."
e = "a string with a right side."
print(w + e)
