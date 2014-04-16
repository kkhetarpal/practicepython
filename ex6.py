#palindrome or not

string = raw_input("Please enter a string: ")
rev_string = string[::-1]
print rev_string

if list(string) == list(rev_string):
    print("it is a pallindrome")
else:
    print("It is not a palindrome")

#print list(string)
# def is_pallindrome(string):
#     rev_string = string[::-1]
#     if(list(string)==list(rev_string)):
#         return True
#     else:
#         return False
# is_pallindrome(string)




    
