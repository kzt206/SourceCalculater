import numpy as np

# 計算回数と最大値の設定
numCal = 0
maxCal = 10

# 計算グリッドの設定
grid = np.array([0.01,0.01,0.01,0.01])
dx = 0.1
dy = 0.1
dz = 0.
dt = 0.01

# 地震計の位置と観測された地震波の到達時間の設定
numPoints = 10
xs = np.array([-12,-45,-44,20,35,-1,5,-11,42,23])
ys = np.array([50,16,10,11,9,-11,-19,-25,-27,-39])
zs = np.zeros(numPoints)
ts = np.array([10.477,9.759,9.243,4.984,7.499,2.980,4.409,5.817,10.184,9.274])


di = np.zeros(numPoints)
dd = np.zeros(numPoints)

# print(g)

# 震源の位置と時刻の初期値を設定
mi = np.array([-10,10,20,0]) # set a temporal initial source 

#地震波速度
V = 5 #km/s

# 更新回数が設定回数を上回った？
while numCal < maxCal:
    print("\nnumCal: " + str(numCal) )
    G = np.zeros((numPoints,4))
    # 予測される地震波の到達時刻の計算
    di = np.sqrt(np.square(xs-mi[0]) + np.square(ys-mi[1]) + np.square(zs-mi[2])) /V + mi[3]
    print(di)

    # 観測との差を計算
    dd = ts - di 
    print(dd)

    # 行列Gを求める G(i,j) = d(di)/d(mj)
    # mi_0 = mi + np.array([dx,0,0,0])
    # di_0 = np.sqrt(np.square(xs-mi_0[0]) + np.square(ys-mi_0[1]) + np.square(zs-mi_0[2])) /V + mi_0[3]
    # G[:,0] = (di_0 - di) / dx
    # print("G:")
    # print(G[:,0])

    # print("j:")
    for j in range(4):
        # print(j)
        grid_tmp = np.zeros(4)
        grid_tmp[j] = grid[j]
        # print(grid_tmp)
        mi_tmp = mi + grid_tmp
        di_tmp = np.sqrt(np.square(xs-mi_tmp[0]) + np.square(ys-mi_tmp[1]) + np.square(zs-mi_tmp[2])) /V + mi_tmp[3]
        if grid[j] != 0:
            G[:,j] = (di_tmp - di) / grid[j]
        else:
            G[:,j] = 0
    print("G:")
    print(G)

    # 正方行列　GtG を求める
    Gt = G.transpose()
    print("Gt:")
    print(Gt)
    GtG = np.dot(Gt,G)
    print("GtG:")
    print(GtG)


    # (GtG)-1　を求める
    invGtG = np.linalg.inv(GtG)
    print("invGtG")
    print(invGtG)

    # dm = (GtG)-1 Gt Ddを求める
    dm = np.dot(invGtG,(np.dot(Gt,dd)))
    print("dm:")
    print(dm)

    # dmを使って震源の位置と時刻の値を更新する
    mi = mi+dm
    print("mi:")
    print(mi)

    # dmの絶対値はゼロに近い？　ー＞　おわり
    if np.max(dm) < 1.e-5:
        print("Calculation end")
        break

    numCal += 1