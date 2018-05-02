import numpy as np
import scipy.ndimage as nd
import time

# X = np.random.rand(25, 224, 224, 3)
# X = nd.zoom(X, (1, 1.2, 1.2, 1))
# print(X.shape)


def crop_center(img, cropx, cropy):
    y, x, channels = img.shape
    startx = x//2-(cropx//2)
    starty = y//2-(cropy//2)
    return img[starty:starty+cropy, startx:startx+cropx, :]


# X = crop_center(X, 224, 224)
# print(X.shape)


# start = time.time()
# X = np.random.rand(1, 25, 224, 224, 3)
# X = nd.zoom(X, (1, 1, 1.2, 1.2, 1))
# print(X.shape)
# finish = time.time()
# print("time for 5 d", finish-start)
start = time.time()
X = np.random.rand(224, 224, 3)
X = nd.zoom(X, (1.2, 1.2, 1))
print(X.shape)
print("time for 3 d", time.time() - start)

start = time.time()
X = np.random.rand(1, 25, 224, 224, 3)
for i in range(25):
    Y = X[0][i]
    Y = nd.zoom(Y, (1.2, 1.2, 1))
    Y = crop_center(Y, 224, 224)
    X[0][i] = Y
print("time for 25 frames 3d", time.time() - start)
print(X.shape)