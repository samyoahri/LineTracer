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



dictionary = {#"steer_duration":"0","throttle_duration":"0",
              "left":"0","Right":"0","Center":"0"}
# def move_forward_slow():
#     kit.continuous_servo[throttle_channel].throttle = 0.025
# def move_forward_fast():
#     kit.continuous_servo[throttle_channel].throttle = 0.04


#right
right_angle_big = 158#180
right_angle_small = 130#135
#center
center_angle = 90
#left
left_angle_small = 45
left_angle_big = 0

speed_low = 0.035
speed_mid = 0.055
speed_high_left = 0.04725 #angle#65 49
speed_high_go = 0.048 # go#0.85 #51 48
#speed_high_choo = 0.0285

delay_time = 0.001574 #0.002 #148 #160 #1578
stack = []
# prevAngleG = 90

def move():
    # print("move")
    # print(prevAngleG)
    global prevAngleG

    ######################
    # print("f{angle3}")
    # kit.servo[angle_channel].angle = angle3
    # kit.continuous_servo[throttle_channel].throttle = 0.025
    # time.sleep(1)
    ######################
    # kit.servo[angle_channel].angle = 180
    # kit.continuous_servo[throttle_channel].throttle = 0.5
    # time.sleep(1)
    # kit.continuous_servo[throttle_channel].throttle = -0.5
    # time.sleep(1)
    # black0 white1
    if dictionary["left"]=="0" and dictionary["Center"]=="0" and dictionary["Right"]=="0":
        #kit.servo[angle_channel].angle = center_angle
        ### kit.servo[angle_channel].angle = prevAngle
        if len(stack) == 0:
            return
        prevAngleG = stack.pop()
        kit.servo[angle_channel].angle = 180-prevAngleG
        # prevAngleG = center_angle
        # kit.servo[angle_channel].angle = prevAngle
        kit.continuous_servo[throttle_channel].throttle = 0.3
        time.sleep(0.001442)#0.0012 1434 144
        kit.continuous_servo[throttle_channel].throttle = 0
        time.sleep(0.001442)
        # kit.continuous_servo[throttle_channel].throttle = 0
        # time.sleep(delay_time)
        # kit.continuous_servo[throttle_channel].throttle = -speed_high
        # time.sleep(delay_time)
        # # kit.continuous_servo[throttle_channel].throttle = -speed_high
        # print("you failed!")
        # kit.continuous_servo[throttle_channel].throttle = speed_high   

    elif dictionary["left"]=="0" and dictionary["Center"]=="0" and dictionary["Right"]=="1":
        #kit.servo[angle_channel].angle = left_angle
        ### prevAngle=angle5
        kit.servo[angle_channel].angle = left_angle_small
        stack.append(left_angle_small)
        # prevAngleG = left_angle_big
        kit.continuous_servo[throttle_channel].throttle = speed_high_left
        time.sleep(delay_time)
        kit.continuous_servo[throttle_channel].throttle = -speed_high_left
        time.sleep(delay_time)
    
    #     # kit.continuous_servo[throttle_channel].throttle = -speed_high
        
  
        
    elif dictionary["left"]=="0" and dictionary["Center"]=="1" and dictionary["Right"]=="0":
        #kit.servo[angle_channel].angle = center_angle
        ### prevAngle=angle3
        kit.servo[angle_channel].angle = center_angle
        # prevAngleG = center_angle
        stack.append(center_angle)
        kit.continuous_servo[throttle_channel].throttle = speed_high_go
        time.sleep(delay_time)
        kit.continuous_servo[throttle_channel].throttle = -speed_high_go
        time.sleep(delay_time)
    
        # kit.continuous_servo[throttle_channel].throttle = -speed_high
         
    elif dictionary["left"]=="0" and dictionary["Center"]=="1" and dictionary["Right"]=="1":
    #     kit.servo[angle_channel].angle = left_angle
    #     # prevAngle=angle4
        kit.servo[angle_channel].angle = left_angle_big
        # prevAngleG = left_angle_big
        stack.append(left_angle_big)
        kit.continuous_servo[throttle_channel].throttle = speed_high_left
        time.sleep(delay_time)
        kit.continuous_servo[throttle_channel].throttle = -speed_high_left
        time.sleep(delay_time)
    
        # kit.continuous_servo[throttle_channel].throttle = -speed_high
          
    elif dictionary["left"]=="1" and dictionary["Center"]=="0" and dictionary["Right"]=="0":
    #     kit.servo[angle_channel].angle = right_angle
    #     # prevAngle=angle1
        kit.servo[angle_channel].angle = right_angle_small
        # prevAngleG = right_angle_big
        stack.append(135)
        kit.continuous_servo[throttle_channel].throttle = 0.040#54
        time.sleep(delay_time)
        kit.continuous_servo[throttle_channel].throttle = -0.040
        time.sleep(delay_time)
    
        # kit.continuous_servo[throttle_channel].throttle = -speed_high
          
    elif dictionary["left"]=="1" and dictionary["Center"]=="0" and dictionary["Right"]=="1":
    #     kit.servo[angle_channel].angle = center_angle
    #     # prevAngle=angle3
        kit.servo[angle_channel].angle = center_angle
        # prevAngleG = center_angle
        stack.append(center_angle)
        kit.continuous_servo[throttle_channel].throttle = speed_high_go
        time.sleep(delay_time)
        kit.continuous_servo[throttle_channel].throttle = -speed_high_go
        time.sleep(delay_time)
        # kit.continuous_servo[throttle_channel].throttle = -speed_high
            
    elif dictionary["left"]=="1" and dictionary["Center"]=="1" and dictionary["Right"]=="0":
    #     kit.servo[angle_channel].angle = right_angle
    #     # prevAngle=angle2
        kit.servo[angle_channel].angle = right_angle_big
        # prevAngleG = right_angle_big
        stack.append(179)
        kit.continuous_servo[throttle_channel].throttle = 0.0455#56
        time.sleep(delay_time)
        kit.continuous_servo[throttle_channel].throttle = -0.0455#44
        time.sleep(delay_time)
    
        # kit.continuous_servo[throttle_channel].throttle = -speed_high
        
    elif dictionary["left"]=="1" and dictionary["Center"]=="1" and dictionary["Right"]=="1":
        # kit.servo[angle_channel].angle = center_angle
        ### prevAngle=angle3
        # print(prevAngle)
        kit.servo[angle_channel].angle = center_angle
        stack.append(center_angle)
        kit.continuous_servo[throttle_channel].throttle = speed_high_go
        # kit.continuous_servo[throttle_channel].throttle = speed_high
        time.sleep(delay_time)
        # while(1):
        #             kit.servo[angle_channel].angle = center_angle
        #             kit.continuous_servo[throttle_channel].throttle = 0
        #             time.sleep(300)
        # kit.continuous_servo[throttle_channel].throttle = speed_high
        # time.sleep(delay_time)
        # kit.continuous_servo[throttle_channel].throttle = 0
        # time.sleep(delay_time)

        
    
    #     kit.continuous_servo[throttle_channel].throttle = 0
    #     kit.continuous_servo[throttle_channel].throttle = speed_high
    
        # kit.continuous_servo[throttle_channel].throttle = -speed_high
        # print("You Success!")
        # kit.servo[angle_channel].angle = center_angle

    # print(prevAngle)
   
    
    # kit.continuous_servo[throttle_channel].throttle = 0.5
    # move_forward_fast()
    # kit.continuous_servo[throttle_channel].throttle = -0.0281

