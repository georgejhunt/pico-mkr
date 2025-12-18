
# Config the SDcard
#%serialconnect /dev/ttyACM0
import os
from machine import Pin, SPI
import sdcard
import sys
dir(os)
#vfs = os.VfsFat()
#vfs.mount(machine.SDCard(), "/sd")
# Initialize SPI for SD card communication
spi = SPI(0, baudrate=10000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
sd_formatted = sdcard.SDCard(spi, Pin(17)) # Initialize SD card object

# Create a FAT filesystem on the SD card
#
#sd_formatted= os.VfsFat.mkfs(sd)
print("sd card formatted FAT")
try:
    os.mount(sd_formatted, "/sd")
    print("SD mounted successfully")
except OSError as e:
    print("Error:",str(e))
    sys.exit(1)

with open("/sd/testfile.txt",'a') as fp:
    for i in range(2):
        fp.write("ANEW george\n")
    fp.close()
with open("/sd/testfile.txt",'r') as f:
    for line in f:
        print(line.strip())
    fp.close()