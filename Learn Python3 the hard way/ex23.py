import sys
script, input_encoding, error = sys.argv

# main函数做了递归。
def main(language_file, encoding, errors):
    line = language_file.readline()

    if line: # if line的内容不为空
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors) # recursion 递归

# strip(str):把字符串前后含有str中字符的部分删除，直到不包含在str中的字符出现。
# 或者说，strip是由两侧向中间的过程，到不能删除的部分截止，即使中间还有可以删的字符。
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)

'''
输出utf-8字符时出现乱码，问题根源在于所使用的font不包含对应的文字，
右键点击cmd标题栏，properties，Font，选择NSimSun，此字体支持的
文字种类最多，但还是不全。
Unicode 只是一个符号集，它只规定了符号的二进制代码，却没有规定这个二进制代码应该如何存储。
UTF-8 就是在互联网上使用最广的一种 Unicode 的实现方式。UTF-8 最大的一个特点，
就是它是一种变长的编码方式。它可以使用1~4个字节表示一个符号，根据不同的符号而变化字节长度。
UTF-8 的编码规则很简单，只有二条：

1）对于单字节的符号，字节的第一位设为0，后面7位为这个符号的 Unicode 码。
因此对于英语字母，UTF-8 编码和 ASCII 码是相同的。

2）对于n字节的符号（n > 1），第一个字节的前n位都设为1，第n + 1位设为0，
后面字节的前两位一律设为10。剩下的没有提及的二进制位，全部为这个符号的 Unicode 码。
'''
