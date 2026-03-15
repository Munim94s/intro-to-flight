import math

# ISA Layer data: [base_altitude (m), base_temp (K), lapse_rate (K/m)]
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

#Constants
R = 287     #J/kg.K
g = 9.81    #m/s^2


def calc_base(layers):   
    layer_data = [row[:] for row in layers]  # Avoids changing the original and keeping a copy

    for i in range(len(layer_data)):
        if len(layer_data[i]) <= 3:
            alt_base = layer_data[i-1][0]
            temp_base = layer_data[i-1][1]
            gradient = layer_data[i-1][2]
            p_base = layer_data[i-1][3]
            rho_base = layer_data[i-1][4]

            alt = layer_data[i][0]
            temp = layer_data[i][1]
            p = None
            rho = None

            #For Isothermic layers
            if gradient == 0:
                p = p_base*math.e**(-1*((g/(R*temp_base))*(alt - alt_base)))
                rho = rho_base*math.e**(-1*((g/(R*temp_base))*(alt - alt_base)))
            #For Gradient layers
            else:
                p = p_base*(temp/temp_base)**-(g/(gradient*R))
                rho = rho_base*(temp/temp_base)**-((g/(gradient*R))+1)
            layer_data[i].append(p)
            layer_data[i].append(rho)
    return layer_data

            
print(calc_base(layers))