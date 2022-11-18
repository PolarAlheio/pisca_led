#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# mapeamento das portas
bt1, bt2, led = 2, 3, 4
botoes = [bt1, bt2]

# configuração das portas
GPIO.setup(botoes, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT, initial = 1)

# variável de controle
bit = True

# função
def invertBit():
    global bit
    
    bit = not bit
  
# eventos nos botões
GPIO.add_event_detect(bt1, GPIO.RISING, callback = invertBit(), bouncetime = 200)

GPIO.add_event_detect(bt2, GPIO.RISING, bouncetime = 200)


try:
    while True:
        if bit:
            GPIO.output(led, 1)
            time.sleep(0.5)
            GPIO.output(led, 0)
            time.sleep(0.5)
            
        else:
            GPIO.output(led, 1)
            time.sleep(0.2)
            
except GPIO.event_detected(bt2):
    pass

time.sleep(0.1)
GPIO.output(led, 0)
GPIO.cleanup()