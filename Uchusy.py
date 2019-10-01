# coding: utf-8
"""
Использование графического модуля graph.py.
GR_SIMPLE - простые программы
  (C) К. Поляков, 2017
  e-mail: kpolyakov@mail.ru
  web: http://kpolyakov.spb.ru
"""

from graph import *
from random import *
import random as rm
import math

# Программа рисующая картинку лошади с окружающим фоном

tt = 0 # переменная отвечающая за время. До 100 яблоки падают, после оного они катятся по земле

#рисует дерево
def Tree():
	penColor(150,90,50)
	penSize(1)
	brushColor(150,90,50)
	rectangle(50, 350, 70, 420)
	penColor(0,100,0)
	penSize(1)
	brushColor(0,100,0)
	polygon([(60, 100), (80, 105), (95, 120), (102, 130), (110, 170), (105, 190), (100, 200), (120, 205), (135, 220), (148, 235), (150, 250), (145, 265), (135, 280), (115, 295), (100, 300), (103, 305), (105, 320), (100, 336), (90, 350), (75,366), (60, 370), (45,366), (30, 350), (22, 339), (15, 320), (17, 305), (20, 300), (0, 285), (0, 215), (20, 200), (15, 190), (10, 170), (18, 130), (25, 120), (40, 105)])
	penColor(255,100,100)
	penSize(1)
	brushColor(255,100,100)

#sets compleat color of your pen
def color(x):
    penColor(x)
    brushColor(x)

#Tree-fractal function
def tker(x,y,N, N0, alpha,l,q,delta, obj):
    if N==0:
        return
    if N >= N0 - 3:
        color("brown")
    else:
        color("green")
    penSize(N*1.5)
    rnd_l = rm.uniform(0.97, 1.04)
    rnd_a = rm.uniform(0.95 +0.04, 1.05 - 0.04)
    alpha*=rnd_a
    rnd_d = rm.uniform(0.95 +0.05, 1.05 - 0.05)
    delta*=rnd_d
    obj.append(line(x,y,x+l*math.cos(alpha),y+l*math.sin(alpha)))
    tker(x+l*math.cos(alpha),y+l*math.sin(alpha),N-1, N0, alpha+delta,q*l*rnd_l,q,delta, obj)
    tker(x+l*math.cos(alpha),y+l*math.sin(alpha),N-1, N0, alpha-delta,q*l*rnd_l,q,delta, obj)
    tker(x+l*math.cos(alpha),y+l*math.sin(alpha),N-1, N0, alpha,q*l*rnd_l,q,delta, obj)


#Draws a tree
def FrTree(x, y, l, N, q, obj):
    for i in obj:
        deleteObject(i)
    color("green")
    tker(x, y ,N, N, -math.pi/2, l ,q,math.pi*0.2, obj)


