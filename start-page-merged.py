import sys, pygame, time
import numpy as np

pygame.init()

clock = pygame.time.Clock()

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("chess game")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

startpageicon = pygame.image.load('assets/resized-start-page-icon.png')

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

pygame.mixer.init()

pygame.mixer.music.load('assets/button_switch_on.ogg')
pygame.mixer.music.set_volume(0.5)

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
move = 0
cut_pieces = [0,0,0]
rot = (move % 3) * 8
#ghost = pygame.image.load('assets/transparent.png')
r_b = pygame.image.load('assets/rook-b.png')
n_b = pygame.image.load('assets/knight-b.png')
b_b = pygame.image.load('assets/bishop-b.png')
k_b = pygame.image.load('assets/king-b.png')
q_b = pygame.image.load('assets/queen-b.png')
p_b = pygame.image.load('assets/pawn-b.png')

r_w = pygame.image.load('assets/rook-w.png')
n_w = pygame.image.load('assets/knight-w.png')
b_w = pygame.image.load('assets/bishop-w.png')
k_w = pygame.image.load('assets/king-w.png')
q_w = pygame.image.load('assets/queen-w.png')
p_w = pygame.image.load('assets/pawn-w.png')

r_g = pygame.image.load('assets/rook-g.png')
n_g = pygame.image.load('assets/knight-g.png')
b_g = pygame.image.load('assets/bishop-g.png')
k_g = pygame.image.load('assets/king-g.png')
q_g = pygame.image.load('assets/queen-g.png')
p_g = pygame.image.load('assets/pawn-g.png')

c = [[[519.98, 415.69], [569.56, 422.17], [619.14, 428.65], [668.71, 435.13], [718.29, 441.61], [767.87, 448.09]],
     [[511.84, 446.19], [558.05, 465.28], [604.26, 484.36], [650.48, 503.45], [696.69, 522.54], [742.91, 541.62]],
     [[496.08, 473.55], [535.78, 503.94], [575.49, 534.33], [615.19, 564.72], [654.89, 595.12], [694.6, 625.51]],
     [[473.78, 495.9], [504.27, 535.53], [534.76, 575.16], [565.25, 614.78], [595.74, 654.41], [626.23, 694.04]],
     [[446.46, 511.72], [465.66, 557.89], [484.87, 604.06], [504.07, 650.22], [523.27, 696.39], [542.47, 742.56]],
     [[415.98, 519.94], [422.58, 569.5], [429.19, 619.06], [435.79, 668.63], [442.4, 718.19], [449.0, 767.75]],
     [[384.41, 519.99], [377.97, 569.57], [371.53, 619.16], [365.08, 668.74], [358.64, 718.32], [352.2, 767.91]],
     [[353.9, 511.87], [334.85, 558.1], [315.8, 604.33], [296.75, 650.56], [277.7, 696.79], [258.65, 743.02]],
     [[326.53, 496.14], [296.17, 535.87], [265.81, 575.59], [235.45, 615.32], [205.09, 655.05], [174.73, 694.78]],
     [[304.16, 473.86], [264.55, 504.38], [224.95, 534.9], [185.35, 565.42], [145.74, 595.95], [106.14, 626.47]],
     [[288.31, 446.55], [242.16, 465.79], [196.01, 485.03], [149.86, 504.26], [103.71, 523.5], [57.56, 542.74]],
     [[280.07, 416.08], [230.52, 422.72], [180.96, 429.36], [131.4, 436.01], [81.85, 442.65], [32.29, 449.29]],
     [[280.0, 384.51], [230.41, 378.1], [180.82, 371.7], [131.23, 365.3], [81.64, 358.89], [32.05, 352.49]],
     [[288.09, 353.99], [241.85, 334.98], [195.6, 315.96], [149.36, 296.95], [103.11, 277.94], [56.87, 258.92]],
     [[303.8, 326.6], [264.05, 296.28], [224.3, 265.95], [184.55, 235.62], [144.8, 205.29], [105.04, 174.96]],
     [[326.06, 304.22], [295.51, 264.64], [264.96, 225.06], [234.4, 185.48], [203.85, 145.9], [173.3, 106.32]],
     [[353.36, 288.35], [334.08, 242.22], [314.81, 196.08], [295.54, 149.94], [276.26, 103.81], [256.99, 57.67]],
     [[383.83, 280.09]
         , [377.15, 230.53], [370.46, 180.98], [363.78, 131.43], [357.1, 81.88], [350.41, 32.33]],
     [[415.4, 279.98], [421.76, 230.39], [428.13, 180.8], [434.49, 131.2], [440.85, 81.61], [447.22, 32.02]],
     [[445.92, 288.05], [464.9, 241.79], [483.87, 195.53], [502.85, 149.28], [521.83, 103.02], [540.8, 56.76]],
     [[473.32, 303.74], [503.62, 263.97], [533.91, 224.19], [564.21, 184.42], [594.51, 144.64], [624.8, 104.87]],
     [[495.72, 325.99], [535.28, 295.4], [574.83, 264.82],
      [614.39, 234.23], [653.94, 203.65], [693.5, 173.07]],
     [[511.61, 353.27], [557.73, 333.96], [603.85, 314.65], [649.97, 295.34], [696.09, 276.03], [742.21, 256.72]],
     [[519.9, 383.73], [569.45, 377.01], [618.99, 370.29], [668.54, 363.57], [718.09, 356.84], [767.63, 350.12]]]

