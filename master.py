import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)

angle_channel = 3
throttle_channel = 2

import serial
import datetime
import time
import busio
from board import SCL, SDA
import argparse
from adafruit_pca9685 import PCA9685

dictionary = {"left": "0", "Right": "0", "Center": "0"}

right_angle_big = 158
right_angle_small = 130
center_angle = 90
left_angle_small = 45
left_angle_big = 0

speed_low = 0.035
speed_mid = 0.055
speed_high_left = 0.04725
speed_high_go = 0.048

delay_time = 0.001574
stack = []


def move():
    global prevAngleG

    if dictionary["left"] == "0" and dictionary["Center"] == "0" and dictionary["Right"] == "0":
        if len(stack) == 0:
            return
        prevAngleG = stack.pop()
        kit.servo[angle_channel].angle = 180 - prevAngleG
        kit.continuous_servo[throttle_channel].throttle = 0.3
        time.sleep(0.001442)
        kit.continuous_servo[throttle_channel].throttle = 0
        time.sleep(0.001442)

    elif dictionary["left"] == "0" and dictionary["Center"] == "0" and dictionary["Right"] == "1":
        kit.servo[angle_channel].angle = left_angle_small
        stack.append(left_angle_small)
        kit.continuous_servo[throttle_channel].throttle = speed_high_left
        time.sleep(delay_time)
        kit.continuous_servo[throttle_channel].throttle = -speed_high_left
        time.sleep(delay_time)

    elif dictionary["left"] == "0" and dictionary["Center"] == "1" and dictionary["Right"] == "0":
        kit.servo[angle_channel].angle = center_angle
        stack.append(center_angle)
        kit.continuous_servo[throttle_channel].throttle = speed_high_go
        time.sleep(delay_time)
        kit.continuous_servo[throttle_channel].throttle = -speed_high_go
        time.sleep(delay_time)

    elif dictionary["left"] == "0" and dictionary["Center"] == "1" and dictionary["Right"] == "1":
        kit.servo[angle_channel].angle = left_angle_big
        stack.append(left_angle_big)
        kit.continuous_servo[throttle_channel].throttle = speed_high_left
        time.sleep(delay_time)
        kit.continuous_servo[throttle_channel].throttle = -speed_high_left
        time.sleep(delay_time)

    elif dictionary["left"] == "1" and dictionary["Center"] == "0" and dictionary["Right"] == "0":
        kit.servo[angle_channel].angle = right_angle_small
        stack.append(135)
        kit.continuous_servo[throttle_channel].throttle = 0.040
        time.sleep(delay_time)
        kit.continuous_servo[throttle_channel].throttle = -0.040
        time.sleep(delay_time)

    elif dictionary["left"] == "1" and dictionary["Center"] == "0" and dictionary["Right"] == "1":
        kit.servo[angle_channel].angle = center_angle
        stack.append(center_angle)
        kit.continuous_servo[throttle_channel].throttle = speed_high_go
        time.sleep(delay_time)
        kit.continuous_servo[throttle_channel].throttle = -speed_high_go
        time.sleep(delay_time)

    elif dictionary["left"] == "1" and dictionary["Center"] == "1" and dictionary["Right"] == "0":
        kit.servo[angle_channel].angle = right_angle_big
        stack.append(179)
        kit.continuous_servo[throttle_channel].throttle = 0.0455
        time.sleep(delay_time)
        kit.continuous_servo[throttle_channel].throttle = -0.0455
        time.sleep(delay_time)

    elif dictionary["left"] == "1" and dictionary["Center"] == "1" and dictionary["Right"] == "1":
        kit.servo[angle_channel].angle = center_angle
        stack.append(center_angle)
        kit.continuous_servo[throttle_channel].throttle = speed_high_go
        time.sleep(delay_time)


if __name__ == "__main__":
    serial_port = '/dev/ttyACM1'
    baud_rate = 115200
    ser = serial.Serial(serial_port, baudrate=baud_rate, timeout=3)
    while True:
        try:
            ser_in10 = ser.readline().decode('utf-8').strip()
            arr1 = ser_in10.split(",")
            for pair in arr1:
                key, value = pair.split(':')
                if key == "left":
                    dictionary[key] = value
                elif key == "Right":
                    dictionary[key] = value
                elif key == "Center":
                    dictionary[key] = value
        except Exception as e:
            print("Error:", end=''); print(e)
            continue
        else:
            move()
        finally:
            print(dictionary)