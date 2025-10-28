

#function print sqaure of odd number in a range
def sqrOfOdd():

 x = int(input("enter a start num"))
 y = int(input("enter a end num"))
 
 for n in range( x , y+1 ):
   if n%2 != 0:
     print( n * n )

#Main
sqrOfOdd()