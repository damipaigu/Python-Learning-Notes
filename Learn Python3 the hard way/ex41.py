import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []
# PHRASES中，%%% @@@ *** 都是所见即所得。
PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",

    "class %%%(object):\n\tdef __init__(self, ***)":
      "class %%% has-a __init__ that takes self and *** params.",

    "class %%%(object): \n\tdef ***(self, @@@)":
      "classs %%% has-a function *** that takes self and @@@ params.",

    "*** = %%%()":
      "Set *** to an instance of class %%%.",

    "***.***(@@@)":
      "From *** get the *** function, call it with params self, @@@.",

    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding='utf-8'))

'''random.sample(population, k): return a k length list of unique elements
chosen from the population sequence or set.'''
'''.capitalize() function converts the first letter of the string to capital. If
its first letter is already capital, then it returns the original string.
'''
def convert(snippet, phrase):
    # 按照snippet中%%%的个数，随机从WORDS中选取对应数量的item，打乱顺序、首字母大写
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    # 同上一条，按照snippet中***的数量随机选取
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)    # randint(a, b): a, b both inclusive.
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:    # snippet, phrase 这种写法表示他俩组成了一个tuple，我好蠢！！！！
"""snippet为PHRASHES的key，phrase为PHRASES的value，此循环共循环两次：snippet，phrase各一次。
参考test1.py。分别替换key和value中的%%%、***、@@@，替换为上面代码随机选取出来的单词。随后把修改好的内容（result）
append到results。results类型为list。
"""
        result = sentence[:]
#        print(f'Type of result: {type(result)}')

        # fake class class_names
        for word in class_names:
            #.replace(old_string, new_string, max_num_of_str_to_be_replaced)
            result = result.replace("%%%", word, 1)    # 此处要搭配for loop 所以要限制每次只改一个，每次改需要改的不一样

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    # print(f'results are {results}')
    # print(type(results))
    # return results


# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER:    {answer}\n\n")
except EOFError:
    print("\nBye")
