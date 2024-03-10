import pygame
import math

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Moja gra")

# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)
BIALY = (255, 255, 255)
CZARNY = (0, 0, 0)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #białe tło
    win.fill(BIALY)

    #czarna obwódka

    grubosc_obwodki = 5
    pygame.draw.rect(win, CZARNY, (0, 0, 500, grubosc_obwodki))
    pygame.draw.rect(win, CZARNY, (0, 0, grubosc_obwodki, 500))
    pygame.draw.rect(win, CZARNY, (495, 0, grubosc_obwodki, 500))
    pygame.draw.rect(win, CZARNY, (0, 495, 500, grubosc_obwodki))


    # Rysowanie prostokąta
    szerokosc_prostokata = 120
    wysokosc_prostokata = 60
    x_środek = (500 - szerokosc_prostokata) // 2
    y_środek = (500 - wysokosc_prostokata) // 2

    pygame.draw.rect(win, NIEBIESKI, (x_środek, y_środek, szerokosc_prostokata, wysokosc_prostokata))

    # Rysowanie dolnego trójkąta
    srodek_x = 250
    srodek_y = 315
    dlugosc_boku = 120
    wysokosc_trójkąta = dlugosc_boku * math.sqrt(3) / 2

    x1 = srodek_x - dlugosc_boku / 2
    y1 = srodek_y + (math.sqrt(3) / 2) * dlugosc_boku / 3
    x2 = srodek_x + dlugosc_boku / 2
    y2 = y1
    x3 = srodek_x
    y3 = srodek_y - ((math.sqrt(3) / 2) * dlugosc_boku / 3)

    punkty = [(x1, y1), (x2, y2), (x3, y3)]
    pygame.draw.polygon(win, NIEBIESKI, punkty)

    # Rysowanie górnego trójkąta
    srodek_x2 = 250
    srodek_y2 = 185
    dlugosc_boku2 = 120

    ax1 = srodek_x2 - dlugosc_boku2 / 2
    ay1 = srodek_y2 - (math.sqrt(3) / 2) * dlugosc_boku2 / 3
    ax2 = srodek_x2 + dlugosc_boku2 / 2
    ay2 = ay1
    ax3 = srodek_x2
    ay3 = srodek_y2 + ((math.sqrt(3) / 2) * dlugosc_boku2 / 3)

    punkty = [(ax1, ay1), (ax2, ay2), (ax3, ay3)]
    pygame.draw.polygon(win, NIEBIESKI, punkty)











    pygame.display.update()