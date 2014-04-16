#exercise 5: list overlap
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

import random 
a = random.sample(range(50),10)
b = random.sample(range(80),15)


common_elements = []
for i in a:
    for j in b:
        if (i==j):
            common_elements.append(i)

common_elements = list(set(common_elements)) #removes the duplicate items and sorts the list 

print a
print b
print common_elements
