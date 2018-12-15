try:
    from PIL import Image
except ImportError:
    import Image

import os, sys

img_black = Image.open('filtered/solid_000000.png').convert('RGB')
img_white = Image.open('filtered/solid_FFFFFF.png').convert('RGB')

img_black_original = Image.open('original/solid_000000.png').convert('RGB')
img_white_original = Image.open('original/solid_FFFFFF.png').convert('RGB')

img_checker_bw_0 = Image.open('filtered/checker_bw_0.png').convert('RGB')
img_checker_bw_1 = Image.open('filtered/checker_bw_1.png').convert('RGB')
img_horiz_bw_stripes_0 = Image.open('filtered/horiz_bw_stripes_0.png').convert('RGB')
img_horiz_bw_stripes_1 = Image.open('filtered/horiz_bw_stripes_1.png').convert('RGB')
img_vert_bw_stripes_0 = Image.open('filtered/vert_bw_stripes_0.png').convert('RGB')
img_vert_bw_stripes_1 = Image.open('filtered/vert_bw_stripes_1.png').convert('RGB')


img_checker_bw_0_jpg = Image.open('original_jpg/checker_bw_0.jpg').convert('RGB')
img_checker_bw_1_jpg = Image.open('original_jpg/checker_bw_1.jpg').convert('RGB')
img_horiz_bw_stripes_0_jpg = Image.open('original_jpg/horiz_bw_stripes_0.jpg').convert('RGB')
img_horiz_bw_stripes_1_jpg = Image.open('original_jpg/horiz_bw_stripes_1.jpg').convert('RGB')
img_vert_bw_stripes_0_jpg = Image.open('original_jpg/vert_bw_stripes_0.jpg').convert('RGB')
img_vert_bw_stripes_1_jpg = Image.open('original_jpg/vert_bw_stripes_1.jpg').convert('RGB')

img = Image.new('RGB', (1080, 1080), color = 'white')

def generate_color_error(error):
    # A simple function that transforms counted error into color pixel representation
    return (int((error/10)*256), 0, 255)

def count_error(pixel1, pixel2):
    # used to count difference between two given pixels
    # returns average of errors for each color channel
    (r1, g1, b1) = pixel1
    (r2, g2, b2) = pixel2
    error_red = ((abs(r1-r2) / 255)*100)
    error_green = ((abs(g1-g2) / 255)*100)
    error_blue = ((abs(b1-b2) / 255)*100)
    return (error_red + error_green + error_blue)/3

def check_error_checker_image(image, img_check1, img_check2, img, error_image_name):
    # used generating error images for checker_image
    # images are generated into folder error_images    
    width, height = image.size
    im = image.load()
    im_check1 = img_check1.load()
    im_check2 = img_check2.load()

    test = img.load()

    error_sum = 0
    count = 0
    max_error = 0
    for x in range(0, width, 2):
        for y in range(0, width, 2):
            current_error = count_error(im[x,y], im_check1[x,y])
            if current_error > max_error:
                max_error = current_error
            error_sum += current_error
            count = count + 1
            test[x, y] = generate_color_error(current_error)
    error1 = error_sum/count
    
    error_sum = 0
    count = 0    
    for x in range(1, width, 2):
        for y in range(1, width, 2):
            current_error = count_error(im[x,y], im_check1[x,y])
            error_sum += current_error
            count = count + 1
            test[x, y] = generate_color_error(current_error)
    error2 = error_sum/count
    
    error_im_check1 = (error1 + error2)/2
    print(error_im_check1)
    
    error_sum = 0
    count = 0
    for x in range(0, width, 2):
        for y in range(1, width, 2):
            current_error = count_error(im[x,y], im_check2[x,y])
            error_sum += current_error
            count = count + 1
            test[x, y] = generate_color_error(current_error)
    error1 = error_sum/count

    error_sum = 0
    count = 0 
    for x in range(1, width, 2):
        for y in range(0, width, 2):
            current_error = count_error(im[x,y], im_check2[x,y])
            error_sum += current_error
            count = count + 1
            test[x, y] = generate_color_error(current_error)
    error2 = error_sum/count
    
    error_im_check2 = (error1 + error2)/2

    print(error_im_check2)

    ####
    img.save('error_images/' + error_image_name)
    ####
    
    return (error_im_check1 + error_im_check2)/2

