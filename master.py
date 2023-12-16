# import serial
# import datetime
# import time
# import busio
# from board import SCL, SDA
# import argparse
# import os
# import getch
# from Jetson import GPIO
# from adafruit_pca9685 import PCA9685

# def logging(filename):
#     # i2c 버스 인터페이스 생성
#     i2c_bus = busio.I2C(SCL, SDA)
    
#     # pca 인터페이스 생성
#     pca = PCA9685(i2c_bus)

#     # PWM 프리퀀시 설정
#     freq=90 
#     pca.frequency = freq
    
#     left = 0x1D00
#     left2 = 0x1CF0
#     left3 = 0x1CC0
#     center = 0x1B80
#     right = 0x11B0
#     right2 = 0x1700
#     right3 = 0x1B00
#     right4 = 0x1800
#     go10 = 0x1B10
#     go0 = 0x1B00
#     go = 0x1AF0
#     go2 = 0x1AF0
#     stop = 0x18B0
# # steer = center
# # throttle = stop
# # pca.channels[0].duty_cycle = steer
# # pca.channels[1].duty_cycle = throttle
# # pca.channels[14].duty_cycle = steer
# # pca.channels[15].duty_cycle = throttle

# # while True:
# #     os.system('clear')
# #     print(' freq:{}\n   steer:{}\nthrottle:{}'.format(pca.frequency,hex(steer),hex(throttle)))

# #     keyin = getch.getch()

# #     if keyin == 'i':
# #         if throttle <= 0xFFE0:
# #             throttle += 0x10
# #     elif keyin == 'j':
# #         if steer <= 0xFFE0:
# #             steer += 0x10
# #     elif keyin == 'k':
# #         if throttle >= 0x0010:
# #             throttle -= 0x10
# #     elif keyin == 'l':
# #         if steer >= 0x0010:
# #             steer -= 0x10
# #     elif keyin == 'r':
# #         os.system('clear')
# #         print('reset GPIO')

# #         GPIO.cleanup()
# #         PCA9685.reset()
# #         i2c_bus = busio.I2C(SCL,SDA)
# #         pca = PCA9685(i2c_bus)
# #         pca.frequency = freq
# #     elif keyin == 'f':
# #         os.system('clear')
# #         freq = int(input('new frequency:'))

# #         pca.frequency = freq

# #     pca.channels[0].duty_cycle = steer
# #     pca.channels[1].duty_cycle = throttle

# #     pca.channels[14].duty_cycle = steer
# #     pca.channels[15].duty_cycle = throttle

# #     time.sleep(0.005)


#     # left = 0x1B30
#     # center = 0x2380
#     # right = 0x2E60
    
#     # forward= 0x2D40
#     # stop = 0x2140
#     # backward = 0x1A70
    
#     # pca.channels[0].duty_cycle = center
#     # pca.channels[1].duty_cycle = stop
#     f = open(filename, 'w')

#     with serial.Serial('/dev/tty2', 9600, timeout=10) as ser:

#         start = input('Do you want to start logging? ')[0]
#         if start in 'yY':
#             ser.write(bytes('YES\n', 'utf-8'))
#             while True:
#                 ser_in = ser.readline().decode('utf-8')
#                 print(ser_in)
#                 sensorf = ser_in.split('/')[0]
#                 sensorb = ser_in.split('/')[1]
#                 sensor_print = str(sensorf)

