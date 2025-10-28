
#program to print reverse of a number
def reverse(n):
 
 while n > 0:
  rem = int( n%10 ) # it will give the last digit
  print( rem , end='')
  n = int(n/10)  # it will remove the last digit


reverse(123)
