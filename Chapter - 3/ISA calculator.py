import math

#Utility functions
def get_layer(altitude, data):
    if altitude == 0:               
        return data[0]
    
    for i in range(len(data)):      
        if altitude < data[i][0]:
            return data[i-1]
        
    return data[-1] #Returns last layer if above all layers

#Calculation functions       
def calc_temp(altitude, h_base, t_base, grad):
    if grad != 0:
        return t_base + grad * (altitude - h_base)
    
    else:
        return t_base


#base_altitude, base_temp, gradient in the following order
layers = [
    [0,      288.16, -6.5*10**-3],      
    [11000,  216.66,  0],
    [25000,  216.66,  3*10**-3],
    [47000,  283.66,  0],
    [53000,  283.66, -4.5*10**-3],
    [79000,  165.66,  0],
    [90000,  165.66,  4*10**-3],
    [106000, 225.66,  0]
]

altitude = 12000                                         #Must be < 105000 and > 0 in meters

def main(altitude, data):
    base_layer = get_layer(altitude, data)
    return base_layer

print(main(altitude, layers))