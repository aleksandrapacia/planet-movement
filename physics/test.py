import pygame, sys, pymunk


# Fd = m * a * r
# vk = v * r
#PLANET
def create_planet(space):
    body = pymunk.Body(1,60, body_type = pymunk.Body.DYNAMIC) # Static Body - a body that does not move but other bodies can collidewith it
    body.position = (400,0)
    body.center_of_gravity = (25,25)
    shape = pymunk.Circle(body, 80)
    space.add(body,shape)
    return shape 

def draw_planet(planets):
    for planet in planets:
        pos_x = int(planet.body.position.x)
        pos_y = int(planet.body.position.y)
        pygame.draw.circle(screen, (255,255,255), (pos_x,pos_y),80)
#SUN
def create_static_star(space):
    body = pymunk.Body(body_type= pymunk.Body.STATIC)
    body.position = (300, 300)
    body.center_of_gravity = (25,25)
    
    shape  = pymunk.Circle(body, 50)    
    space.add(body,shape)
    return shape
def draw_static_star(stars):
    for star in stars:
        pos_x = int(star.body.position.x)
        pos_y = int(star.body.position.y)
        pygame.draw.circle(screen, (255, 247, 0), (pos_x,pos_y),40)


pygame.init()
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity= (0,50)
stars = []
stars.append(create_static_star(space))

planets = []
planets.append(create_planet(space))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0,0,0))
    draw_static_star(stars)
    draw_planet(planets)
    space.step(3/50)
    pygame.display.update()
    clock.tick(120)
