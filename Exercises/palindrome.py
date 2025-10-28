# program to check a string is palindrome


def palindrome(str):
    i = 0
    j = len(str) -1 

    while i < j:
        if str[i] != str[j]:
            print(f"{str} is not palindrome")
            return
               
        else:
            i += 1
            j = j-1 
  
    print(f"{str} is palindrome")


palindrome("madam")
