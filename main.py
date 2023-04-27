import pandas as pd
import numpy as np
import PySimpleGUI as sg
import pygame
import os, codecs, time


pygame.font.init()

#--------------------------------------------------------------PyGame_Interface----------------------------------------------------------------------#
objects = []

    #----------------------------------------------Skapa en klass för knappar-----------------------------------------------#
class button():
    def __init__(self, x, y, width, height, color, color_hover, on_click = None, button_value = -1, text = None, font_size = 15):
        

        #-------------------------------------------skapar objektet---------------------------------------#
        surface = pygame.Surface((width, height))
        rect_object = pygame.Rect(x, y, width, height)
        surface.fill(color)
        
        
        #-------------------------------------------Visar up objecktet på skärmen---------------------------------------#
        def blit():
            # Om det fins en text som ska på så lägger den ut den. 
            if text != None:
                #skapar en font och gör en objekt med texten och fonten
                font =  pygame.font.SysFont('comicsans', font_size)
                temp = font.render(text, 1 , (255,255,255))
                
                # Lägger på text på objektet
                surface.blit(temp, [
                            rect_object.width/2 - surface.get_rect().width/2 + 10,
                            rect_object.height/2.5 ])
                
            #
            objects.append(self)
            window.blit(surface, rect_object) 

        #---------------------------------------------funktion för knappen-------------------------------------#
        def process():
            # Kollar positionen av din mus
            mousePos = pygame.mouse.get_pos()
            
            # Kollar om rektangeln och musen överlappar
            if rect_object.collidepoint(mousePos):
                surface.fill(color_hover)
                
                # Kollar om en av mus knapparna är tryckt
                if True in pygame.mouse.get_pressed():
                    # I fall funktionen ska använda sig av ett specifikt värde
                    if button_value != -1:
                        on_click(button_value)
                    else:
                        on_click
                    
                        
        # Kör igenom dessa funktionerna varönda gång loopen går genom classen
        process() 
        blit()
        
# En funktion för att ändra vilket fönster som ska användas
def window_change(window_number):
    global win
    
    time.sleep(0.1)

    win = window_number


#-----------------------------------------------------Main loopen för pygame-----------------------------------------------#      
def start():
    # Globala värden för att enklare kunna byta genom fönster
    global run
    global win 
    global window_Size
    global window
    run = True
    win = 0
    # Storleken kommer ändras men detta determinerar vart fönstret först börjar
    window_Size = [1000,700]
    
   
    while run == True:
        #skapa fönsteret
        window = pygame.display.set_mode(window_Size)
        pygame.display.set_caption("Välkomen")
        
        clock = pygame.time.Clock()
        
         
        # visar olika fönster beroende på verdet
        if win == 0:
            win0()
        elif win == 1:
            win1()
        elif win == 2:
            win2()

        # Händelser (events)
        for event in pygame.event.get():
            # I fall man trycker på korset så stänger programmen av sig
            if event.type == pygame.QUIT:
                run = False 
        
         
        pygame.display.update()
        clock.tick(20)

#-------------------------------------------------------skapar alla fönster-------------------------------------------------#

    
def win0():
    global run
    global window_Size
    window_Size = [1000,600]
    
    
    window.fill((0,153,0))
        

    button(300, 100, 200, 200,(70,20,159),(0,0,0), window_change, 1, "helllo")
    button(100, 100, 200, 200,(70,20,0),(0,0,0), window_change, 2, "helllo")
    
            
def win1():
    global run
    global window_Size
    
    window_Size = [800,600] 
    
              
    window.fill((90,150,40))
    
    button(10, 10, 100, 50, (255,70,70), (255,0,0), window_change, 0, "back")
    
         
def win2():
    global run
    global window_Size
    
    window_Size = [600,400] 
            
    window.fill((90,70,40))
    
    button(10, 10, 100, 50, (255,70,70), (255,0,0), window_change, 0, "back")















# + startar PyGameLoopen och programme + #         
start()

