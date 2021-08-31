import numpy as np
import cv2
import matplotlib.pyplot as plt

h,  w = 540, 956

mtx = np.array([[1.019148736205558748e+03, 0, 4.543907475076335913e+02],[0, 1.025519691143287901e+03, 2.894037118747232284e+02], [0, 0, 1]])
dist = np.array([-4.971605177084769123e-01,1.874575939087049781e-01,-2.658143561773393827e-03,-1.691380333517990709e-03,3.543487326723160913e-01])

newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))

# undistort
mapx,mapy = cv2.initUndistortRectifyMap(mtx,dist,None,newcameramtx,(w,h),5)
print(mapx.shape)
mapx_test = np.zeros((mapx.shape[0], mapx.shape[1]), dtype=np.float32)
mapy_test = np.zeros((mapx.shape[0], mapx.shape[1]), dtype=np.float32)
for i in range(mapx_test.shape[0]):
    mapx_test[i,:] = [x for x in range(mapx_test.shape[1])]

for j in range(mapy_test.shape[1]):
    mapy_test[:,j] = [y for y in range(mapy_test.shape[0])]


mapx_ = mapx_test-mapx

mapy_ = mapy_test-mapy

plt.imshow(mapx)
plt.show()

# cv2.imshow('mapx',mapx_)
# cv2.imshow('mapy',mapy_)
# cv2.waitKey()
