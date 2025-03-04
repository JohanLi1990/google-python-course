#!/usr/bin/python3
from pathlib import Path

# path = Path('pi_digits.txt')
# contents = path.read_text().rstrip()
# lines = contents.splitlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
# print(pi_string)

# path = Path('programming.txt')
# path.write_text("i luv programming")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    firstNumber = input("\nFirst number:")
    if firstNumber == 'q':
        break
    second_number = input("\nSecond number:")
    if second_number == 'q':
        break
    try:
        answer = int(firstNumber) / int(second_number)
    except ZeroDivisionError:
        print("U cannot divide by zero")
    else : 
        print(answer)