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
smallfont = pygame.font.SysFont("arial", 14)
bold = pygame.font.SysFont("arial", 40, bold=True)
smallfontbold = pygame.font.SysFont("arial", 20, bold=True)
ceramic = (225,186,133)
navy_blue = (14,42,65)
white = (255, 255, 255)
dark_wood = (139,69,19)
light_wood = (160,82,45)
lightred_wood = (220, 20, 60)
darkred_wood = (187, 10, 31)
green_wood = (119,109,22)

def create_button(x, y, width, height, hovercolor, defaultcolor, msg):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed(3)
    
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, hovercolor, (x, y, width, height), border_top_left_radius = 3, border_top_right_radius = 3, border_bottom_left_radius = 3, border_bottom_right_radius=3)
        if click[0] == 1:
            return True
    else:
        pygame.draw.rect(screen, defaultcolor, (x, y, width, height),  border_top_left_radius = 3, border_top_right_radius = 3, border_bottom_left_radius = 3, border_bottom_right_radius=3)
    if msg == "Start":
        buttontext = bold.render(msg, True, white)
        screen.blit(buttontext, (int((screen_width - buttontext.get_width()) / 2), 315))
    elif msg == "Leave":
        buttontext = smallfontbold.render(msg, True, white)
        screen.blit(buttontext, (int((screen_width - buttontext.get_width()) / 2), 450))
    
def start_menu():
    startText = titlefont.render("Chess Game", True, navy_blue)
    smallText = smallfont.render("Good Game", True, ceramic)
    pygame.draw.line(screen, (255, 0, 0), (screen_width//2, 0), (screen_width//2, screen_height), 50)
     
    while True: 
        screen.fill(ceramic)
        screen.blit(startText, ((screen_width - startText.get_width()) / 2, 0))
        
        startbutton = create_button(x=250, y=282.5, width=300, height=100, hovercolor=light_wood, defaultcolor=dark_wood, msg="Start")
        leavebutton = create_button(x=337.5, y=435, width=125, height=50, hovercolor=lightred_wood, defaultcolor=dark_wood, msg="Leave") 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        clock.tick(15)
        return True

while True:
    start_menu()    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

    clock.tick(15)
