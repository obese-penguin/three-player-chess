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
mediumfont = pygame.font.SysFont("arial", 20)
helpfontbold = pygame.font.SysFont("arial", 20, bold=True)
smallfont = pygame.font.SysFont("arial", 14)
bold = pygame.font.SysFont("arial", 40, bold=True)
mediumfontbold = pygame.font.SysFont("arial", 25, bold=True)
smallfontbold = pygame.font.SysFont("arial", 20, bold=True)
creditfont = pygame.font.SysFont("arial", 15, bold=True)
namefont = pygame.font.SysFont("arial", 13)

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
credit_color = (104, 51, 14)
#credit_color = (0, 50, 0)
black = (0, 0, 0)

king_b = pygame.image.load('assets/knight-b-100.png')
king_g = pygame.image.load('assets/knight-g-100.png')
king_w = pygame.image.load('assets/knight-w-100.png')

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
    elif msg == "Play" or msg == "Next":
        buttontext = smallfontbold.render(msg, True, white)
        screen.blit(buttontext, (728, 11))

def next_rules():
    next_rules_running = True
    while next_rules_running:
        screen.fill(ceramic)
        next_rules_backbutton = create_button(x=7, y=7, width=80, height=26, hovercolor=light_wood, defaultcolor=dark_wood, msg="Back")

        rules10 = [helpfontbold.render('10.', True, dark_wood), mediumfont.render("If either order of a knight's move would carry it horizontally", True, dark_wood),
                mediumfont.render("across a moat. without that knight being able to bridge the moat then that move is illegal.", True, dark_wood)]
        rules11 = [helpfontbold.render('11.', True, dark_wood), mediumfont.render("A team's checkmate status is not finalized until it is their turn unless", True, dark_wood),
                mediumfont.render("their king is captured.", True, dark_wood)]
        rules12 = [helpfontbold.render('12.', True, dark_wood), mediumfont.render("When a player is checkmated that player is eliminated from the game", True, dark_wood),
                mediumfont.render("but all their pieces remain on the board these pieces do not move.", True, dark_wood)]
        rules13 = [helpfontbold.render('13.', True, dark_wood), mediumfont.render("If you wish to occupy a space with an eliminated player's piece on it", True, dark_wood),
                mediumfont.render("then you must capture that piece.", True, dark_wood)]
        rules14 = [helpfontbold.render('14.', True, dark_wood), mediumfont.render("If a player cannot make a legal move called a stalemate and three players", True, dark_wood),
                mediumfont.render("are still in then that player is considered checkmated.", True, dark_wood)]
        rules15 = [helpfontbold.render('15.', True, dark_wood), mediumfont.render("If there are only two players during a stalemate then the game is a draw", True, dark_wood),
                mediumfont.render("otherwise the game continues until only one player remains.", True, dark_wood)]

        screen.blit(rules10[0], (100-rules10[0].get_width()/2, 125-rules10[0].get_height()/2))
        screen.blit(rules10[1], (120, 125-rules10[0].get_height()/2))
        screen.blit(rules10[2], (120, 150-rules10[0].get_height()/2))

        screen.blit(rules11[0], (100-rules11[0].get_width()/2, 190-rules11[0].get_height()/2))
        screen.blit(rules11[1], (120, 190-rules11[0].get_height()/2))
        screen.blit(rules11[2], (120, 215-rules11[0].get_height()/2))

        screen.blit(rules12[0], (100-rules12[0].get_width()/2, 255-rules12[0].get_height()/2))
        screen.blit(rules12[1], (120, 255-rules12[0].get_height()/2))
        screen.blit(rules12[2], (120, 280-rules12[0].get_height()/2))

        screen.blit(rules13[0], (100-rules13[0].get_width()/2, 320-rules13[0].get_height()/2))
        screen.blit(rules13[1], (120, 320-rules13[0].get_height()/2))
        screen.blit(rules13[2], (120, 345-rules13[0].get_height()/2))

        screen.blit(rules14[0], (100-rules14[0].get_width()/2, 385-rules14[0].get_height()/2))
        screen.blit(rules14[1], (120, 385-rules14[0].get_height()/2))
        screen.blit(rules14[2], (120, 410-rules14[0].get_height()/2))

        screen.blit(rules15[0], (100-rules15[0].get_width()/2, 450-rules15[0].get_height()/2))
        screen.blit(rules15[1], (120, 450-rules15[0].get_height()/2))
        screen.blit(rules15[2], (120, 475-rules15[0].get_height()/2))

        if next_rules_backbutton:
            next_rules_running = False
            return True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()
        clock.tick(15)

