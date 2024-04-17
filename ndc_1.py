import pyxel
import time
import random

class App:
    
    def __init__(self):
        pyxel.init(128, 128, title="NDC 2023")
        self.x = 0
        self.Personnage =  Personnage()
        self.Fantome = Fantome(24, 24)
        pyxel.load("theme.pyxres")
        self.tm = pyxel.tilemap(0)
        pyxel.run(self.update, self.draw)
        
    def update(self):
        self.x = (self.x + 1) % pyxel.width
        self.Personnage.deplacement(self.tm)
        self.Fantome.deplacement()
        if self.Personnage._y == 128:
            self.Personnage.respawn()
            
        for t in self.Personnage.tirs:
            self.Fantome.collisionTir(t)
        if self.Personne.isDead() :
            
        
    def draw(self):
        #pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 128, 128)
        self.Personnage.draw()
        if self.Fantome.enVie:
            self.Fantome.draw()
        else:
            
        
class Personnage:
    def __init__(self):
        self._x = 8
        self._y = 112
        self.vies = 3
        self.dir = 0 # 0 -> droite, 1 -> gauche
        self.tirs = []
        self.sautEnCours = False
        self.debutSaut = 0
        
        self.plateformes = [(6, 6), (0, 7)] + [(x, 5) for x in range(6)]
        
    def draw (self):
        pyxel.load("theme.pyxres")
        if self.dir == 0:
            pyxel.blt(self._x, self._y, 0, 0, 0, 8, 8, 0)
        else:    
            pyxel.blt(self._x, self._y, 0, 24, 0, 8, 8, 0)
        
        for t in self.tirs:
            t.draw()

    def deplacement(self, tm):
        
        if self.vies > 0:
            tile = tm.pget(self._x // 8, self._y // 8 + 1)
            #print(tile, self._y)
            
            if pyxel.btn(pyxel.KEY_RIGHT) and self._x < 120:
                self.dir = 0
                self._x += 2
            if pyxel.btn(pyxel.KEY_LEFT) and self._x > 0:
                self.dir = 1
                self._x -= 2
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.tirs.append(Tir(self))
                
            if pyxel.btnp(pyxel.KEY_UP):
    #             self.sautEnCours = True
    #             self.debutSaut = pyxel.frame_count
                if self._y > 0:
                    self._y -= 14
                
            #elif self._y < 128 - 8:
            elif tile not in self.plateformes or self._y % 8 != 0:
                self._y += 2
                
            for t in self.tirs:
                t.deplacement()
                
                if not t.alive:
                    self.tirs.remove(t)
            if self._y > 128 :
                self.vies -= 1
    
    def isDead(self):
    
        return self.vies == 0
    
    def respawn(self):
        self._x = 8
        self._y = 112
        
class Tir:
    def __init__(self, joueur):
        
        self.dir = joueur.dir
        if self.dir == 1:
            self.x = joueur._x - 1
            self.y = joueur._y + 3
        else:
            self.x = joueur._x + 8
            self.y = joueur._y + 3
        self.alive = True
        
    def draw(self):
        
        pyxel.rect(self.x, self.y, 2, 1, 2)
        
    def deplacement(self) :
        if self.dir == 0:
            self.x += 2
        else:
            self.x -= 2
        
        if self.x > 128 or self.x < 0:
            self.alive = False
            
    def gauche(self) :
        self.x += -2
        
        if self.x < -4:
            self.alive = False
            
class Fantome:
    def __init__(self, x, y):
        
        self.x = x
        self.y = y
        self.dir = 0
        self.vies = 5
        self.enVie = True
        
    def deplacement(self):
            
        if pyxel.frame_count % 20 == 0:
            self.dir = random.randint(1, 4)
        
        
        
        
        if self.dir == 1 and self.x > 8:
            self.x -= 2
                
        if self.dir == 2 and self.y > 8:
            self.y -= 2
                
        if self.dir == 3 and self.x < 120:
            self.x += 2
            
        if self.dir == 4 and self.y < 120:
            self.y += 2
            
    def collisionTir(self, tir):
        
        if self.x -1 < tir.x < self.x + 8 and self.y - 1 < tir.y < self.y + 8:
            print("!!!!")
            self.vies -= 1
            
            if self.vies <= 0 :
                self.enVie = False
        
    def collisionPerso(self, personnage): 
        
        if self.x -1 < personnage.x < self.x + 8 and self.y - 1 < personnage.y < self.y + 8:
            self.personnage.vies -= 1
            personnage.respawn()
            
    def draw(self):
        
        pyxel.blt(self.x, self.y, 0, 0, 72, 8, 8, 0)
    
App()
