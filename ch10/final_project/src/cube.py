import pygame

X_POS = 50
Y_POS = 362
SCALE_FACTOR = 70
JUMP_VELOCITY = 8

class Cube(pygame.sprite.Sprite):
    def __init__(self, img="assets/cubeicon.png"):
        """
        Initalizes the avatar object, which will be a cube.
        args: x and y coordinate (int)
        return: none
        """
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(img), (SCALE_FACTOR, SCALE_FACTOR))
        self.is_jumping = False

        self.cube_rect = self.image.get_rect()
        self.cube_rect.x = X_POS
        self.cube_rect.y = Y_POS
        self.jump_velocity = JUMP_VELOCITY

    def update(self, key_press):
        """
        """
        if self.is_jumping:
            self.jump()
        if (key_press[pygame.K_UP] and not self.is_jumping) or (key_press[pygame.K_SPACE] and not self.is_jumping):
            self.is_jumping = True

    def jump(self):
        """
        """
        if self.is_jumping:
            self.cube_rect.y -= self.jump_velocity * 2 # how high the cube will go up
            self.jump_velocity -= 0.5 # strength of gravity/rate at which cube will come back down
        if self.jump_velocity < -JUMP_VELOCITY:
            self.is_jumping = False
            self.jump_velocity = JUMP_VELOCITY # reset jump velocity

        # make cube flip when jumping

    def draw(self, screen):
        """
        """
        screen.blit(self.image, (self.cube_rect.x, self.cube_rect.y))

