from typing import Tuple
class Transform:
    def __init__(self,
                 size:Tuple=(800,600),
                 center:Tuple=(400,300),
                 sx:Tuple=(-1,1),
                 sy:Tuple=(-1,1)):
        self.width,self.height=size
        self.ox,self.oy=center
        self.sx=sx
        self.sy=sy
        self.step_x=self.width/(sx[1]-sx[0])
        self.step_y=self.height/(sy[1]-sy[0])

    
    def scale(self,val):
        x1,x2=self.sx
        self.sx=x1*val,x2*val
        y1,y2=self.sy
        self.sy=y1*val,y2*val
        self.step_x=self.width/(self.sx[1]-self.sx[0])
        self.step_y=self.height/(self.sy[1]-self.sy[0])

    def toScreen(self,p:Tuple)->Tuple:
        x=self.ox+self.step_x*p[0]
        y=self.oy+self.step_y*p[1]
        return x,y
        
    def toCoordinate(self,sp:Tuple)->Tuple:
        x=round((sp[0]-self.ox)/self.step_x)
        y=round((sp[1]-self.oy)/self.step_y)
        return int(x),int(y)
