import serial
import numpy as np
import matplotlib.pyplot as plt
from drawnow import *
from visual import *

arduinoData = serial.Serial("com4",115200)
hcData = []
plt.ion() #Tell matplotlib to enable interactive mode.
cnt = 0 ;
def makeFig():
   plt.plot(hcData,"ro-") 

while(1):
    while (arduinoData.inWaiting == 0):
        pass #if there is no data do nothing
    
    dataString = arduinoData.readline()
    dataNow = float(dataString)
    print dataNow
    hcData.append(dataNow)
    drawnow(makeFig)
    cnt+=1
    if(cnt>50):
        hcData.pop(0)
    plt.pause(.000001)
        
