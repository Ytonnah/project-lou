#project lou
import pygame as pg


screen = pg.display.set_mode((640, 480))

class obstacle:
    def __init__(self,screen,x,y):
       obs1 = pg.Rect(300,300,x,y)
       #self.create_rect(screen,"white",obs1)
       pg.draw.rect(screen,"white",obs1)
       pg.display.flip()

    def create_rect(x=0,y=0,screen=screen):
        obs1=  pg.Rect(300,300,x,y)
        return pg.draw.rect(screen,'red',obs1 )
    
        

def main():

    
    clock = pg.time.Clock()
    rect = pg.Rect(300, 220, 20, 20)
    velocity = (0, 0)
    rect2 = pg.Rect(300,230, 500,10)
    
    done = False
    gravity = False


    #creating the map using arrays

    map_data = {
        "WWWWWWWWWWWWWWWW",
        "W      W   W   W",
        "W       W  W   W",
        "W",
        "WWWWWWWWWWWWWWWW"
    }

    for rows in map_data:
        print("\n")
        for col in rows:
            print("x",sep="")
       

    rowx = 0
    rowy = 0
    for rows in map_data:
        rowy+=10
        for cols in rows:
            rowx+=10
            #print("x",end="")
            if cols == "W":
                
                obstacle(screen,rowx,rowy)
                #obstacle.create_rect(rowx,rowy,screen)
                #pg.draw.rect(screen,'blue',obstacle.create_rect(rowx,rowy)
            #print("\n")

                

    #game loop
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True 
        
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:  #to move left
            rect.x -= 4
        if keys[pg.K_d]: #to move right
            rect.x += 4
        if keys[pg.K_w]:
            
            #rect.y -= 4
            rect.y -=4
        if keys[pg.K_s]:
            rect.y +=4

        if gravity:
            falling = True
            if keys[pg.K_w]:
                falling = False
                for i in range(4):
                    rect.y-=15*(i*0.8)

            if falling:
                for i in range(4):
                    rect.y+=15*(i*0.2)#0.8 is the pull strength
                #rect.y+=15

        screen.fill((40, 40, 40))
        pg.draw.rect(screen, (150, 200, 20), rect)
        #pg.draw.rect(screen, 'red',rect2)

        pg.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    main()
    pg.quit()
