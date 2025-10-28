
#function prints all factor of n

def factors(n):
 for i in range(1,n+1):
   if n % i == 0:
     print(i)

factors(10)