import pygame
pygame.init()

#Part A
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

#Part B
def graph_coordinates(threeplus1_iters_dict):
    coordinates = [threeplus1_iters_dict]
    new_display = pygame.display.set_mode()
    flipped_screen = pygame.transform.flip(new_display, False, True)
    width, height = new_display.get_size()
    scaled_screen = pygame.transform.scale(new_display, (width*3, height*3))
    new_display.blit(flipped_screen, (0,0))
    pygame.display.flip()
    pygame.time.wait(2000)

graph_coordinates(threep1range(upper_limit=0))