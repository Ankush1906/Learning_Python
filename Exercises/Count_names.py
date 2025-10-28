
#funtion return a list of names that start with vowel

def count_names():

  list = []
  for i in range(5):
   name = input("write a name")
   if name[0].lower() in 'aeiou':
      list.append(name)


  return list
     

print(count_names())