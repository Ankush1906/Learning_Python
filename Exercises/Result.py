#Write a Python script that reads a list of marks and prints “Pass” if all marks are above 40, otherwise “Fail”, using logical AND.

def check_result():

    marks = list(map(int, input("Enter marks : ").split()))

    if marks[0] > 40 and marks[1] > 40 and marks[2] > 40 and marks[3] > 40 and marks[4] > 40:
        print("Pass")
    else:
        print("Fail")

check_result()