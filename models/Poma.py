import random
from models.Avatar import Avatar

class Poma(Avatar):
    def __init__(self,x,y,w,h,tile):
        super().__init__(x,y,w,h)
        self.tile=tile   

    def pintar(self,tauler):
        print("pintar poma")     

    def __str__(self):
        return f"Poma x:{self.x} y:{self.y} w:{self.w} h:{self.h}"
