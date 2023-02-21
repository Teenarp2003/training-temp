# import numpy as np
# num=int(input("Enter the number: "))
# class Define:
#     def positive:
#         if num > 0
#         return ("number is positive")
#     def negative:
#         if num < 0:
#             return("Number is negative")
#     def zero:
#         if num ==0:
#             return("number is zero")
        
        
        
        
        
# class Number:
#     def __init__(self, num):
#         self.num = num

#     def check(self):
#         if self.num > 0:
#             print("Positive")
#         elif self.num == 0:
#             print("Zero")
#         else:
#             print("Negative")

# # Create an object of the Number class
# num = Number(int(input("Enter number: ")))

# # Call the check method to determine if the number is positive, negative, or zero
# num.check()

class DuplicateCounter:
    def __init__(self, lst):
        self.lst = lst

    def count_duplicates(self):
        duplicates = {}
        for i in self.lst:
            if i in duplicates:
                duplicates[i] += 1
            else:
                duplicates[i] = 1
        count = 0
        for key, value in duplicates.items():
            if value > 1:
                count += 1
        return count
arr[]
for i in range(10):
   arr.append(input("Enter element: ")) 

my_list =arr[] 
counter = DuplicateCounter(my_list)
print(counter.count_duplicates())  # Output: 6
