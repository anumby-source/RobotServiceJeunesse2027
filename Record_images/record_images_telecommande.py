import network
import espnow
from machine import Pin, ADC
from time import sleep_ms, ticks_ms
from mac_addr import robot_mac, telecommande_mac
import os
import st7789
import tft_config
import vga2_bold_16x32 as font
#
num =  # numéro du couple robot/telecommande
robotAddr = robot_mac[num]

#
# red, green, blue, white, black = (0, 128, 0), (128, 0, 0), (0, 0, 128), (32, 32, 32), (0, 0, 0)

#
def normalize(x, amp=100):
    ''' resize x -> [-amp;+amp] '''
    x -= midadc
    if x > dzw:
        x = int(amp*(x-dzw)/szw)
    elif x < -dzw:
        x = int(amp*(x+dzw)/szw)
    else:
        x = 0
    return x
#
def constrain(x):
    return min(max(x, -100), 100)
# init display
tft = tft_config.config(3, buffer_size=4096)
tft.init()
# display logo
png_file_name = '/russhughes/demos/Anumby-240x135.png'
tft.png(png_file_name, 0, 0)
sleep_ms(1000)
# init ADC
a0 = ADC(Pin(39, Pin.IN), atten=ADC.ATTN_11DB)
a1 = ADC(Pin(36, Pin.IN), atten=ADC.ATTN_11DB)
midadc = 1730         # adc middle
maxadc = 3150         # adc max
dzw    = 200          # dead zone width
szw    = midadc - dzw # sensitive zone width
samp   = 100
ramp   = 50

# init push buttons
p0, s0   = Pin(0, Pin.IN), True
p35, s35 = Pin(35, Pin.IN), True

# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.STA_IF)  # Or network.AP_IF
sta.active(True)
sta.disconnect()      # For ESP8266

# init espnow
e = espnow.ESPNow()
e.active(True)
print("telecommande.py : Network active, Espnow ok")

try:
    e.add_peer(robotAddr)      # Must add_peer() before send()
except:
    pass
print("telecommande.py : robot added to peers")
#
while True:
    try:
        r, s = a0.read_uv()/1000, a1.read_uv()/1000
        r = normalize(r, ramp)     # r in [-ramp,+ramp]
        s = normalize(s, samp)     # s in [-samp,+samp]
        ls, rs = constrain(s+r), constrain(s-r)
        cmd = 'ml.set_speed(' + str(ls) + ')\r'
        cmd += 'mr.set_speed(' + str(rs) + ')\r'
        e.send(robotAddr, cmd.encode(), False)
#         print(cmd.encode())
        if s0 and (not p0.value()):
            s0 = False
            e.send(robotAddr, 'u.write("record")'.encode(), False)
            print('u.write("record")'.encode())
        elif (not s0) and p0.value():
            s0 = True
        addr, ans = e.recv(0)
        if ans and (addr == robotAddr):
            tft.fill(0)
            tft.text(font, ans, 0, 0)
            print(ans)
        sleep_ms(100)
    except:
#         np[0] = red
#         np.write()
        break
tft.fill(0)
del tft