colour_list = ["white", "grey", "black","dead"]
rank_list = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king',"dead"]


def possible_king(selection):
    a = []
    for i in range(3):
        for j in range(3):
            pos_a = (selection.a + (i - 1)) % 24
            pos_r = (selection.r+(j-1))
            if pos_r<=5 and not [pos_a,pos_r] == [selection.a,selection.r]:
                    a.append([pos_a,pos_r])
    return a
def possible_rook(selection):
    a = []
    b = []
    for i in range(24):
        if [(selection.a + i + 1) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4],
                                                         [10, 4],
                                                         [18, 4], [2, 5], [10, 5], [18, 5]] and [
            (selection.a + i + 2) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4],
                                                         [10, 4],
                                                         [18, 4], [2, 5], [10, 5], [18, 5]]:
            break
        b.append([(selection.a+i+1)%24, selection.r])
    a.append(b)
    b = []
    for i in range(24):
        if [(selection.a + i + 1) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4],
                                                         [10, 4],
                                                         [18, 4], [2, 5], [10, 5], [18, 5]] and [
            (selection.a + i + 2) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4],
                                                         [10, 4],
                                                         [18, 4], [2, 5], [10, 5], [18, 5]]:
            break
        b.append([(selection.a-i-1)%24, selection.r])
    a.append(b)
    b = []
    for i in range(6-selection.r):
        b.append([(selection.a), selection.r+i])
    a.append(b)
    b = []
    for i in range(selection.r):
        b.append([selection.a,selection.r-i])
    for i in range(6):
        b.append([(selection.a+12)%24,i])
    a.append(b)
    b = []
    return a
def possible_bishop(selection):
    a = []
    b = []
    for i in range(selection.r+1):
        if [(selection.a + i + 1) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4],
                                                         [10, 4],
                                                         [18, 4], [2, 5], [10, 5], [18, 5]] and [
            (selection.a + i + 2) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4],
                                                         [10, 4],
                                                         [18, 4], [2, 5], [10, 5], [18, 5]]:
            break
        b.append([(selection.a+i)%24,selection.r-i])
    for i in range(6):
        if [(selection.a + i + 1) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4],
                                                         [10, 4],
                                                         [18, 4], [2, 5], [10, 5], [18, 5]] and [
            (selection.a + i + 2) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4],
                                                         [10, 4],
                                                         [18, 4], [2, 5], [10, 5], [18, 5]]:
            break
        b.append([(selection.a+10+i)%24,i])
    a.append(b)
    b = []

    for i in range(6-selection.r):
        if [(selection.a + i + 1) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4],
                                                         [10, 4],
                                                         [18, 4], [2, 5], [10, 5], [18, 5]] and [
            (selection.a + i + 2) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4],
                                                         [10, 4],
                                                         [18, 4], [2, 5], [10, 5], [18, 5]]:
            break
        b.append([(selection.a+i)%24,selection.r+i])
    a.append(b)
    b = []

    for i in range(selection.r+1):
        if [(selection.a + i + 1) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4],
                                                         [10, 4],
                                                         [18, 4], [2, 5], [10, 5], [18, 5]] and [
            (selection.a + i + 2) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4],
                                                         [10, 4],
                                                         [18, 4], [2, 5], [10, 5], [18, 5]]:
            break
        b.append([(selection.a-i)%24,selection.r-i])
    for i in range(6):
        if [(selection.a + i + 1) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4],
                                                         [10, 4],
                                                         [18, 4], [2, 5], [10, 5], [18, 5]] and [
            (selection.a + i + 2) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4],
                                                         [10, 4],
                                                         [18, 4], [2, 5], [10, 5], [18, 5]]:
            break
        b.append([(selection.a+14+i)%24,i])
    a.append(b)
    b = []

    for i in range(6-selection.r):
        if [(selection.a + i + 1) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4],
                                                         [10, 4],
                                                         [18, 4], [2, 5], [10, 5], [18, 5]] and [
            (selection.a + i + 2) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4],
                                                         [10, 4],
                                                         [18, 4], [2, 5], [10, 5], [18, 5]]:
            break
        b.append([(selection.a-i)%24,selection.r+i])
    a.append(b)
    b = []
    return a
