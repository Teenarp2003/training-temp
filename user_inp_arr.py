class Array:
    def main_array():
        arr_1=[]
        n = int(input("Enter number of elements: "))
        for x in range(0,n):
            ele = int(input())
            arr_1.append(ele)
        print(arr_1)
        arr_1.sort()
        print("Ascending order:",arr_1)
        arr_1.sort(reverse=True)
        print("Descending Order:",arr_1)
object=Array
object.main_array()

            