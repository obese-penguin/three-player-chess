from PIL import Image
import pygame
import numpy as np

rot = 16
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

c=[[[519.98, 415.69], [569.56, 422.17], [619.14, 428.65], [668.71, 435.13], [718.29, 441.61], [767.87, 448.09]], [[511.84, 446.19], [558.05, 465.28], [604.26, 484.36], [650.48, 503.45], [696.69, 522.54], [742.91, 541.62]], [[496.08, 473.55], [535.78, 503.94], [575.49, 534.33], [615.19, 564.72], [654.89, 595.12], [694.6, 625.51]], [[473.78, 495.9], [504.27, 535.53], [534.76, 575.16], [565.25, 614.78], [595.74, 654.41], [626.23, 694.04]], [[446.46, 511.72], [465.66, 557.89], [484.87, 604.06], [504.07, 650.22], [523.27, 696.39], [542.47, 742.56]], [[415.98, 519.94], [422.58, 569.5], [429.19, 619.06], [435.79, 668.63], [442.4, 718.19], [449.0, 767.75]], [[384.41, 519.99], [377.97, 569.57], [371.53, 619.16], [365.08, 668.74], [358.64, 718.32], [352.2, 767.91]], [[353.9, 511.87], [334.85, 558.1], [315.8, 604.33], [296.75, 650.56], [277.7, 696.79], [258.65, 743.02]], [[326.53, 496.14], [296.17, 535.87], [265.81, 575.59], [235.45, 615.32], [205.09, 655.05], [174.73, 694.78]], [[304.16, 473.86], [264.55, 504.38], [224.95, 534.9], [185.35, 565.42], [145.74, 595.95], [106.14, 626.47]], [[288.31, 446.55], [242.16, 465.79], [196.01, 485.03], [149.86, 504.26], [103.71, 523.5], [57.56, 542.74]], [[280.07, 416.08], [230.52, 422.72], [180.96, 429.36], [131.4, 436.01], [81.85, 442.65], [32.29, 449.29]], [[280.0, 384.51], [230.41, 378.1], [180.82, 371.7], [131.23, 365.3], [81.64, 358.89], [32.05, 352.49]], [[288.09, 353.99], [241.85, 334.98], [195.6, 315.96], [149.36, 296.95], [103.11, 277.94], [56.87, 258.92]], [[303.8, 326.6], [264.05, 296.28], [224.3, 265.95], [184.55, 235.62], [144.8, 205.29], [105.04, 174.96]], [[326.06, 304.22], [295.51, 264.64], [264.96, 225.06], [234.4, 185.48], [203.85, 145.9], [173.3, 106.32]], [[353.36, 288.35], [334.08, 242.22], [314.81, 196.08], [295.54, 149.94], [276.26, 103.81], [256.99, 57.67]], [[383.83, 280.09]
, [377.15, 230.53], [370.46, 180.98], [363.78, 131.43], [357.1, 81.88], [350.41, 32.33]], [[415.4, 279.98], [421.76, 230.39], [428.13, 180.8], [434.49, 131.2], [440.85, 81.61], [447.22, 32.02]], [[445.92, 288.05], [464.9, 241.79], [483.87, 195.53], [502.85, 149.28], [521.83, 103.02], [540.8, 56.76]], [[473.32, 303.74], [503.62, 263.97], [533.91, 224.19], [564.21, 184.42], [594.51, 144.64], [624.8, 104.87]], [[495.72, 325.99], [535.28, 295.4], [574.83, 264.82],
 [614.39, 234.23], [653.94, 203.65], [693.5, 173.07]], [[511.61, 353.27], [557.73, 333.96], [603.85, 314.65], [649.97, 295.34], [696.09, 276.03], [742.21, 256.72]], [[519.9, 383.73], [569.45, 377.01], [618.99, 370.29], [668.54, 363.57], [718.09, 356.84], [767.63, 350.12]]]


