from natur2xy import *

def test_xy2natur():
    assert xy2natur(0,0) == 0
    assert xy2natur(1,0) == 1
    assert xy2natur(0,1) == 2
    assert xy2natur(2,0) == 3
    assert xy2natur(1,1) == 4
    assert xy2natur(0,2) == 5
    assert xy2natur(3,0) == 6  
    assert xy2natur(2,1) == 7
    assert xy2natur(1,2) == 8
    assert xy2natur(0,3) == 9
    assert xy2natur(4,0) == 10
    assert xy2natur(3,1) == 11  

def test_natur2xy():
    assert natur2xy(0) == (0,0)
    assert natur2xy(1) == (1,0)
    assert natur2xy(2) == (0,1)
    assert natur2xy(3) == (2,0)
    assert natur2xy(4) == (1,1)
    assert natur2xy(5) == (0,2)
    assert natur2xy(6) == (3,0)

def test_natur2xy2natur():
    for i in range(1000):
        assert i == xy2natur(natur2xy(i)[0],natur2xy(i)[1])