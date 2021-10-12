import numpy as np

numPoints = 10
xs = np.array([-12,-45,-44,20,35,-1,5,-11,42,23])
ys = np.array([50,16,10,11,9,-11,-19,-25,-27,-39])
ts = np.array([10.477,9.759,9.243,4.984,7.499,2.980,4.409,5.817,10.184,9.274])

di = np.zeros(numPoints)

for i in range(numPoints):
    print(i)