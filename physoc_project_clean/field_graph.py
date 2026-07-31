import matplotlib.pyplot as plt
import numpy as np
import math as math
from matplotlib.patches import Rectangle
#variables
Ke= 8.99*10*9


##### CLASS FOR EACH TYPE OF SHAPE

'''example = shape(type, precision, charge, x_coor, y_coor, length_rod, dim_x, dim_y)'''

class shapes:
    def __init__(self, type, precision, charge, x_coor, y_coor, length_rod, dim_x, dim_y):
        self.type = type
        self.precision = precision
        self.charge= charge
        self.x_coor= x_coor
        self.y_coor = y_coor
        self.length_rod  =length_rod
        self.dim_x  = dim_x
        self.dim_y= dim_y
    
    def point_charge(self):
        return [ self.charge]
    
    def point(self):
        return [self.type,  [(self.x_coor,self.y_coor)], self.point_charge() ]
    
    def disk_charge(self):
        coor_disk = []
        
        a = 0
        
        for i in range(math.floor(self.length_rod)):
            for _ in range(10):
                a+=1
        
        for i in range(math.floor(self.length_rod)):
            for _ in range(10):
                coor_disk.append(self.charge/(a))
        return coor_disk
    
    def disk(self):
        disk_coor = [(self.x_coor,self.y_coor)]
        
        floor_val = math.floor(self.length_rod)
        
        for _ in range(floor_val):
            for theta in np.linspace(0, 2 * np.pi, 10):  
                x = self.x_coor + self.length_rod * np.cos(theta)  
                y = self.y_coor + self.length_rod* np.sin(theta)  
                disk_coor.append((x,y))
            
        return [self.type,disk_coor, self.disk_charge(), self.length_rod]

    def charges_count_rod(self):           #just the count of charges for a plane
            charge = []
            for _ in range(self.length_rod*10):
                charge.append(self.charge)
            return charge

    def rod_y_fixed(self):           #generate a rod with keyword
        rod= [ ]
        for i in range(self.length_rod*10):
            rod.append((self.x_coor+(i/10), self.y_coor))
        return [self.type, rod, self.charges_count_rod(), self.length_rod+0.6, 1.4]

    def rod_x_fixed(self):     #generate coordinate and key word for a rod
        rod= [ ]
        for i in range(self.length_rod*10):
            rod.append((self.x_coor, self.y_coor+(i/10)))
        return [self.type, rod, self.charges_count_rod(), 0.9, self.length_rod+1.1 ]   

    def charges_count_plane(self):
        charge = []
        for _ in range(self.dim_x):
            for _ in range(self.dim_y):
                charge.append((self.charge)/(self.dim_x * self.dim_y))
        #print(f'length of charges:{len(charge)}' )
        return charge
            

    def plane(self):         #generate all the coordinates, keyword, and bottom left corner
        coor = []
        for i in range(self.dim_x):
            for j in range(self.dim_y):
                coor.append((self.x_coor+i, self.y_coor+j))
        #print(f'length of coor: {len(coor)}')
        return [self.type,coor, self.charges_count_plane(),self.dim_x, self.dim_y]

    def planeV2(self):         #generate all the coordinates, keyword, and bottom left corner
        coor = []
        for i in range(self.dim_x):
            for j in range(self.dim_y):
                coor.append((self.x_coor+i/5, self.y_coor+j/5))
        return [self.type,coor,self.charges_count_plane(), self.dim_x, self.dim_y]

    
    
    def generate(self):
        if self.type == 'point':
            return self.point()
        elif self.type == 'vertical rod':
            return self.rod_x_fixed()
        elif self.type == 'horizontal rod':
            return self.rod_y_fixed()
        elif self.type == 'plane':
            return self.plane()
        elif self.type == 'planeV2':
            return self.planeV2()
        elif self.type == 'disk':
            return self.disk()
        else:
            raise ValueError(f"Unknown shape type: {self.type}")
        
#creation of the coordinates grid

def grid_creation(dim):
    x = np.linspace(-dim, dim, 50)
    y = np.linspace(-dim, dim, 50)
    #creat a matrix representation of the X's and the Y's
    X, Y = np.meshgrid(x, y)
    return X,Y

# a function calculating the electrical field form a point at each coordinate 
# in the grid X and Y,  given the charge q and the distance r between the point
# x and y are like matrixes of each coordiantes

def point_electrical_field(q,position_charge,X,Y):

    X_adjusted = X - position_charge[0]  # a matrix - a constant
    Y_adjusted = Y - position_charge[1]  # a matrix - a constant
    
    R_adjusted = np.sqrt(X_adjusted**2 + Y_adjusted**2)  # sqrt for each index of the matrices
    
    
    
    
    # electrical field
    Ex = Ke * q * X_adjusted / R_adjusted ** 3  # electrical field along x-axis
    Ey = Ke * q * Y_adjusted / R_adjusted ** 3  # electrical field along y-axis
    
    
    
    
    
    return Ex, Ey, R_adjusted

#visuals aspects
def sphere_charge (position,color, radius,ax):     #Generates a symbolic sphere where the reference point is
    ax.add_patch(plt.Circle((position),radius=radius, color= color, fill = True))

def rectangle_charge(position, color, width, height, ax):
    
    # Create a rectangle patch
    rect = Rectangle(position, width, height, color=color)
    
    # Add the rectangle to the plot
    ax.add_patch(rect)

def color_point(q):
    color = 'red'if q>=0 else 'blue'
    return color

