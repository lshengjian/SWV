import pytest
import random
from math import atan2,pi

def test_base():
    assert 2==1+1
    
def test_complex():
    z1=1+1j
    z2=complex(1,1)

    #print(z1)
    assert z1.real==1 and z1.imag==1
    assert z1==z2

    z=complex(3,4)
    assert abs(z)==5
    
def test_math():
    a=atan2(0,0)
    assert 0==a
    a=atan2(0,1)
    assert 0==a
    a=atan2(1,1)
    assert pi/4==a
    a=atan2(1,0)
    assert pi/2==a
    a=atan2(1,-1)
    assert pi/2+pi/4==a
    a=atan2(0,-1)
    assert pi==a
    a=atan2(-1,-1)
    assert -pi/2-pi/4==a
    a=atan2(-1,0)
    assert -pi/2==a
    a=atan2(-1,1)
    assert -pi/4==a
    