import sys # Text says to type "from sys import argv" but that apparently  doesn't work with 3.7.3

script, filename = sys.argv

txt = open(filename)

print(f"Here's your file {filename}")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())