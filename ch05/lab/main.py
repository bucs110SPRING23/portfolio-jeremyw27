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

def threep1range(upper_limit):
    objs_in_sequence = {}
    for _ in range(2, upper_limit+1):
        threenp1(_)
        objs_in_sequence[_] = threenp1(_)
    return objs_in_sequence

def graph_coordinates(threeplus1_iters_dict):
    coordinates = [threeplus1_iters_dict]
    new_display = pygame.display.set_mode()
    new_display = pygame.transform.flip(new_display, False, True)
    width, height = new_display.get_size()
    new_display = pygame.transform.scale(new_display, (width*3, height*3))
    new_display.blit(new_display, (0,0))

    max_so_far = 0
    for _ in threeplus1_iters_dict:
        pass

    font = pygame.font.Font(None, 36)
    msg = font.render("display", True, "black")
    display.blit(msg, pos)


def main():
    pygame.init()
    upper_limit = int(input("Enter some upper limit here: "))
    print(threep1range(upper_limit))
    graph_coordinates(threep1range(upper_limit))
main()