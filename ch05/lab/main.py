import pygame
pygame.init()

def threenp1(n):
    count = 0
    while n > 1.0:
        count += 1
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3 * n + 1)
    return count

def threep1range(upper_limit):
    objs_in_sequence = {}
    for _ in range(2, upper_limit+1):
        threenp1(_)
        objs_in_sequence[_] = threenp1(_)
    return objs_in_sequence

def main():
    n = int(input("Enter some upper limit here: "))
    print(threep1range(n))

main()