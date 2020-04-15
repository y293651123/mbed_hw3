import matplotlib.pyplot as plt
import numpy as np
import serial
import time

t = np.arange(0,10,0.1) 
x = np.arange(0,10,0.1) 
y = np.arange(0,10,0.1)
z = np.arange(0,10,0.1)
tilt = np.arange(0,10,0.1)

serdev = '/dev/ttyACM0'
s = serial.Serial(serdev,115200)
#line=s.readline() # Read an echo string from K66F terminated with '\n'
for i in range(0, int(100)):
    line=s.readline() # Read an echo string from K66F terminated with '\n'
    # print line
    x[i] = float(line)
    line=s.readline() # Read an echo string from K66F terminated with '\n'
    # print line
    y[i] = float(line)
    line=s.readline() # Read an echo string from K66F terminated with '\n'
    # print line
    z[i] = float(line)

for i in range(0, 100):
    if (z[i] < 0.707):
        tilt[i] = 1.0
    else :
        tilt[i] = 0

fig, ax = plt.subplots(2, 1)
ax[0].plot(t,x, color = "blue", linewidth = 1, linestyle = "-", label = "x")
ax[0].plot(t,y, color = "red", linewidth = 1, linestyle = "-", label = "y")
ax[0].plot(t,z, color = "green", linewidth = 1, linestyle = "-", label = "z")
# Show legend
ax[0].legend(loc='lower left', frameon=False)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Acc vector')
for i in range(0, 100) :
    ax[1].plot([i/10, i/10], [0, tilt[i]], color = 'blue', linewidth = 1, linestyle="-") 
    ax[1].scatter([i/10,], [tilt[i],], 70, color = 'blue')
ax[1].plot([0, 10], [0, 0], color = "red", linewidth = 1, linestyle = "-")
ax[1].set_xlabel('Time')
ax[1].set_ylabel('Tilt')
plt.show()
s.close()