import numpy as np
class Test:
    def main():
        a=str(input("Enter your first name: "))
        b=str(input("Enter your last name: "))
        c = a+" "+b
        print("Your name is - > ",c)
    def main_2():
        a = str(input("Enter your School name- > "))
        b = str(input("Enter your name- > "))
        c = str(input("Enter your last name- > "))
        d = str(input("Enter your class name- > "))
        final_str= "My name is {1} {2}. I study in {0} school. I am in {3}"
        print(final_str.format(a,b,c,d))       

class Test1:
    def even_odd():
        a = int(input("Enter starting:"))
        b = int(input("Enter starting:"))
        print("Even numbers are:")
        for x in range(a,b+1):
            if x%2==0:
                print(x,end=" ")
        print("\n")
        print("Odd numbers are:")
        for x in range(a,b+1):
            if x%2==1:
                print(x,end=" ")
#object_loop = Test1
#object_loop.even_odd()

#import random as rand
#abc =rand.randint(a=int(input()),b=int(input()))
# #print abc
# print("""
#       Hello wordl.
#       Hello i study at SIT
#       My name is Praneet.
#       I am SDA""")