def possible_queen(selection):
    a = []
    b = []
    for i in range(24):
        b.append([(selection.a+i+1)%24, selection.r])
        if [(selection.a + i + 1) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4], [10, 4],
                                                [18, 4], [2, 5], [10, 5], [18, 5]] and  [(selection.a + i + 2) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4], [10, 4],
                                                [18, 4], [2, 5], [10, 5], [18, 5]]:
            break
    a.append(b)

    b = []
    for i in range(24):
        if [(selection.a + i + 1) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4],
                                                         [10, 4],
                                                         [18, 4], [2, 5], [10, 5], [18, 5]] and [
            (selection.a + i + 2) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4],
                                                         [10, 4],
                                                         [18, 4], [2, 5], [10, 5], [18, 5]]:
            break
        b.append([(selection.a-i-1)%24, selection.r])
    a.append(b)
    b = []
    for i in range(6-selection.r):
        b.append([(selection.a), selection.r+i])
    a.append(b)
    b = []
    for i in range(selection.r):
        b.append([selection.a,selection.r-i])
    for i in range(6):
        b.append([(selection.a+12)%24,i])
    a.append(b)
    b = []
    for i in range(selection.r+1):
        if [(selection.a + i + 1) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4],
                                                         [10, 4],
                                                         [18, 4], [2, 5], [10, 5], [18, 5]] and [
            (selection.a + i + 2) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4],
                                                         [10, 4],
                                                         [18, 4], [2, 5], [10, 5], [18, 5]]:
            break
        b.append([(selection.a+i)%24,selection.r-i])
    for i in range(6):
        if [(selection.a + i + 1) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4],
                                                         [10, 4],
                                                         [18, 4], [2, 5], [10, 5], [18, 5]] and [
            (selection.a + i + 2) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4],
                                                         [10, 4],
                                                         [18, 4], [2, 5], [10, 5], [18, 5]]:
            break
        b.append([(selection.a+10+i)%24,i])
    a.append(b)
    b = []

    for i in range(6-selection.r):
        if [(selection.a + i + 1) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4],
                                                         [10, 4],
                                                         [18, 4], [2, 5], [10, 5], [18, 5]] and [
            (selection.a + i + 2) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4],
                                                         [10, 4],
                                                         [18, 4], [2, 5], [10, 5], [18, 5]]:
            break
        b.append([(selection.a+i)%24,selection.r+i])
    a.append(b)
    b = []

    for i in range(selection.r+1):
        if [(selection.a + i + 1) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4],
                                                         [10, 4],
                                                         [18, 4], [2, 5], [10, 5], [18, 5]] and [
            (selection.a + i + 2) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4],
                                                         [10, 4],
                                                         [18, 4], [2, 5], [10, 5], [18, 5]]:
            break
        b.append([(selection.a-i)%24,selection.r-i])
    for i in range(6):
        if [(selection.a + i + 1) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4],
                                                         [10, 4],
                                                         [18, 4], [2, 5], [10, 5], [18, 5]] and [
            (selection.a + i + 2) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4],
                                                         [10, 4],
                                                         [18, 4], [2, 5], [10, 5], [18, 5]]:
            break
        b.append([(selection.a+14+i)%24,i])
    a.append(b)
    b = []

    for i in range(6-selection.r):
        if [(selection.a + i + 1) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4],
                                                         [10, 4],
                                                         [18, 4], [2, 5], [10, 5], [18, 5]] and [
            (selection.a + i + 2) % 24, selection.r] in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4],
                                                         [10, 4],
                                                         [18, 4], [2, 5], [10, 5], [18, 5]]:
            break
        b.append([(selection.a-i)%24,selection.r+i])
    a.append(b)
    b = []
    return a