#                 if sensorf[0] == '0' and sensorf[1] == '1' and sensorf[2] == '0':
#                     if sensorb[0] == '1' and sensorb[1] == '0' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = center
#                         pca.channels[1].duty_cycle = go0
#                         print("center\n\n----")
#                     elif sensorb[0] == '0' and sensorb[1] == '0' and sensorb[2] == '1':
#                         pca.channels[0].duty_cycle = left2
#                         pca.channels[1].duty_cycle = go
#                         print("left2\n\n----")
#                     elif sensorb[0] == '1' and sensorb[1] == '1' and sensorb[2] == '1':
#                         if sensorf[0] == '1' and sensorf[1] == '1' and sensorf[2] == '1' and sensorb[0] == '1' and sensorb[1] == '0' and sensorb[2] == '0':
#                             pca.channels[0].duty_cycle = center
#                             pca.channels[1].duty_cycle = stop
#                             print("stop\n\n----")
#                         else:
#                             pca.channels[0].duty_cycle = center
#                             pca.channels[1].duty_cycle = go
#                             print("go\n\n----")
#                     else:
#                         pca.channels[0].duty_cycle = center
#                         pca.channels[1].duty_cycle = go10
#                         print("center\n\n----")
#                 elif sensorf[0] == '0' and sensorf[1] == '0' and sensorf[2] == '1':
#                     if sensorb[0] == '1' and sensorb[1] == '0' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = right2
#                         pca.channels[1].duty_cycle = go
#                         print("right2\n\n----")
#                     elif sensorb[0] == '0' and sensorb[1] == '1' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = right3
#                         pca.channels[1].duty_cycle = go10
#                         print("right3\n\n----")
#                     elif sensorb[0] == '0' and sensorb[1] == '1' and sensorb[2] == '1':
#                         pca.channels[0].duty_cycle = right2
#                         pca.channels[1].duty_cycle = go
#                         print("right3\n\n----")
#                     elif sensorb[0] == '0' and sensorb[1] == '0' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = right2
#                         pca.channels[1].duty_cycle = go
#                         print("right3\n\n----")
#                     elif sensorb[0] == '1' and sensorb[1] == '1' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = right2
#                         pca.channels[1].duty_cycle = go
#                         print("right3\n\n----")
#                     elif sensorb[0] == '0' and sensorb[1] == '0' and sensorb[2] == '1':
#                         pca.channels[0].duty_cycle = right2
#                         pca.channels[1].duty_cycle = go
#                         print("right3\n\n----")
#                     else:
#                         pca.channels[0].duty_cycle = right2
#                         pca.channels[1].duty_cycle = go2
#                         print("right2\n\n----")
#                 elif sensorf[0] == '1' and sensorf[1] == '0' and sensorf[2] == '0':
#                     if sensorb[0] == '0' and sensorb[1] == '1' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = left2
#                         pca.channels[1].duty_cycle = go
#                         print("left\n\n----")
#                     elif sensorb[0] == '1' and sensorb[1] == '0' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = center
#                         pca.channels[1].duty_cycle = go2
#                         print("go2\n\n----")
#                     elif sensorb[0] == '1' and sensorb[1] == '1' and sensorb[2] == '1':
#                         pca.channels[0].duty_cycle = left
#                         pca.channels[1].duty_cycle = go2
#                         print("left\n\n----")
#                     else:
#                         pca.channels[0].duty_cycle = left
#                         pca.channels[1].duty_cycle = go2
#                         print("left\n\n----")
#                 elif sensorf[0] == '0' and sensorf[1] == '1' and sensorf[2] == '1':
#                     if sensorb[0] == '0' and sensorb[1] == '1' and sensorb[2] == '1':
#                         pca.channels[0].duty_cycle = right2
#                         pca.channels[1].duty_cycle = go
#                         print("right2\n\n----")
#                     elif sensorb[0] == '0' and sensorb[1] == '1' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = right2
#                         pca.channels[1].duty_cycle = go
#                         print("right2\n\n----")
#                     elif sensorb[0] == '0' and sensorb[1] == '0' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = right2
#                         pca.channels[1].duty_cycle = go
#                         print("right2\n\n----")
#                     elif sensorb[0] == '1' and sensorb[1] == '0' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = right2
#                         pca.channels[1].duty_cycle = go0
#                         print("right2\n\n----")
#                     else:
#                         pca.channels[0].duty_cycle = right2
#                         pca.channels[1].duty_cycle = go2
#                         print("right2\n\n----")
#                 elif sensorf[0] == '1' and sensorf[1] == '1' and sensorf[2] == '0':
#                     if sensorb[0] == '0' and sensorb[1] == '1' and sensorb[2] == '1':
#                         pca.channels[0].duty_cycle = left3
#                         pca.channels[1].duty_cycle = go2
#                         print("left3\n\n----")
#                     elif sensorb[0] == '0' and sensorb[1] == '0' and sensorb[2] == '1':
#                         pca.channels[0].duty_cycle = left2
#                         pca.channels[1].duty_cycle = go2
#                         print("left2\n\n----")
#                     elif sensorb[0] == '1' and sensorb[1] == '1' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = center
#                         pca.channels[1].duty_cycle = go2
#                         print("center\n\n----")
#                     elif sensorb[0] == '1' and sensorb[1] == '1' and sensorb[2] == '1':
#                         pca.channels[0].duty_cycle = left
#                         pca.channels[1].duty_cycle = go
#                         print("stop\n\n----")
#                     else:
#                         pca.channels[0].duty_cycle = left
#                         pca.channels[1].duty_cycle = go
#                         print("left\n\n----")
#                 elif sensorf[0] == '1' and sensorf[1] == '1' and sensorf[2] == '1':
#                     if sensorb[0] == '1' and sensorb[1] == '1' and sensorb[2] == '1':
#                         pca.channels[0].duty_cycle = center
#                         pca.channels[1].duty_cycle = stop
#                         print("stop\n\n----")
#                     elif sensorb[0] == '0' and sensorb[1] == '1' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = center
#                         pca.channels[1].duty_cycle = stop
#                         print("stop\n\n----")
#                         time.sleep(2)
#                     elif sensorb[0] == '0' and sensorb[1] == '0' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = center
#                         pca.channels[1].duty_cycle = stop
#                         print("stop\n\n----")
#                         time.sleep(2)
#                     elif sensorb[0] == '0' and sensorb[1] == '0' and sensorb[2] == '1':
#                         pca.channels[0].duty_cycle = center
#                         pca.channels[1].duty_cycle = stop
#                         print("stop\n\n----")
#                     elif sensorb[0] == '0' and sensorb[1] == '1' and sensorb[2] == '1':
#                         pca.channels[0].duty_cycle = center
#                         pca.channels[1].duty_cycle = stop
#                         print("stop\n\n----")
#                     else:
#                         pca.channels[0].duty_cycle = center
#                         pca.channels[1].duty_cycle = stop
#                         print("stop\n\n----")
#                 elif sensorb[0] == '1' and sensorb[1] == '1' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = right2
#                         pca.channels[1].duty_cycle = go
#                         print("right2\n\n----")
#                 elif sensorb[0] == '0' and sensorb[1] == '1' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = right
#                         pca.channels[1].duty_cycle = go0
#                         print("right\n\n----")
#                 elif sensorb[0] == '0' and sensorb[1] == '0' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = right3
#                         pca.channels[1].duty_cycle = go0
#                         print("right3\n\n----")
#                 elif sensorb[0] == '1' and sensorb[1] == '1' and sensorb[2] == '1':
#                         pca.channels[0].duty_cycle = right3
#                         pca.channels[1].duty_cycle = go
#                         print("right3\n\n----")
#                 else:
#                         pca.channels[0].duty_cycle = center
#                         pca.channels[1].duty_cycle = stop
#                         print("stop1\n\n----")
#     f.close()

