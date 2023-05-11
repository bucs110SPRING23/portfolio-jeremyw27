import pygame

class Cube(pygame.sprite.Sprite):
    def __init__(self, img="assets/cubeicon.png"):
        """
        Instantiates the player object, which will be a cube. The cube will be a sprite to manage collisions with spikes.
        args: none
        return: none
        """
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load(img), (45, 45))
        self.is_jumping = False
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 381
        self.jump_velocity = 8

        # death effect image
        self.death_effect = pygame.transform.scale(pygame.image.load("assets/death_effect.png"), (60, 60)) # create function to switch to death effect 

    def update(self, key_press):
        """
        Update the cube. Check if the cube is jumping and make it jump by using either the spacebar or the up-arrow key.
        args: key_press (checks whether a key is being pressed)
        return: none
        """
        if self.is_jumping:
            self.jump()
        if (key_press[pygame.K_UP] and not self.is_jumping) or (key_press[pygame.K_SPACE] and not self.is_jumping):
            self.is_jumping = True

    def jump(self):
        """
        Enables the jumping function of the cube.
        args: none
        return: none
        """
        if self.is_jumping:
            self.rect.y -= self.jump_velocity * 4 # how high the cube will go up
            self.jump_velocity -= 0.5 # strength of gravity/rate at which cube will come back down
        if self.jump_velocity < -8:
            self.is_jumping = False
            self.jump_velocity = 8 # reset jump velocity

    def draw(self, screen):
        """
        Display the cube on the screen.
        args: screen
        return: none
        """
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def death(self):
        """
        When the cube collides with an obstacle, it will update the original cube image to the death effect image.
        args: none
        return: none
        """
        self.image = self.death_effect

