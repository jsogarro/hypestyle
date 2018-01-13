import pytest
from sample import add, mult, div

def test_add():
    assert add(1,2) == 3

def test_mult():
    assert mult(2, 3) == 6

def test_div():
    assert div(6, 2) == 3

@pytest.mark.skip(reason='Test not implemented')
def not_implemented():
    pass
