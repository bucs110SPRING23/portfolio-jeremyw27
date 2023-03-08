def star_pyramid(rows):
    for i in range(1,rows+1):
        print("*" * i)

def rstar_pyramid(rows):
    for i in range(rows, 0, -1):
        print("*" * i)

num_rows = int(input("enter number of rows:"))
star_pyramid(num_rows)
rstar_pyramid(num_rows)