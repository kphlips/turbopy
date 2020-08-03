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
    input_data = {"Clock": {"start_time": 0, "end_time": 1, "dt": 0.1},
                  "type": "BorisPush",
                  "Grid": {"N": 10, "min": 20, "max": 30},
                  "PhysicsModules": {}}
    owner = Simulation(input_data)
    owner.prepare_simulation()
    push_example = BorisPush(owner, input_data)
    arr = np.ndarray(shape=(2, 2), dtype=float)
    arr.fill(1)
    push_example.push(arr, arr, 1, 1, arr, arr)
    assert True
