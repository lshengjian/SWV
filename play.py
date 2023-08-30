from random import randint
from math import cos,sin,sqrt,pi
from pyglet.window import Window,key
from pyglet import shapes,graphics
from pyglet.text import Label
from pyglet import clock
from config import CFG
from transform import Transform
from imgui.integrations.pyglet import create_renderer

import pyglet
import imgui
#pipreqs --encoding utf-8
class App(Window):
    POINTS:int=CFG['POINTS']
    RANGE:int=CFG['RANGE']
    W,H=CFG['WIDTH'],CFG['HEIGHT']  
    FPS:int=60 
    K=0.1
    N:int=3 
    def __init__(self):
        super().__init__(App.W,App.H , 'Square Wave Viewer', resizable=False)

        self.set_vsync(False)
        self._points=[]
        clock.schedule_interval(self.update, 1/App.FPS)

        self._batch=graphics.Batch()
        imgui.create_context()
        self._impl = create_renderer(self)
        App.K=1
        self.trans=Transform((App.W,App.H), \
                             (App.W//2,App.H//2) , \
                             (-App.RANGE/2,App.RANGE/2) ,
                             (-4,4)
                        )
        self.dx=(self.trans.sx[1]-self.trans.sx[0])/App.POINTS
        self.make_points()

    def on_mouse_scroll(self,x, y, scroll_x, scroll_y):
        App.K*=1.2 if scroll_y>0.5 else 0.8
        self.trans.scale(App.K)
        self.dx=(self.trans.sx[1]-self.trans.sx[0])/App.POINTS
        self.make_points()

    def make_points(self):
        self._points.clear()
        ys=[0]*App.POINTS
        for i in range(1,1+App.N):
            c=(randint(5,245),randint(5,245),randint(5,245))
            for j in range(App.POINTS):
                k=2*i-1
                x=self.trans.sx[0]+j*self.dx  
                sx,sy=self.trans.toScreen((x,4/pi*sin(k*x)/k))
                circle = shapes.Circle(x=sx,y=sy,radius=1,color=c,batch=self._batch)
                self._points.append(circle)
                ys[j]+=4/pi*sin(k*x)/k
        for j in range(App.POINTS):
            x=self.trans.sx[0]+j*self.dx  
            sx,sy=self.trans.toScreen((x,ys[j]))
            circle = shapes.Circle(x=sx,y=sy,radius=2,color=(255,0,0),batch=self._batch)
            self._points.append(circle)    
        
    def draw(self):
        self.clear()
        self._batch.draw()
        imgui.render()
        self._impl.render(imgui.get_draw_data())


    def update(self, dt):
        imgui.new_frame()
        imgui.begin("Config")
        changed, App.N = imgui.slider_int("N", App.N, \
            min_value = 1, max_value = 10)

        if changed :
            self.make_points()
        imgui.end()
        self.draw()

if __name__ == "__main__":
    App()
    pyglet.app.run()
