try:
    from PIL import Image
except ImportError:
    import Image

import os, sys

def hasOverlay(filename):
    # returns True if all the pixels in the image are same
    # returns False if otherwise
    img = Image.open(filename).convert('RGB')
    width, height = img.size
    im = img.load()

    i = 0
    (r, g, b) = im[1,1]
    while i<height:
        j = 0
        while j<width:
            if (r, g, b) != im[i,j]:
                return True
            (r, g, b) = im[j,i]
            j = j+1
        i = i+1
    return False
