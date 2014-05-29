

factors = [1, 5, 7, 13, 29, 35, 65, 91, 145, 203, 377, 455, 1015, 1885, 2639, 13195]

length = len(factors)
j = length-1


while j < length and j >= 0 :
    count = 0
    num  = factors[j]
    #print num 
    for k in range(2,num):
        if (num%k == 0):
           count = 1 
    #print count
    if (count == 0):
        print num
        break
    j = j - 1
   
           

