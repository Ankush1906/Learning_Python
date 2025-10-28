
def count_words():

 file = open('test.txt',"r")
 lines = file.readlines()
 file.close()
 print(f" lines in  {len(lines)}")

 words = 0
 char = 0
  
 for line in lines :
    char += len(line)  
    words += len(line.split())



 print(f"words in lines {words}")
 print(f"chars in lines {char}")


count_words()