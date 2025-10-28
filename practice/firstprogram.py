
# a = int(input("enter a number"))
# b = int(input("enter a number"))
# c = int(input("enter a number"))


# # if a > b & a > c:
# #  print("large vaue",a) 
# # elif b > a & b >c:
# #  print(b)
# # else :
# #  print(c)



# largest = a
# var = "a"

# if b > largest:
#   largest = b
#   var = "b"

#   if c>largest:
#    largest = c
#    var = "c"
  
# print(largest,var)





i = input('write input')
g = open('test.txt','w')
g.write(i)
g.close()

g = open('test.txt','a')
g.write(" chennai")
g.close()



f = open('test.txt','r')
content = f.read()
print(content)