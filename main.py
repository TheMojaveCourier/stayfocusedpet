from __future__ import print_function
import datetime
from time import time, sleep
import win32gui
import json
from enum import  auto
import pygame
from pygame.locals import *
import os
pygame.init()

active_window_name = ""
activity_name = ""
start_time = datetime.datetime.now()
first_time = True
health = 0
counter = 0
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
width = WIN.get_width()
height = WIN.get_height()
pygame.display.set_caption("Stay Focused Pet")

FPS = 60
scale1 = 80
scale2 = 80
points_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
health_message = font.render("Your pet is in Danger", True, (255,255,0))
Shop_message = font.render("You don't have enough points", True, (255,255,0))

Backround = pygame.image.load(os.path.join('Assets', 'backround.png'))
Shop_backround = pygame.image.load(os.path.join('Assets', 'shop_backround.png'))
Dog_young = pygame.image.load(os.path.join('Assets', 'dog_baby.png'))
Dog_adult = pygame.image.load(os.path.join('Assets', 'dog_adult.png'))
Dog_young_eyes = pygame.image.load(os.path.join('Assets', 'baby_eyes_close.png'))
Shop_icon = pygame.image.load(os.path.join('Assets', 'shop_icon.png'))
Shop_icon_scale = pygame.transform.scale(Shop_icon, (scale1, scale2))
Point_icon = pygame.image.load(os.path.join('Assets', 'point_icon.png'))
Point_icon_scale = pygame.transform.scale(Point_icon, (scale1, scale2))
Point_number_0 = pygame.image.load(os.path.join('Assets', 'point_number_0.png'))
Point_number_0_scale = pygame.transform.scale(Point_number_0, (scale1, scale2))
Point_number_1 = pygame.image.load(os.path.join('Assets', 'point_number_1.png'))
Point_number_1_scale = pygame.transform.scale(Point_number_1, (scale1, scale2))
Back_button = pygame.image.load(os.path.join('Assets', 'back_button.png'))
Doge_card = pygame.image.load(os.path.join('Assets', 'doge_shop_card.png'))
Doge_card_scale = pygame.transform.scale(Doge_card, (256, 310))
Doge = pygame.image.load(os.path.join('Assets', 'doge.png'))
Doge_scale = pygame.transform.scale(Doge, (200,250))



def show_points():

    points = font.render("Points :" + str(points_value), True, (255,255,0))
    WIN.blit(points, (0, 0))


def draw_window(keys, Bought, Dogemode):
    WIN.blit(Backround, (0, 0))
    if counter == 100:
        if Dogemode:
            WIN.blit(Doge_scale, (250,260))
        else:
            WIN.blit(Dog_adult, (250, 260))

    else:
        WIN.blit(Dog_young, (250, 260))
    show_points()
    if Bought:
        WIN.blit(font.render("Press D for Doge Mode", True, (0,0,0)), (0, 50))
    if health <= 0:
        WIN.blit(font.render("Your Pet has died", True, (255, 0, 0)), (0, 50))



    if keys:
        WIN.blit(Shop_backround, (0, 0))
        WIN.blit(Back_button, (700, 5))
        WIN.blit(Doge_card_scale, (50, 100))
        WIN.blit(Point_number_1_scale, (300, 150))
        WIN.blit(Point_number_0_scale, (350, 150))
        WIN.blit(Point_number_0_scale, (410, 150))
        WIN.blit(Point_number_0_scale, (470, 150))
        WIN.blit(Point_icon_scale, (550, 150))
        if counter < 100:
            WIN.blit(font.render("Pet not old enough", True, (0, 0, 0)), (350, 350))

        if Bought == False:
            WIN.blit(font.render("Press B to Buy", True, (0,0,0)), (350, 300))
        else:
            WIN.blit(font.render("Already bought", True, (0,0,0)), (350, 300))


    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    Dogemode = False
    Bought = False
    run = True
    keys = False
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_s:
                    keys = True
                elif event.key == K_TAB:
                    keys = False
                elif event.key == K_ESCAPE:
                    run = False
                elif event.key == K_b:
                    if points_value > 1000 or counter > 100:
                        Bought = True
                        Dogemode = True

        draw_window(keys, Bought, Dogemode)

    pygame.quit()

main()
global activeList, new_window_name,TimeEntry


def url_to_name(url):
    string_list = url.split('/')
    return string_list[2]


def get_active_window():
    _active_window_name = None
    window = win32gui.GetForegroundWindow()
    _active_window_name = win32gui.GetWindowText(window)
    return _active_window_name


def get_chrome_url():
    window = win32gui.GetForegroundWindow()
    chromeControl = auto.ControlFromHandle(window)
    edit = chromeControl.EditControl()
    return 'https://' + edit.GetValuePattern().Value

try:
    activeList.initialize_me()
except Exception:
    print('Den yparxei json file')

try:
    while True:
        previous_site =""
        new_window_name = get_active_window()
        if 'Google Chrome' in new_window_name:
            new_window_name = url_to_name(get_chrome_url())


        if active_window_name != new_window_name:
           print(active_window_name)
           activity_name = active_window_name
           points_value += 100
           health += 100
           counter += 5

           if not first_time:
              end_time = datetime.datetime.now()
              time_entry = TimeEntry(start_time,end_time,0,0,0,0)
              time_entry._get_specific_times()
              health -=  50

              exists = False
              for activity in activeList.activities:
                  if activity.name == activity_name:
                    exists =True
                    activity.time_entries.append(time_entry)

              if not exists:
                activity = activity(activity_name,[time_entry])
                activeList.activities.append(activity)
              with open('data.json','w') as json_file:
                json.dump(activeList.serialize(),json_file,
                          indent=4, sort_keys=True)
                start_ti,e = datetime.datetime.now()
        first_time = False
        active_window_name = new_window_name
        sleep(1)

except KeyboardInterrupt:
    with open('data.json', 'w') as json_file:
        json.dump(activeList.serialize(), json_file, indent=4, sort_keys=True)
