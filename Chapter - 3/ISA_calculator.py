import math
from ISA_base_calculator import calc_base

#Constants
R = 287     #J/kg.K
g = 9.81    #m/s^2

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

def calc_pressure(alt, temp, gradient, alt_base, p_base, temp_base):
        #For Isothermic layers
        if gradient == 0:
            p = p_base*math.e**(-1*((g/(R*temp_base))*(alt - alt_base)))
        #For Gradient layers
        else:
            p = p_base*(temp/temp_base)**-(g/(gradient*R))

        return p

def calc_density(alt, temp, gradient, alt_base, temp_base, rho_base):
        #For Isothermic layers
        if gradient == 0:
            rho = rho_base*math.e**(-1*((g/(R*temp_base))*(alt - alt_base)))
        #For Gradient layers
        else:
            rho = rho_base*(temp/temp_base)**-((g/(gradient*R))+1)
        
        return rho


# ISA Layer data: [base_altitude (m), base_temp (K), gradient(K/m), pressure(N/m^2), density(kg/m^3)]
#Sea level data hardcoded from the book
layers = [
    [0,      288.15, -6.5*10**-3, 1.01325*10**5, 1.2250],     #Initial pressure and density from the book
    [11000,  216.66,  0],
    [25000,  216.66,  3*10**-3],
    [47000,  283.66,  0],
    [53000,  283.66, -4.5*10**-3],
    [79000,  165.66,  0],
    [90000,  165.66,  4*10**-3],
    [106000, 225.66,  0]
]

calc_base(layers) #Calculates missing base pressure and density for each layer

altitude = 14000                                         #Must be < 105000 and > 0 in meters

def main(altitude, data):
    layer_base = get_layer(altitude, data)
    alt_base = layer_base[0]
    temp_base = layer_base[1]
    gradient = layer_base[2]
    p_base = layer_base[3]
    rho_base = layer_base[4]

    temp = calc_temp(altitude, alt_base, temp_base, gradient)
    pressure = calc_pressure(altitude, temp, gradient, alt_base, p_base, temp_base)
    rho = calc_density(altitude, temp, gradient, alt_base, temp_base, rho_base)

    return {
        "altitude": altitude,
        "temp": temp,
        "pressure": pressure,
        "density": rho
    }

print(main(altitude, layers))