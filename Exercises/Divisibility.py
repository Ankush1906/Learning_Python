# funtion that check a number is divisible by 3 and 5 but not 7


def check_number(n):

    if (n / 3 == 0 and n / 5 == 0) and n / 7 != 0:
       print(f"{n} is divisible by 3 and 5 but not 7")
    else:
        print(f"{n} does not satisfy the condition")


check_number(15)