if __name__ == "__main__":


#     freq=63
#     pca.frequency = freq
    
    serial_port = '/dev/ttyACM1'
    baud_rate = 115200
    ser = serial.Serial(serial_port, baudrate=baud_rate, timeout=3)
    # prevAngle = 90
    while(True):

        
        # kit.servo[angle_channel].angle = 90
        # kit.continuous_servo[throttle_channel].throttle = 0
        try:
            ser_in10 = ser.readline().decode('utf-8').strip()
            arr1 = ser_in10.split(",")
            for pair in arr1:
                key,value = pair.split(':')
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
            # if "steer_duration" in key:
            #     dictionary["steer_duration"] = value
            # elif "throttle_duration" in key:
            #     dictionary["throttle_duration"] = value
            # elif "left" in key:
            #     dictionary["left"] = value
            # elif "Right" in key:
            #     dictionary["Right"] = value
            # elif "Center" in key:
            #     dictionary["Center"] = value
            move()
        finally:
            print(dictionary)


    
    #staright speed up, curb ? / import time
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



dictionary = {#"steer_duration":"0","throttle_duration":"0",
              "left":"0","Right":"0","Center":"0"}
# def move_forward_slow():
#     kit.continuous_servo[throttle_channel].throttle = 0.025
# def move_forward_fast():
#     kit.continuous_servo[throttle_channel].throttle = 0.04


