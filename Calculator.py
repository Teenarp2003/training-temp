def add(inp1,inp2):
    return inp1 + inp2 
def subtract(inp1,inp2):
    return inp1 - inp2
def multiply(inp1,inp2):
    return inp1 * inp2
def divide(inp1,inp2):
    if inp2 ==0:
        return "Error:cannot devide by 0"
    else:    
        return inp1 / inp2
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op = input("Enter the operation you want to perform (+, -, *, /): ")
if op == "+":
    result = add(num1, num2)
elif op == "-":
    result = subtract(num1, num2)
elif op == "*":
    result = multiply(num1, num2)
elif op == "/":
    result = divide(num1, num2)
else:
    result = "Error: Invalid operation"

print("Result: ", result)

    
  