#     #             f.write("{} {}".format(datetime.datetime.now(), ser_in))
#     #             print("{} {}".format(datetime.datetime.now(), ser_in), end='')
#     #             steer = int(ser_in.split(' ')[2].split('/')[0])
#     #             throttle = int(ser_in.split(' ')[5].split('/')[0])
                
#     #             if int(steer) <= 1000:
#     #                 steer = int(0x2380)
#     #             elif int(steer) <= 1444:
#     #                 steer = int(((0x2380 - 0x1B30) / (1444 - 1108)) * (steer - 1444) + 0x2380)
#     #             elif int(steer <= 2000):
#     #                 steer = int(((0x2E60 - 0x2380) / (1888 - 1444)) * (steer - 1444) + 0x2380)
#     #             else:
#     #                 steer = int(center)
                    
#     #             if int(throttle) <= 1000:
#     #                 throttle = int(0x2140)
#     #             elif int(throttle) >= 1352:
#     #                 throttle = int(((0x2D40 - 0x2140) / (1840 - 1352)) * (throttle - 1352) + 0x2140)
#     #             else:
#     #                 throttle = int(((0x2140 - 0x1A70) / (1352 - 1076)) * (throttle - 1352) + 0x2140)
                    
#     #             pca.channels[0].duty_cycle = steer
#     #             pca.channels[1].duty_cycle = throttle
#     # f.close()
    
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="")
#     parser.add_argument('--log_file_name', metavar= 'K', type=str, nargs=1, help="log file's name")
#     args = parser.parse_args()
#     logging(args.log_file_name)

# image_list = []
# action_list = []

# def make_dataset(path, filename):
#     print(filename)
#     image_list = []
#     action_list = []

#     logpath = path+filename+'.log'
#     avipath = path+filename+'.mp4'

#     logfile = open(logpath, 'r')
#     avifile = cv2.VideoCapture(avipath)

#     loglines = logfile.readlines()

#     current_avi_time = 0
#     start_time = datetime.datetime(int(filename[0:4]), int(filename[4:6]), int(filename[6:8]),int(filename[9:11]),int(filename[11:13]),int(filename[13:15]))

#     i = 0

#     for line in loglines:
#         i += 1
#         logdata = line.split(' ')
#         date = logdata[0].split('-')
#         time = logdata[1].split(':')
#         log_time = datetime.datetime(int(date[0]),int(date[1]),int(date[2]),int(time[0]),int(time[1]),int(time[2].split('.'[0])),int(time[2].split('.'[1])))

#         delt_time = (log_time-start_time).total_seconds()

#         image = None
#         steer = (int(logdata[4].split('/')[0]) - 1352) / 1840
#         throttle = (int(logdata[7].split('/')[0]) - 1352) / 1840

#         while(avifile.isOpened() and current_avi_time < delt_time):
#             ret, frame = avifile.read()
#             if ret == True:
#                 current_avi_time += 1/30
#                 if current_avi_time > delt_time:
#                     image = frame
#                     image_list.append(image)
#                     action_list.append([steer, throttle])
#             else:
#                 break

##############################################################################################

# import serial
# import datetime
# import time
# import busio
# from board import SCL, SDA
# import argparse
# import os
# import getch
# from Jetson import GPIO
# from adafruit_pca9685 import PCA9685

# def logging(filename):
#     #GPIO.cleanup()

#     i2c_bus = busio.I2C(SCL, SDA)
    
