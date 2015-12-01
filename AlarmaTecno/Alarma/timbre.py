#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Edgar Arturo Haas Pacheco
# @Date:   2015-10-05 ‏‎‏‎4:08:24
from __future__ import absolute_import
from time import sleep
from datetime import datetime
from celery import task
# import RPi.GPIO as GPIO

# def setup():
#     GPIO.setmode(GPIO.BOARD)
#     GPIO.setup(16, GPIO.OUT)
#     GPIO.setup(11, GPIO.OUT)
#     GPIO.setup(13, GPIO.OUT)
#     GPIO.setup(15, GPIO.OUT)
#     GPIO.output(11, GPIO.LOW)
#     GPIO.output(13, GPIO.LOW)
#     GPIO.output(15, GPIO.LOW)
#     GPIO.setup(16, GPIO.LOW)


# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(16, GPIO.OUT)
# GPIO.setup(11, GPIO.OUT)
# GPIO.setup(13, GPIO.OUT)
# GPIO.setup(15, GPIO.OUT)
# GPIO.output(11, GPIO.LOW)
# GPIO.output(13, GPIO.LOW)
# GPIO.output(15, GPIO.LOW)
# GPIO.setup(16, GPIO.LOW)

def estado(states):
    # setup()
    tiempo = str(datetime.now())
    if states == 1:
        # GPIO.output(11, GPIO.HIGH)
        sleep(5)
        # GPIO.output(11, GPIO.LOW)
        print "1"

    elif states == 2:
        # GPIO.output(13, GPIO.HIGH)
        for tiempo in range(0, 25):
            # GPIO.output(11, GPIO.HIGH)
            sleep(0.5)
            # GPIO.output(11, GPIO.LOW)
            sleep(0.2)
        # GPIO.output(13, GPIO.LOW)
        print "2"
        sleep(50)

    elif states == 3:
        # GPIO.output(15, GPIO.HIGH)
        print "Foco escendido"

    elif states == 4:
        # GPIO.output(15, GPIO.LOW)
        print "Foco Apagado"

    print("%s: pressed B1" % datetime.now(), states)
    # GPIO.cleanup()
    log(tiempo, states)


def log(tiempo, timbre):
    archivo_log = open("Log.txt", "a")
    archivo_log.write("Alarma tocada "+str(tiempo)+" y la alarma fue la numero: "+str(timbre) + "\n")
    archivo_log.close()


@task
def control():
    print "1"
    # GPIO.output(16, GPIO.HIGH)
    sleep(0.2)
    # GPIO.output(16, GPIO.LOW)
    sleep(0.5)
    print "funciona"
