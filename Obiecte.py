import pygame

class dizo:
    def __init__(self, posx, posy, pos, pos2):
        self.posx = posx
        self.posy = posy
        self.pos = pos
        self.pos2 = pos2
    def draw(self, ecran):
        img = ''
        if self.pos == 1:
            img = pygame.image.load('Needed/dizo1.png')
        elif self.pos == 2:
            img = pygame.image.load('Needed/dizo2.png')
        elif self.pos == 3:
            img = pygame.image.load('Needed/dizo3.png')
        elif self.pos == 4:
            img = pygame.image.load('Needed/dizo4.png')
        elif self.pos == 5:
            img = pygame.image.load('Needed/dizo5.png')
        ecran.blit(img, (self.posx, self.posy))

class pasare:
    def __init__(self, posx, posy, nr):
        self.posx = posx
        self.posy = posy
        self.pos = nr
    def draw(self, ecran):
        img = ''
        if self.pos == 1:
            img = pygame.image.load('Needed/pas1.png')
        elif self.pos == 2:
            img= pygame.image.load('Needed/pas2.png')
        ecran.blit(img, (self.posx, self.posy))

class cactus:
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
    def draw(self, ecran):
        img = pygame.image.load('Needed/cactus.png')
        ecran.blit(img, (self.posx, self.posy))

class nor:
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
    def draw(self, ecran):
        img = pygame.image.load('Needed/nor.png')
        ecran.blit(img, (self.posx, self.posy))

class sol:
    def __init__(self, posx1, posy1, posx2, posy2, culoare):
        self.posx1 = posx1
        self.posy1 = posy1
        self.posx2 = posx2
        self.posy2 = posy2
        self.culoare = culoare
    def draw(self, ecran):
       pygame.draw.line(ecran, self.culoare, [self.posx1, self.posy1], [self.posx2, self.posy2], 2)

class Text:
    def __init__(self, posx, posy, marime, culoare, txt):
        self.posx = posx
        self.posy = posy
        self.culoare = culoare
        self.txt = txt
        self.Font = pygame.font.Font('freesansbold.ttf', marime)
    def draw(self, ecran):
        text = self.Font.render(self.txt, True, self.culoare)
        textfinal = text.get_rect()
        textfinal.center = (self.posx, self.posy)
        ecran.blit(text, textfinal)