#main function, will generate the vectors and compute the whole electrical field

def main(dimensions, positions):
    #creation of the canvas for the visuals
    fig, ax = plt.subplots()

    ax.set_xlim(-dimensions, dimensions)
    ax.set_ylim(-dimensions, dimensions)

    ax.set_aspect('equal')
    

    X,Y = grid_creation(dimensions)
    
    Ex_tot = np.zeros_like(X)
    Ey_tot = np.zeros_like(Y)
    Ex_tot_0 = np.zeros_like(X)
    Ey_tot_0 = np.zeros_like(Y)
    
    
    '''example = shape(type, precision, charge, x_coor, y_coor, length_rod, dim_x, dim_y)'''
    for j in range(len(positions)):
        if positions[j][0] in ('horizontal rod', 'plane', 'vertical rod'):
            #print('positions[j]',positions[j])
            if positions[j][1][0][0]<0:
                if positions[j][1][0][1]<0:
                    rectangle_charge((positions[j][1][0][0]-0.5, positions[j][1][0][1]-(0.7-1/(positions[j][1][0][1]*0.95))), color_point(positions[j][2][0]),positions[j][3] , positions[j][4], ax)
                elif positions[j][1][0][1]>0:
                    rectangle_charge((positions[j][1][0][0]-0.5, positions[j][1][0][1]-(0.07*positions[j][1][0][1])+0.07), color_point(positions[j][2][0]),positions[j][3] , positions[j][4], ax)
            elif positions[j][1][0][0]>0:
                if positions[j][1][0][1]>0:
                    rectangle_charge((positions[j][1][0][0]-0.3, positions[j][1][0][1]-(0.07*positions[j][1][0][1])+0.07), color_point(positions[j][2][0]),positions[j][3] , positions[j][4], ax)
                elif positions[j][1][0][1]<0:
                    rectangle_charge((positions[j][1][0][0]-0.3, positions[j][1][0][1]-(0.7-1/(positions[j][1][0][1]*0.95))), color_point(positions[j][2][0]),positions[j][3] , positions[j][4], ax)  
                    
        if positions[j][0] == 'disk':
                sphere_charge(positions[j][1][0], color_point(positions[j][2][0]), positions[j][3],ax )
        if positions[j][0] == 'point':
                sphere_charge(positions[j][1][0], color_point(positions[j][2][0]), 0.3,ax )
        for i in range(len(positions[j][2])):# uses the lsite to be abble to add as many sources as we want( merci thomas pour l'idee des listes)

            Ex ,Ey, R= point_electrical_field(positions[j][2][i], positions[j][1][i], X, Y)
            
            Ex_tot_0 += np.copy(Ex)
            Ey_tot_0 += np.copy(Ey)

            #add the suppresion of the center points here, with something of the likes:
            radius_min = 0.6
            
            if positions[j][0] == 'disk':
                radius_min2 = positions[j][3] + radius_min
                
                X_center = positions[j][1][0][0]                
                Y_center = positions[j][1][0][1]

                X_adj_center = X - X_center
                Y_adj_center = Y - Y_center

                distance_to_center_disk = np.sqrt(X_adj_center**2+Y_adj_center**2)
                radius = positions[j][3]

                Ex[  distance_to_center_disk < radius ] = np.nan   #+ positions[j][3]
            
                Ey[  distance_to_center_disk < radius ] = np.nan      #+ positions[j][3]

            
            else:  
                Ex[ R < radius_min ] = np.nan
                
                Ey[ R < radius_min ] = np.nan
        

            


            Ex_tot += Ex
            Ey_tot += Ey


    E_mag = np.sqrt(Ex_tot_0**2 + Ey_tot_0**2) 
    
    ax.streamplot( X, Y, Ex_tot, Ey_tot, color=E_mag, cmap='plasma', density=3, linewidth=1)
    # ax.contourf( X, Y, E_mag, cmap='plasma',alpha = 0.4)
    
    plt.show()
    


# def of system

dimensions = 30
# charges = [ 1*10**-9 , -1*10**-9 , 2*10**-9 , -3*10**-9]
# points =[ (-3,-4) , (2,4) , (-2,4) , (0,0)]
a, b =[ 1*10**-9 , -1*10**-9,  ]


def points(list_element):
    points = []
    for i in range(len(list_element)):
        points.append(shapes.generate(list_element[i]))
    return(points)
        
#test charges
# plane_test = shapes('plane', 5, 1*10**-9, -4,-4, None, 15, 15)
# rod_test  =shapes('vertical rod', 10, b, 10, 10, 7, 1, 7)
# rod_opp_test = shapes( 'vertical rod', None, b, -12,12, 7, None,None)

# rod_test2 =shapes('vertical rod', 10, b, 10,-10, 7, 1, 7)
# rod_opp_test2 = shapes( 'vertical rod', 10, b, -12,1, 7, None,None)

# rod_opp_test3 = shapes( 'horizontal rod', None, b, 1,10, 7, None,None)
# rod_opp_test4 = shapes( 'horizontal rod', None, a, 1,1, 7, None,None)

# point_test = shapes('point', None, a, 10,10,None, None, None)

# point_test2 = shapes('point', None, b, -10,-10,None, None, None)

# disk_test = shapes('disk', None, a, 1,1, 5, None, None)


'''test = shapes('type', 'precision', 'charge', 'x_0','y_0', 'rod length', 'dim_x', 'dim_y')'''




#main(dimensions, points([rod_opp_test2 ]))