#     pca = PCA9685(i2c_bus)

#     freq=83 
#     pca.frequency = freq
    
# #     # pca.channels[0].duty_cycle = 0x1B30
# #     # pca.channels[0].duty_cycle = 0x2380
# #     # pca.channels[0].duty_cycle = 0x2E60
    
    
# #     # pca.channels[1].duty_cycle = 0x2D40
# #     # pca.channels[1].duty_cycle = 0x2140
# #     # pca.channels[1].duty_cycle = 0x1A70
    
#     left = 0x1D00
#     left2 = 0x1CF0
#     left3 = 0x1CC0
#     center = 0x1B80
#     right = 0x11B0
#     right2 = 0x1700
#     right3 = 0x1B00
#     right4 = 0x1800
#     go10 = 0x1B10
#     go0 = 0x1B00
#     go = 0x1AF0
#     go2 = 0x1AF0
#     stop = 0x18B0
# # steer = center
# # throttle = stop
# # pca.channels[0].duty_cycle = steer
# # pca.channels[1].duty_cycle = throttle
# # pca.channels[14].duty_cycle = steer
# # pca.channels[15].duty_cycle = throttle

# # while True:
# #     os.system('clear')
# #     print(' freq:{}\n   steer:{}\nthrottle:{}'.format(pca.frequency,hex(steer),hex(throttle)))

# #     keyin = getch.getch()

# #     if keyin == 'i':
# #         if throttle <= 0xFFE0:
# #             throttle += 0x10
# #     elif keyin == 'j':
# #         if steer <= 0xFFE0:
# #             steer += 0x10
# #     elif keyin == 'k':
# #         if throttle >= 0x0010:
# #             throttle -= 0x10
# #     elif keyin == 'l':
# #         if steer >= 0x0010:
# #             steer -= 0x10
# #     elif keyin == 'r':
# #         os.system('clear')
# #         print('reset GPIO')

# #         GPIO.cleanup()
# #         PCA9685.reset()
# #         i2c_bus = busio.I2C(SCL,SDA)
# #         pca = PCA9685(i2c_bus)
# #         pca.frequency = freq
# #     elif keyin == 'f':
# #         os.system('clear')
# #         freq = int(input('new frequency:'))

# #         pca.frequency = freq

# #     pca.channels[0].duty_cycle = steer
# #     pca.channels[1].duty_cycle = throttle

# #     pca.channels[14].duty_cycle = steer
# #     pca.channels[15].duty_cycle = throttle

# #     time.sleep(0.005)


#     # left = 0x1B30
#     # center = 0x2380
#     # right = 0x2E60
    
#     # forward= 0x2D40
#     # stop = 0x2140
#     # backward = 0x1A70
    
#     # pca.channels[0].duty_cycle = center
#     # pca.channels[1].duty_cycle = stop
#     f = open(filename, 'w')

#     with serial.Serial('/dev/tty2', 9600, timeout=10) as ser:

#         start = input('Do you want to start logging? ')[0]
#         if start in 'yY':
#             ser.write(bytes('YES\n', 'utf-8'))
#             while True:
#                 ser_in = ser.readline().decode('utf-8')
#                 print(ser_in)
#                 sensorf = ser_in.split('/')[0]
#                 sensorb = ser_in.split('/')[1]
#                 sensor_print = str(sensorf)

