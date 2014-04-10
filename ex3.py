#exercise3: lists
#sample
# my_list  = [1, 3, "Khimya", [5,6,7]]
# for element in my_list:
#     print element

# #exercise
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for element in a:
#     if (element < 5):
#         print element

# #extras
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for element in a:
#     if (element < 5):
#         new_list = element
#         print new_list

#extras
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
num = int(raw_input("Please Enter a number of your choice: "))
print "From the original list , Here are numbers smaller than your choice "
for element in a:
    if (element < num):
        return_list = element
        print return_list
