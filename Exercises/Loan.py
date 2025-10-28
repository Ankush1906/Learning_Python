#14. Using logical operators, write a program that accepts a user’s age and salary and determines if they are eligible for a loan (age ≥ 21 and salary ≥ ₹25,000).


def check_loan():
 
  age = int(input("your age"))
  salary = int(input("your salary"))

  if age >= 21 and salary >= 25000 :
    print("your are eligible for Loan")
  else:
    print("you are not eligible for Loan")




check_loan()