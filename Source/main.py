import pygame
import sys
import random
from player import player

pygame.init()
pygame.font.init()

rozliseni_okna = (800, 600)

okno = pygame.display.set_mode(rozliseni_okna)
soubor = open("G:\Python\projecterectermecternerder\Mine-nuhazgvdtzasfztHSFDztjhdzjgHASYGtfrSZTJ-HGJfSAUTFDuzr-IKSDJ-H\safe\Save.txt", 'r', encoding = 'utf-8')

for jeden_radek in soubor:
    skorestr = jeden_radek
    skore = int(skorestr)
        

soubor.close()

randoms = random.randint(50,500)
pozice_micku_y = randoms
pozice_micku_x = 400
velikost_micku = 50
randoms2 = random.randint(1,2)
if randoms2 == 1:
    rychlost_micku_x = 0.3
if randoms2 == 2:
    rychlost_micku_x = -0.3
rychlost_micku_y = 0.3

velikost_hrace_vyska = 150
velikost_hrace_sirka = 50

pozice_hrace_x = 10
pozice_hrace_y = 300
rychlost_hrace = 0.6

velikost_hrace_vyska2 = 150
velikost_hrace_sirka2 = 50

clock = pygame.time.Clock()

pozice_hrace_x2 = 740
pozice_hrace_y2 = 300
rychlost_hrace2 = 0.6

button_rect2 = pygame.Rect(300, 200, 200, 100)
button_rect = pygame.Rect(300, 330, 200, 100)
button_color = (100, 100, 100)
click_color = (100, 100, 100)

font = pygame.font.SysFont(None , 40)
font2 = pygame.font.SysFont(None , 40)
esc = False

jo = False
jo2 = False 
fps = str(int(clock.get_fps()))

def draw_button(rect, color, text):
    pygame.draw.rect(okno, color, rect)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=rect.center)
    okno.blit(text_surface, text_rect)
    
def draw_text(x, y):
    txtimg = font2.render("Skore: " + str(skore), True, (0, 0, 0))
    okno.blit(txtimg, (x, y))

def fps_counter():
    fps = str(int(clock.get_fps()))
    fps_t = font.render(fps , 1, pygame.Color("RED"))
    okno.blit(fps_t,(0,0))

def reset_game():     
    global pozice_micku_x, pozice_micku_y, skore
    pozice_micku_x = 400
    pozice_micku_y = 300
    skore = 0
    
while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif udalost.type == pygame.KEYDOWN:
            if udalost.key == pygame.K_ESCAPE:
                esc = not esc
        elif udalost.type == pygame.MOUSEBUTTONDOWN:
            if udalost.button == 1:
                if button_rect.collidepoint(udalost.pos):
                    print("reset")
                    reset_game()
        elif udalost.type == pygame.MOUSEBUTTONDOWN:
            if udalost.button == 1:
                if button_rect2.collidepoint(udalost.pos):
                    print("Quited")
                    quit()
        
    
    if esc:
        is_hovered = button_rect.collidepoint(pygame.mouse.get_pos())
        is_hovered2 = button_rect2.collidepoint(pygame.mouse.get_pos())
        
        pygame.draw.rect(okno, (0, 0, 0), (100, 100, 600, 400))
        if is_hovered:
            if pygame.mouse.get_pressed()[0]:  # Left mouse button is pressed
                draw_button(button_rect, click_color, "Reseted")
            else:
                draw_button(button_rect, button_color, "Reset")
        else:
            draw_button(button_rect, button_color, "Reset")

        if is_hovered2:
            if pygame.mouse.get_pressed()[0]:  # Left mouse button is pressed
                draw_button(button_rect2, click_color, "Quited and Saved")
                soubor2 = open("G:\Python\projecterectermecternerder\Mine-nuhazgvdtzasfztHSFDztjhdzjgHASYGtfrSZTJ-HGJfSAUTFDuzr-IKSDJ-H\safe\Save.txt", 'w', encoding = 'utf-8')
                soubor2.write(str(skore))
                soubor2.close()
                
                quit()
            else:
                draw_button(button_rect2, button_color, "Quit and Save")
        else:
            draw_button(button_rect2, button_color, "Quit and Save")
            
        pygame.display.flip()
        
    playerx = 20
    playery = 440
    velikostx = 40
    velikosty = 60
    
    if not esc:            
        stisknute_klavesy = pygame.key.get_pressed()
        okno.fill((0, 0, 0))
        
        fps_counter()
        clock.tick(60)  
        
        #jump
        if stisknute_klavesy[pygame.K_SPACE]:
            on_ground = playery == 440
            jump_count = 10  

            if on_ground:
                jump_count = 10  

            if stisknute_klavesy[pygame.K_SPACE]:
                if on_ground:
                    jump_count = 10  
            else:
                jump_count = 0  

            if not on_ground or jump_count > 0:
                playery -= 3
                jump_count -= 1

            if playery < 440:
                on_ground = False
            else:
                on_ground = True
                playery =  440

        player(20, 440, 40, 60)
     
        pygame.display.update()
    