#                 if sensorf[0] == '0' and sensorf[1] == '1' and sensorf[2] == '0':
#                     if sensorb[0] == '1' and sensorb[1] == '0' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = center
#                         pca.channels[1].duty_cycle = go0
#                         print("center\n\n----")
#                     elif sensorb[0] == '0' and sensorb[1] == '0' and sensorb[2] == '1':
#                         pca.channels[0].duty_cycle = left2
#                         pca.channels[1].duty_cycle = go
#                         print("left2\n\n----")
#                     elif sensorb[0] == '1' and sensorb[1] == '1' and sensorb[2] == '1':
#                         if sensorf[0] == '1' and sensorf[1] == '1' and sensorf[2] == '1' and sensorb[0] == '1' and sensorb[1] == '0' and sensorb[2] == '0':
#                             pca.channels[0].duty_cycle = center
#                             pca.channels[1].duty_cycle = stop
#                             print("stop\n\n----")
#                         else:
#                             pca.channels[0].duty_cycle = center
#                             pca.channels[1].duty_cycle = go
#                             print("go\n\n----")
#                     else:
#                         pca.channels[0].duty_cycle = center
#                         pca.channels[1].duty_cycle = go10
#                         print("center\n\n----")
#                 elif sensorf[0] == '0' and sensorf[1] == '0' and sensorf[2] == '1':
#                     if sensorb[0] == '1' and sensorb[1] == '0' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = right2
#                         pca.channels[1].duty_cycle = go
#                         print("right2\n\n----")
#                     elif sensorb[0] == '0' and sensorb[1] == '1' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = right3
#                         pca.channels[1].duty_cycle = go10
#                         print("right3\n\n----")
#                     elif sensorb[0] == '0' and sensorb[1] == '1' and sensorb[2] == '1':
#                         pca.channels[0].duty_cycle = right2
#                         pca.channels[1].duty_cycle = go
#                         print("right3\n\n----")
#                     elif sensorb[0] == '0' and sensorb[1] == '0' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = right2
#                         pca.channels[1].duty_cycle = go
#                         print("right3\n\n----")
#                     elif sensorb[0] == '1' and sensorb[1] == '1' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = right2
#                         pca.channels[1].duty_cycle = go
#                         print("right3\n\n----")
#                     elif sensorb[0] == '0' and sensorb[1] == '0' and sensorb[2] == '1':
#                         pca.channels[0].duty_cycle = right2
#                         pca.channels[1].duty_cycle = go
#                         print("right3\n\n----")
#                     else:
#                         pca.channels[0].duty_cycle = right2
#                         pca.channels[1].duty_cycle = go2
#                         print("right2\n\n----")
#                 elif sensorf[0] == '1' and sensorf[1] == '0' and sensorf[2] == '0':
#                     if sensorb[0] == '0' and sensorb[1] == '1' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = left2
#                         pca.channels[1].duty_cycle = go
#                         print("left\n\n----")
#                     elif sensorb[0] == '1' and sensorb[1] == '0' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = center
#                         pca.channels[1].duty_cycle = go2
#                         print("go2\n\n----")
#                     elif sensorb[0] == '1' and sensorb[1] == '1' and sensorb[2] == '1':
#                         pca.channels[0].duty_cycle = left
#                         pca.channels[1].duty_cycle = go2
#                         print("left\n\n----")
#                     else:
#                         pca.channels[0].duty_cycle = left
#                         pca.channels[1].duty_cycle = go2
#                         print("left\n\n----")
#                 elif sensorf[0] == '0' and sensorf[1] == '1' and sensorf[2] == '1':
#                     if sensorb[0] == '0' and sensorb[1] == '1' and sensorb[2] == '1':
#                         pca.channels[0].duty_cycle = right2
#                         pca.channels[1].duty_cycle = go
#                         print("right2\n\n----")
#                     elif sensorb[0] == '0' and sensorb[1] == '1' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = right2
#                         pca.channels[1].duty_cycle = go
#                         print("right2\n\n----")
#                     elif sensorb[0] == '0' and sensorb[1] == '0' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = right2
#                         pca.channels[1].duty_cycle = go
#                         print("right2\n\n----")
#                     elif sensorb[0] == '1' and sensorb[1] == '0' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = right2
#                         pca.channels[1].duty_cycle = go0
#                         print("right2\n\n----")
#                     else:
#                         pca.channels[0].duty_cycle = right2
#                         pca.channels[1].duty_cycle = go2
#                         print("right2\n\n----")
#                 elif sensorf[0] == '1' and sensorf[1] == '1' and sensorf[2] == '0':
#                     if sensorb[0] == '0' and sensorb[1] == '1' and sensorb[2] == '1':
#                         pca.channels[0].duty_cycle = left3
#                         pca.channels[1].duty_cycle = go2
#                         print("left3\n\n----")
#                     elif sensorb[0] == '0' and sensorb[1] == '0' and sensorb[2] == '1':
#                         pca.channels[0].duty_cycle = left2
#                         pca.channels[1].duty_cycle = go2
#                         print("left2\n\n----")
#                     elif sensorb[0] == '1' and sensorb[1] == '1' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = center
#                         pca.channels[1].duty_cycle = go2
#                         print("center\n\n----")
#                     elif sensorb[0] == '1' and sensorb[1] == '1' and sensorb[2] == '1':
#                         pca.channels[0].duty_cycle = left
#                         pca.channels[1].duty_cycle = go
#                         print("stop\n\n----")
#                     else:
#                         pca.channels[0].duty_cycle = left
#                         pca.channels[1].duty_cycle = go
#                         print("left\n\n----")
#                 elif sensorf[0] == '1' and sensorf[1] == '1' and sensorf[2] == '1':
#                     if sensorb[0] == '1' and sensorb[1] == '1' and sensorb[2] == '1':
#                         pca.channels[0].duty_cycle = center
#                         pca.channels[1].duty_cycle = stop
#                         print("stop\n\n----")
#                     elif sensorb[0] == '0' and sensorb[1] == '1' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = center
#                         pca.channels[1].duty_cycle = stop
#                         print("stop\n\n----")
#                         time.sleep(2)
#                     elif sensorb[0] == '0' and sensorb[1] == '0' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = center
#                         pca.channels[1].duty_cycle = stop
#                         print("stop\n\n----")
#                         time.sleep(2)
#                     elif sensorb[0] == '0' and sensorb[1] == '0' and sensorb[2] == '1':
#                         pca.channels[0].duty_cycle = center
#                         pca.channels[1].duty_cycle = stop
#                         print("stop\n\n----")
#                     elif sensorb[0] == '0' and sensorb[1] == '1' and sensorb[2] == '1':
#                         pca.channels[0].duty_cycle = center
#                         pca.channels[1].duty_cycle = stop
#                         print("stop\n\n----")
#                     else:
#                         pca.channels[0].duty_cycle = center
#                         pca.channels[1].duty_cycle = stop
#                         print("stop\n\n----")
#                 elif sensorb[0] == '1' and sensorb[1] == '1' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = right2
#                         pca.channels[1].duty_cycle = go
#                         print("right2\n\n----")
#                 elif sensorb[0] == '0' and sensorb[1] == '1' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = right
#                         pca.channels[1].duty_cycle = go0
#                         print("right\n\n----")
#                 elif sensorb[0] == '0' and sensorb[1] == '0' and sensorb[2] == '0':
#                         pca.channels[0].duty_cycle = right3
#                         pca.channels[1].duty_cycle = go0
#                         print("right3\n\n----")
#                 elif sensorb[0] == '1' and sensorb[1] == '1' and sensorb[2] == '1':
#                         pca.channels[0].duty_cycle = right3
#                         pca.channels[1].duty_cycle = go
#                         print("right3\n\n----")
#                 else:
#                         pca.channels[0].duty_cycle = center
#                         pca.channels[1].duty_cycle = stop
#                         print("stop1\n\n----")
#     f.close()

