# 9 am - 5pm
# water - water.mp3 (3.5liter) drank log every 40 min
# eyes - eyes.mp3 - every 30 min - eydone - log- every 30 min(
# physical activities - physical.mp3 every - 45 min - exdone- log
# rules
# pygame module to play mixer
from pygame import mixer
from datetime import datetime
from time import time
def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def log_now(ms):
    with open("mylogs.txt","a") as f:
        f.write(f"{ms} {datetime.now()}\n")



if __name__ == '__main__':

    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 20
    exsecs= 10
    eyessecs = 5


    while True:
        if time()- init_water >watersecs:
            print("water drinking time. enter 'drank'to stop the alam")
            musiconloop('water.mp3','drank')
            init_water = time()
            log_now("drank water at")
        if time()- init_eyes >eyessecs:
            print("eye drinking time. enter 'done'to stop the alam")
            musiconloop('eyes.mp3','done')
            init_eyes = time()
            log_now("eyes relaxed at")
        if time()- init_exercise >exsecs:
            print("physical activity time. enter 'done'to stop the alam")
            musiconloop('water.mp3','done')
            init_exercise = time()
            log_now("physical activity at")







