import pygame
import random
import Obiecte
from pygame import mixer

# Culori

Gri = (247, 247, 247)
Gri2 = (83, 83, 83)
Rosu = (255, 0, 0)

pygame.init()
pygame.font.init()
mixer.init()

mixer.music.load('Needed/sound.mp3')
mixer.music.set_volume(0.5)

# Ecran
Latime = 850
Inaltime = 375
Ecran = pygame.display.set_mode((Latime, Inaltime))
pygame.display.set_caption('Chrome dino game')
img = pygame.image.load('Needed/icon.png')
pygame.display.set_icon(img)

# Obiecte
# Dino
Dino = Obiecte.dizo(5, Inaltime - Inaltime//4 - 13, 3, 1)
Dinoinit = Inaltime - Inaltime//4 - 13

# Nori
Nori = []
Nori.append(Obiecte.nor(Latime + 5, 50))
Nori.append(Obiecte.nor(Latime + 95, 75))
Nori.append(Obiecte.nor(Latime + 295, 60))
Nori.append(Obiecte.nor(Latime + 390, 80))
Nori.append(Obiecte.nor(Latime + 530, 90))
Nori.append(Obiecte.nor(Latime + 650, 70))

# Sol
Sols = []
lng1 = Latime - 10
lng2 = random.randrange(30)
dif = 75
inalt = random.randint(Inaltime - Inaltime//6 + 10, Inaltime - 10)

for i in range(15):
    Sols.append(Obiecte.sol(lng1, inalt, lng1 + lng2, inalt, Gri2)) 
    lng1 += dif
    lng2 = random.randrange(30)
    inalt = random.randint(Inaltime - Inaltime//6 + 10, Inaltime + 30)

# Cactusi
Cactusi = []
Cactusi.append(Obiecte.cactus(-1, Inaltime - Inaltime//4 - 13))
Cactusi.append(Obiecte.cactus(-1, Inaltime - Inaltime//4 - 13))
Cactusi.append(Obiecte.cactus(-1, Inaltime - Inaltime//4 - 13))
Cactusi.append(Obiecte.cactus(-1, Inaltime - Inaltime//4 - 13))
Cactusi.append(Obiecte.cactus(-1, Inaltime - Inaltime//4 - 13))

# Pasari
Pasari = []
Pasinalt = random.randint(Inaltime//2 + 50, Inaltime - Inaltime//5 - 30)
Pasari.append(Obiecte.pasare(-1, Pasinalt, 1))
Pasari.append(Obiecte.pasare(-1, Pasinalt, 1))
Pasari.append(Obiecte.pasare(-1, Pasinalt, 1))
Pasari.append(Obiecte.pasare(-1, Pasinalt, 1))
Pasari.append(Obiecte.pasare(-1, Pasinalt, 1))

# Text
Scortext = Obiecte.Text(Latime - 35, 11, 16, Gri2, 0)
Scormaretext = Obiecte.Text(Latime - 35, 30, 16, Gri2, '')
Exittext = Obiecte.Text(Latime//2, Inaltime//2, 20, Gri2, 'Apasa tasta SPACE pentru a incepe iar')

Exit = False
Start = False
Scorevent = pygame.USEREVENT + 4 
Ievent = pygame.USEREVENT + 1
Cactevent = pygame.USEREVENT +2
Pas2event = pygame.USEREVENT + 5
Intervalcact1 = 5500
Intervalcact2 = 10500
cactinterval = random.randint(Intervalcact1, Intervalcact2)
Pasevent = pygame.USEREVENT + 3
Intervalpas1 = 8500
Intervalpas2 = 12500
pasinterval = random.randint(Intervalpas1, Intervalpas2)
Pas = False
sarit = False
Saritinapoi = False
Pierdut = False
Jos = False

# Scor
scor = 0

# Init
Ecran.fill(Gri)
pygame.draw.line(Ecran, Gri2, [0, Inaltime - Inaltime//6], [Latime, Inaltime - Inaltime//6], 4)
pygame.draw.rect(Ecran, Gri, [65, 0, Latime, Inaltime], 0)       
Dino.draw(Ecran)
pygame.display.flip()

ceas = pygame.time.Clock()
pygame.time.set_timer(Ievent, 75)
pygame.time.set_timer(Cactevent, cactinterval)
pygame.time.set_timer(Pasevent, pasinterval)
pygame.time.set_timer(Scorevent, 500)
pygame.time.set_timer(Pas2event, 300)


while not Exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mixer.music.play()
                Start = True
                Dino.pos = 1

    while Start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Exit = True
                Start = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and not sarit and not Saritinapoi:
                    if not Jos:
                        Dino.pos = 4
                    Jos = True
                    Dino.pos2 = 2
                    Dino.posy = Inaltime - Inaltime//4 + 3
                elif event.key == pygame.K_SPACE and not Jos:
                    mixer.music.play()
                    sarit = True
            if  event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN and not sarit and not Saritinapoi:
                    Jos = False
                    Dino.pos2 = 1
                    Dino.posy = Inaltime - Inaltime//4 - 13
            if event.type == Scorevent:
                scor += 10
                if scor > 5:
                    Pas = True
            if event.type == Ievent:
                if Dino.pos2 == 1:
                    if Dino.pos == 1:
                        Dino.pos = 2
                    else:
                        Dino.pos = 1
                else:
                    if Dino.pos == 4:
                        Dino.pos = 5
                    else:
                        Dino.pos = 4
            if event.type == Pas2event:
                for pasare in Pasari:
                    if pasare.pos == 1:
                        pasare.pos = 2
                    else:
                        pasare.pos = 1
            if event.type == Cactevent:
                cactinterval = random.randint(Intervalcact1, Intervalcact2)
                if Intervalcact1 > 4250:
                    Intervalcact1 -= 250
                if Intervalcact2 > 6750:
                    Intervalcact2 -= 250
                pygame.time.set_timer(Cactevent, cactinterval)
                while True:
                    for cactus in Cactusi:
                        if cactus.posx < 0:
                            cactus.posx = Latime + 30
                            break
                    break
            if event.type == Pasevent:
                pasinterval = random.randint(Intervalpas1, Intervalpas2)
                pygame.time.set_timer(Pasevent, pasinterval)
                if Intervalpas1 > 6250:
                    Intervalpas1 -= 250
                if Intervalpas2 > 9750:
                    Intervalpas2 -= 250
                if Pas:
                    while True:
                        for pasare in Pasari:
                            if pasare.posx < 0:
                                pasare.posx = Latime + 30
                                pasare.posy = random.randint(Inaltime//2 + 50, Inaltime - Inaltime//5 - 30)
                                break
                        break         

        for nor in Nori:
            if 0 <= nor.posx:
                nor.posx -= 0.5
            else:
                nor.posx = Latime + 10
                nor.posy = random.randint(50, 90)
        for sol in Sols:
            if sol.posx1 <= 0:
                sol.posx1 = Latime + 10
                sol.posx2 = Latime + 20
                random.randint(Inaltime - Inaltime//6 + 10, Inaltime - 10)
            else:
                sol.posx1 -= 0.5
                sol.posx2 -= 0.5

        for cactus in Cactusi:
            if cactus.posx > 0:
                if cactus.posx + 15 > Dino.posx + 32 >= cactus.posx:
                    if cactus.posy <= Dino.posy + 30:
                        Start = False
                        Pierdut = True
                break
        for Pasare in Pasari:
            if Pasare.posx > 0:
                if Pasare.posx + 40 >= Dino.posx + 32 >= Pasare.posx:
                    if Pasare.posy < Dino.posy < Pasare.posy + 20 or Pasare.posy < Dino.posy + 30 < Pasare.posy + 20:
                        Start = False
                        Pierdut = True
                break

        Ecran.fill(Gri)
        for cactus in Cactusi:
            if cactus.posx >= 0:
                cactus.posx -= 0.5
                cactus.draw(Ecran)
        for pasare in Pasari:
            if  pasare.posx >= 0:
                pasare.posx -= 0.5
                pasare.draw(Ecran)

        pygame.draw.line(Ecran, Gri2, [0, Inaltime - Inaltime//6], [Latime, Inaltime - Inaltime//6], 3)
        if sarit:
            if Dino.posy > Dinoinit - 115 and not Saritinapoi:
                Dino.posy -= 0.75
            elif Dino.posy < Dinoinit:
                Saritinapoi = True
                Dino.posy += 0.85
            else:
                sarit = False
                Saritinapoi = False
                

        Dino.draw(Ecran)
        if Scormaretext.txt:
            Scormaretext.draw(Ecran)
        a = ''
        if scor < 100:
            a = '00000' + str(scor)
        elif scor < 1000:
            a = '0000' + str(scor)
        elif scor < 10000:
            a = '000' + str(scor)
        elif scor < 100000:
            a = '00' + str(scor)        
        Scortext.txt = a
        Scortext.draw(Ecran)
        for nor in Nori:
            nor.draw(Ecran)
        for sol in Sols:
            sol.draw(Ecran)

        pygame.display.flip()
    
    if Pierdut:
        for cactus in Cactusi:
            cactus.posx = -1
        for pasare in Pasari:
            pasare.posx = -1
        Scormaretext.txt = Scortext.txt
        scor = 0
        Intervalpas1 = 8500
        Intervalpas2 = 12500
        Intervalcact1 = 5500
        Intervalcact2 = 10500   
        Exittext.draw(Ecran)

    pygame.display.flip()

    ceas.tick(60)

pygame.quit()