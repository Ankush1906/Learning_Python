#program to read a text file  line by line and check if it contains owrd " python" 


def ReadLine():
 f = open('test.txt','r')
 lines = f.readlines()
 
 for line in lines:
  if "python" in line.lower():
   print(line)


ReadLine()

 


 