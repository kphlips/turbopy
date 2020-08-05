"Test for the BorisPush Computetool in turbopy/computetools.py"

import numpy as np
from turbopy.computetools import BorisPush
from turbopy.core import Simulation


def test_init_should_create_object():
    """Method that creates a BorisPush object to test __init__"""
    init_example = BorisPush(Simulation({"type": "BorisPush"}),
                             {"type": "BorisPush"})
    assert isinstance(init_example, BorisPush)
    assert init_example.c2 == 2.9979e8 ** 2


def test_push():
    """Tests the functionality of the push method"""
    input_data = {"Clock": {"start_time": 0, "end_time": 1, "dt": 1e-9},
                  "type": "BorisPush",
                  "Grid": {"N": 10, "min": 20, "max": 30},
                  "PhysicsModules": {}}
    owner = Simulation(input_data)
    owner.prepare_simulation()
    push_example = BorisPush(owner, input_data)
    charge = 1.6022e-19
    mass = 1.6726e-27
    E = np.zeros(3)
    B = np.zeros(3)
    x0 = np.array([[0, 0, 0.0]], dtype=np.float)
    v0 = np.array([[0, 0, 3.0e6]], dtype=np.float)
    p0 = mass * v0
    dt = 1e-9
    Nt = 10
    xfinal = v0 * Nt * dt
    for i in range(Nt):
        push_example.push(x0, p0, charge, mass, E, B)
    assert np.allclose(x0, xfinal, rtol=1.e-4)
