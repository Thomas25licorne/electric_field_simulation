from box import *
import math
from slider import *

class DrawBoard(Box):
    
    def __init__(self, coords, color):
        """
        Constructor Funct.
        
        charges: list: stores all data concerning charges (coords, type, amount, etc...)
        memory: list: stores the current type of the charge as well as its sign. It is set as a positive point charge by default
        """
        super().__init__(coords, color) # Import all properties from the Box class
        
        self.all = []
        self.point_charges = []
        self.planes = []
        self.disks = []

        self.plane = []
        self.plane_step = 1
        
        self.rod = []
        self.rod_step = 1    
        
        self.disk = []
        self.disk_step = 1
        
        
        self.memory = [101, 1]
                

    
    def mouse_in_board(self, mouse_pos):
        """
        Returns a bool whether the mouse is in the drawboard (True) or not (False)     
        """
        return super().mouse_in_box(mouse_pos) # Import the method mouse_in_box from the Box class
    
    
    def filter_type(self, type):
        
        if type == 101:
            self.color = [0, 0, 200]
            self.memory[0] = 101
        elif type == 102:
            self.color = [200, 200, 0]
            self.memory[0] = 102
        elif type == 103:
            self.color = [0, 200, 0]
            self.memory[0] = 103
        elif type == 104:
            self.memory[0] = 104
        else:
            self.color = [0, 0, 0]

            
        if type == 201:
            self.memory[1] = 1
        elif type == 202:
            self.memory[1] = -1
            
    
    def mouse_action_in_board(self, mouse_pos, left_click, time, type):

        
        if type == 0 and len(self.point_charges) != 0 and time[0] < 1:
            self.point_charges.pop()
            type = 9999
            
        
        if self.mouse_in_board(mouse_pos):
            
            
            if left_click and time[0] < 1:
                if self.memory[0] == 101:
                    self.make_point_charge(mouse_pos)
                elif self.memory[0] == 102:
                    self.make_plane(mouse_pos)    
                elif self.memory[0] == 103:
                    self.make_rod(mouse_pos)
                elif self.memory[0] == 104:
                    self.make_disk(mouse_pos)               
                        
            
            
    def make_point_charge(self, mouse_pos):
        
        pt_charge_coords = mouse_pos
        pt_charge_sign = self.memory[1]
        point_charge = [pt_charge_coords, pt_charge_sign]
        self.point_charges.append(point_charge)
        
        
        info_all = [pt_charge_coords, "point", self.memory[1] * charge_slider.value * 10 ** charge_slider.exponent]
        self.all.append(info_all)
        

    def make_plane(self, mouse_pos):
        
        if self.plane_step == 1:
            init_coords = mouse_pos
            self.plane.append(init_coords)
            self.plane_step += 1
        else:
            final_plane = []

            end_coords = mouse_pos
            plane_sign = self.memory[1]
            self.plane.append(end_coords)            
        
            self.plane = self.sort_coords_rect()
                        
            final_plane.append(self.plane)
            final_plane.append(plane_sign)
            
            self.planes.append(final_plane)
            
            info_all = [self.plane, "plane", self.memory[1] * charge_slider.value * 10 ** charge_slider.exponent]
            self.all.append(info_all)
            
            
            
            self.plane = []
            self.plane_step = 1


    def make_rod(self, mouse_pos):       
        if self.rod_step == 1:
            init_coords = mouse_pos
            self.plane.append(init_coords)
            self.rod_step += 1
        else:
            final_rod = []

            end_coords = mouse_pos
            rod_sign = self.memory[1]
            self.plane.append(end_coords)            
        
            self.rod = self.sort_coords_rect()
            self.correct_coords_rod()
            
            final_rod.append(self.rod)
            final_rod.append(rod_sign)
            
            self.planes.append(final_rod)
            
            info_all = [self.rod, "rod", self.memory[1] * charge_slider.value * 10 ** charge_slider.exponent]
            self.all.append(info_all)
            
            
            self.plane = []
            self.rod = []
            self.rod_step = 1


        

    def sort_coords_rect(self):
        init_coords = self.plane[0]
        end_coords = self.plane[1]
        
        final_init_coords = [min(init_coords[0], end_coords[0]), min(init_coords[1], end_coords[1])]
        final_end_coords = [max(init_coords[0], end_coords[0]), max(init_coords[1], end_coords[1])]
        
        rect_coords = [final_init_coords[0], final_init_coords[1], final_end_coords[0] - final_init_coords[0], final_end_coords[1] - final_init_coords[1]]
        return rect_coords
    
    
    def correct_coords_rod(self):
        
        if self.rod[2] >= self.rod[3]:
            self.rod[3] = 12
        else:
            self.rod[2] = 12
         
         
    def make_disk(self, mouse_pos):
        
        if self.disk_step == 1:
            init_coords = mouse_pos
            self.disk.append(init_coords)
            self.disk_step += 1
        else:
            final_disk = []

            end_coords = mouse_pos
            disk_sign = self.memory[1]
            

            
            disk_radius = math.sqrt((self.disk[0][0] - end_coords[0]) ** 2 + (self.disk[0][1] - end_coords[1]) ** 2)
            
            disk_coords = [self.disk[0], disk_radius]
            final_disk.append(disk_coords)
            final_disk.append(disk_sign)
            
            self.disks.append(final_disk)
            
            info_all = [disk_coords, "disk", self.memory[1] * charge_slider.value * 10 ** charge_slider.exponent]
            self.all.append(info_all)
            
            
            
            
            self.disk = []
            self.disk_step = 1     
        
        
    
    
            
            
    
    
myBoard = DrawBoard([150, 50, 400, 400], [0, 0, 0])