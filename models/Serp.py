from models.Avatar import Avatar

class Serp(Avatar):
    def __init__(self,x,y,w,h,direccio,tile):
        super().__init__(x,y,w,h)
        self.direccio=direccio
        self.tile=tile
        self.cua=[]
    
    def translate(self,x,y):
        self.x=self.x+x;
        self.y=self.y+y;

    def pintar(self,tauler):
        print("pinta")     

    def __str__(self):
        return f"Serp x:{self.x} y:{self.y} w:{self.w} h:{self.h}"
