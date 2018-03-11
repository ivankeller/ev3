#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ev3dev.ev3 import *
from time import sleep

md = MediumMotor('outC')

def write_to_file(data, filepath):
    with open(filepath, 'w') as f:
        f.write("angle,distance\n")
        counter = 0
        for item in data:
            line = "{},{}\n".format(item[0], item[1])
            f.write(line)
            counter += 1
    print("{} lines written to file {}".format(counter, filepath))
    
    
# Set type of sensor used
dist_sensor_type = "infrared"   # or "ultrasonic"

if dist_sensor_type == "infrared":
    dist_sensor = InfraredSensor()
    dist_sensor.mode = 'IR-PROX'
    file_suffix = '_ir'
elif dist_sensor_type == "ultrasonic":
    dist_sensor = UltrasonicSensor() 
    dist_sensor.mode = 'US-DIST-CM'
    file_suffix = '_us'
 
speed = 100
max_angle = 80
# Put motor in 0 position
print("Position before moving to 0 =", md.position)
md.run_to_abs_pos(position_sp=0, speed_sp=speed, stop_action="hold") 
md.wait_while('running')
print("Position after moving to 0 =", md.position)

# Put motor in -max_angle position
md.run_to_abs_pos(position_sp=-max_angle, speed_sp=speed, stop_action="hold")
md.wait_while('running')

# Scan position from -60 to 60 deg and collect data
list_of_pos_dist = []
angle_incr = 2
while md.position <= max_angle:
    dist = dist_sensor.value()
    print(md.position, dist)
    list_of_pos_dist.append((md.position, dist))
    md.run_to_rel_pos(position_sp=angle_incr, speed_sp=speed, stop_action="hold") 
    md.wait_while('running')

# Save result to file 
write_to_file(list_of_pos_dist, "/home/robot/data/output/angle_distance{}.csv".format(file_suffix))
