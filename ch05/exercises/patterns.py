rows = int(input("enter number of rows:"))

def star_pyramid():
    for i in range(1,rows+1):
        print("*" * i)
star_pyramid()

def rstar_pyramid():
    for i in range(rows, 0, -1):
        print("*" * i)
rstar_pyramid()