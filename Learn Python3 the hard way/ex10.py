tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# Escape Sequence
print('Backslash (\\): \\\\')
print('Single-quote (\'): \\\'')
print('Double-quote (\"): \\\"')
print('ASCII bell (BEL): \\a')
print('ASCII backspace (BS): \\b')
print('ASCII formfeed (FF): \\f')
print('ASCII linefeed (LF): \\n')
print('Character named name in the Unicode database (Unicode only): \\N{name}')
print('Carriage Return (CR): \\r')
print('Horizontal Tab (TAB): \\t')
print('Character with octal 八进制 value ooo: \\ooo')
print('Character with hex 十六进制（8-bit??） value hh: \\xhh')
print('Character with 16-bit hex 十六进制 value xxxx: \\uxxxx')
print('Character with 32-bit hex 十六进制 value xxxxxxxx: \\Uxxxxxxxx')
print('ASCII vertical tab (VT): \\v')
