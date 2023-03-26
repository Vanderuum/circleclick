import pygame
import random
import math

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

    
    def processInput(circle):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                circle.running = False
                break
            elif pygame.mouse.get_pressed(3) == (1,0,0): # check if mouse is pressed
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
                    print(circle.moveCommandX)
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
        

    def render(circle):
        circle.window.fill((0,0,0))
        x = circle.gameState.x
        y = circle.gameState.y
        pygame.draw.circle(circle.window,(0,0,255),(x,y),10)
        score_text = circle.font.render(f'Score: {circle.score}', True, (255, 255, 0))
        circle.window.blit(score_text, (10, 10))
        pygame.display.update()
    
    def run(circle):
        while circle.running:
            circle.processInput()
            circle.update()
            circle.render()
            circle.clock.tick(60)

userInterface = UserInterface()
userInterface.run()

pygame.quit()