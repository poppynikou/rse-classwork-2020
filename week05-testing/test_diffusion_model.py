from diffusion_model import energy
import numpy as np 


def test_energy():
    density = np.array([0,0,3,5,8,4,2,1])
    """ Optional description for reporting """
    # Test something
    assert energy(density) > 0

def test_density():
    density = np.array([0,0,3,5,8,4,2,1])
    for i in density:
            assert type(i) == np.int32
    assert density.any() > 0
    assert len(density) > 1 


test_energy()
test_density()