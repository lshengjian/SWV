import  sys
from os import path
dir=path.abspath(path.dirname(__file__) + './..')
sys.path.append(dir)

from transform import Transform

def test_default():
    t=Transform()
    p=t.toCoordinate((400,300))
    assert p[0]==0 and p[1]==0
    p=t.toScreen((0,0))
    assert p[0]==400 and p[1]==300

    p=t.toCoordinate((800,600))
    assert p[0]==1 and p[1]==1
    p=t.toCoordinate((0,0))
    assert p[0]==-1 and p[1]==-1
    
def test_custom():
    t=Transform(size=(400,400),center=(0,0), \
                sx=(0.0,4.0),sy=(0.0,4.0)
        )
    p=t.toCoordinate((200,200))
    assert p[0]==2.0 and p[1]==2.0
    p=t.toCoordinate((0,0))
    assert p[0]==0.0 and p[1]==0.0
    
    p=t.toScreen((0,0))
    assert p[0]==0 and p[1]==0

    p=t.toScreen((4.0,4.0))
    assert p[0]==400 and p[1]==400