#right
right_angle_big = 158#180
right_angle_small = 130#135
#center
center_angle = 90
#left
left_angle_small = 45
left_angle_big = 0

speed_low = 0.035
speed_mid = 0.055
speed_high_left = 0.04725 #angle#65 49
speed_high_go = 0.048 # go#0.85 #51 48
#speed_high_choo = 0.0285

delay_time = 0.001574 #0.002 #148 #160 #1578
stack = []
# prevAngleG = 90

def move():
    # print("move")
    # print(prevAngleG)
    global prevAngleG

    ######################
    # print("f{angle3}")
    # kit.servo[angle_channel].angle = angle3
    # kit.continuous_servo[throttle_channel].throttle = 0.025
    # time.sleep(1)
    ######################
    # kit.servo[angle_channel].angle = 180
    # kit.continuous_servo[throttle_channel].throttle = 0.5
    # time.sleep(1)
    # kit.continuous_servo[throttle_channel].throttle = -0.5
    # time.sleep(1)
    # black0 white1
    if dictionary["left"]=="0" and dictionary["Center"]=="0" and dictionary["Right"]=="0":
        #kit.servo[angle_channel].angle = center_angle
        ### kit.servo[angle_channel].angle = prevAngle
        if len(stack) == 0:
            return
        prevAngleG = stack.pop()
        kit.servo[angle_channel].angle = 180-prevAngleG
        # prevAngleG = center_angle
        # kit.servo[angle_channel].angle = prevAngle
        kit.continuous_servo[throttle_channel].throttle = 0.3
        time.sleep(0.001442)#0.0012 1434 144
        kit.continuous_servo[throttle_channel].throttle = 0
        time.sleep(0.001442)
        # kit.continuous_servo[throttle_channel].throttle = 0
        # time.sleep(delay_time)
        # kit.continuous_servo[throttle_channel].throttle = -speed_high
        # time.sleep(delay_time)
        # # kit.continuous_servo[throttle_channel].throttle = -speed_high
        # print("you failed!")
        # kit.continuous_servo[throttle_channel].throttle = speed_high   

    elif dictionary["left"]=="0" and dictionary["Center"]=="0" and dictionary["Right"]=="1":
        #kit.servo[angle_channel].angle = left_angle
        ### prevAngle=angle5
        kit.servo[angle_channel].angle = left_angle_small
        stack.append(left_angle_small)
        # prevAngleG = left_angle_big
        kit.continuous_servo[throttle_channel].throttle = speed_high_left
        time.sleep(delay_time)
        kit.continuous_servo[throttle_channel].throttle = -speed_high_left
        time.sleep(delay_time)
    
    #     # kit.continuous_servo[throttle_channel].throttle = -speed_high
        
  
        
    elif dictionary["left"]=="0" and dictionary["Center"]=="1" and dictionary["Right"]=="0":
        #kit.servo[angle_channel].angle = center_angle
        ### prevAngle=angle3
        kit.servo[angle_channel].angle = center_angle
        # prevAngleG = center_angle
        stack.append(center_angle)
        kit.continuous_servo[throttle_channel].throttle = speed_high_go
        time.sleep(delay_time)
        kit.continuous_servo[throttle_channel].throttle = -speed_high_go
        time.sleep(delay_time)
    
        # kit.continuous_servo[throttle_channel].throttle = -speed_high
         
    elif dictionary["left"]=="0" and dictionary["Center"]=="1" and dictionary["Right"]=="1":
    #     kit.servo[angle_channel].angle = left_angle
    #     # prevAngle=angle4
        kit.servo[angle_channel].angle = left_angle_big
        # prevAngleG = left_angle_big
        stack.append(left_angle_big)
        kit.continuous_servo[throttle_channel].throttle = speed_high_left
        time.sleep(delay_time)
        kit.continuous_servo[throttle_channel].throttle = -speed_high_left
        time.sleep(delay_time)
    
        # kit.continuous_servo[throttle_channel].throttle = -speed_high
          
    elif dictionary["left"]=="1" and dictionary["Center"]=="0" and dictionary["Right"]=="0":
    #     kit.servo[angle_channel].angle = right_angle
    #     # prevAngle=angle1
        kit.servo[angle_channel].angle = right_angle_small
        # prevAngleG = right_angle_big
        stack.append(135)
        kit.continuous_servo[throttle_channel].throttle = 0.040#54
        time.sleep(delay_time)
        kit.continuous_servo[throttle_channel].throttle = -0.040
        time.sleep(delay_time)
    
        # kit.continuous_servo[throttle_channel].throttle = -speed_high
          
    elif dictionary["left"]=="1" and dictionary["Center"]=="0" and dictionary["Right"]=="1":
    #     kit.servo[angle_channel].angle = center_angle
    #     # prevAngle=angle3
        kit.servo[angle_channel].angle = center_angle
        # prevAngleG = center_angle
        stack.append(center_angle)
        kit.continuous_servo[throttle_channel].throttle = speed_high_go
        time.sleep(delay_time)
        kit.continuous_servo[throttle_channel].throttle = -speed_high_go
        time.sleep(delay_time)
        # kit.continuous_servo[throttle_channel].throttle = -speed_high
            
    elif dictionary["left"]=="1" and dictionary["Center"]=="1" and dictionary["Right"]=="0":
    #     kit.servo[angle_channel].angle = right_angle
    #     # prevAngle=angle2
        kit.servo[angle_channel].angle = right_angle_big
        # prevAngleG = right_angle_big
        stack.append(179)
        kit.continuous_servo[throttle_channel].throttle = 0.0455#56
        time.sleep(delay_time)
        kit.continuous_servo[throttle_channel].throttle = -0.0455#44
        time.sleep(delay_time)
    
        # kit.continuous_servo[throttle_channel].throttle = -speed_high
        
    elif dictionary["left"]=="1" and dictionary["Center"]=="1" and dictionary["Right"]=="1":
        # kit.servo[angle_channel].angle = center_angle
        ### prevAngle=angle3
        # print(prevAngle)
        kit.servo[angle_channel].angle = center_angle
        stack.append(center_angle)
        kit.continuous_servo[throttle_channel].throttle = speed_high_go
        # kit.continuous_servo[throttle_channel].throttle = speed_high
        time.sleep(delay_time)
        # while(1):
        #             kit.servo[angle_channel].angle = center_angle
        #             kit.continuous_servo[throttle_channel].throttle = 0
        #             time.sleep(300)
        # kit.continuous_servo[throttle_channel].throttle = speed_high
        # time.sleep(delay_time)
        # kit.continuous_servo[throttle_channel].throttle = 0
        # time.sleep(delay_time)

        
    
    #     kit.continuous_servo[throttle_channel].throttle = 0
    #     kit.continuous_servo[throttle_channel].throttle = speed_high
    
        # kit.continuous_servo[throttle_channel].throttle = -speed_high
        # print("You Success!")
        # kit.servo[angle_channel].angle = center_angle

    # print(prevAngle)
   
    
    # kit.continuous_servo[throttle_channel].throttle = 0.5
    # move_forward_fast()
    # kit.continuous_servo[throttle_channel].throttle = -0.0281

if __name__ == "__main__":


#     freq=63
#     pca.frequency = freq
    
    serial_port = '/dev/ttyACM1'
    baud_rate = 115200
    ser = serial.Serial(serial_port, baudrate=baud_rate, timeout=3)
    # prevAngle = 90
    while(True):

        
        # kit.servo[angle_channel].angle = 90
        # kit.continuous_servo[throttle_channel].throttle = 0
        try:
            ser_in10 = ser.readline().decode('utf-8').strip()
            arr1 = ser_in10.split(",")
            for pair in arr1:
                key,value = pair.split(':')
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
            # if "steer_duration" in key:
            #     dictionary["steer_duration"] = value
            # elif "throttle_duration" in key:
            #     dictionary["throttle_duration"] = value
            # elif "left" in key:
            #     dictionary["left"] = value
            # elif "Right" in key:
            #     dictionary["Right"] = value
            # elif "Center" in key:
            #     dictionary["Center"] = value
            move()
        finally:
            print(dictionary)


    
    #staright speed up, curb ? / 