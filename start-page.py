import sys, pygame

pygame.init()

clock = pygame.time.Clock()

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("chess game")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

titlefont = pygame.font.SysFont("Times New Roman", 50)
font = pygame.font.SysFont("arial", 40)
mediumfont = pygame.font.SysFont("arial", 25)
smallfont = pygame.font.SysFont("arial", 14)
bold = pygame.font.SysFont("arial", 40, bold=True)
mediumfontbold = pygame.font.SysFont("arial", 25, bold=True)
smallfontbold = pygame.font.SysFont("arial", 20, bold=True)
ceramic = (225,186,133)
dark_gray = (140,140,139)
navy_blue = (14,42,65)
white = (255, 255, 255)
dark_wood = (139,69,19)
another_dark_wood = (67,24,17)
light_wood = (160,82,45)
lightred_wood = (220, 20, 60)
darkred_wood = (187, 10, 31)
green_wood = (119,109,22)
black = (0, 0, 0)
hoverblack = (33, 33, 33)
gray = (192, 192, 192)
hovergray = (154, 154, 154)
hoverwhite = (179, 179, 179)
help_wood = (143,129,126)
blue_wood = (81,102,119)
help_wood = (140,178,215)

king_b = pygame.image.load('assets/king-b-100.png')
king_g = pygame.image.load('assets/king-g-100.png')
king_w = pygame.image.load('assets/king-w-100.png')

