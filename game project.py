#project lou
import pygame as pg

class obstacle:
    def create_rect(x=0,y=0):
        return pg.Rect(300,300,x,y)
        

def main():

    screen = pg.display.set_mode((640, 480))
    clock = pg.time.Clock()
    rect = pg.Rect(300, 220, 20, 20)
    velocity = (0, 0)
    rect2 = pg.Rect(300,230, 500,10)
    
    done = False
    gravity = True
    #creating the map using arrays

    map_data = {
        "WWWWWWWWWWWWWWWW",
        "W      W   W   W",
        "W       W  W   W",
        "W"
    }
    rowx = 0
    rowy = 0
    for rows in map_data:
        rowy+=10
        for cols in rows:
            rowx+=10
            if cols == "W":
                pg.draw.rect(screen,'blue',obstacle.create_rect(rowx,rowy)

                )




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
            rect.y -= 4
        if keys[pg.K_s]:
            rect.y +=4

        if gravity:
            falling = True
            if keys[pg.K_w]:
                falling = False
                rect.y-4
            if falling:
                rect.y+=8

        screen.fill((40, 40, 40))
        pg.draw.rect(screen, (150, 200, 20), rect)
        pg.draw.rect(screen, 'red',rect2)

        pg.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    main()
    pg.quit()
