from abc import ABC, abstractmethod

class Avatar(ABC):
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y        
        self.w=w
        self.h=h
    
    def colissio(self,a):
        return self.x==a.x+self.y==a.y

    def moure(self,x,y):
        self.x=x
        self.y=y

    @abstractmethod
    def pintar(self,tauler):
        pass

    def __str__(self):
        return f"Avatar {self.w}x{self.h} [{self.x},{self.h}]"
