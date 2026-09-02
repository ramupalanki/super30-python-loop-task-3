text = input("Enter a string: ")

reversed_text = ""

for i in range(len(text) - 1, -1, -1):
    reversed_text = reversed_text + text[i]

if text == reversed_text:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")