import numpy as np

def energy(density, coeff=1.0):
    """ 
    Energy associated with the diffusion model

    Parameters
    ----------

    density: array of positive integers
        Number of particles at each position i in the array
    coeff: float
        Diffusion coefficient.
    """
    # making sure the type and length of the input array are correct
    if density.dtype.kind != 'i' and len(density) >0:
        raise TypeError("Density should be an array of integers")
    # making sure the values within the array are positive
    if any(density <0):
        raise ValueError("Density should be an array of *positive* integers.")
  # implementation goes here
    Energy = np.sum(density * (density -1))

    return int(Energy)

def random_move(density):
    # move
    location = np.random.randint(low = 0, high = (len(density)))
    move = np.random.randint(low = -1, high = +2)
    if density[location] -1 >= 0:
        if move == 1 and location != len(density)-1:
            density[location] = density[location] - 1
            density[location+1] = density[location+1] + 1
        elif  move == 1 and location == len(density)-1:
            density[location-1] = density[location-1] - 1
            density[0]= density[0] +1
        elif move == -1 and location != len(density)-1:
            density[location] = density[location] - 1
            density[location-1] = density[location-1] + 1
        elif move == -1 and location == len(density)-1:
            density[location-1] = density[location-1] - 1
            density[location] = density[location] + 1
        else: 
            pass 
    else:
        print("This would result in negative density")
        # somehow think of a way to loop this round

    return density


def probability(E1,E2,beta):
          
    return np.exp(-beta*(E2-E1)) 


density = np.array([0,0,3,5,8,4,2,1])
E1 = energy(density)
E2 = energy(random_move(density))
Energy = np.maximum(E1,E2)

