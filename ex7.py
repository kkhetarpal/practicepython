#one line code to get a new list from given list

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_a = [i for i in a if ((i%2)==0)]
odd_a = [i for i in a if ((i%2)!=0)]
print even_a
print odd_a
