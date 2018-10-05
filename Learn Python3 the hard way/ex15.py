from sys import argv

script, filename = argv
# filename need to be open first
text = open(filename)
# then read the opened text 
print(f"Here's your file {filename}")
print(text.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
