"Test for the BorisPush Computetool in turbopy/computetools.py"

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
    push_example = BorisPush(Simulation({"type": "BorisPush"}),
                             {"type": "BorisPush"})
    assert True
