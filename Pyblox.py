import math
import pygame

# colours
pink = (255, 20, 147) # player
brue = (0, 191, 255) # ball
this = (119, 136, 153) # background
green = (124, 252, 0) # blocks
red = (255, 0, 0) # text

# height and width of the blocks
block_width = 50
block_height = 20
 
class Block(pygame.sprite.Sprite): # blocks to be eliminated
    def __init__(self, color, x, y): # Constructor
        super().__init__()
        self.image = pygame.Surface([block_width, block_height]) # blocks on screen
        self.image.fill(color) # filling colour
        self.rect = self.image.get_rect() # rectangle blocks
        self.rect.x = x # x position of the block
        self.rect.y = y # y position of the block
 
 
class Ball(pygame.sprite.Sprite): # ball
    speed = 12.3 # ball speed

    # position at the start
    x = 0.0
    y = 200.0
    direction = 150 # direction of the ball 
    width = 10
    height = 10

    def __init__(self): # Constructor
        super().__init__()
        self.image = pygame.Surface([self.width, self.height]) # ball on screen
        self.image.fill(brue) # blue colour
        self.rect = self.image.get_rect() # shape of rect
        
        # screen attributes
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
     
    def bounce(self, diff): # bouncing from a surface
        self.direction = (180 - self.direction) % 360
        self.direction -= diff
     
    def update(self): # position of the ball on the screen
        direction_radians = math.radians(self.direction) # conversion
        
        # changing x, y positions according to speed and direction
        self.x += self.speed * math.sin(direction_radians)
        self.y -= self.speed * math.cos(direction_radians)

        # position of x and y
        self.rect.x = self.x
        self.rect.y = self.y
         
        if self.y <= 0: # bouncing from the top
            self.bounce(0)
            self.y = 1

        if self.x <= 0: # bouncing from the left
            self.direction = (360 - self.direction) % 360
            self.x = 1

        if self.x > self.screenwidth - self.width: # bouncing from the right
            self.direction = (360 - self.direction) % 360
            self.x = self.screenwidth - self.width - 1
            
        if self.y > 600: # out of the bottom screen
            return True
        
        else: # no bouncing
            return False
 
class Player(pygame.sprite.Sprite): # Player
    def __init__(self): # Constructor
        super().__init__()
        
        # width and height of the player block at the bottom
        self.width = 85
        self.height = 15
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((pink)) # colour pink
        self.rect = self.image.get_rect()
        
        # placing on the screen
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
        
        # window opens
        self.rect.x = -10 
        self.rect.y = self.screenheight-self.height
     
    def update(self): # position of the player on the screen
        pos = pygame.mouse.get_pos() # mouse's location is the player
        self.rect.x = pos[0] # left side of player = mouse position
        
        # player stays on screen
        if self.rect.x > self.screenwidth - self.width:
            self.rect.x = self.screenwidth - self.width
 
pygame.init() # pygame library
screen = pygame.display.set_mode([1020, 600]) # screen of the game
pygame.display.set_caption('Pyblox Game') # name of the window
pygame.mouse.set_visible(0) # mouse isn't visible on screen
font = pygame.font.Font(None, 36) # sie of the text
background = pygame.Surface(screen.get_size()) # surface for drawing

# sprite lists pygame
blocks = pygame.sprite.Group()
balls = pygame.sprite.Group()
allsprites = pygame.sprite.Group()

# player object
player = Player()
allsprites.add(player)

# ball object
ball = Ball()
allsprites.add(ball)
balls.add(ball)

# distance between the block and the top
top = 30
blockcount = 14 # columns of blocks on screen
 
for row in range(5): # number of blocks rows
    for column in range(0, blockcount):
        
        # distance between top and bottom and from each other
        block = Block(green, column * (block_width + 20) + 30, top)
        blocks.add(block)
        allsprites.add(block)
        
    top += block_height + 8 # distance between each block

# for speed 
clock = pygame.time.Clock()

# checking for game
game_over = False

# checking to exit
exit_program = False
 
while exit_program != True:
    clock.tick(35) # FPS
    screen.fill(this) # clearing screen
     
    for event in pygame.event.get(): # for game over
        if event.type == pygame.QUIT:
            exit_program = True
     
    if not game_over: # keep on playing if nto game over
        player.update()
        game_over = ball.update()
     
    if game_over: # when game is over
        text = font.render("Game Over > Restart to play again", True, red)
        textpos = text.get_rect(centerx=background.get_width()/2)
        textpos.top = 300 # from the top
        screen.blit(text, textpos)
     
    if pygame.sprite.spritecollide(player, balls, False): # ball hitting the player
        # ball being deflected in different directons by the player
        diff = (player.rect.x + player.width/2) - (ball.rect.x+ball.width/2)

        # ball's y position if hit by the player
        ball.rect.y = screen.get_height() - player.rect.height - ball.rect.height - 1
        ball.bounce(diff)
        
    # collisions between ball and blocks 
    deadblocks = pygame.sprite.spritecollide(ball, blocks, True)
     
    if len(deadblocks) > 0: # bounce ball if hit
        ball.bounce(0)

        # game ends if no blocks left
        if len(blocks) == 0:
            game_over = True

    allsprites.draw(screen) # drawing on screen
    pygame.display.flip() # show what's being drawn
pygame.quit() # quitting from the game
