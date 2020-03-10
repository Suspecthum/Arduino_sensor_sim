import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
from drawnow import *
from visual import *

arduinoData = serial.Serial("com5", 115500)
style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
cnt = 0 
sensors = []
error = []

def animate(i):
    error.append(sensors[6])
    ax1.plot(error,len(error))
    
while(1):
    while(arduinoData.inWaiting()==0):
        pass
    
    sensorLine = arduinoData.readline()
    sensorLine = sensorLine.split('\t')
    sensors = [int(sensor) for sensor in sensorLine]    
    
    cnt+=1
    if(cnt > 50):
        error.pop(0)

    ani = animation.FuncAnimation(fig, animate, interval=250)
    
    plt.show()    
        
        