def possible_knight(selection):
    a = []
    if not selection.r == 0 and not selection.r == 1:
        for i in range(2):
            for j in range(2):
                pos_a = (selection.a + (i*2)-1)%24
                pos_r = selection.r + 2*(j*2 - 1)
                if pos_r <= 5:
                    a.append([pos_a,pos_r])

        for i in range(2):
            for j in range(2):
                pos_a = (selection.a + 2*((i*2)-1))%24
                pos_r = selection.r + (j*2 - 1)
                if pos_r<=5:
                    a.append([pos_a,pos_r])
    if selection.r == 1 :
        for i in range(2):
            for j in range(2):
                pos_a = (selection.a + 2 * ((i * 2) - 1)) % 24
                pos_r = selection.r + (j * 2 - 1)
                a.append([pos_a, pos_r])

        a.append([(selection.a+11)%24 , 0])
        a.append([(selection.a + 13)%24, 0])
    if selection.r == 0:
        a.append([(selection.a+10)%24,0])
        a.append([(selection.a+14)%24,0])
        a.append([(selection.a+11)%24,1])
        a.append([(selection.a + 9) % 24, 1])

        for i in range(2):
                pos_a = (selection.a + (i*2)-1)%24
                pos_r = selection.r + 2
                if pos_r <= 5:
                    a.append([pos_a,pos_r])

        for i in range(2):
                pos_a = (selection.a + 2*((i*2)-1))%24
                pos_r = selection.r + 1
                if pos_r <= 5:
                    a.append([pos_a,pos_r])



    return a


def possible_pawn(selection):
    a = []
    cuttable = []
    #print(selection.pawncenter)
    if selection.moved == 0 :
        a.append([selection.a,selection.r-1])
        a.append([selection.a, selection.r - 2])
        cuttable.append([(selection.a-1)%24,selection.r-1])
        cuttable.append([(selection.a + 1)%24, selection.r-1])
    if selection.moved == 1 :
        if selection.pawncenter==0:
            a.append([selection.a,selection.r-1])
            cuttable.append([(selection.a - 1)%24, selection.r - 1])
            cuttable.append([(selection.a + 1)%24, selection.r - 1])
        if selection.pawncenter == 1:
            a.append([(selection.a+12)%24,0])
            cuttable.append([(selection.a+13)%24 , 0])
            cuttable.append([(selection.a+11)%24 , 0])
        if selection.pawncenter == 2:
            if selection.r+1<=6:
                a.append([selection.a, selection.r + 1])
                cuttable.append([(selection.a - 1)%24, selection.r + 1])
                cuttable.append([(selection.a + 1)%24, selection.r + 1])
    #print([a,cuttable])
    return [a,cuttable]

