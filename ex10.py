#exercise 10: list overlap

import random 
a = random.sample(range(100),10)
b = random.sample(range(100),15)
common_elements = [i for i in a for j in b if i==j]

print a
print b
print common_elements
