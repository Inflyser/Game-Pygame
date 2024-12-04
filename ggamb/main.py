import pygame as pg
    
    
class Person():
    def __init__(self, name: str, hp: int, mana: int, exp: int, skin: str):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.exp = exp
        self.skin = skin
        self.lvl = exp // 100
        
class Object():
    def __init__(self, name: str, size_wight: int, size_height: int, skin: str):
        self.name = name
        self.size_height = size_height
        self.size_wight = size_wight
        self.skin = skin
    
    def Initialization(self):
        return pg.transform.scale(pg.image.load(self.skin).convert_alpha(), 
            (self.size_wight, self.size_height))

Hero = Person("Name", 100, 100, 0, r"img\Hero\h0-Photoroom.png")

obelisck = Object("Obelisck", 75, 150, r'img\image-Photoroom.png')

rip = Object("Rip", 200, 200, r'img\rips.gif')
desk = Object("Desk", 50, 50, r'img\pcdfv.jpg')

pg.init() # Установка экрана

WIDTH, HEIGHT = 1600, 900
screen = pg.display.set_mode((WIDTH, HEIGHT))

hero = pg.image.load(Hero.skin).convert_alpha()
hero = pg.transform.scale(hero, (85, 78))


frame_right_hero = [ 
    pg.image.load(rf'img\Hero\frame_right\h{number_frame}-Photoroom.png').convert_alpha() 
    for number_frame in range(1, 9)
]

frame_left_hero = [
    pg.image.load(rf'img\Hero\frame_left\h{number_frame}-Photoroom2.png').convert_alpha() 
    for number_frame in range(1, 9)
]

clock = pg.time.Clock()

coynt = 0
speed = 40



def main():
    global coynt
    
    flLeft = flRight = flUp = flDown = False
    
    X, Y = 900, 300
    X_Center, Y_Center = 800, 450
    
    # screen.blit(f, (0, 0)) 
    ranning = True
    while ranning:
        
        for i in range(0, 1600, 50):
            for j in range(0, 900, 50):
                screen.blit(desk.Initialization(), (i, j)) # доска вывести
        
        
        if flLeft == flRight == flUp == flDown:
            screen.blit(hero, (X_Center, Y_Center)) 
        # if flLeft == True:
         
        def Frame_pozition(Frame):
            global coynt, last_frame
            last_frame = Frame
            
            screen.blit(Frame[coynt], (X_Center, Y_Center))
            if coynt == len(Frame)-1:
                coynt = 0
            else:
                coynt+=1

        
        
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                ranning = False
                pg.quit()
                exit()
    
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_d:
                    flLeft = True
                    
                elif event.key == pg.K_w: 
                    flUp = True         
                    
                elif event.key == pg.K_s: 
                    flDown = True
                    
                elif event.key == pg.K_a: 
                    flRight = True
            
            elif event.type == pg.KEYUP:
                if event.key in [pg.K_d, pg.K_a, pg.K_w, pg.K_s]:
                    flLeft = flRight = flDown = flUp = False
                    while coynt != len(frame_right_hero)-1:
                        coynt += 1
                   
                    
             
        if flLeft:         
            X -= speed
            
            Frame_pozition(frame_right_hero)
            
        elif flRight:    
            X += speed
            
            Frame_pozition(frame_left_hero)

            
        elif flUp:           
            Y += speed
            
            Frame_pozition(last_frame)
            
        elif flDown:
            Y -= speed
            
            Frame_pozition(last_frame)
        
        ob = 6
        for Ix in range(0, 150*ob+1, 150):
            screen.blit(obelisck.Initialization(), (X+Ix, Y)) 

        screen.blit(rip.Initialization(), (X+450, Y-300)) 
   
   
        clock.tick(60)
        
        pg.display.update()
        pg.display.flip()  

main()