
#function counts number of vowels in a string
def CountOfVowels(str):
 
 count = 0 
 for char in str:
    if char in 'aeiou':
      count += 1

 return count

#main
 
vowels = print(CountOfVowels('ankush'))