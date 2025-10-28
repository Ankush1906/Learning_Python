# function takes positive number until a user enter a negative number
def always_positive(): 

 n = int(input("enter a number"))

 while n > 0:
  n = int(input("enter another number"))

 
print(n)


always_positive()