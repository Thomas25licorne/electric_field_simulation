import agregg as Vz
import field_graph as mn
import numpy as np


dimensions = 30

def pointconv_x(point):
    #print('pointconv_x', point)
    centerd_point = (point-150)-200 # first y at 150, and y range from 150 to 550, so 0 at y = 350
    #print(centerd_point)
    return centerd_point * dimensions/200 # bring point to scale

def pointconv_y(point):
    #print ('pointconv_y',point)
    centerd_point = 200-(point-50) # first x at 50 and x range from 50 to 450 so 0 at  x =250
    #print(centerd_point)
    return centerd_point * dimensions/200 # bring point to scale

def rod_orientation(ak_input):

    # print(ak_input[0][0],ak_input[0][1],ak_input[0][2],ak_input[0][3])
    lenght_X = abs(ak_input[0][2])
    lenght_y = abs(ak_input[0][3])
    # print(lenght_X,lenght_y)

    type = 'horizontal rod' if lenght_X > lenght_y else 'vertical rod'
    
    start_X = ak_input[0][0]
    start_Y = ak_input[0][1] - lenght_y# there is a move on the y axis but not the X as the Y is revesed between the 2 grid
    lenght_rod = max(lenght_X,lenght_y)
    
    return type,start_X,start_Y,lenght_rod
    
#will take akiras output and transform it into thoams input
def input_changes( ak_input):
    Th_input=[]
    #run a loop unnthe main liste to select the sub liste
    for i in range(len(ak_input)):
        
        type = ak_input[i][1]

        #select the sub liste type
        if type == 'point' : 

            #[type, None, charge ,X_position,Y_position, None, None, None]    
            th_input_ith = mn.shapes(type , None , ak_input[i][2], pointconv_x(ak_input[i][0][0]) , pointconv_y( ak_input[i][0][1]), None, None, None)
            
        elif type == 'disk':
            
            #[type, None, charge ,X_center,Y_center,radius,None,None]
            th_input_ith = mn.shapes(type , None , ak_input[i][2],pointconv_x(ak_input[i][0][0][0]),pointconv_y(ak_input[i][0][0][1]),ak_input[i][0][1]*dimensions/200,None,None )

        elif type == 'plane' :

            lenght_X = ak_input[i][0][2]
            lenght_y = ak_input[i][0][3]

            #[type , 5 , charge, X_start,Y_start+lenght_Y,None, lenght_X, lenght_Y] the + lenght_y as the y axis is reversed
            th_input_ith = mn.shapes(type, 5, ak_input[i][2], pointconv_x(ak_input[i][0][0]), pointconv_y(ak_input[i][0][1] + lenght_y), None, int(np.floor(lenght_X*dimensions/200)),int(np.floor(lenght_y*dimensions/200)))
        
        elif type == 'rod':

            ak_input[i][0][0],ak_input[i][0][1],ak_input[i][0][2],ak_input[i][0][3] = pointconv_x(ak_input[i][0][0]),pointconv_y(ak_input[i][0][1]),ak_input[i][0][2]*dimensions/200,ak_input[i][0][3]*dimensions/200
            
            type,start_X,start_Y,lenght_rod = rod_orientation(ak_input[i])            
            
            #[type,None, charge, start_X,start_Y,lneght_rod,None,None ]
            th_input_ith = mn.shapes(type , None , ak_input[i][2],start_X,start_Y,int(lenght_rod),None,None)

        Th_input.append(th_input_ith)
    
    return Th_input

def run ():
    
    ak_input = Vz.input()
    #print(ak_input)
    liste = input_changes(ak_input)    
    mn.main(dimensions,mn.points(liste))



run()

