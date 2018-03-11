#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ev3dev.ev3 import *
from time import sleep

#mr = LargeMotor('outC')
#ml = LargeMotor('outB')
md = MediumMotor('outC')

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

def write_to_file(data, filepath):
    with open(filepath, 'w') as f:
        f.write("angle,distance\n")
        couter = 0
        for item in data:
            line = "{},{}\n".format(item[0], item[1])
            f.write(line)
            counter += 1
    print("{} lines written to file {}".format(counter, filepath))
    

us = UltrasonicSensor()
assert us.connected, "Connect a single ultrasonic sensor to any port"
ts = TouchSensor()
assert ts.connected, "Connect a single touch sensor to any port"

# Put the Ultra sonic sensor into distance mode.
us.mode = 'US-DIST-CM'

speed = 100

# Put motor in 0 position
print("Position before moving to 0 =", md.position)
md.run_to_abs_pos(position_sp=0, speed_sp=speed, stop_action="hold") 
md.wait_while('running')
print("Position after moving to 0 =", md.position)

# Put motor in -60 position
md.run_to_abs_pos(position_sp=-60, speed_sp=speed, stop_action="hold")
md.wait_while('running')

# Scan position from -60 to 60 deg and collect data
list_of_pos_dist = []
angle_incr = 2
while md.position <= 60:
    dist = us.value()
    print(md.position, dist)
    list_of_pos_dist.append((md.position, dist))   # collect position and distance
    md.run_to_rel_pos(position_sp=angle_incr, speed_sp=speed, stop_action="hold") 
    md.wait_while('running')
print(list_of_pos_dist)

#
    




