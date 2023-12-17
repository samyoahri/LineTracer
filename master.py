import time
from adafruit_servokit import ServoKit
import serial

class LineTracingController:
    def __init__(self):
        self.kit = ServoKit(channels=16)
        self.angle_channel = 3
        self.throttle_channel = 2
        
        self.line_status = {"left": "0", "Right": "0", "Center": "0"}
        
        self.right_angle_big = 158
        self.right_angle_small = 130
        
        self.center_angle = 90
        
        self.left_angle_small = 45
        self.left_angle_big = 0
        
        self.speed_high_left = 0.04725
        self.speed_high_go = 0.048
        
        self.delay_time = 0.001574
        self.angle_stack = []
        
    def move(self):
        if self.line_status["left"] == "0" and self.line_status["Center"] == "0" and self.line_status["Right"] == "0":
            self.move_back()
        elif self.line_status["left"] == "0" and self.line_status["Center"] == "0" and self.line_status["Right"] == "1":
            self.make_small_left_turn()
        elif self.line_status["left"] == "0" and self.line_status["Center"] == "1" and self.line_status["Right"] == "1":
            self.make_big_left_turn()
        elif self.line_status["left"] == "0" and self.line_status["Center"] == "1" and self.line_status["Right"] == "0":
            self.move_straight()
        elif self.line_status["left"] == "1" and self.line_status["Center"] == "0" and self.line_status["Right"] == "1":
            self.move_straight()
        elif self.line_status["left"] == "1" and self.line_status["Center"] == "1" and self.line_status["Right"] == "1":
            self.move_straight()
        elif self.line_status["left"] == "1" and self.line_status["Center"] == "0" and self.line_status["Right"] == "0":
            self.make_small_right_turn()
        elif self.line_status["left"] == "1" and self.line_status["Center"] == "1" and self.line_status["Right"] == "0":
            self.make_big_right_turn()
            
    def move_back(self):
        if len(self.angle_stack) == 0:
            return
        prev_angle = self.angle_stack.pop()
        self.kit.servo[self.angle_channel].angle = 180 - prev_angle
        self.kit.continuous_servo[self.throttle_channel].throttle = 0.3
        time.sleep(self.delay_time)
        self.kit.continuous_servo[self.throttle_channel].throttle = 0
        time.sleep(self.delay_time)

    def make_small_left_turn(self):
        self.kit.servo[self.angle_channel].angle = self.left_angle_small
        self.angle_stack.append(self.left_angle_small)
        self.kit.continuous_servo[self.throttle_channel].throttle = self.speed_high_left
        time.sleep(self.delay_time)
        self.kit.continuous_servo[self.throttle_channel].throttle = -self.speed_high_left
        time.sleep(self.delay_time)

    def make_big_left_turn(self):
        self.kit.servo[self.angle_channel].angle = self.left_angle_big
        self.angle_stack.append(self.left_angle_big)
        self.kit.continuous_servo[self.throttle_channel].throttle = self.speed_high_left
        time.sleep(self.delay_time)
        self.kit.continuous_servo[self.throttle_channel].throttle = -self.speed_high_left
        time.sleep(self.delay_time)

    def move_straight(self):
        self.kit.servo[self.angle_channel].angle = self.center_angle
        self.angle_stack.append(self.center_angle)
        self.kit.continuous_servo[self.throttle_channel].throttle = self.speed_high_go
        time.sleep(self.delay_time)
        self.kit.continuous_servo[self.throttle_channel].throttle = -self.speed_high_go
        time.sleep(self.delay_time)

    def make_small_right_turn(self):
        self.kit.servo[self.angle_channel].angle = self.right_angle_small
        self.angle_stack.append(135)
        self.kit.continuous_servo[self.throttle_channel].throttle = 0.040
        time.sleep(self.delay_time)
        self.kit.continuous_servo[self.throttle_channel].throttle = -0.040
        time.sleep(self.delay_time)

    def make_big_right_turn(self):
        self.kit.servo[self.angle_channel].angle = self.right_angle_big
        self.angle_stack.append(179)
        self.kit.continuous_servo[self.throttle_channel].throttle = 0.0455
        time.sleep(self.delay_time)
        self.kit.continuous_servo[self.throttle_channel].throttle = -0.0455
        time.sleep(self.delay_time)
        
if __name__ == "__main__":
    line_tracing_controller = LineTracingController()
    serial_port = '/dev/ttyACM1'
    baud_rate = 115200
    ser = serial.Serial(serial_port, baudrate=baud_rate, timeout=3)

    while True:
        try:
            ser_in10 = ser.readline().decode('utf-8').strip()
            arr1 = ser_in10.split(",")
            for pair in arr1:
                key, value = pair.split(':')
                if key in line_tracing_controller.line_status:
                    line_tracing_controller.line_status[key] = value
        except Exception as e:
            print("Error:", end=''); print(e)
            continue
        else:
            line_tracing_controller.move()
        finally:
            print(line_tracing_controller.line_status)

# import time
# from adafruit_servokit import ServoKit