def check_error_ver_stripes(image, img_check1, img_check2, img, error_image_name):
    # used generating error images for ver_stripes
    width, height = image.size
    im = image.load()
    im_check1 = img_check1.load()
    im_check2 = img_check2.load()
    test = img.load()

    error_sum = 0
    count = 0
    for x in range(0, width, 2):
        for y in range(height):
            current_error = count_error(im[x,y], im_check1[x,y])
            error_sum += current_error
            count = count + 1
            test[x, y] = generate_color_error(current_error)
    error1 = error_sum/count

    error_sum = 0
    count = 0
    for x in range(1, width, 2):
        for y in range(height):
            current_error = count_error(im[x,y], im_check2[x,y])
            error_sum += current_error
            count = count + 1
            test[x, y] = generate_color_error(current_error)
    error2 = error_sum/count

    ####
    img.save('error_images/' + error_image_name)
    ####

    return (error1 + error2)/2

def check_error_horiz_stripes(image, img_check1, img_check2, img, error_image_name):
    # used generating error images for horiz_stripes
    width, height = image.size
    im = image.load()
    im_check1 = img_check1.load()
    im_check2 = img_check2.load()
    test = img.load()

    error_sum = 0
    count = 0
    for x in range(width):
        for y in range(0, height, 2):
            current_error = count_error(im[x,y], im_check1[x,y])
            error_sum += current_error
            count = count + 1
            test[x, y] = generate_color_error(current_error)
    error1 = error_sum/count

    error_sum = 0
    count = 0
    for x in range(width):
        for y in range(1, height, 2):
            current_error = count_error(im[x,y], im_check2[x,y])
            error_sum += current_error
            count = count + 1
            test[x, y] = generate_color_error(current_error)
    error2 = error_sum/count

    ####
    img.save('error_images/' + error_image_name)
    ####

    return (error1 + error2)/2

print('Error on image img_checker_bw_0 = ' + str(check_error_checker_image(img_checker_bw_0, img_white, img_black, img, 'checker_bw_0_error.png')) + '%')
print('Error on image img_checker_bw_1 = ' + str(check_error_checker_image(img_checker_bw_1, img_black, img_white, img, 'checker_bw_1_error.png')) + '%')

print('Error on image horiz_bw_stripes_0 = ' + str(check_error_horiz_stripes(img_horiz_bw_stripes_0, img_black, img_white, img, 'horiz_bw_stripes_0_error.png')) + '%')
print('Error on image horiz_bw_stripes_1 = ' + str(check_error_horiz_stripes(img_horiz_bw_stripes_1, img_white, img_black, img, 'horiz_bw_stripes_1_error.png')) + '%')

print('Error on image ver_bw_stripes_0 = ' + str(check_error_ver_stripes(img_vert_bw_stripes_0, img_black, img_white, img, 'ver_bw_stripes_0.png')) + '%')
print('Error on image ver_bw_stripes_1 = ' + str(check_error_ver_stripes(img_vert_bw_stripes_1, img_white, img_black, img, 'ver_bw_stripes_1.png')) + '%')

print('Error on image img_checker_bw_0_jpg = ' + str(check_error_checker_image(img_checker_bw_0_jpg, img_white_original, img_black_original, img, 'checker_bw_0_error_jpg.png')) + '%')
print('Error on image img_checker_bw_1_jpg = ' + str(check_error_checker_image(img_checker_bw_1_jpg, img_black_original, img_white_original, img, 'checker_bw_1_error_jpg.png')) + '%')

print('Error on image horiz_bw_stripes_0_jpg = ' + str(check_error_horiz_stripes(img_horiz_bw_stripes_0_jpg, img_black_original, img_white_original, img, 'horiz_bw_stripes_0_error_jpg.png')) + '%')
print('Error on image horiz_bw_stripes_1_jpg = ' + str(check_error_horiz_stripes(img_horiz_bw_stripes_1_jpg, img_white_original, img_black_original, img, 'horiz_bw_stripes_1_error_jpg.png')) + '%')

print('Error on image ver_bw_stripes_0_jpg = ' + str(check_error_ver_stripes(img_vert_bw_stripes_0_jpg, img_black_original, img_white_original, img, 'ver_bw_stripes_0_jpg.png')) + '%')
print('Error on image ver_bw_stripes_1_jpg = ' + str(check_error_ver_stripes(img_vert_bw_stripes_1_jpg, img_white_original, img_black_original, img, 'ver_bw_stripes_1_jpg.png')) + '%')





