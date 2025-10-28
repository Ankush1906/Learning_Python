# n = 5
# if n%2 == 0:  # remainder
#  print(f"{n} is not a prime number")
# else:
#  print(f"{n} is a prime number")


#function to check a number is prime

import math

def isPrime(n):
  
  if n < 2:
      return
  
  rear = int(math.sqrt(n))+1

  for i in range(2 ,rear):
    if n%i == 0:
     return
  else:
   print(n)




# print prime in range 
def PrimeRange():
 
 x = int(input("Enter  start number"))
 y = int(input("Enter  end number"))
 
 for n in range (x,y+1):
  isPrime(n)



  #Main 
PrimeRange()