class Piece(pygame.sprite.Sprite):
    def __init__(self, image, a, r, colour, rank,moved,pawncenter,piece_index):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.a = a
        self.r = r
        self.rect = self.image.get_rect()
        self.rect.center = (c[a][r][0], c[a][r][1])
        self.colour = colour
        self.rank = rank
        self.piece_index = piece_index
        if rank==0:
            self.moved = moved
            self.pawncenter = pawncenter
        if rank == 5:
            self.moved = moved


    def eliminate(self):
        if self.rank == 5:
            print("dead",colour_list[self.colour])
            lost_pieces = [s for s in pieces if s.colour == self.colour]
            for i in range(len(lost_pieces)):
                lost_pieces[i].rank = 6
        self.rank = 6
        self.r = 0
        self.a = 0
        self.rect.center = (850 + 40 * ((cut_pieces[self.colour]) % 6),
                            50 + round((800 * self.colour) / 3 - (50 * ((cut_pieces[self.colour]) // 6))))
        cut_pieces[self.colour] += 1

    def control_linear(self, a, r,path):
        original_coord = [self.a, self.r]
        touch_sprites = []
        if [a, r] in path:
            print("index=",path.index([a,r]))
            for j in range(path.index([a,r])+1):
                    print("j=",j)
                    touch_sprites.append([s for s in pieces if [s.a,s.r]==path[j] and not s==self])
                    if path.index([a,r])== j:
                        print("reached")
                        if not touch_sprites[j]:
                            print("e happened")
                            self.rect.center = (c[a][r][0], c[a][r][1])
                            self.a = a
                            self.r = r
                        elif not touch_sprites[j][0].colour == self.colour and [touch_sprites[j][0].a,touch_sprites[j][0].r] not in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4], [10, 4],
                                                [18, 4], [2, 5], [10, 5], [18, 5]]:
                            print("b happened")
                            touch_sprites[j][0].eliminate()
                            self.rect.center = (c[a][r][0], c[a][r][1])
                            self.a = a
                            self.r = r
                            break
                    elif not touch_sprites[j]:
                        print("e happened")
                    elif touch_sprites[j][0].colour == self.colour:
                        show_text("illegal move")
                        break

                    elif not touch_sprites[j][0].colour == self.colour:
                        show_text("illegal move")
                        break

        else:
            print("d happened")

        for i in range(len(touch_sprites)):
            for j in range(len(touch_sprites[i])):
                print(touch_sprites[i][j].rank,touch_sprites[i][j].colour)


    def control(self, a, r):
        touch_sprites = [s for s in pieces if s.rect.collidepoint(c[coordangle][d])]
        if not touch_sprites == []:
            for i in range(len(touch_sprites)):
                if touch_sprites[i].colour ==(self.colour+1)%3 or touch_sprites[i].colour == (self.colour+2)%3:
                    if self.rect.center in [[1, 4], [9, 4], [17, 4], [1, 5], [9, 5], [17, 5], [2, 4], [10, 4],
                                                [18, 4], [2, 5], [10, 5], [18, 5]] or [a, r] in [[1, 4], [9, 4],
                                                                                                      [17, 4], [1, 5],
                                                                                                      [9, 5], [17, 5],
                                                                                                      [2, 4], [10, 4],
                                                                                                      [18, 4], [2, 5],
                                                                                                      [10, 5], [18, 5]]:
                        print("blocked")
                    else:
                        touch_sprites[i].eliminate()
                        self.rect.center = (c[a][r][0], c[a][r][1])
                        print("cut")
                        self.r = r
                        self.a = a

        if not touch_sprites:
            self.rect.center = (c[a][r][0], c[a][r][1])
            self.r = r
            self.a = a

    def move_pawn(self,selection,a,r):


        #blockable
        for i in range(len(selection)):
            touched_sprites2 = [s for s in pieces if [s.a,s.r] == [a,r]]

        if not touched_sprites2 and [a,r] in selection:
            self.rect.center = (c[a][r][0], c[a][r][1])
            self.a = a
            self.r = r


    def cut_pawn(self,selection,a,r):
        for i in range(len(selection)):
            touched_sprites = [s for s in pieces if (s.a,s.r)==(a,r) ]
            print(selection[i][0],selection[i][1])
        #finalisation
        for i in range(len(touched_sprites)):
            print(touched_sprites)
            print(i, "cuttable")
        for j in range(2):
            if [a,r] == [touched_sprites[i].a,touched_sprites[i].r]:
                if not touched_sprites[i].colour == self.colour:
                    touched_sprites[i].eliminate()
                    print("eliminated")
                    self.rect.center = (c[a][r][0], c[a][r][1])
                    self.r = r
                    self.a = a
    def get_rank(self):
        return rank_list[self.rank]


r_b_R = Piece(r_b, (2 + rot) % 24, 5, 2, 3,0,0,0)
n_b_R = Piece(n_b, (3 + rot) % 24, 5, 2, 1,0,0,1)
b_b_R = Piece(b_b, (4 + rot) % 24, 5, 2, 2,0,0,2)
k_b_O = Piece(k_b, (6 + rot) % 24, 5, 2, 5,0,0,3)
q_b_O = Piece(q_b, (5 + rot) % 24, 5, 2, 4,0,0,4)
b_b_L = Piece(b_b, (7 + rot) % 24, 5, 2, 2,0,0,5)
n_b_L = Piece(n_b, (8 + rot) % 24, 5, 2, 1,0,0,6)
r_b_L = Piece(r_b, (9 + rot) % 24, 5, 2, 3,0,0,7)
p_b_1 = Piece(p_b, (2 + rot) % 24, 4, 2, 0,0,0,8)
p_b_2 = Piece(p_b, (3 + rot) % 24, 4, 2, 0,0,0,9)
p_b_3 = Piece(p_b, (4 + rot) % 24, 4, 2, 0,0,0,10)
p_b_4 = Piece(p_b, (5 + rot) % 24, 4, 2, 0,0,0,11)
p_b_5 = Piece(p_b, (6 + rot) % 24, 4, 2, 0,0,0,12)
p_b_6 = Piece(p_b, (7 + rot) % 24, 4, 2, 0,0,0,13)
p_b_7 = Piece(p_b, (8 + rot) % 24, 4, 2, 0,0,0,14)
p_b_8 = Piece(p_b, (9 + rot) % 24, 4, 2, 0,0,0,15)

r_g_R = Piece(r_g, (10 + rot) % 24, 5, 1, 3,0,0,0 )
n_g_R = Piece(n_g, (11 + rot) % 24, 5, 1, 1,0,0,1 )
b_g_R = Piece(b_g, (12 + rot) % 24, 5, 1, 2,0,0,2 )
k_g_O = Piece(k_g, (13 + rot) % 24, 5, 1, 5,0,0,3 )
q_g_O = Piece(q_g, (14 + rot) % 24, 5, 1, 4,0,0,4 )
b_g_L = Piece(b_g, (15 + rot) % 24, 5, 1, 2,0,0,5 )
n_g_L = Piece(n_g, (16 + rot) % 24, 5, 1, 1,0,0,6 )
r_g_L = Piece(r_g, (17 + rot) % 24, 5, 1, 3,0,0,7 )
p_g_1 = Piece(p_g, (10 + rot) % 24, 4, 1, 0,0,0,8 )
p_g_2 = Piece(p_g, (11 + rot) % 24, 4, 1, 0,0,0,9 )
p_g_3 = Piece(p_g, (12 + rot) % 24, 4, 1, 0,0,0,10 )
p_g_4 = Piece(p_g, (13 + rot) % 24, 4, 1, 0,0,0,11 )
p_g_5 = Piece(p_g, (14 + rot) % 24, 4, 1, 0,0,0,12 )
p_g_6 = Piece(p_g, (15 + rot) % 24, 4, 1, 0,0,0,13 )
p_g_7 = Piece(p_g, (16 + rot) % 24, 4, 1, 0,0,0,14 )
p_g_8 = Piece(p_g, (17 + rot) % 24, 4, 1, 0,0,0,15 )

r_w_R = Piece(r_w, (18 + rot) % 24, 5, 0, 3,0,0,0)
n_w_R = Piece(n_w, (19 + rot) % 24, 5, 0, 1,0,0,1)
b_w_R = Piece(b_w, (20 + rot) % 24, 5, 0, 2,0,0,2)
k_w_O = Piece(k_w, (21 + rot) % 24, 5, 0, 5,0,0,3)
q_w_O = Piece(q_w, (22 + rot) % 24, 5, 0, 4,0,0,4)
b_w_L = Piece(b_w, (23 + rot) % 24, 5, 0, 2,0,0,5)
n_w_L = Piece(n_w, (0 + rot) % 24, 5, 0, 1,0,0,6)
r_w_L = Piece(r_w, (1 + rot) % 24, 5, 0, 3,0,0,7)
p_w_1 = Piece(p_w, (18 + rot) % 24, 4, 0, 0,0,0,8)
p_w_2 = Piece(p_w, (19 + rot) % 24, 4, 0, 0,0,0,9)
p_w_3 = Piece(p_w, (20 + rot) % 24, 4, 0, 0,0,0,10)
p_w_4 = Piece(p_w, (21 + rot) % 24, 4, 0, 0,0,0,11)
p_w_5 = Piece(p_w, (22 + rot) % 24, 4, 0, 0,0,0,12)
p_w_6 = Piece(p_w, (23 + rot) % 24, 4, 0, 0,0,0,13)
p_w_7 = Piece(p_w, (0 + rot) % 24, 4, 0, 0,0,0,14)
p_w_8 = Piece(p_w, (1 + rot) % 24, 4, 0, 0,0,0,15)

# format is r,n,b,k,q,b,n,r,p--
Piece_index_list = [[[18, 5], [19, 5], [20, 5], [21, 5], [22, 5], [23, 5], [0, 5], [1, 5], [18, 4], [19, 4], [20, 4], [21, 4],
          [22, 4], [23, 4], [0, 4], [1, 4]],[[10, 5], [11, 5], [12, 5], [13, 5], [14, 5], [15, 5], [16, 5], [17, 5], [10, 4], [11, 4], [12, 4], [13, 4],
          [14, 4], [15, 4], [16, 4], [17, 4]],[[2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5], [9, 5], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4],
          [7, 4], [8, 4], [9, 4]]]
pieces = [r_b_R, n_b_R, b_b_R, k_b_O, q_b_O, r_b_L, n_b_L, b_b_L, r_g_R, n_g_R, b_g_R, k_g_O, q_g_O, b_g_L, n_g_L,
          r_g_L, r_w_R, n_w_R, b_w_R, k_w_O, q_w_O, b_w_L, n_w_L, r_w_L, p_b_1, p_b_2, p_b_3, p_b_4, p_b_5, p_b_6,
          p_b_7, p_b_8, p_g_1, p_g_2, p_g_3, p_g_4, p_g_5, p_g_6, p_g_7, p_g_8, p_w_1, p_w_2, p_w_3, p_w_4, p_w_5,
          p_w_6, p_w_7, p_w_8, ]

size = 25, 25

pygame.init()
white = (255, 255, 255)

X = 800
Y = 800

#display_surface = pygame.display.set_mode((X, Y))

pygame.display.set_caption('Image')
path = 'assets/chessboard.jpeg'

image = pygame.image.load(path)


def select_piece():
    pos = pygame.mouse.get_pos()
    clicked_sprites = [s for s in pieces if s.rect.collidepoint(pos)]
    # print(clicked_sprites[0])
    # if len(clicked_sprites == 1):
    #    return clicked_sprites[0]
    # print(clicked_sprites[0])
    return clicked_sprites[0]

def show_text(a):
    medium_font_bold = pygame.font.SysFont('arial', 25, bold=True)
    white_colour = (255,255,255)
    screen.blit(image, (0, 0))
    text = [medium_font_bold.render(a, True, white_colour)]

    screen.blit(text[0], (400 - text[0].get_width() / 2, 400 - text[0].get_height()))


players = []
def create_button(x, y, width, height, hovercolor, defaultcolor, msg, player1='', player2='', player3=''):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed(3)
    
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, hovercolor, (x, y, width, height), border_top_left_radius = 5, border_top_right_radius = 5,
                        border_bottom_left_radius = 5, border_bottom_right_radius = 5)
        if click[0] == 1:
            pygame.time.wait(150)
            pygame.mixer.music.play()
            if msg == "Enter":
                players.extend([player1, player2, player3])
            return True
    else:
        pygame.draw.rect(screen, defaultcolor, (x, y, width, height),  border_top_left_radius = 3, border_top_right_radius = 3,
                            border_bottom_left_radius = 3, border_bottom_right_radius=3)
    if msg == "Start":
        buttontext = bold.render(msg, True, white)
        screen.blit(buttontext, (int((screen.get_width() - buttontext.get_width()) / 2), 432.5))
    elif msg == "Leave":
        buttontext = smallfontbold.render(msg, True, white)
        screen.blit(buttontext, (int((screen.get_width() - buttontext.get_width()) / 2), 577.5-buttontext.get_height()/2))
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

        rules10 = [helpfontbold.render('10.', True, dark_wood), mediumfont.render("If either order of a knight's move would carry it horizontally across a", True, dark_wood),
                mediumfont.render("moat. Without that knight being able to bridge the moat then that", True, dark_wood), 
                mediumfont.render("move is illegal.", True, dark_wood)]

        rules11 = [helpfontbold.render('11.', True, dark_wood), mediumfont.render("A team's checkmate status is not finalized until it is their turn unless", True, dark_wood),
                mediumfont.render("their king is captured.", True, dark_wood)]
        rules12 = [helpfontbold.render('12.', True, dark_wood), mediumfont.render("When a player is checkmated that player is eliminated from the game", True, dark_wood),
                mediumfont.render("but all their pieces remain on the board these pieces do not move.", True, dark_wood)]
        rules13 = [helpfontbold.render('13.', True, dark_wood), mediumfont.render("If you wish to occupy a space with an eliminated player's piece on it", True, dark_wood),
                mediumfont.render("then you must capture that piece.", True, dark_wood)]
        rules14 = [helpfontbold.render('14.', True, dark_wood), mediumfont.render("If a player cannot make a legal move called a stalemate and three", True, dark_wood),
                mediumfont.render("players are still in then that player is considered checkmated.", True, dark_wood)]
        rules15 = [helpfontbold.render('15.', True, dark_wood), mediumfont.render("If there are only two players during a stalemate then the game is", True, dark_wood),
                mediumfont.render("a draw otherwise the game continues until only one player remains.", True, dark_wood)]

        screen.blit(rules10[0], (100-rules10[0].get_width()/2, 125-rules10[0].get_height()/2))
        screen.blit(rules10[1], (120, 125-rules10[0].get_height()/2))
        screen.blit(rules10[2], (120, 150-rules10[0].get_height()/2))
        screen.blit(rules10[3], (120, 175-rules10[0].get_height()/2))

        screen.blit(rules11[0], (100-rules11[0].get_width()/2, 215-rules11[0].get_height()/2))
        screen.blit(rules11[1], (120, 215-rules11[0].get_height()/2))
        screen.blit(rules11[2], (120, 240-rules11[0].get_height()/2))

        screen.blit(rules12[0], (100-rules12[0].get_width()/2, 280-rules12[0].get_height()/2))
        screen.blit(rules12[1], (120, 280-rules12[0].get_height()/2))
        screen.blit(rules12[2], (120, 305-rules12[0].get_height()/2))

        screen.blit(rules13[0], (100-rules13[0].get_width()/2, 345-rules13[0].get_height()/2))
        screen.blit(rules13[1], (120, 345-rules13[0].get_height()/2))
        screen.blit(rules13[2], (120, 370-rules13[0].get_height()/2))

        screen.blit(rules14[0], (100-rules14[0].get_width()/2, 410-rules14[0].get_height()/2))
        screen.blit(rules14[1], (120, 410-rules14[0].get_height()/2))
        screen.blit(rules14[2], (120, 435-rules14[0].get_height()/2))

        screen.blit(rules15[0], (100-rules15[0].get_width()/2, 475-rules15[0].get_height()/2))
        screen.blit(rules15[1], (120, 475-rules15[0].get_height()/2))
        screen.blit(rules15[2], (120, 500-rules15[0].get_height()/2))

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
    selected = False

    while game_running:
        screen.fill(ceramic)
        screen.fill(white)
        screen.blit(image, (0, 0))
        all_sprites = pygame.sprite.Group()
        for piece in pieces:
            all_sprites.add(piece)
        all_sprites.draw(screen)
        x, y = pygame.mouse.get_pos()
        r = round(np.sqrt((x - 400) ** 2 + (y - 400) ** 2), 2)
        ang = round(np.arctan2(y - 400, x - 400), 2)
        d = int(abs((r - 96)) // 50)
        coordangle = int((ang * 57.2) // 15)%24

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and not selected:
                try:
                    piece_selected = select_piece()

                    selected = True

                except:
                    selected = False

            elif event.type == pygame.MOUSEBUTTONDOWN and selected:
                if piece_selected.get_rank() == "rook" :
                    for i in range(len(possible_rook(piece_selected))):
                        if [coordangle,d] in possible_rook(piece_selected)[i]:
                            piece_selected.control_linear(coordangle, d,possible_rook(piece_selected)[i])
                if piece_selected.get_rank() == "bishop" :
                    for i in range(len(possible_bishop(piece_selected))):
                        if [coordangle,d] in possible_bishop(piece_selected)[i]:
                            piece_selected.control_linear(coordangle, d,possible_rook(piece_selected)[i])
                if piece_selected.get_rank() == "queen" :
                    for i in range(len(possible_queen(piece_selected))):
                        if [coordangle,d] in possible_queen(piece_selected)[i]:
                            piece_selected.control_linear(coordangle, d,possible_queen(piece_selected)[i])
                if piece_selected.get_rank() == "king" :
                    if [coordangle,d] in possible_king(piece_selected):
                        piece_selected.control(coordangle, d)
                    else:
                        show_text("illegal move")
                if piece_selected.get_rank() == "knight" :
                    if [coordangle,d] in possible_knight(piece_selected):
                        piece_selected.control(coordangle, d)
                    else:
                        show_text("illegal move")
                if piece_selected.get_rank() == "pawn":
                    if [coordangle,d] in possible_pawn(piece_selected)[0]:
                        piece_selected.move_pawn(possible_pawn(piece_selected)[0],coordangle, d)
                        piece_selected.moved = 1
                        if piece_selected.r == 0:
                            piece_selected.pawncenter +=1
                    elif [coordangle,d] in possible_pawn(piece_selected)[1]:
                        piece_selected.cut_pawn(possible_pawn(piece_selected)[1],coordangle, d)
                        piece_selected.moved = 1
                        if piece_selected.r == 0:
                            piece_selected.pawncenter +=1
                        if piece_selected.r == 5:
                            piece_selected.rank = 6
                            piece_selected.image = [s for s in pieces if s.colour==piece_selected.colour and piece_selected.rank==6][0].image
                        else: show_text("illegal move")


                selected = False

        game_backbutton = create_button(x=7, y=7, width=80, height=26, hovercolor=light_wood, defaultcolor=dark_wood, msg="Back")
        if game_backbutton:
            game_running = False

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
        screen.blit(startText, ((screen.get_width() - startText.get_width()) / 2, 0))
    
        screen.blit(startpageicon, ((screen.get_width() - 400)/2, 100))

        startbutton = create_button(x=(screen.get_width()-300)/2, y=400, width=300, height=100, hovercolor=light_wood, defaultcolor=dark_wood, msg="Start")
        leavebutton = create_button(x=(screen.get_width()-125)/2, y=552.5, width=125, height=50, hovercolor=lightred_wood, defaultcolor=dark_wood, msg="Leave") 
    
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
