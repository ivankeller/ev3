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

for i in range(4):
    forward(3)
    mr.wait_while('running')
    turn(90)
    mr.wait_while('running')
