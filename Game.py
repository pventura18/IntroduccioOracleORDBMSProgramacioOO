import pygame
import time
from random import randrange
from ViewModel import ViewModel
from models.Poma import Poma
from models.Serp import Serp

# Crer el ViewModel del joc
vm = ViewModel()

# Inicialitzar Pygame
pygame.init()
fpsClock = pygame.time.Clock()

# Crear la finestra (screen) i la zona per a pintar (tauler)
screen = pygame.display.set_mode((vm.screen_width, vm.screen_height))
tauler = pygame.Surface((vm.screen_width, vm.screen_height))

# Text de la finestra
pygame.display.set_caption("El joc de la serp")

# Configurar la lectura del teclat
pygame.key.set_repeat(1, 50)


# Propietats de la poma
poma_x=randrange(vm.grid_rows)
poma_y=randrange(vm.grid_columns)
poma_width=vm.tile_width
poma_height=vm.tile_height
imatge_poma = vm.getTile('poma');

poma = Poma(poma_x,
            poma_y,
            poma_width,
            poma_height,
            imatge_poma)

# Propietats de la sep
serp_x = vm.grid_rows//3
serp_y = vm.grid_columns//2
serp_width=vm.tile_width
serp_height=vm.tile_height
serp_direccio = [1,0]
imatge_serp = vm.getTile('serp');
serp_cua = [] 

serp = Serp(serp_x,
            serp_y,
            serp_width,
            serp_height,
            serp_direccio,
            imatge_serp)

# Pantalla inicial del joc
font = pygame.font.SysFont(None, 36)
txtTitol = font.render('Press key to starting', True, (255, 255, 255))
rect = txtTitol.get_rect(center=screen.get_rect().center)
screen.fill((0, 0, 0)) 
screen.blit(txtTitol, rect)
while vm.estat=="init":
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()        
        elif evento.type == pygame.KEYDOWN:
            vm.estat="playing"
    pygame.display.flip()

            
# Bucle principal del joc
while vm.estat=="playing":

    ###################
    # Event de teclat #
    ###################
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                serp.direccio=[-1,0]
            elif evento.key == pygame.K_RIGHT:
                serp.direccio=[1,0]
            elif evento.key == pygame.K_UP:
                serp.direccio=[0,-1]
            elif evento.key == pygame.K_DOWN:
                serp.direccio=[0,1]

    ##########
    # logica #
    ##########

    # colissió amb la poma
    if poma.x==serp.x and poma.y==serp.y:
        #modificar la posció de la poma
        poma.x=randrange(vm.grid_rows)
        poma.y=randrange(vm.grid_columns)
        #afegir un tros de cua a la serp
        serp.cua.append([0,0])
        #en col·lissionar amb la poma incrementar el punts i incrementar la velocitat del joc
        vm.punts=vm.punts+1
        vm.FPS=vm.FPS+vm.incrFPS

    # moure el cap
    pos_x = serp.x
    pos_y = serp.y
    serp.x=serp.x+serp.direccio[0]
    serp.y=serp.y+serp.direccio[1]

    # moure la cua
    for num in range(len(serp.cua)-1,-1,-1):
        if num>0:
            serp.cua[num][0]=serp.cua[num-1][0]
            serp.cua[num][1]=serp.cua[num-1][1]
        else:
            serp.cua[0][0]=pos_x
            serp.cua[0][1]=pos_y

    # final de joc    
    if serp.x<0 or serp.x>=vm.grid_rows or serp.y<0 or serp.y>=vm.grid_columns:
        vm.estat="end"

    ##########
    # render #
    ##########

    #pintar el fons de blanc
    tauler.fill((0, 0, 25)) 

    #pintar la poma
    tauler.blit(vm.getTile('poma'), (poma.x*vm.tile_width, poma.y*vm.tile_height)) 

    #pintar el cap de la serp
    tauler.blit(vm.getTile('serp'), (serp.x*vm.tile_width, serp.y*vm.tile_height)) 

    #pintar la cua
    for cua in serp.cua:
        tauler.blit(vm.getTile('cua'), (cua[0]*vm.tile_width, cua[1]*vm.tile_height))

    # Aplicar el doble buffering        
    screen.blit(tauler, (0, 0))
    pygame.display.flip()
    pygame.display.update()
    fpsClock.tick(vm.FPS)

# Pantalla final del joc
font = pygame.font.SysFont(None, 36)
txtTitol = font.render(f'Has aconseguit {vm.punts} pomes.', True, (255, 255, 255))
rect = txtTitol.get_rect(center=screen.get_rect().center)
screen.fill((0, 0, 0)) 
screen.blit(txtTitol, rect)
pygame.display.flip()
time.sleep(3) 