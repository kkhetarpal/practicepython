#Exercise 2: practisepython
num =  int(raw_input("Please enter a number of your choice: "))
if ((num%4) == 0):
    print ("Number is a multiple of 4")
elif ((num % 2) == 0):
    print ("It is an even number, but not a multiple of 4")
elif ((num % 2) == 1):
    print ("It is an odd number")

