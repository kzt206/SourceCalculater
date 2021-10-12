import numpy as np

# 計算回数と最大値の設定
numCal = 1
maxCal = 10

# 地震計の位置と観測された地震波の到達時間の設定
numPoints = 10
xs = np.array([-12,-45,-44,20,35,-1,5,-11,42,23])
ys = np.array([50,16,10,11,9,-11,-19,-25,-27,-39])
zs = np.zeros(numPoints)
ts = np.array([10.477,9.759,9.243,4.984,7.499,2.980,4.409,5.817,10.184,9.274])


di = np.zeros(numPoints)
dd = np.zeros(numPoints)
g = np.zeros((numPoints,4))
# print(g)

# 震源の位置と時刻の初期値を設定
mi = np.array([-10,10,20,0]) # set a temporal initial source 

#地震波速度
V = 5 #km/s

while numCal < maxCal:
    print("\nnumCal: " + str(numCal) )
    # 予測される地震波の到達時刻の計算
    di = np.sqrt(np.square(xs-mi[0]) + np.square(ys-mi[1]) + np.square(zs-mi[2])) /V + mi[3]
    print(di)

    # 観測との差を計算
    dd = ts - di 
    print(dd)

    numCal += 1