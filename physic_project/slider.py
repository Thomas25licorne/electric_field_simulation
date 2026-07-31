import math
from buttons import *

class Slider():
    
    def __init__(self, center_coords, radius, slider_dim):
        
        self.center_coords = center_coords
        self.radius = radius
        self.slider_dim = slider_dim
        self.exponent = -9
        self.value = 5.00
        self.action_on_button = False
        
    def mouse_in_slider(self, mouse_pos, left_click):
        
        if math.sqrt((self.center_coords[0] - mouse_pos[0])**2 + (self.center_coords[1] - mouse_pos[1])**2) < self.radius and left_click:
            self.action_on_button = True
            
        else:
            if not left_click:
                self.action_on_button = False
            
        
        if self.action_on_button and left_click:
            if self.center_coords[0] - self.radius < self.slider_dim[0]:
                self.center_coords[0] = self.slider_dim[0] + self.radius
                self.action_on_button = False
                self.value = 1.00

            elif self.center_coords[0] + self.radius > self.slider_dim[0] + 250:
                self.center_coords[0] = self.slider_dim[0] + 250 - self.radius
                self.action_on_button = False
                self.value = 9.99
            
            else:
                self.center_coords[0] = mouse_pos[0]
                self.value = round(10 * (self.center_coords[0]/(self.slider_dim[1] + self.slider_dim[0]/5)), 2)
      
        
charge_slider = Slider([power_buttons[0] + 200, power_buttons[1] + 30], 10, [power_buttons[0] + 75, power_buttons[1] + 27])