# # Set channels to the number of servo channels on your kit.
# # 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
# kit = ServoKit(channels=16)

# angle_channel = 3
# throttle_channel = 2

# import serial
# import datetime
# import time
# import busio
# from board import SCL, SDA
# import argparse
# from adafruit_pca9685 import PCA9685

# dictionary = {"left": "0", "Right": "0", "Center": "0"}

# right_angle_big = 158
# right_angle_small = 130
# center_angle = 90
# left_angle_small = 45
# left_angle_big = 0

# speed_low = 0.035
# speed_mid = 0.055
# speed_high_left = 0.04725
# speed_high_go = 0.048

# delay_time = 0.001574
# stack = []


# def move():
#     global prevAngleG
#     # 라인을 벗어났으므로 라인을 찾기위한 후진
#     if dictionary["left"] == "0" and dictionary["Center"] == "0" and dictionary["Right"] == "0":
#         if len(stack) == 0:
#             return
#         prevAngleG = stack.pop()
#         kit.servo[angle_channel].angle = 180 - prevAngleG
#         kit.continuous_servo[throttle_channel].throttle = 0.3
#         time.sleep(0.001442)
#         kit.continuous_servo[throttle_channel].throttle = 0
#         time.sleep(0.001442)
#     # 작게 좌회전 이동
#     elif dictionary["left"] == "0" and dictionary["Center"] == "0" and dictionary["Right"] == "1":
#         kit.servo[angle_channel].angle = left_angle_small
#         stack.append(left_angle_small)
#         kit.continuous_servo[throttle_channel].throttle = speed_high_left
#         time.sleep(delay_time)
#         kit.continuous_servo[throttle_channel].throttle = -speed_high_left
#         time.sleep(delay_time)
#     # 크게 좌회전 이동
#     elif dictionary["left"] == "0" and dictionary["Center"] == "1" and dictionary["Right"] == "1":
#         kit.servo[angle_channel].angle = left_angle_big
#         stack.append(left_angle_big)
#         kit.continuous_servo[throttle_channel].throttle = speed_high_left
#         time.sleep(delay_time)
#         kit.continuous_servo[throttle_channel].throttle = -speed_high_left
#         time.sleep(delay_time)
        
#     # 직진이동
#     elif dictionary["left"] == "0" and dictionary["Center"] == "1" and dictionary["Right"] == "0":
#         kit.servo[angle_channel].angle = center_angle
#         stack.append(center_angle)
#         kit.continuous_servo[throttle_channel].throttle = speed_high_go
#         time.sleep(delay_time)
#         kit.continuous_servo[throttle_channel].throttle = -speed_high_go
#         time.sleep(delay_time)
#     # 직진이동
#     elif dictionary["left"] == "1" and dictionary["Center"] == "0" and dictionary["Right"] == "1":
#         kit.servo[angle_channel].angle = center_angle
#         stack.append(center_angle)
#         kit.continuous_servo[throttle_channel].throttle = speed_high_go
#         time.sleep(delay_time)
#         kit.continuous_servo[throttle_channel].throttle = -speed_high_go
#         time.sleep(delay_time)
#     # 직진이동
#     elif dictionary["left"] == "1" and dictionary["Center"] == "1" and dictionary["Right"] == "1":
#         kit.servo[angle_channel].angle = center_angle
#         stack.append(center_angle)
#         kit.continuous_servo[throttle_channel].throttle = speed_high_go
#         time.sleep(delay_time)
        
#     # 작게 우회전 이동
#     elif dictionary["left"] == "1" and dictionary["Center"] == "0" and dictionary["Right"] == "0":
#         kit.servo[angle_channel].angle = right_angle_small
#         stack.append(135)
#         kit.continuous_servo[throttle_channel].throttle = 0.040
#         time.sleep(delay_time)
#         kit.continuous_servo[throttle_channel].throttle = -0.040
#         time.sleep(delay_time)

#     # 크게 우회전 이동
#     elif dictionary["left"] == "1" and dictionary["Center"] == "1" and dictionary["Right"] == "0":
#         kit.servo[angle_channel].angle = right_angle_big
#         stack.append(179)
#         kit.continuous_servo[throttle_channel].throttle = 0.0455
#         time.sleep(delay_time)
#         kit.continuous_servo[throttle_channel].throttle = -0.0455
#         time.sleep(delay_time)



# if __name__ == "__main__":
#     serial_port = '/dev/ttyACM1'
#     baud_rate = 115200
#     ser = serial.Serial(serial_port, baudrate=baud_rate, timeout=3)
#     while True:
#         try:
#             ser_in10 = ser.readline().decode('utf-8').strip()
#             arr1 = ser_in10.split(",")
#             for pair in arr1:
#                 key, value = pair.split(':')
#                 if key == "left":
#                     dictionary[key] = value
#                 elif key == "Right":
#                     dictionary[key] = value
#                 elif key == "Center":
#                     dictionary[key] = value
#         except Exception as e:
#             print("Error:", end=''); print(e)
#             continue
#         else:
#             move()
#         finally:
#             print(dictionary)