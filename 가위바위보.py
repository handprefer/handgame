import pygame
import random

#0:바위 1:가위 2:보
#01 내      12 내       20 내
#10 너      21 너       02 너
#11 비김    22 비김     00 비김
def judge(me,you):
    global money
    global text_money
    if(me+1==you or me-2==you):
        money+=1
        text_money=font_money.render("money : "+str(money),True,(0,0,0))
        return "win"
    elif(me==you):
        text_money=font_money.render("money : "+str(money),True,(0,0,0))
        return "draw"
    else:
        money-=1
        text_money=font_money.render("money : "+str(money),True,(0,0,0))
        return "lose"

pygame.init()
screen=pygame.display.set_mode((500,650))
pygame.display.set_caption("가위바위보")

case=0
start=0
temp=0
image=["바위.png","가위.png","보.png","상대방.png"]

character=[]

for i in range(4):
    character.append(pygame.image.load(image[i]))

money=500
font_title=pygame.font.SysFont('malgungothic',50)
text_title=font_title.render("가위바위보",True,(0,0,0))
font_start=pygame.font.SysFont('malgungothic',30)
text_start=font_start.render("start",True,(0,0,0))
font_money=pygame.font.SysFont('malgungothic',20)
text_money=font_money.render("money : "+str(money),True,(0,0,0))

clock = pygame.time.Clock()
run = True

# Game Loop
while run:
    # 1) 사용자 입력 처리
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if case==0:
                if(pygame.mouse.get_pos()[0]>=222 and pygame.mouse.get_pos()[0]<=280 and pygame.mouse.get_pos()[1]>=233 and pygame.mouse.get_pos()[1]<=253):
                    case=1
            elif case==1:
                if(pygame.mouse.get_pos()[0]>=0 and pygame.mouse.get_pos()[0]<=106 and pygame.mouse.get_pos()[1]>=500 and pygame.mouse.get_pos()[1]<=650):
                    me=0
                elif(pygame.mouse.get_pos()[0]>=188 and pygame.mouse.get_pos()[0]<=294 and pygame.mouse.get_pos()[1]>=500 and pygame.mouse.get_pos()[1]<=650):
                    me=1
                elif(pygame.mouse.get_pos()[0]>=389 and pygame.mouse.get_pos()[0]<=500 and pygame.mouse.get_pos()[1]>=500 and pygame.mouse.get_pos()[1]<=650):
                    me=2
                
                you=random.randrange(0,3)
                me_character=pygame.transform.scale(character[me],(139,200))
                you_character=pygame.transform.scale(character[you],(139,200))
                you_character=pygame.transform.rotate(you_character,180)
                case=2
                

            elif case==2:
                
                if(temp==0):
                    result=judge(me,you)
                    font_result=pygame.font.SysFont('malgungothic',50)
                    text_result=font_result.render(result,True,(0,0,0))
                    temp=1
                else:
                    case=1
                    temp=0

    if case==0:
        # 3) 게임 장면 그리기
        screen.fill(pygame.color.Color(255,255,255))
        screen.blit(text_title,(125,150))
        screen.blit(text_start,(220,220))
    elif case==1:
        screen.fill(pygame.color.Color(255,255,255))
        
        screen.blit(text_money,(0,0))
        screen.blit(character[0],(0,500))
        screen.blit(character[1],(189,500))
        screen.blit(character[2],(388,500))
        screen.blit(character[3],(100,120))
        
    elif case==2:
        screen.fill(pygame.color.Color(0,255,255))
        screen.blit(me_character,(300,350))
        screen.blit(you_character,(50,80))
        if(temp==1):
            screen.blit(text_result,(200,280))

        

    pygame.display.flip()
    clock.tick(1000)

pygame.quit()

