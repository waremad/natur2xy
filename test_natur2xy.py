from natur2xy import *

def test_natur2xy():
    assert natur2xy(1) == (1,1)
    assert natur2xy(2) == (2,1)
    assert natur2xy(3) == (1,2)
    assert natur2xy(4) == (3,1)
    assert natur2xy(5) == (2,2)
    assert natur2xy(6) == (1,3)