def rules():
    rules_running = True
    while rules_running:
        screen.fill(ceramic)
        rules_backbutton = create_button(x=7, y=7, width=80, height=26, hovercolor=light_wood, defaultcolor=dark_wood, msg="Back")
        next_button = create_button(x=713, y=7, width=80, height=26, hovercolor=light_wood, defaultcolor=dark_wood, msg="Next")
    
        if next_button:
            next_rules()

        # pygame.draw.line(screen, (255, 0, 0), (0, 125), (screen_width, 125), 3)
       # pygame.draw.line(screen, (255, 0, 0), (0, 190), (screen_width, 190), 3)

       # pygame.draw.line(screen, (255, 0, 0), (100, 0), (100, screen_height), 3)
       # pygame.draw.line(screen, (255, 0, 0), (120, 0), (120, screen_height), 3)
       # pygame.draw.line(screen, (255, 0, 0), (700, 0), (700, screen_height), 3)
        
        rules1 = [helpfontbold.render('1.', True, dark_wood), mediumfont.render('The object of the game is to checkmate both opponents kings.', True, dark_wood)]

        rules2 = [helpfontbold.render('2.', True, dark_wood), mediumfont.render('The center of the board may be passed through. It is not a space', True, dark_wood), 
                mediumfont.render('that can be occupied. Pieces may move straight to the other side.', True, dark_wood)]

        rules3 = [helpfontbold.render('3.', True, dark_wood), mediumfont.render('To move a piece diagonally through the center follow the trajectory', True, dark_wood), 
                mediumfont.render('lines out from the square to the other side.', True, dark_wood)]

        rules4 = [helpfontbold.render('4.', True, dark_wood), mediumfont.render('Knights can move two squares vertically then one square horizont-', True, dark_wood), 
                mediumfont.render('ally or one square vertically then two squares horizontally.', True, dark_wood)]

        rules5 = [helpfontbold.render('5.', True, dark_wood), mediumfont.render('Moats are the thick green lines that border each team on the outer', True, dark_wood), 
                mediumfont.render("row. No piece can check an opponent's king through a moat.", True, dark_wood)]

        rules6 = [helpfontbold.render('6.', True, dark_wood), mediumfont.render('No piece may travel across a moat horizontally or diagonally unless', True, dark_wood), 
                mediumfont.render('the moat is bridged. ', True, dark_wood)]

        rules7 = [helpfontbold.render('7.', True, dark_wood), mediumfont.render("A piece may momentarily bridge a moat if its move doesn't result in", True, dark_wood), 
                mediumfont.render("the capture of a piece or puts an opponent's king in check.", True, dark_wood)]

        rules8 = [helpfontbold.render('8.', True, dark_wood), mediumfont.render('If a player is eliminated then both of its moats are permanently', True, dark_wood), 
                mediumfont.render('bridged for all pieces.', True, dark_wood)]

        rules9 = [helpfontbold.render('9.', True, dark_wood), mediumfont.render('Once an active player vacates their outer row, even if they bring p-', True, dark_wood), 
                mediumfont.render('ieces back later then their moats are also permanently bridged.', True, dark_wood)]

        screen.blit(rules1[0], (100-rules1[0].get_width()/2, 125-rules1[0].get_height()/2))
        screen.blit(rules1[1], (120, 125-rules1[0].get_height()/2))
    
        screen.blit(rules2[0], (100-rules2[0].get_width()/2, 190-rules2[0].get_height()/2))
        screen.blit(rules2[1], (120, 190-rules2[0].get_height()/2))
        screen.blit(rules2[2], (120, 215-rules2[0].get_height()/2))

        screen.blit(rules3[0], (100-rules3[0].get_width()/2, 255-rules3[0].get_height()/2))
        screen.blit(rules3[1], (120, 255-rules3[0].get_height()/2))
        screen.blit(rules3[2], (120, 280-rules3[0].get_height()/2))

        screen.blit(rules4[0], (100-rules4[0].get_width()/2, 320-rules4[0].get_height()/2))
        screen.blit(rules4[1], (120, 320-rules4[0].get_height()/2))
        screen.blit(rules4[2], (120, 345-rules4[0].get_height()/2))

        screen.blit(rules5[0], (100-rules5[0].get_width()/2, 385-rules5[0].get_height()/2))
        screen.blit(rules5[1], (120, 385-rules5[0].get_height()/2))
        screen.blit(rules5[2], (120, 410-rules5[0].get_height()/2))

        screen.blit(rules6[0], (100-rules6[0].get_width()/2, 450-rules6[0].get_height()/2))
        screen.blit(rules6[1], (120, 450-rules6[0].get_height()/2))
        screen.blit(rules6[2], (120, 475-rules6[0].get_height()/2))

        screen.blit(rules7[0], (100-rules7[0].get_width()/2, 515-rules7[0].get_height()/2))
        screen.blit(rules7[1], (120, 515-rules7[0].get_height()/2))
        screen.blit(rules7[2], (120, 540-rules7[0].get_height()/2))

        screen.blit(rules8[0], (100-rules8[0].get_width()/2, 580-rules8[0].get_height()/2))
        screen.blit(rules8[1], (120, 580-rules8[0].get_height()/2))
        screen.blit(rules8[2], (120, 605-rules8[0].get_height()/2))

        screen.blit(rules9[0], (100-rules9[0].get_width()/2, 645-rules9[0].get_height()/2))
        screen.blit(rules9[1], (120, 645-rules9[0].get_height()/2))
        screen.blit(rules9[2], (120, 670-rules9[0].get_height()/2))
        

        if rules_backbutton:
            rules_running = False
            return True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()
        clock.tick(15)

