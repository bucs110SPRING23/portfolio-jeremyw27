def multiply_nums(x, y):
    multiply = 0
    for i in range(y):
        multiply = multiply + x
    return multiply

def exponent(x, y):
    exponent = 1
    for i in range(y):
        exponent = exponent * x
    return exponent

def square(x):
    return exponent(x, 2)

def main():
    x = int(input("enter a number: "))
    y = int(input("enter a number (will be exponent): "))
    result = multiply_nums(x, y)
    print("your numbers multiplied is: " + str(result))
    result = exponent(x, y)
    print("your numbers exponentiated: " + str(result))
    result = square(x)
    print("your numbers squared: " + str(result))

main()