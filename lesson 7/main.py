import random
import pgzrun
from time import time

HEIGHT = 600
WIDTH = 800

satellites = []
number_of_satellite = 8
next_satellite = 0

lines = []

start_time = 0
total_time = 0
end_time = 0

def create_satellite():
    global start_time
    for i in range(number_of_satellite):
        satellite = Actor("sat")
        satellite.pos = random.randint (50,750), random.randint (50,550)
        satellites.append(satellite)
    start_time = time()
create_satellite()

def draw():
    global total_time
    screen.blit("space",(0,0))
    number = 1
    for satellite in satellites:
        satellite.draw()
        screen.draw.text(str(number),(satellite.pos[0], satellite.pos[1]+20))
        number = number + 1

def update():
    pass

















pgzrun.go()
       
