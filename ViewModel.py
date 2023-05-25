import pygame

class ViewModel:

    def __init__(self):
        #estat del joc
        self.estat="init"

        #puntuació del joc (nombre de pomes recollides)
        self.punts=0

        #velocitat del joc
        self.FPS = 4
        self.incrFPS = 0.5

        #dimensions de la finestra
        self.screen_width=800
        self.screen_height=600

        #nombre de files i de columnes
        self.grid_rows=40
        self.grid_columns=30

        #dimensions de cada tile (cuadrat)
        self.tile_width = self.screen_width/self.grid_rows
        self.tile_height = self.screen_height/self.grid_columns

        #imatges
        self._tiles = {}
        self._loadTile('serp',"./imatges/cap.png")
        self._loadTile('cua',"./imatges/cua.png")
        self._loadTile('poma',"./imatges/poma.png")

    def _loadTile(self,key,url):
        img = pygame.image.load(url) 
        img=pygame.transform.scale(img, (self.tile_width, self.tile_height))
        self._tiles[key]=img

    def getTile(self,key):
        return self._tiles[key];

