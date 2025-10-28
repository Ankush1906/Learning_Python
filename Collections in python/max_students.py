# Write a program to collect all the students information and find who is score maximum




print ('Enter "START" to enter the student details and "STOP" to finish the details')

choice = input("")


students = []

while choice != "STOP":
   name = input("enter  name")
   marks = int(input("enter  marks"))
   students.append((name,marks))
   choice = input('To stop type "STOP" or press ENTER to continue ')


# highest = 0
# topper = ""

# for n , m in students:
#   if m > highest:
#     highest = m
#     topper = name

print([students])

max_marks = max(students,key = lambda x : x[1] )

print(max_marks)

