#exercise 4: Divisors :: Create a program that asks the user for a
#number and then prints out a list of all the divisors of that
#number. (If you don't know what a divisor is, it is a number that
#divides evenly into another number. For example, 13 is a divisor of
#26 because 26 / 13 has no remainder.)

num = int(raw_input("Enter a number:"))
all = range(1,num+1) #numbers from 1-maximum number
divisors = []
for i in all:
    if((num%i)==0):
        divisors.append(i)
print " The number" + 'num' + "has the following divisors:"  
print divisors
       