class Piece(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image

        self.rect = self.image.get_rect()
        self.rect.center = (c[x][y][0], c[x][y][1])


r_b_R = Piece(r_b,(2+rot)%24,5)
n_b_R = Piece(n_b,(3+rot)%24,5)
b_b_R = Piece(b_b,(4+rot)%24,5)
k_b_O = Piece(k_b,(6+rot)%24,5)
q_b_O = Piece(q_b,(5+rot)%24,5)
b_b_L = Piece(b_b,(7+rot)%24,5)
n_b_L = Piece(n_b,(8+rot)%24,5)
r_b_L = Piece(r_b,(9+rot)%24,5)
p_b_1 = Piece(p_b,(2+rot)%24,4)
p_b_2 = Piece(p_b,(3+rot)%24,4)
p_b_3 = Piece(p_b,(4+rot)%24,4)
p_b_4 = Piece(p_b,(5+rot)%24,4)
p_b_5 = Piece(p_b,(6+rot)%24,4)
p_b_6 = Piece(p_b,(7+rot)%24,4)
p_b_7 = Piece(p_b,(8+rot)%24,4)
p_b_8 = Piece(p_b,(9+rot)%24,4)


r_g_R = Piece(r_g,(10+rot)%24,5)
n_g_R = Piece(n_g,(11+rot)%24,5)
b_g_R = Piece(b_g,(12+rot)%24,5)
k_g_O = Piece(k_g,(13+rot)%24,5)
q_g_O = Piece(q_g,(14+rot)%24,5)
b_g_L = Piece(b_g,(15+rot)%24,5)
n_g_L = Piece(n_g,(16+rot)%24,5)
r_g_L = Piece(r_g,(17+rot)%24,5)
p_g_1 = Piece(p_g,(10+rot)%24,4)
p_g_2 = Piece(p_g,(11+rot)%24,4)
p_g_3 = Piece(p_g,(12+rot)%24,4)
p_g_4 = Piece(p_g,(13+rot)%24,4)
p_g_5 = Piece(p_g,(14+rot)%24,4)
p_g_6 = Piece(p_g,(15+rot)%24,4)
p_g_7 = Piece(p_g,(16+rot)%24,4)
p_g_8 = Piece(p_g,(17+rot)%24,4)


r_w_R = Piece(r_w,(18+rot)%24,5)
n_w_R = Piece(n_w,(19+rot)%24,5)
b_w_R = Piece(b_w,(20+rot)%24,5)
k_w_O = Piece(k_w,(21+rot)%24,5)
q_w_O = Piece(q_w,(22+rot)%24,5)
b_w_L = Piece(b_w,(23+rot)%24,5)
n_w_L = Piece(n_w,(0+rot)%24,5)
r_w_L = Piece(r_w,(1+rot)%24,5)
p_w_1 = Piece(p_w,(18+rot)%24,4)
p_w_2 = Piece(p_w,(19+rot)%24,4)
p_w_3 = Piece(p_w,(20+rot)%24,4)
p_w_4 = Piece(p_w,(21+rot)%24,4)
p_w_5 = Piece(p_w,(22+rot)%24,4)
p_w_6 = Piece(p_w,(23+rot)%24,4)
p_w_7 = Piece(p_w,(0+rot)%24,4)
p_w_8 = Piece(p_w,(1+rot)%24,4)

# format is r,n,b,k,q,b,n,r,p--
Bpiece = [[2,5],[3,5],[4,5],[5,5],[6,5],[7,5],[8,5],[9,5],[2,4],[3,4],[4,4],[5,4],[6,4],[7,4],[8,4],[9,4]]
Gpiece =[[10,5],[11,5],[12,5],[13,5],[14,5],[15,5],[16,5],[17,5],[10,4],[11,4],[12,4],[13,4],[14,4],[15,4],[16,4],[17,4]]
Wpiece = [[18,5],[19,5],[20,5],[21,5],[22,5],[23,5],[0,5],[1,5],[18,4],[19,4],[20,4],[21,4],[22,4],[23,4],[0,4],[1,4]]
pieces = [r_b_R,n_b_R,b_b_R,k_b_O,q_b_O,r_b_L,n_b_L,b_b_L,r_g_R,n_g_R,b_g_R,k_g_O,q_g_O,b_g_L,n_g_L,r_g_L,r_w_R,n_w_R,b_w_R,k_w_O,q_w_O,b_w_L,n_w_L,r_w_L,p_b_1,p_b_2,p_b_3,p_b_4,p_b_5,p_b_6,p_b_7,p_b_8,p_g_1,p_g_2,p_g_3,p_g_4,p_g_5,p_g_6,p_g_7,p_g_8,p_w_1,p_w_2,p_w_3,p_w_4,p_w_5,p_w_6,p_w_7,p_w_8,]

size = 25, 25


pygame.init()
white = (255, 255, 255)

X = 800
Y = 800

display_surface = pygame.display.set_mode((X, Y ))

pygame.display.set_caption('Image')
path = 'assets/chessboard.jpeg'

image = pygame.image.load(path)



while True :

    display_surface.fill(white)
    display_surface.blit(image, (0, 0))
    all_sprites = pygame.sprite.Group()
    for piece in pieces:
        all_sprites.add(piece)
    all_sprites.draw(display_surface)
    x, y = pygame.mouse.get_pos()
    r = round(np.sqrt((x-400)**2 + (y-400)**2),2)
    ang = round(np.arctan2(y-400, x-400),2)
    d = int(abs((r-96))//50)
    coordangle = int((ang*57.2)//15)
    if coordangle<0:
        coordangle = 24+coordangle

    print(coordangle,d,x,y)

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
        pygame.display.update()
