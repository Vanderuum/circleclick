import pygame
import random
import math
import win32api
import win32con
import mouse
import keyboard

class GameState():
    def __init__(circle):
        circle.x = 120
        circle.y = 120
    def update(circle,moveCommandX,moveCommandY):
        circle.x += moveCommandX
        circle.y += moveCommandY

class UserInterface():
    def __init__(circle):
        pygame.init()
        circle.window = pygame.display.set_mode((640,480))
        pygame.display.set_caption("Click the Circles Game")
        circle.clock = pygame.time.Clock()
        circle.gameState = GameState()
        circle.running = True
        circle.mousetarget = pygame.math.Vector2(0,0)
        circle.move=True
        circle.font = pygame.font.Font(None, 36)
         #score defaults
        circle.score = 0
        circle.score_increment = 1
        circle.aion = False
        pygame.mouse.set_pos(0,0)

    def processInput(circle):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                circle.running = False
                break
            elif event.type == pygame.MOUSEBUTTONUP:             #check if mouse is pressed
                    if circle.distance<=10: # check for distance between circle and mouse
                            if random.randint(0,1) == 1: # random circle movement after respawn
                                circle.moveCommandX *= 1.1
                            else:
                                circle.moveCommandX *= -1.1
                            if random.randint(0,1) == 1:
                                circle.moveCommandY *= 1.1
                            else:
                                circle.moveCommandY *= -1.1
                            circle.gameState.x = random.randint(0,640) #random circle placement
                            circle.gameState.y = random.randint(0,480)
                            circle.score += circle.score_increment #increase score
            

        # mouse position
        mousePos = pygame.mouse.get_pos()
        circle.mousetarget.x = mousePos[0]
        circle.mousetarget.y = mousePos[1]

        #mouse vs circle collision detection
        circle.distx = circle.mousetarget.x - circle.gameState.x
        circle.disty = circle.mousetarget.y - circle.gameState.y
        circle.distance = math.sqrt((circle.distx*circle.distx)+(circle.disty*circle.disty))

        # boundary collision detection and circle movement
        
        def circlemove():
                while circle.move == True:
                    circle.moveCommandX = 1
                    circle.moveCommandY = -1
                    circle.move = False
                    break

        circlemove()

        if circle.gameState.x > 630:
            circle.moveCommandX *= -1
            circle.gameState.x = 630
        if circle.gameState.y > 470:
            circle.moveCommandY *= -1
            circle.gameState.y = 470
        if circle.gameState.x < 10:
            circle.moveCommandX *= -1
            circle.gameState.x = 10
        if circle.gameState.y < 10:
            circle.moveCommandY *= -1
            circle.gameState.y = 10
            

    def update(circle):
        circle.gameState.update(circle.moveCommandX,circle.moveCommandY)

    def easyreactaicalcpos(circle):
    #calculate the 8 positions around the mouse cursor
            circle.aimousepos1 = [circle.mousetarget.x + 10, circle.mousetarget.y]
            circle.aimousepos2 = [circle.mousetarget.x, circle.mousetarget.y + 10]
            circle.aimousepos3 = [circle.mousetarget.x + 10, circle.mousetarget.y + 10]
            circle.aimousepos4 = [circle.mousetarget.x - 10, circle.mousetarget.y + 10]
            circle.aimousepos5 = [circle.mousetarget.x - 10, circle.mousetarget.y]
            circle.aimousepos6 = [circle.mousetarget.x - 10, circle.mousetarget.y - 10]
            circle.aimousepos7 = [circle.mousetarget.x, circle.mousetarget.y - 10]
            circle.aimousepos8 = [circle.mousetarget.x + 10, circle.mousetarget.y - 10]
        
    def easyreactaicalcdis1(circle):
    #calculate the distance between each position and the circle
            circle.AIdistx1 = circle.aimousepos1[0] - circle.gameState.x
            circle.AIdisty1 = circle.aimousepos1[1] - circle.gameState.y
            circle.AIdistance1 = math.sqrt((circle.AIdistx1*circle.AIdistx1)+(circle.AIdisty1*circle.AIdisty1))

            circle.AIdistx2 = circle.aimousepos2[0] - circle.gameState.x
            circle.AIdisty2 = circle.aimousepos2[1] - circle.gameState.y
            circle.AIdistance2 = math.sqrt((circle.AIdistx2*circle.AIdistx2)+(circle.AIdisty2*circle.AIdisty2))
    
            circle.AIdistx3 = circle.aimousepos3[0] - circle.gameState.x
            circle.AIdisty3 = circle.aimousepos3[1] - circle.gameState.y
            circle.AIdistance3 = math.sqrt((circle.AIdistx3*circle.AIdistx3)+(circle.AIdisty3*circle.AIdisty3))
    
            circle.AIdistx4 = circle.aimousepos4[0] - circle.gameState.x
            circle.AIdisty4 = circle.aimousepos4[1] - circle.gameState.y
            circle.AIdistance4 = math.sqrt((circle.AIdistx4*circle.AIdistx4)+(circle.AIdisty4*circle.AIdisty4))
    
            circle.AIdistx5 = circle.aimousepos5[0] - circle.gameState.x
            circle.AIdisty5 = circle.aimousepos5[1] - circle.gameState.y
            circle.AIdistance5 = math.sqrt((circle.AIdistx5*circle.AIdistx5)+(circle.AIdisty5*circle.AIdisty5))
    
            circle.AIdistx6 = circle.aimousepos6[0] - circle.gameState.x
            circle.AIdisty6 = circle.aimousepos6[1] - circle.gameState.y
            circle.AIdistance6 = math.sqrt((circle.AIdistx6*circle.AIdistx6)+(circle.AIdisty6*circle.AIdisty6))
    
            circle.AIdistx7 = circle.aimousepos7[0] - circle.gameState.x
            circle.AIdisty7 = circle.aimousepos7[1] - circle.gameState.y
            circle.AIdistance7 = math.sqrt((circle.AIdistx7*circle.AIdistx7)+(circle.AIdisty7*circle.AIdisty7))
    
            circle.AIdistx8 = circle.aimousepos8[0] - circle.gameState.x
            circle.AIdisty8 = circle.aimousepos8[1] - circle.gameState.y
            circle.AIdistance8 = math.sqrt((circle.AIdistx8*circle.AIdistx8)+(circle.AIdisty8*circle.AIdisty8))

    def easyreactaiminimum(circle):
        #choose the shortest distance out of the 8 calculated distances
            circle.AIcalcdistance = [circle.AIdistance1, circle.AIdistance2, circle.AIdistance3, circle.AIdistance4, circle.AIdistance5, circle.AIdistance6, circle.AIdistance7, circle.AIdistance8]
            circle.AImindistance = min(circle.AIcalcdistance)

        #find and match the correlated minimum distance with the original coordinates
            if circle.AImindistance == circle.AIdistance1:
             circle.AIcursormove = circle.aimousepos1
            elif circle.AImindistance == circle.AIdistance2:
             circle.AIcursormove = circle.aimousepos2
            elif circle.AImindistance == circle.AIdistance3:
             circle.AIcursormove = circle.aimousepos3
            elif circle.AImindistance == circle.AIdistance4:
                circle.AIcursormove = circle.aimousepos4
            elif circle.AImindistance == circle.AIdistance5:
             circle.AIcursormove = circle.aimousepos5
            elif circle.AImindistance == circle.AIdistance6:
                circle.AIcursormove = circle.aimousepos6
            elif circle.AImindistance == circle.AIdistance7:
                circle.AIcursormove = circle.aimousepos7
            elif circle.AImindistance == circle.AIdistance8:
                circle.AIcursormove = circle.aimousepos8

    def easyreactaimovecur(circle):
        #translation layer between coordinates in window to coordinates on computer
        circle.AImoveRelx = circle.AIcursormove[0] - circle.mousetarget.x
        circle.AImoveRely = circle.AIcursormove[1] - circle.mousetarget.y
        #move cursor towards the calculated closest distance
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(circle.AImoveRelx), int(circle.AImoveRely), 0, 0) 

    def easyreactaiclickoncontact(circle):
        #click when the cursor is on the circle
        if circle.distance<=10:
            mouse.click('left')

    def aikey(circle):
        if circle.aion == False:
                if keyboard.is_pressed('a'):
                    circle.aion = True
        elif circle.aion == True:
                if keyboard.is_pressed('s'):
                    circle.aion = False
        
    def aistart(circle):
            if circle.aion == True:
                circle.easyreactaicalcpos()
                circle.easyreactaicalcdis1()
                circle.easyreactaiminimum()
                circle.easyreactaimovecur()
                circle.easyreactaiclickoncontact()

    def render(circle):
        circle.window.fill((0,0,0))
        x = circle.gameState.x
        y = circle.gameState.y
        pygame.draw.circle(circle.window,(0,0,255),(x,y),10)
        score_text = circle.font.render(f'Score: {circle.score}', True, (255, 255, 0))
        circle.window.blit(score_text, (10, 10))
        if circle.aion == True:
             aitextfield = "On"
        elif circle.aion == False:
             aitextfield = "Off"
        ai_text = circle.font.render(f'AI: {aitextfield}', True, (255, 255, 0))
        circle.window.blit(ai_text, (400, 10))
        aitoggle1_text = circle.font.render(f'a = On', True, (255, 255, 0))
        circle.window.blit(aitoggle1_text, (500, 10))
        aitoggle2_text = circle.font.render(f's = Off', True, (255, 255, 0))
        circle.window.blit(aitoggle2_text, (500, 40))
        pygame.display.update()
    
    def run(circle):
        while circle.running:
            circle.processInput()
            circle.update()
            circle.render()
            circle.aikey()
            circle.aistart()
            circle.clock.tick(60)


userInterface = UserInterface()
userInterface.run()

pygame.quit()