#     #             f.write("{} {}".format(datetime.datetime.now(), ser_in))
#     #             print("{} {}".format(datetime.datetime.now(), ser_in), end='')
#     #             steer = int(ser_in.split(' ')[2].split('/')[0])
#     #             throttle = int(ser_in.split(' ')[5].split('/')[0])
                
#     #             if int(steer) <= 1000:
#     #                 steer = int(0x2380)
#     #             elif int(steer) <= 1444:
#     #                 steer = int(((0x2380 - 0x1B30) / (1444 - 1108)) * (steer - 1444) + 0x2380)
#     #             elif int(steer <= 2000):
#     #                 steer = int(((0x2E60 - 0x2380) / (1888 - 1444)) * (steer - 1444) + 0x2380)
#     #             else:
#     #                 steer = int(center)
                    
#     #             if int(throttle) <= 1000:
#     #                 throttle = int(0x2140)
#     #             elif int(throttle) >= 1352:
#     #                 throttle = int(((0x2D40 - 0x2140) / (1840 - 1352)) * (throttle - 1352) + 0x2140)
#     #             else:
#     #                 throttle = int(((0x2140 - 0x1A70) / (1352 - 1076)) * (throttle - 1352) + 0x2140)
                    
#     #             pca.channels[0].duty_cycle = steer
#     #             pca.channels[1].duty_cycle = throttle
#     # f.close()
    
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="")
#     parser.add_argument('--log_file_name', metavar= 'K', type=str, nargs=1, help="log file's name")
#     args = parser.parse_args()
#     logging(args.log_file_name)

# # image_list = []
# # action_list = []

# # def make_dataset(path, filename):
# #     print(filename)
# #     image_list = []
# #     action_list = []

# #     logpath = path+filename+'.log'
# #     avipath = path+filename+'.mp4'

# #     logfile = open(logpath, 'r')
# #     avifile = cv2.VideoCapture(avipath)

# #     loglines = logfile.readlines()

# #     current_avi_time = 0
# #     start_time = datetime.datetime(int(filename[0:4]), int(filename[4:6]), int(filename[6:8]),int(filename[9:11]),int(filename[11:13]),int(filename[13:15]))

# #     i = 0

# #     for line in loglines:
# #         i += 1
# #         logdata = line.split(' ')
# #         date = logdata[0].split('-')
# #         time = logdata[1].split(':')
# #         log_time = datetime.datetime(int(date[0]),int(date[1]),int(date[2]),int(time[0]),int(time[1]),int(time[2].split('.'[0])),int(time[2].split('.'[1])))

# #         delt_time = (log_time-start_time).total_seconds()

# #         image = None
# #         steer = (int(logdata[4].split('/')[0]) - 1352) / 1840
# #         throttle = (int(logdata[7].split('/')[0]) - 1352) / 1840

# #         while(avifile.isOpened() and current_avi_time < delt_time):
# #             ret, frame = avifile.read()
# #             if ret == True:
# #                 current_avi_time += 1/30
# #                 if current_avi_time > delt_time:
# #                     image = frame
# #                     image_list.append(image)
# #                     action_list.append([steer, throttle])
# #             else:
# #                 break

###############################################
import serial
import datetime
import time
import busio
from board import SCL, SDA
import argparse
import os
import getch
from Jetson import GPIO
from adafruit_pca9685 import PCA9685

