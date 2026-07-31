import pygame       
from buttons import *
from drawboard import *
from slider import *
from text_to_blit import * 
 

pygame.init()
def input(): 
    # Initialize the variables
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    GRAY = (128, 128, 128) 

    PI = 3.141592653
    
    size = (700, 550)
    screen = pygame.display.set_mode(size)
    done = False
    clock = pygame.time.Clock()


    left_click = False 
    time = [0, 0]
    mouse_pos = [1000, 1000]
    current_type = 101
    point_charge_radius = 7
    
    
    
    # Main loop
    while not done:
        
        # Getting the input of the user 
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                done = True  

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:    
                    print(myBoard.all)
                        

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    left_click = True
                    time[0] = 0
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    left_click = False
                    left_clicked = True
                    time[1] = 0

                    
                for button in buttons:
                    button.left_clicked = False
                    if button.mouse_in_button(mouse_pos):
                        button.left_clicked = True
                    
                    
        # Logic             
        mouse_pos = pygame.mouse.get_pos() 

        
        for button in buttons:
            if button.mouse_action_in_button(mouse_pos, left_click, time):
                current_type = button.value_correspondence
            
                if current_type == 301:
                    charge_slider.exponent -= 1
                elif current_type == 302:
                    charge_slider.exponent += 1
                
                elif current_type == 1:
                    done = True
            



        myBoard.mouse_action_in_board(mouse_pos, left_click, time, current_type)
        charge_slider.mouse_in_slider(mouse_pos, left_click)

        myBoard.filter_type(current_type)


        time[0] += 1
        time[1] += 1


        # Displaying the screen in gray
        screen.fill(GRAY)
                    
        # Draw all types of charges
        if len(myBoard.point_charges) > 0:
            for charges in myBoard.point_charges:
                if charges[1] == -1:
                    pygame.draw.circle(screen, [0, 0, 255], charges[0], point_charge_radius, 0)
                else:
                    pygame.draw.circle(screen, [255, 0, 0], charges[0], point_charge_radius, 0)
        
        if len(myBoard.planes) > 0:
            for charges in myBoard.planes:
                if charges[1] == -1:
                    pygame.draw.rect(screen, [0, 0, 255], charges[0], 0)
                else:
                    pygame.draw.rect(screen, [255, 0, 0], charges[0], 0)
        
        if len(myBoard.disks) > 0:
            for charges in myBoard.disks:
                if charges[1] == -1:
                    pygame.draw.circle(screen, [0, 0, 255], charges[0][0], charges[0][1], 0)
                else:
                    pygame.draw.circle(screen, [255, 0, 0], charges[0][0], charges[0][1], 0)
        
        # Redraw the main screen white       
        pygame.draw.rect(screen, WHITE, [0, 0, 150, size[1]], 0)                
        pygame.draw.rect(screen, WHITE, [0, 0, size[0], 50], 0)                
        pygame.draw.rect(screen, WHITE, [550, 0, size[0], size[1]], 0)                
        pygame.draw.rect(screen, WHITE, [0, 450, size[0], size[1]], 0)                

        # Draw the board
        pygame.draw.rect(screen, myBoard.color, myBoard.general, 1)

        # Draw the buttons
        for button in buttons:
            pygame.draw.rect(screen, button.color, button.general, 0)
            
        # Draw the slider
        pygame.draw.rect(screen, (150, 150, 150), [charge_slider.slider_dim[0], charge_slider.slider_dim[1] , 250, 5], 0)
        pygame.draw.circle(screen, RED, charge_slider.center_coords, charge_slider.radius, 0)
        
        # Draw the positive
        pygame.draw.rect(screen, WHITE, [pos_neg_buttons[0] + 10, pos_neg_buttons[1] + 18, 20, 5], 0)
        pygame.draw.rect(screen, WHITE, [pos_neg_buttons[0] + 18, pos_neg_buttons[1] + 10, 5, 20], 0)
        
        # Draw the negative sign
        pygame.draw.rect(screen, WHITE, [pos_neg_buttons[0] + 10, pos_neg_buttons[1] + 118, 20, 5], 0)




        font = pygame.font.SysFont('Calibri', 25, True, False)

        value = font.render(str(charge_slider.value) + "x10^" + str(charge_slider.exponent), True, BLACK)

        text_print_pygame(texts, coords_text)





        screen.blit(value, [10, 450])


        pygame.display.flip()
        
        
        
        clock.tick(60)
        
    
    pygame.quit()
    return myBoard.all


# charges_info = input()
# print(charges_info)


# input()