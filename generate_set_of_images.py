import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from skimage import color
from skimage import img_as_float, img_as_ubyte

imgsize = (1080, 1080)

test_images = dict()

print("Generating set of solid color images")
test_images["solid_FFFFFF"] = np.ones((imgsize[0], imgsize[1], 3))
test_images["solid_000000"] = np.zeros((imgsize[0], imgsize[1], 3))
test_images["solid_0000FF"] = np.ones((imgsize[0], imgsize[1], 3)) * [0.0, 0.0, 1.0]
test_images["solid_00FF00"] = np.ones((imgsize[0], imgsize[1], 3)) * [0.0, 1.0, 0.0]
test_images["solid_FF0000"] = np.ones((imgsize[0], imgsize[1], 3)) * [1.0, 0.0, 0.0]

print("Generating set of separated color planes")
test_images["rg_plane"] = np.ones((imgsize[0], imgsize[1], 3),np.uint8)
test_images["gb_plane"] = np.ones((imgsize[0], imgsize[1], 3),np.uint8)
test_images["rb_plane"] = np.ones((imgsize[0], imgsize[1], 3),np.uint8)

for x in range(0, imgsize[0]):
    for y in range(0, imgsize[1]):
        test_images["rg_plane"][x, y, :] *= [np.uint8(x % 256), np.uint8(y % 256), np.uint8(0)]
        test_images["gb_plane"][x, y, :] *= [np.uint8(0), np.uint8(x % 256), np.uint8(y % 256)]
        test_images["rb_plane"][x, y, :] *= [np.uint8(x % 256), np.uint8(0), np.uint8(y % 256)]

print("Generating set of checker images")
grid = np.ogrid[0:imgsize[0], 0:imgsize[1]]
test_images["checker_bw_0"] = color.gray2rgb(((grid[0] + grid[1]) % 2) == 0)
test_images["checker_bw_1"] = color.gray2rgb(((grid[0] + grid[1]) % 2) != 0)

print("Generating set of stripe images")
test_images["horiz_bw_stripes_0"] = np.ones((imgsize[0], imgsize[1], 3))
test_images["horiz_bw_stripes_1"] = np.zeros((imgsize[0], imgsize[1], 3))
for x in range(0, imgsize[0], 2):
    test_images["horiz_bw_stripes_0"][x,:,:] = 0.0
    test_images["horiz_bw_stripes_1"][x,:,:] = 1.0

test_images["vert_bw_stripes_0"] = np.ones((imgsize[0], imgsize[1], 3))
test_images["vert_bw_stripes_1"] = np.zeros((imgsize[0], imgsize[1], 3))
for y in range(0, imgsize[0], 2):
    test_images["vert_bw_stripes_0"][:,y,:] = 0.0
    test_images["vert_bw_stripes_1"][:,y,:] = 1.0

print("Saving...")
for name, img in test_images.items():
    plt.imsave('original/' + name + '.png', img_as_ubyte(img))
print("Done")