def logging(filename):
    #GPIO.cleanup()

    i2c_bus = busio.I2C(SCL, SDA)
    
    pca = PCA9685(i2c_bus)

    freq=83 
    pca.frequency = freq
    
    
    left = 0x1D00
    left2 = 0x1CF0
    left3 = 0x1CC0
    center = 0x1B80
    right = 0x11B0
    right2 = 0x1700
    right3 = 0x1B00
    right4 = 0x1800
    go10 = 0x1B10
    go0 = 0x1B00
    go = 0x1AF0
    go2 = 0x1AF0
    stop = 0x18B0
    f = open(filename, 'w')

    with serial.Serial('/dev/tty2', 9600, timeout=10) as ser:

        start = input('Do you want to start logging? ')[0]
        if start in 'yY':
            ser.write(bytes('YES\n', 'utf-8'))
            while True:
                ser_in = ser.readline().decode('utf-8')
                print(ser_in)
                sensorf = ser_in.split('/')[0]
                sensorb = ser_in.split('/')[1]
                sensor_print = str(sensorf)

                if sensorf[0] == '0' and sensorf[1] == '1' and sensorf[2] == '0':
                    if sensorb[0] == '1' and sensorb[1] == '0' and sensorb[2] == '0':
                        pca.channels[0].duty_cycle = center
                        pca.channels[1].duty_cycle = go0
                        print("center\n\n----")
                    elif sensorb[0] == '0' and sensorb[1] == '0' and sensorb[2] == '1':
                        pca.channels[0].duty_cycle = left2
                        pca.channels[1].duty_cycle = go
                        print("left2\n\n----")
                    elif sensorb[0] == '1' and sensorb[1] == '1' and sensorb[2] == '1':
                        if sensorf[0] == '1' and sensorf[1] == '1' and sensorf[2] == '1' and sensorb[0] == '1' and sensorb[1] == '0' and sensorb[2] == '0':
                            pca.channels[0].duty_cycle = center
                            pca.channels[1].duty_cycle = stop
                            print("stop\n\n----")
                        else:
                            pca.channels[0].duty_cycle = center
                            pca.channels[1].duty_cycle = go
                            print("go\n\n----")
                    else:
                        pca.channels[0].duty_cycle = center
                        pca.channels[1].duty_cycle = go10
                        print("center\n\n----")
                elif sensorf[0] == '0' and sensorf[1] == '0' and sensorf[2] == '1':
                    if sensorb[0] == '1' and sensorb[1] == '0' and sensorb[2] == '0':
                        pca.channels[0].duty_cycle = right2
                        pca.channels[1].duty_cycle = go
                        print("right2\n\n----")
                    elif sensorb[0] == '0' and sensorb[1] == '1' and sensorb[2] == '0':
                        pca.channels[0].duty_cycle = right3
                        pca.channels[1].duty_cycle = go10
                        print("right3\n\n----")
                    elif sensorb[0] == '0' and sensorb[1] == '1' and sensorb[2] == '1':
                        pca.channels[0].duty_cycle = right2
                        pca.channels[1].duty_cycle = go
                        print("right3\n\n----")
                    elif sensorb[0] == '0' and sensorb[1] == '0' and sensorb[2] == '0':
                        pca.channels[0].duty_cycle = right2
                        pca.channels[1].duty_cycle = go
                        print("right3\n\n----")
                    elif sensorb[0] == '1' and sensorb[1] == '1' and sensorb[2] == '0':
                        pca.channels[0].duty_cycle = right2
                        pca.channels[1].duty_cycle = go
                        print("right3\n\n----")
                    elif sensorb[0] == '0' and sensorb[1] == '0' and sensorb[2] == '1':
                        pca.channels[0].duty_cycle = right2
                        pca.channels[1].duty_cycle = go
                        print("right3\n\n----")
                    else:
                        pca.channels[0].duty_cycle = right2
                        pca.channels[1].duty_cycle = go2
                        print("right2\n\n----")
                elif sensorf[0] == '1' and sensorf[1] == '0' and sensorf[2] == '0':
                    if sensorb[0] == '0' and sensorb[1] == '1' and sensorb[2] == '0':
                        pca.channels[0].duty_cycle = left2
                        pca.channels[1].duty_cycle = go
                        print("left\n\n----")
                    elif sensorb[0] == '1' and sensorb[1] == '0' and sensorb[2] == '0':
                        pca.channels[0].duty_cycle = center
                        pca.channels[1].duty_cycle = go2
                        print("go2\n\n----")
                    elif sensorb[0] == '1' and sensorb[1] == '1' and sensorb[2] == '1':
                        pca.channels[0].duty_cycle = left
                        pca.channels[1].duty_cycle = go2
                        print("left\n\n----")
                    else:
                        pca.channels[0].duty_cycle = left
                        pca.channels[1].duty_cycle = go2
                        print("left\n\n----")
                elif sensorf[0] == '0' and sensorf[1] == '1' and sensorf[2] == '1':
                    if sensorb[0] == '0' and sensorb[1] == '1' and sensorb[2] == '1':
                        pca.channels[0].duty_cycle = right2
                        pca.channels[1].duty_cycle = go
                        print("right2\n\n----")
                    elif sensorb[0] == '0' and sensorb[1] == '1' and sensorb[2] == '0':
                        pca.channels[0].duty_cycle = right2
                        pca.channels[1].duty_cycle = go
                        print("right2\n\n----")
                    elif sensorb[0] == '0' and sensorb[1] == '0' and sensorb[2] == '0':
                        pca.channels[0].duty_cycle = right2
                        pca.channels[1].duty_cycle = go
                        print("right2\n\n----")
                    elif sensorb[0] == '1' and sensorb[1] == '0' and sensorb[2] == '0':
                        pca.channels[0].duty_cycle = right2
                        pca.channels[1].duty_cycle = go0
                        print("right2\n\n----")
                    else:
                        pca.channels[0].duty_cycle = right2
                        pca.channels[1].duty_cycle = go2
                        print("right2\n\n----")
                elif sensorf[0] == '1' and sensorf[1] == '1' and sensorf[2] == '0':
                    if sensorb[0] == '0' and sensorb[1] == '1' and sensorb[2] == '1':
                        pca.channels[0].duty_cycle = left3
                        pca.channels[1].duty_cycle = go2
                        print("left3\n\n----")
                    elif sensorb[0] == '0' and sensorb[1] == '0' and sensorb[2] == '1':
                        pca.channels[0].duty_cycle = left2
                        pca.channels[1].duty_cycle = go2
                        print("left2\n\n----")
                    elif sensorb[0] == '1' and sensorb[1] == '1' and sensorb[2] == '0':
                        pca.channels[0].duty_cycle = center
                        pca.channels[1].duty_cycle = go2
                        print("center\n\n----")
                    elif sensorb[0] == '1' and sensorb[1] == '1' and sensorb[2] == '1':
                        pca.channels[0].duty_cycle = left
                        pca.channels[1].duty_cycle = go
                        print("stop\n\n----")
                    else:
                        pca.channels[0].duty_cycle = left
                        pca.channels[1].duty_cycle = go
                        print("left\n\n----")
                elif sensorf[0] == '1' and sensorf[1] == '1' and sensorf[2] == '1':
                    if sensorb[0] == '1' and sensorb[1] == '1' and sensorb[2] == '1':
                        pca.channels[0].duty_cycle = center
                        pca.channels[1].duty_cycle = stop
                        print("stop\n\n----")
                    elif sensorb[0] == '0' and sensorb[1] == '1' and sensorb[2] == '0':
                        pca.channels[0].duty_cycle = center
                        pca.channels[1].duty_cycle = stop
                        print("stop\n\n----")
                        time.sleep(2)
                    elif sensorb[0] == '0' and sensorb[1] == '0' and sensorb[2] == '0':
                        pca.channels[0].duty_cycle = center
                        pca.channels[1].duty_cycle = stop
                        print("stop\n\n----")
                        time.sleep(2)
                    elif sensorb[0] == '0' and sensorb[1] == '0' and sensorb[2] == '1':
                        pca.channels[0].duty_cycle = center
                        pca.channels[1].duty_cycle = stop
                        print("stop\n\n----")
                    elif sensorb[0] == '0' and sensorb[1] == '1' and sensorb[2] == '1':
                        pca.channels[0].duty_cycle = center
                        pca.channels[1].duty_cycle = stop
                        print("stop\n\n----")
                    else:
                        pca.channels[0].duty_cycle = center
                        pca.channels[1].duty_cycle = stop
                        print("stop\n\n----")
                elif sensorb[0] == '1' and sensorb[1] == '1' and sensorb[2] == '0':
                        pca.channels[0].duty_cycle = right2
                        pca.channels[1].duty_cycle = go
                        print("right2\n\n----")
                elif sensorb[0] == '0' and sensorb[1] == '1' and sensorb[2] == '0':
                        pca.channels[0].duty_cycle = right
                        pca.channels[1].duty_cycle = go0
                        print("right\n\n----")
                elif sensorb[0] == '0' and sensorb[1] == '0' and sensorb[2] == '0':
                        pca.channels[0].duty_cycle = right3
                        pca.channels[1].duty_cycle = go0
                        print("right3\n\n----")
                elif sensorb[0] == '1' and sensorb[1] == '1' and sensorb[2] == '1':
                        pca.channels[0].duty_cycle = right3
                        pca.channels[1].duty_cycle = go
                        print("right3\n\n----")
                else:
                        pca.channels[0].duty_cycle = center
                        pca.channels[1].duty_cycle = stop
                        print("stop1\n\n----")
    f.close()

    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('--log_file_name', metavar= 'K', type=str, nargs=1, help="log file's name")
    args = parser.parse_args()
    logging(args.log_file_name)