def game():
    game_running = True
    while game_running:
        screen.fill(ceramic)
        game_backbutton = create_button(x=7, y=7, width=80, height=26, hovercolor=light_wood, defaultcolor=dark_wood, msg="Back")
        if game_backbutton:
            game_running = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(players)
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(15)


def menu():
    running = True
    player1, player2, player3 = "", "", ""
    player1_NameActive, player2_NameActive, player3_NameActive = False, False, False

    while running:
        back = False
        screen.fill(ceramic)
        screen.blit(king_b, (600-(king_w.get_width()//2), 65))
        screen.blit(king_g, (600-(king_w.get_width()//2), 275))
        screen.blit(king_w, (600-(king_w.get_width()//2), 495))


        backbutton = create_button(x=7, y=7, width=80, height=26, hovercolor=light_wood, defaultcolor=dark_wood, msg="Back")
        helpbutton = create_button(x=713, y=767, width=80, height=26, hovercolor=blue_wood, defaultcolor=help_wood, msg="Rules")    
        playbutton = create_button(x=713, y=7, width=80, height=26, hovercolor=light_wood, defaultcolor=dark_wood, msg="Play")

        if helpbutton == True:
            back = rules()
        
        elif backbutton == True and back == False:
            running=False
        
        elif playbutton == True:
            game()

        player1Surface = mediumfontbold.render(player1, True, another_dark_wood)
        player1Border = pygame.Rect(((500 - player1Surface.get_width()) / 2)-5, screen_height * .10 - 10, player1Surface.get_width() + 10, 50)

        player2Surface = mediumfontbold.render(player2, True, another_dark_wood)
        player2Border = pygame.Rect(((500 - player2Surface.get_width()) / 2)-5, 290, player2Surface.get_width()+10, 50)

        player3Surface = mediumfontbold.render(player3, True, another_dark_wood)
        player3Border = pygame.Rect(((500 - player3Surface.get_width()) / 2)-5, 510, player3Surface.get_width()+10, 50)

        screen.blit(player1Surface, (int((500 - player1Surface.get_width()) / 2),int(screen_height * .10)))
        screen.blit(player2Surface, (int((500 - player2Surface.get_width()) / 2), 290+10))
        screen.blit(player3Surface, (int((500 - player3Surface.get_width()) / 2), 510+10))

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

        screen.blit(player1Prompt, ((500 - player1Prompt.get_width())/2, (screen_height * .10) + player1Prompt.get_height()))
        screen.blit(player2Prompt, ((500 - player2Prompt.get_width())/2, 10 + 290 + player2Prompt.get_height()))   
        screen.blit(player3Prompt, ((500 - player3Prompt.get_width())/2, 10 + 510 + player3Prompt.get_height()))

        pygame.display.update()
        clock.tick(15)

def start_menu():
    startText = titlefont.render("Chess Game", True, navy_blue)
    credit = [creditfont.render("Made by: ", True, credit_color), creditfont.render("Ashesh Mishra", True, credit_color),creditfont.render("Riddhiman Sengupta", True, credit_color), 
                creditfont.render("Rachit Kumar", True, credit_color), creditfont.render("Soham Chakraborty", True, credit_color)]
    
    x = mediumfontbold.render("Made by: ", True, white)
    while True: 
        screen.fill(ceramic)
        screen.blit(startText, ((screen_width - startText.get_width()) / 2, 0))
        
        startbutton = create_button(x=250, y=282.5, width=300, height=100, hovercolor=light_wood, defaultcolor=dark_wood, msg="Start")
        leavebutton = create_button(x=337.5, y=435, width=125, height=50, hovercolor=lightred_wood, defaultcolor=dark_wood, msg="Leave") 
    
        screen.blit(credit[1], (160-credit[1].get_width()/2, 782))
        screen.blit(credit[2], (160-credit[2].get_width()/2 + 160, 782))
        screen.blit(credit[3], (160-credit[3].get_width()/2 + 320, 782))
        screen.blit(credit[4], (160-credit[4].get_width()/2 + 480, 782))

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
