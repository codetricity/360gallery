import pygame, sys
import requests
import json
from thetapylib import *

WHITE = (255,255,255)
GRAY = (230, 230, 230)
GREEN = (100, 200, 50)
DARK = (64, 64, 64)


pygame.init()
SCREENSIZE = (300, 600)
SCREEN = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("THETA S Unofficial Hacking Guide Example")

font = pygame.font.Font("fnt/Lato-Bold.ttf", 20)

phoneFrame = pygame.image.load("icon/phone.png")
headerText = font.render("Kaiyotesoft A-Frame", True, DARK)
headerBox = headerText.get_rect(topleft=(34,120))
descriptionText = font.render("     THETA Photo Taker", True, DARK)
descriptionBox = headerText.get_rect(topleft=(34,148))

mainRoomIcon = pygame.image.load("icon/main-room.png")
mainRoomButton = mainRoomIcon.get_rect(topleft=(100,220))

room2Icon = pygame.image.load("icon/room-2.png")
room2Button = mainRoomIcon.get_rect(topleft=(100,320))

room3Icon = pygame.image.load("icon/room-3.png")
room3Button = mainRoomIcon.get_rect(topleft=(100,420))

sid = "SID_0001"
room = "main"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mainRoomButton.collidepoint(mouse_pos):
                sid = startSession()
                takePicture(sid)
                #wait 8 seconds as picture is processed
                pygame.time.delay(8000)
                fileUri = latestFileUri()
                realEstateMain(fileUri, room)
            if room2Button.collidepoint(mouse_pos):
                sid = startSession()
                takePicture(sid)
                #wait 8 seconds as picture is processed
                pygame.time.delay(8000)
                fileUri = latestFileUri()
                realEstateMain(fileUri, "room2")

            if room3Button.collidepoint(mouse_pos):
                sid = startSession()
                takePicture(sid)
                #wait 8 seconds as picture is processed
                pygame.time.delay(8000)
                fileUri = latestFileUri()
                realEstateMain(fileUri, "room3")


    SCREEN.fill(WHITE) # blank out screen

    SCREEN.blit(phoneFrame, (0,0))
    SCREEN.blit(headerText, headerBox)
    SCREEN.blit(descriptionText, descriptionBox)
    # draw take picture button
    SCREEN.blit(mainRoomIcon, mainRoomButton)
    SCREEN.blit(room2Icon, room2Button)
    SCREEN.blit(room3Icon, room3Button)

    pygame.display.update()