#Отвечает за падение яблок
def ApplesFall():
    global tt
    if tt<100:
        moveObjectBy(App1, 0, randint(0, 2)+tt//25-1)
        moveObjectBy(App2, 0, randint(0, 2)+tt//25)
        moveObjectBy(App3, 0, randint(0, 2)+tt//25)
        moveObjectBy(App4, 0, randint(0, 2)+tt//25+1)
    tt=tt+1

#Отвечает за качение  яблок по земле
def ApplesJump():
	global tt
	if tt>100:
		moveObjectBy(App1, 2, randint(-1, 1)+tt%13-5)
		moveObjectBy(App2, 2, randint(-1, 1)+tt%15-6)
		moveObjectBy(App3, 2, randint(-1, 1)+tt%17-7)
		moveObjectBy(App4, 2, randint(-1, 1)+tt%19-8)

#Фон
def Background():
	penColor(0,255,0)
	penSize(1)
	brushColor(0,255,0)
	rectangle(0, 300, 500, 600)

	penColor(200,200,255)
	penSize(1)
	brushColor(200,200,255)
	rectangle(0, 0, 500, 300)

	penColor(255,255,0)
	penSize(1)
	brushColor(255,255,0)
	circle(470, 50, 80)

#Лошадь
def horse():
	penColor(250,250,255)
	penSize(1)
	brushColor(250,250,255)
	rectangle(300, 400, 310, 470)
	rectangle(400, 400, 410, 470)
	rectangle(320, 390, 330, 460)
	rectangle(420, 390, 430, 460)
	polygon([(360, 335), (400, 335), (420, 345), (440, 375), (430, 395), (420, 405), (390, 415), (360, 420), (330, 415), (300, 405), (290, 395), (280, 375), (300, 345)])
	rectangle(400, 310, 440, 375)
	polygon([(400, 310), (430, 290), (460, 290), (470, 295), (477, 310), (470, 325), (460, 330), (440, 335)])

	penColor(180,180,255)
	penSize(1)
	brushColor(180,180,255)
	polygon([(450, 290), (470, 250), (460, 290)])
	penColor(150,150,255)
	penSize(1)
	brushColor(150,150,255)
	circle(450, 305, 6)
	penColor(0,0,0)
	penSize(1)
	brushColor(0,0,0)
	circle(451, 304, 3)

#Грива рисуется отдельно, чтобы переливалась
def fur():
	i=randint(1, 300)
	penSize(5)
	if i%3==0:
		penColor(randint(150, 255), 150, 150)
		A1=line(390, 336, 360, 333)
		penColor(150, randint(150, 255), 150)
		A2=line(403, 333, 378, 335)
		penColor(100, 100, randint(150, 255))
		A3=line(407, 320, 362, 325)
		penColor(randint(150, 255), 150, 150)
		A4=line(403, 325, 365, 332)
		penColor(150, randint(150, 255), 150)
		A5=line(404, 315, 370, 318)
		penColor(100, 100, randint(150, 255))
		A6=line(411, 310, 374, 312)
		penColor(randint(150, 255), 150, 150)
		A7=line(425, 302, 372, 308)
		penColor(150, randint(150, 255), 150)
		A8=line(440, 296, 381, 301)
		penColor(100, 100, randint(150, 255))
		A9=line(444, 290, 399, 294)
	if i%3==1:
		penColor(100, 100, randint(150, 255))
		A1=line(390, 336, 360, 333)
		penColor(randint(150, 255), 150, 150)
		A2=line(403, 333, 378, 335)
		penColor(150, randint(150, 255), 150)
		A3=line(407, 320, 362, 325)
		penColor(100, 100, randint(150, 255))
		A4=line(403, 325, 365, 332)
		penColor(randint(150, 255), 150, 150)
		A5=line(404, 315, 370, 318)
		penColor(150, randint(150, 255), 150)
		A6=line(411, 310, 374, 312)
		penColor(100, 100, randint(150, 255))
		A7=line(425, 302, 372, 308)
		penColor(randint(150, 255), 150, 150)
		A8=line(440, 296, 381, 301)
		penColor(150, randint(150, 255), 150)
		A9=line(444, 290, 399, 294)
	if i%3==2:
		penColor(150, randint(150, 255), 150)
		A1=line(390, 336, 360, 333)
		penColor(100, 100, randint(150, 255))
		A2=line(403, 333, 378, 335)
		penColor(randint(150, 255), 150, 150)
		A3=line(407, 320, 362, 325)
		penColor(150, randint(150, 255), 150)
		A4=line(403, 325, 365, 332)
		penColor(100, 100, randint(150, 255))
		A5=line(404, 315, 370, 318)
		penColor(randint(150, 255), 150, 150)
		A6=line(411, 310, 374, 312)
		penColor(150, randint(150, 255), 150)
		A7=line(425, 302, 372, 308)
		penColor(100, 100, randint(150, 255))
		A8=line(440, 296, 381, 301)
		penColor(randint(150, 255), 150, 150)
		A9=line(444, 290, 399, 294)

	penSize(5)
	penColor(randint(150, 255), randint(150, 255), randint(150, 255))
	B1=line(310, 340, 280, 360)
	penColor(randint(150, 255), randint(150, 255), randint(150, 255))
	B2=line(280, 375, 250, 410)
	penColor(randint(150, 255), randint(150, 255), randint(150, 255))
	B3=line(285, 370, 255, 410)
	penColor(randint(150, 255), randint(150, 255), randint(150, 255))
	B4=line(285, 380, 255, 420)
	penColor(randint(150, 255), randint(150, 255), randint(150, 255))
	B5=line(300, 345, 265, 380)
	penColor(randint(150, 255), randint(150, 255), randint(150, 255))
	B6=line(275, 400, 230, 440)
	penColor(randint(150, 255), randint(150, 255), randint(150, 255))
	B7=line(280, 410, 220, 445)
	penColor(randint(150, 255), randint(150, 255), randint(150, 255))
	B8=line(265, 425, 230, 430)
	penColor(randint(150, 255), randint(150, 255), randint(150, 255))
	B9=line(310, 340, 280, 360)
	penColor(randint(150, 255), randint(150, 255), randint(150, 255))
	B10=line(260, 430, 220, 445)
	penColor(randint(150, 255), randint(150, 255), randint(150, 255))
	B11=line(265, 380, 230, 430)
	penColor(randint(150, 255), randint(150, 255), randint(150, 255))
	B12=line(285, 350, 250, 400)
	penColor(randint(150, 255), randint(150, 255), randint(150, 255))
	B13=line(265, 395, 230, 420)
	penColor(randint(150, 255), randint(150, 255), randint(150, 255))
	B14=line(270, 395, 225, 430)

def frtree():

    FrTree(60, 420, 100, 8, 0.7, tree)

Background()
horse()
fur()
#Tree()
color('red')
App1=circle(75, 335, 15)
App2=circle(15, 255, 15)
App3=circle(130, 250, 15)
App4=circle(70, 130, 15)
tree = []
onTimer(fur, 100)
onTimer(ApplesFall, 10)
onTimer(ApplesJump, 30)
onTimer(frtree, 50)
run()
