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
