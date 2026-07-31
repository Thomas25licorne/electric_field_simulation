import pygame

pygame.init()

BLACK = (0, 0, 0)

size = (700, 550)
screen = pygame.display.set_mode(size)

font = pygame.font.SysFont('Calibri', 25, True, False)
font2 = pygame.font.SysFont('Calibri', 20, True, False)
font3 = pygame.font.SysFont('Calibri', 15, True, False)


    
point_charge = font.render("Point Charge", True, BLACK)
plane = font.render("Plane", True, BLACK)
rod = font.render("Rod", True, BLACK)
disk = font.render("Disk", True, BLACK)

charge_value = font.render("Charge Value", True, BLACK)

positive = font2.render("Positive Charge", True, BLACK)
negative = font2.render("Negarive Charge", True, BLACK)


exp_up = font3.render("Exponent Up", True, BLACK)
exp_down = font3.render("Exponent Down", True, BLACK)



done = font.render("Done", True, BLACK)


texts = [point_charge, plane, rod, disk, charge_value, positive, negative, exp_up, exp_down, done]





coords_text = [
    
    [560, 70],
    [560, 150],
    [560, 230],
    [560, 310],
    [10, 420],
    [15, 180],
    [10, 280],
    [480, 455], 
    [130, 455],    
    [615, 510],
]

def text_print_pygame(texts, coords_text):
    
    for i in range(len(texts)):
        screen.blit(texts[i], coords_text[i])


    