#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ev3dev.ev3 import *
from time import sleep


mr = LargeMotor('outC')
ml = LargeMotor('outB')

def forward(distance, speed=300, stop_action="brake"):
    """Run robot on distance decimeters.

    Parameters
    ----------
    distance : float
        number of decimeters to move.
    speed : integer
        speed in motor unit (0-1000)
    stop_action : string
        the way motor stops, possible values: "brake", "hold" or "coast"
    """
    ONE_DECIMETER = 360/1.34
    rot = distance * ONE_DECIMETER
    mr.run_to_rel_pos(position_sp=rot, speed_sp=speed, stop_action=stop_action)
    ml.run_to_rel_pos(position_sp=rot, speed_sp=speed, stop_action=stop_action)

def turn(angle):
    """Turn robot a given angle.

    Parameters
    ----------
    angle : float
        angle (in degrees) to turn right (negative for turning left)
    """
    speed = 300
    stop_action = "brake"
    rot = angle * 360/133     #convertion angle rotation moteur en rotation robot
    mr.run_to_rel_pos(position_sp=-rot, speed_sp=speed, stop_action=stop_action)
    ml.run_to_rel_pos(position_sp=rot, speed_sp=speed, stop_action=stop_action)



us = UltrasonicSensor()
assert us.connected, "Connect a single ultrasonic sensor to any port"
ts = TouchSensor()
assert ts.connected, "Connect a single touch sensor to any port"

# Put the infrared sensor into proximity mode.
us.mode = 'US-DIST-CM'

mr.run_forever(speed_sp=300)
ml.run_forever(speed_sp=300)
while not ts.value():    # Stop program by pressing touch sensor button
    # Ultrasonic sensor measure distance to the closest object in front of it.
    distance = us.value()
    print(distance)

    if distance < 200:
        Leds.set_color(Leds.LEFT, Leds.RED)
        # stop
        mr.stop(stop_action="brake")
        ml.stop(stop_action="brake")
        # turn
        turn(90)
        mr.wait_while('running')
        # run
        mr.run_forever(speed_sp=300)
        ml.run_forever(speed_sp=300)
    else:
        Leds.set_color(Leds.LEFT, Leds.GREEN)

mr.stop(stop_action="brake")
ml.stop(stop_action="brake")
Sound.beep()
Leds.set_color(Leds.LEFT, Leds.GREEN)
#make sure left led is green before exiting

"""
    mr.run_forever(speed_sp=300)
    ml.run_forever(speed_sp=300)
    if distance < 30:

"""
