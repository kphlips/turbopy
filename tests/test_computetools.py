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
    input_data = {"Clock": {"start_time": 0, "end_time": 100, "dt": 1e-9},
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
    x_i = np.array([[0, 0, 0.0]], dtype=np.float)
    v_i = np.array([[0, 0, 3.0e6]], dtype=np.float)
    p_i = mass * v_i
    clock = input_data["Clock"]
    N = 10
    xfinal = v_i * N * clock["dt"]
    for i in range(N):
        push_example.push(x_i, p_i, charge, mass, E, B)
    assert np.allclose(x_i, xfinal, rtol=1e-4)
    x_i = np.array([[0, 0, 0.0]], dtype=np.float)
    p_i = 0 * v_i
    E = np.array([[0, 0, 1e100]], dtype=np.float)
    B = np.array([[0, 0, 1e100]], dtype=np.float)
    for i in range(N):
        push_example.push(x_i, p_i, charge, mass, E, B)
    check = np.array([[0, 0, 3.0]], dtype=np.float)
    assert np.allclose(x_i, check, rtol=1e-3)
