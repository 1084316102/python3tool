# -*- coding:utf-8 -*- 
import pygame
import sys
import time
import random
from pygame.locals import *
import os

directory = 'C:\\Users\\xietong\\Downloads\\PythonSuperMario-master\\PythonSuperMario-master\\resources\\graphics'
pic = 'level_1.png'
pygame.init()
fc = pygame.time.Clock()
playSuface = pygame.display.set_mode((640,480))
pygame.display.set_caption('ttt')
image = pygame.image.load('C:\\Users\\xietong\\Desktop\\111\\game.ico')
pygame.display.set_icon(image)
# img = pygame.image.load(os.path.join(directory, pic))

while True:
	img = pygame.image.load(os.path.join(directory, pic))
	print(1)