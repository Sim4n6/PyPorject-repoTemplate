import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from product1.product import inc


def test_answer():
    assert inc(3) == 4
