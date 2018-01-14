#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from ev3dev.ev3 import *
from time import sleep

def run_motor_timed():
    m = LargeMotor('outC')
    duration = 5000
    increm = 500. / 1000
    m.run_timed(time_sp=duration, speed_sp=300)
    print("set speed (speed_sp) = " + str(m.speed_sp))
    for i in range(int(duration / (increm * 1000))):
        print("actual speed = " + str(m.speed))
        sleep(increm)  # it takes a moment for the motor to start moving

def run_motor_1():
    m = LargeMotor('outC')
    m.run_timed(time_sp=3000, speed_sp=300)
    Sound.beep()

def run_motor_2():
    m = LargeMotor('outC')
    m.run_timed(time_sp=3000, speed_sp=300)
    m.wait_while('running')
    Sound.beep()

#run_motor_timed()
run_motor_1()
