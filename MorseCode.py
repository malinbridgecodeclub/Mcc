from gpiozero import Buzzer, Button
from time import sleep, time
import urllib2

buzzer = Buzzer(22)
button = Button(4)

beep_start = 0
beep_stop = 0
pause_start = 0
pause_stop = 0

buzzer.off()

def start_buzzing():
        global beep_start
        global pause_start
        global pause_stop
        beep_start = time()
        pause_stop = time()
        pause_length = pause_stop - pause_start
        print("Start: %.1f" % (beep_start))
        print("Pause length: %.3f" % (pause_length))
        buzzer.on()


def stop_buzzing():
        global beep_start
        global pause_start
        beep_stop = time()
        pause_start = time()
        beep_length = beep_stop - beep_start
        print("Length: %.1f" % (beep_length))
        if beep_length > 0 and beep_length < 0.3:
                print(".")
                #urllib2.urlopen("http://morsecode.local/send.php?symbol=dot").read()
        elif beep_length >= 0.3:
                print("-")
                #urllib2.urlopen("http://morsecode.local/send.php?symbol=dash").read()
        buzzer.off()

while True:
        button.when_pressed = start_buzzing
        button.when_released = stop_buzzing

