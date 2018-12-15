import matplotlib.pyplot as plt
try:
    from PIL import Image
except ImportError:
    import Image

import cv2 

img_original_rb = Image.open('original/rb_plane.png').convert('RGB')
img_filtered_rb = Image.open('filtered/rb_plane.png').convert('RGB')
im_original_rb = img_original_rb.load()
im_filtered_rb = img_filtered_rb.load()

img_original_rg = Image.open('original/rg_plane.png').convert('RGB')
img_filtered_rg = Image.open('filtered/rg_plane.png').convert('RGB')
im_original_rg = img_original_rg.load()
im_filtered_rg = img_filtered_rg.load()

img_original_gb = Image.open('original/gb_plane.png').convert('RGB')
img_filtered_gb = Image.open('filtered/gb_plane.png').convert('RGB')
im_original_gb = img_original_gb.load()
im_filtered_gb = img_filtered_gb.load()

def countDiference(original_image, filtered_image, inverse, color):
    x1, y1 = [],[]
    values = []
    for j in range(0, 256, 16):
        x1, y1 = [], []
        for i in range(0, 256, 16):
            if (inverse == False):
                (r1, g1, b1) = original_image[j, i]
                (r2, g2, b2) = filtered_image[j, i]
            else:
                (r1, g1, b1) = original_image[i, j]
                (r2, g2, b2) = filtered_image[i, j]

            if (color == "red"):
                a1 = r1
                a2 = r2
            elif (color == "green"):
                a1 = g1
                a2 = g2
            else:
                a1 = b1
                a2 = b2                
            x1.append(a1)
            y1.append(a2)
        touple = (x1, y1)

        values.append(touple)
    return values
        
def generateGraph(title, color_of_image, values):
    plt.xlabel('original')
    plt.ylabel('filtered')
    plt.title(title)

    for i in range(0, len(values)):
        x, y = values[i]
        plt.plot(x, y, color=color_of_image)
    plt.show()
    return

def generateOppositeGraphs(color1, color2, values1, values2):
    title = "Dependency of " + color1 + " channel on " + color2 + " channel and VV"
    plt.xlabel('original')
    plt.ylabel('filtered')
    plt.title(title)

    for i in range(0, len(values1)):
        x, y = values1[i]
        plt.plot(x, y, color=color1)

    for i in range(0, len(values2)):
        x, y = values2[i]
        plt.plot(x, y, color=color2)

    plt.show()
    return
  

generateGraph("Dependency of red channel on blue channel", "red", countDiference(im_original_rb, im_filtered_rb, False, "red"))
generateGraph("Dependency of red channel on green channel", "red", countDiference(im_original_rg, im_filtered_rg, False, "red"))
generateGraph("Dependency of green channel on blue channel", "green", countDiference(im_original_gb, im_filtered_gb, False, "green"))
generateGraph("Dependency of green channel on red channel", "green", countDiference(im_original_rg, im_filtered_rg, True, "green"))
generateGraph("Dependency of blue channel on red channel", "blue", countDiference(im_original_rb, im_filtered_rb, True, "blue"))
generateGraph("Dependency of blue channel on green channel", "blue", countDiference(im_original_gb, im_filtered_gb, True, "blue"))

generateOppositeGraphs("red", "blue", countDiference(im_original_rb, im_filtered_rb, False, "red"), countDiference(im_original_rb, im_filtered_rb, True, "blue"))
generateOppositeGraphs("red", "green", countDiference(im_original_rg, im_filtered_rg, False, "red"), countDiference(im_original_rg, im_filtered_rg, True, "green"))
generateOppositeGraphs("green", "blue", countDiference(im_original_gb, im_filtered_gb, False, "green"), countDiference(im_original_gb, im_filtered_gb, True, "blue"))

