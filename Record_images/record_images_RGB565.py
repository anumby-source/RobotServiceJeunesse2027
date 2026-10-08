import gc
import image
import sensor
from time import sleep
import os
from fpioa_manager import *
from machine import UART
from modules import ws2812
from gc import collect

# init rgb led
led = ws2812(8,100)
r, j, v, b, vi, blk = (250, 0, 0), (200, 32, 0), (0, 128, 0),(0, 0, 250), (128, 0, 128), (0, 0, 0)
leds = (r, j, v, b, vi)


# init UART
fm.register(34, fm.fpioa.UART1_TX, force=True)
fm.register(35, fm.fpioa.UART1_RX, force=True)
u = UART(UART.UART1, 115200)

def findMaxIDinDir(dirname):
    larNum = -1
    try:
        dirList = os.listdir(dirname)
        for fileName in dirList:
            currNum = int(fileName.split(".jpg")[0])
            if currNum > larNum:
                larNum = currNum
        return larNum
    except:
        return 0


def initialize_camera():
    while 1:
        try:
            sensor.reset() # Reset sensor may failed, let's try some times
            break
        except:
            sleep(0.1)
            continue
    sensor.set_pixformat(sensor.RGB565)
    sensor.set_framesize(sensor.QVGA)      #QVGA=320x240
    sensor.set_windowing((224, 224))
    sensor.run(1)

initialize_camera()

currentDirectory = 1
u.write("Class 1\n")

if "sd" not in os.listdir("/"):
    print("Error: Cannot read SD Card")

try:
    os.mkdir("/sd/images")
except Exception as e:
    pass

try:
    currentImage = findMaxIDinDir("/sd/images/" + str(currentDirectory)) + 1
except:
    currentImage = 0
    pass

try:
    while True:
        collect()
        led.set_led(0, blk)
        led.display()
        cmd = u.read()
        if cmd == b'record':
            img = sensor.snapshot()
            led.set_led(0, r)
            led.display()
            try:
                if str(currentDirectory) not in os.listdir("/sd/images"):
                    try:
                        os.mkdir("/sd/images/" + str(currentDirectory))
                    except:
                        pass
                photo = img.save("/sd/images/" + str(currentDirectory) + "/" + str(currentImage) + ".jpg", quality=95)
                u.write("/sd/images/" + str(currentDirectory) + "/" + str(currentImage) + "\n")
            except:
                u.write("Write Error\n")
                sleep(1)

            currentImage = currentImage + 1

        elif cmd == b'change':
            led.set_led(0, b)
            led.display()
            currentDirectory = currentDirectory + 1
            if currentDirectory == 11:
                currentDirectory = 1
            currentImage = findMaxIDinDir("/sd/images/" + str(currentDirectory)) + 1
            u.write("Class " + str(currentDirectory) + "\n")

except KeyboardInterrupt:
    pass