players = []
def create_button(x, y, width, height, hovercolor, defaultcolor, msg, player1='', player2='', player3=''):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed(3)
    
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, hovercolor, (x, y, width, height), border_top_left_radius = 3, border_top_right_radius = 3,
                        border_bottom_left_radius = 3, border_bottom_right_radius=3)
        if click[0] == 1:
            if msg == "Enter":
                players.extend([player1, player2, player3])
            return True
    else:
        pygame.draw.rect(screen, defaultcolor, (x, y, width, height),  border_top_left_radius = 3, border_top_right_radius = 3,
                            border_bottom_left_radius = 3, border_bottom_right_radius=3)
    if msg == "Start":
        buttontext = bold.render(msg, True, white)
        screen.blit(buttontext, (int((screen_width - buttontext.get_width()) / 2), 315))
    elif msg == "Leave":
        buttontext = smallfontbold.render(msg, True, white)
        screen.blit(buttontext, (int((screen_width - buttontext.get_width()) / 2), 450))
    elif msg == "Back":
        buttontext = smallfontbold.render(msg, True, white)
        screen.blit(buttontext, (20, 11))
    elif msg == "Rules":
        buttontext = smallfontbold.render(msg, True, white)
        screen.blit(buttontext, (728, 771))
    elif msg == "Enter":
        buttontext = smallfontbold.render(msg, True, white)
        screen.blit(buttontext, (350+buttontext.get_width()//2, 715+buttontext.get_height()//2))
    

def rules():
    rules_running = True
    while rules_running:
        screen.fill(ceramic)
        rules_backbutton = create_button(x=7, y=7, width=80, height=26, hovercolor=light_wood, defaultcolor=dark_wood, msg="Back")
        
        if rules_backbutton:
            rules_running = False
            return True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()
        clock.tick(15)


def menu():
    running = True
    player1, player2, player3 = "", "", ""
    player1_NameActive, player2_NameActive, player3_NameActive = False, False, False
    blackActive, grayActive, whiteActive = False, False, False

    while running:
        back = False
        screen.fill(ceramic)
        screen.blit(king_b, (400-(king_w.get_width()//2), 165))
        screen.blit(king_g, (400-(king_w.get_width()//2), 385))
        screen.blit(king_w, (400-(king_w.get_width()//2), 605))


        backbutton = create_button(x=7, y=7, width=80, height=26, hovercolor=light_wood, defaultcolor=dark_wood, msg="Back")
        helpbutton = create_button(x=713, y=767, width=80, height=26, hovercolor=blue_wood, defaultcolor=help_wood, msg="Rules")
        
        if helpbutton == True:
            back = rules()
        
        if backbutton == True and back == False:
            running=False
        
        player1Surface = mediumfontbold.render(player1, True, another_dark_wood)
        player1Border = pygame.Rect(((screen_width - player1Surface.get_width()) / 2)-5, screen_height * .10 - 10, player1Surface.get_width() + 10, 50)

        player2Surface = mediumfontbold.render(player2, True, another_dark_wood)
        player2Border = pygame.Rect(((screen_width - player2Surface.get_width()) / 2)-5, 290, player2Surface.get_width()+10, 50)

        player3Surface = mediumfontbold.render(player3, True, another_dark_wood)
        player3Border = pygame.Rect(((screen_width - player3Surface.get_width()) / 2)-5, 510, player3Surface.get_width()+10, 50)

        screen.blit(player1Surface, (int((screen_width - player1Surface.get_width()) / 2),int(screen_height * .10)))
        screen.blit(player2Surface, (int((screen_width - player2Surface.get_width()) / 2), 290+10))
        screen.blit(player3Surface, (int((screen_width - player3Surface.get_width()) / 2), 510+10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(players)
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player1Border.collidepoint(event.pos):
                    player1_NameActive = True
                else:
                    player1_NameActive = False

                
                if player2Border.collidepoint(event.pos):
                    player2_NameActive = True
                else:
                    player2_NameActive = False

                
                if player3Border.collidepoint(event.pos):
                    player3_NameActive = True
                else:
                    player3_NameActive = False
                
            if event.type == pygame.KEYDOWN:
                if player1_NameActive:
                    if event.key == pygame.K_BACKSPACE:
                        player1 = player1[:-1]
                    else: 
                        player1 += event.unicode
                elif player2_NameActive:
                    if event.key == pygame.K_BACKSPACE:
                        player2 = player2[:-1]
                    else: 
                        player2 += event.unicode
                elif player3_NameActive:
                    if event.key == pygame.K_BACKSPACE:
                        player3 = player3[:-1]
                    else:
                        player3 += event.unicode
        
        enterbutton = create_button(x=400-50, y=710, width=100, height=50, hovercolor=light_wood, defaultcolor=dark_wood, msg="Enter", player1=player1, player2=player2, player3=player3)

        if player1_NameActive:
            pygame.draw.rect(screen, dark_wood, player1Border, 2)
            player1Prompt = font.render("Black Piece Player", True, dark_wood)
        elif not player1_NameActive:
            pygame.draw.rect(screen, light_wood, player1Border, 2)
            player1Prompt = font.render("Black Piece Player", True, light_wood)
        
        if player2_NameActive:
            pygame.draw.rect(screen, dark_wood, player2Border, 2)
            player2Prompt = font.render("Gray Piece Player", True, dark_wood)
        elif not player2_NameActive:
            pygame.draw.rect(screen, light_wood, player2Border, 2)
            player2Prompt = font.render("Gray Piece Player", True, light_wood)

        if player3_NameActive:
            pygame.draw.rect(screen, dark_wood, player3Border, 2)
            player3Prompt = font.render("White Piece Player", True, dark_wood)
        elif not player3_NameActive:
            pygame.draw.rect(screen, light_wood, player3Border, 2)
            player3Prompt = font.render("White Piece Player", True, light_wood)

        screen.blit(player1Prompt, ((screen_width - player1Prompt.get_width())/2, (screen_height * .10) + player1Prompt.get_height()))
        screen.blit(player2Prompt, ((screen_width - player2Prompt.get_width())/2, 10 + 290 + player2Prompt.get_height()))   
        screen.blit(player3Prompt, ((screen_width - player3Prompt.get_width())/2, 10 + 510 + player3Prompt.get_height()))

        pygame.display.update()
        clock.tick(15)

def start_menu():
    startText = titlefont.render("Chess Game", True, navy_blue)
     
    while True: 
        screen.fill(ceramic)
        screen.blit(startText, ((screen_width - startText.get_width()) / 2, 0))
        
        startbutton = create_button(x=250, y=282.5, width=300, height=100, hovercolor=light_wood, defaultcolor=dark_wood, msg="Start")
        leavebutton = create_button(x=337.5, y=435, width=125, height=50, hovercolor=lightred_wood, defaultcolor=dark_wood, msg="Leave") 
        
        if leavebutton:
            print(players)
            pygame.quit()
            sys.exit()

        elif startbutton:
            menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(players)
                pygame.quit()
                sys.exit()
        
        clock.tick(15)
        return True

while True:
    start_menu()    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(players)
            pygame.quit()
            sys.exit()

    pygame.display.update()

    clock.tick(15)
