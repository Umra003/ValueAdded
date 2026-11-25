
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

if len(num1) != len(num2):
    print("Not anagram numbers")
else:
    for digit in num1:
        if num1.count(digit) != num2.count(digit):
            print("Not anagram numbers")
            break
    else:
        print("Anagram numbers")
