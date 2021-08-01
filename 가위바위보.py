import pygame

pygame.init()
screen=pygame.display.set_mode((500,650))
pygame.display.set_caption("가위바위보")

case=0
start=0
image=["바위.png","가위.png","보.png","상대방.png"]

for i in range(4):
    character=[]
    character.append(pygame.image.load(image[i]))

font_title=pygame.font.SysFont('malgungothic',50)
text_title=font_title.render("가위바위보",True,(0,0,0))
font_start=pygame.font.SysFont('malgungothic',30)
text_start=font_start.render("start",True,(0,0,0))

clock = pygame.time.Clock()
run = True

# Game Loop
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if case==0:
        screen.fill(pygame.color.Color(255,255,255))
        screen.blit(text_title,(125,150))
        screen.blit(text_start,(220,220))
    elif case==1:
        screen.fill(pygame.color.Color(255,255,255))
        screen.blit(character[0],(0,0))
        screen.blit(character[1],(40,40))
        screen.blit(character[2],(80,80))
        screen.blit(character[3],(120,120))
        

    pygame.display.update()


pygame.quit()

