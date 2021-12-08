import random
import pygame
import time
import math

pygame.init()
CLOCK = pygame.time.Clock()
DISPLAY = pygame.display.set_mode(size=(1280,720))

BASE_FONT = pygame.font.Font(None,32)
user_text = [""]
user_texts = ["", "", ""]
typing_prompts = ["The quick brown fox jumped over the lazy dog", "ABCDE", "BCDEF"]
line = 0
input_rect = pygame.Rect(320,480,640,60)
prompt_rect = pygame.Rect(320,480,640,60)
color = pygame.Color("lightskyblue3")


FPS = (60)
text_prompt = BASE_FONT.render(random.choice(typing_prompts)[line],True,(70,70,70))
SAMPLE = "The quick brown fox jumped over the lazy dog"

while True:
    
    DISPLAY.fill((0,0,0))
    
    pygame.draw.rect(DISPLAY, color, input_rect, 2)

    text_surface = BASE_FONT.render(user_texts[line],True,(255,255,255))
    DISPLAY.blit(text_prompt,(prompt_rect.x + 28, prompt_rect.y + 28))
    DISPLAY.blit(text_surface,(input_rect.x + 28, input_rect.y + 28))


    

    pygame.display.flip()
    CLOCK.tick(FPS)   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_texts[line] = user_texts[line][0:-1]
            else:
                if text_surface.get_width() > input_rect.w - 52:
                    line += 1
                user_texts[line] += event.unicode

                

    
     