
# add_10 = lambda x : x+10 
# print(add_10(5))




# multiply = lambda x,y :x*y

# print(multiply(4,5))



# square = lambda x :x*x

# print(square(5))


# Lambda function with a condition


check_even = lambda x : "Even" if x % 2 == 0 else "odd"

print(check_even(6))


# Using map() to add 5 to each element in the list

numbers = [1,2,3,4]

result = map(lambda x : x+5,numbers)


print(list(result))


# Using filter() to get only numbers greater than 3


numbers  = [1,2,3,4,5]

result = filter(lambda x : x*x >5,numbers)

print(list(result))


#sorting a list of students based on marks



student = [("deb",90),("saiman",70),("ayush",80)]

pass_students = sorted(student,key= lambda stu : stu[1])





print(pass_students)



#using lambda with map

num = [ 1,2,3,4,5]
doubled =list(map(lambda x : x*2,num))
print(doubled)


for i in num:
  print(list(i * 2))
