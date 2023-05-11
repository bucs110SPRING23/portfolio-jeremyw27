class Enemy:
    def __init__(self, speed=0, hitbox=0, health=0):
        self.speed = speed # enemy speed
        self.hit_range = hitbox # how far the enemy can hit the player
        self.health = health # health of the enemy

class Tube:
    def __init__(self, color=""):
        self.color = color # color of the tube
        self.has_plant = False # tube has no plant in it by default
        self.accept_player = False # player cannot go in tube by default

class Block:
    def __init__(self, x=0, y=0):
        self.is_mystery = False # block is not a mystery block by default
        self.can_break = False # block cannot break by default
        self.pos = (x,y) # position of the block
