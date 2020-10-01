import pygame,sys, random

pygame.init()

win = pygame.display.set_mode((500, 480))
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
            pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

char = pygame.image.load('standing.png')
screen = pygame.display.set_mode((576,800))
clock = pygame.time.Clock()


bg_surface = pygame.image.load('background_flappy.png').convert()   #pour telecharger le background danss le code
bg_surface = pygame.transform.scale2x(bg_surface)                   #etandre l'image back ground au maximum au point x=0 y=0
bg_x_pos = 0
bg_y_pos = 0

floor_surface = pygame.image.load('base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0
floor_y_pos = 650

pipe_surface = pygame.image.load('pipe-green.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)





class player(object):
    def __init__(self,x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5 #Vitesse
        self.isJump = False #Savoir si il saute ou pas
        self.jumpCount = 10
        self.left = False #Si il bouge vers la gauche
        self.right = False #Si il bouge vers la droite
        self.walkCount= 0 #Compte le nombre de pas

    def draw(self,win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[int(self.walkCount // 3)], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[int(self.walkCount // 3)], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x, self.y))
            self.walkCount = 0



def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    new_pipe = pipe_surface.get_rect(midtop = (1000, random_pipe_pos))
    return new_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes


def redrawGameWindow():
    perso.draw(win)
    pygame.display.update()

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, floor_y_pos))
    screen.blit(floor_surface, (floor_x_pos + 576, floor_y_pos))

def draw_bg():
    screen.blit(bg_surface, (bg_x_pos, bg_y_pos))  # etandre l'image background au maximum au point x=0 y=0
    screen.blit(bg_surface, (bg_x_pos + 1100, bg_y_pos))  # etandre l'image background au maximum au point x=0 y=0
def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface, pipe)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 2000)
pipe_height = [590,570,580]

perso = player(50, 600, 40, 60)
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        if event.type == SPAWNPIPE:
            pipe_list.append(create_pipe())

    pipe_list = move_pipes(pipe_list)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and perso.x > perso.vel:
        perso.x -= perso.vel
        perso.left = True
        perso.right = False

    elif keys[pygame.K_RIGHT] and perso.x < 500 - perso.vel - perso.width:
        perso.x += perso.vel
        perso.left = False
        perso.right = True

    else:
        perso.left = False
        perso.right = False
        perso.walkCount = 0

    if not (perso.isJump):
        if keys[pygame.K_SPACE]:
            perso.isJump = True
            perso.left = False
            perso.right = False
            perso.walkCount = 0
    else:
        if perso.jumpCount >= -10:
            perso.y -= ((perso.jumpCount * abs(perso.jumpCount))) * 0.5
            perso.jumpCount -= 1
        else:
            perso.jumpCount = 10
            perso.isJump = False


    floor_x_pos -= 3  # vitesse vers la droite vers la gauche pour le sol
    bg_x_pos -= 3  # vitesse vers la droite vers la gauche pour le bg
    draw_bg()
    draw_pipes(pipe_list)
    draw_floor()

    if bg_x_pos <= -1100:
        bg_x_pos = 0
    if floor_x_pos <= -576:
        floor_x_pos = 0

    redrawGameWindow()
    pygame.display.update()

pygame.quit()