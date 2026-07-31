from box import *

class Button(Box):
    
    def __init__(self, coords, color, number, text):
        """
        Constructor function
        bright_color: list, while the mouse is hovering over the button, display this color
        dark_color: list, while the button is pressed, display this color
        color: list, current color of the button
        hi: bool, condition that will be used later in other functs
        left_clicked: bool, shows whether the button is clicked or not
        value_correspondence: int, communicates to the main file the type of action of the button (e.g. the type of charge (pt. cha. or cylinder or sphere) the user wants to currently choose / increase or decrease the charge value / go back)
        pressed_text: str, Displays the given text in the terminal when the button is pressed
        """
        
        super().__init__(coords, color) # Import all properties from the Box class
        self.bright_color = [value + 30 for value in self.init_color]
        self.dark_color = [value - 30 for value in self.init_color]
        self.color = color.copy() # We copy so that the variable doesn't point to the same memory address
        self.hi = False
        self.left_clicked = False
        self.value_correspondence = number    
            
        # Optional 
        self.pressed_text = text    
    
    
    def mouse_in_button(self, mouse_pos):
        """
        Returns a bool whether the mouse is in the button (True) or not (False)     
        """
        return super().mouse_in_box(mouse_pos) # import the method mouse_in_box from the Box class
    
    
    def mouse_action_in_button(self, mouse_pos, left_click, time):
        
        """
        Gives the overall descr. of the mouse in the button, taking account the color modifications and whether the button is pressed
       
        Args:
            left_click: bool, whether the left button of the mouse has been clicked
            time: list, will be useful for time constraint in pygame
        """
        
        if self.mouse_in_button(mouse_pos): # Is the mouse hovering the button
            if left_click and time[0] <= 1: # Has the user pressed the left button of their mouse
                self.color = self.dark_color 
                self.hi = True 
                
            # This logic is necessary for the button's color 
            if not self.hi: 
                self.color = self.bright_color
            else:
                self.color = self.dark_color
                
            
            if self.left_clicked and self.hi and time[1] <= 1: # Has the user clicked (pressed + unpress) the button
                self.left_clicked = False 
                self.hi = False 
                return True 
            
        else: # If the mouse isn't in the button
            self.color = self.init_color # Return to it's original color
            
            if self.left_clicked:
                self.hi = False
                self.left_clicked = False
                
        return False
        

# Vars to organize the buttons     
col_buttons_coords = [580, 100]
power_buttons = [150, 470]
pos_neg_buttons = [60, 200]
button_size = 40    

# Call the class and assign it to each instance
blue_button = Button([col_buttons_coords[0], col_buttons_coords[1], button_size, button_size], [30, 30, 200], 101, "Point Charge")
yellow_button = Button([col_buttons_coords[0], col_buttons_coords[1] + 80, button_size, button_size], [200, 200, 30], 102, "Plane")
green_button = Button([col_buttons_coords[0], col_buttons_coords[1] + 160, button_size, button_size], [30, 200, 30], 103, "Rod")
orange_button = Button([col_buttons_coords[0], col_buttons_coords[1] + 240, button_size, button_size], [220, 88, 34], 104, "Disk")


negative_button = Button([pos_neg_buttons[0], pos_neg_buttons[1], 40, 40], [220, 30, 30], 201, "Positive Charge")
positive_button = Button([pos_neg_buttons[0], pos_neg_buttons[1] + 100, 40, 40], [30, 30, 220], 202, "Negative Charge")


power_up = Button([power_buttons[0], power_buttons[1], button_size + 20, button_size + 20], [206, 32, 41], 301, "Power Down")
power_down = Button([power_buttons[0] + 340, power_buttons[1], button_size + 20, button_size + 20], [60, 179, 113], 302, "Power Up")



done_button = Button([580, 490, 120, 60], [50, 200, 50], 1, "Done")




# Will be important in pygame
buttons = [blue_button, yellow_button, green_button, orange_button, power_up, power_down, done_button, positive_button, negative_button]
