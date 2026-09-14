import sensor
import gc
import os
from modules import ws2812
from machine import UART
from time import sleep
from fpioa_manager import fm

########################################
def getNewDataFileNumber():

    newnum = 0
    for file in os.listdir():
        if file[:4] == 'img_' and file[-4:] == '.dat':
            num = int(file[4:-4])
            if num >= newnum:
                newnum = num + 1
    return newnum

# init rgb led
led = ws2812(8,100)
r, j, v, b, vi, blk = (250, 0, 0), (200, 32, 0), (0, 128, 0),(0, 0, 250), (128, 0, 128), (0, 0, 0)
leds = (r, j, v, b, vi)

# init camera
sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QVGA)

# init UART
fm.register(34, fm.fpioa.UART1_TX, force=True)
fm.register(35, fm.fpioa.UART1_RX, force=True)
u = UART(UART.UART1, 115200)

# image counter
num = getNewDataFileNumber()

# process images
while True:
    try:
        if u.read() == b'record':
            led.set_led(0, r)
            led.display()
            img = sensor.snapshot()
            fd = open('img_{:04d}.dat'.format(num), 'wb')
            fd.write(img)
            fd.close()
            u.write(str(num) + '\n')
            num += 1
            sleep(1)
            led.set_led(0, blk)
            led.display()
    except:
        u.write('error\n')
