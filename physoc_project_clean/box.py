class Box():
    
    def __init__(self, coords, color):
        """
        Constructor function
        general: list, general descr. of the box, will be used in pygame
        placement: list, the x and y coords of the top left corner of the box
        dim: list, the x and y length of the box resp.
        """
        
        self.general = coords
        self.placement = coords[0:2]
        self.dim = coords[2:]
        self.init_color = color
    
    def mouse_in_box(self, mouse_pos):
        """
        Returns a bool whether the mouse is in the box (True) or not (False)     
        """
        
        x_mouse = mouse_pos[0]
        y_mouse = mouse_pos[1]
        
        return (x_mouse > self.placement[0]) and (x_mouse < self.placement[0] + self.dim[0]) and (y_mouse > self.placement[1]) and (y_mouse < self.placement[1] + self.dim[1])