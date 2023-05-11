import pygame

def threenp1(n):
    count = 0
    while n > 1.0:
        count += 1
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3 * n + 1)
    return count

def threenp1range(upper_limit):
    objs_in_sequence = {}
    for _ in range(2, upper_limit+1):
        threenp1(_)
        objs_in_sequence[_] = threenp1(_)
    return objs_in_sequence

def graph_coordinates(threenplus1_iters_dict):
    coordinates = []
    for key, value in threenplus1_iters_dict.items():
        coordinates.append((key,value))
    
    screen = pygame.display.set_mode()
    screen.fill("lightblue")
    pygame.draw.lines(screen, "black", False, coordinates, width=1)
    flipped_screen = pygame.transform.flip(screen, False, True)
    width, height = flipped_screen.get_size()
    scaled_screen = pygame.transform.scale(flipped_screen, (width, height))
    screen.blit(scaled_screen, (0,0))
    pygame.display.flip()

    max_so_far = [0,0]
    for key, value in threenplus1_iters_dict.items():
        if value >= max_so_far[1]:
            max_so_far[1] = value
            max_so_far[0] = key
            
    font = pygame.font.Font(None, 36)
    msg = font.render("The largest number of iterations for the value " + str(max_so_far[0]) + " is " + str(max_so_far[1]) + ".", True, "black")
    screen.blit(msg, (width/3, height/2))
    pygame.display.flip()
    pygame.time.wait(4000)


def main():
    pygame.init()
    upper_limit = int(input("Enter some upper limit here: "))
    print(threenp1range(upper_limit))
    graph_coordinates(threenp1range(upper_limit))

main()