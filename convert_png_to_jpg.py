from PIL import Image
from os import listdir
from os.path import splitext

target_directory = 'original/'
target = '.jpg'
save_directory = 'original_jpg/'

for file in listdir(target_directory):
    filename, extension = splitext(file)
    im = Image.open(target_directory + filename + extension)
    rgb_im = im.convert('RGB')
    rgb_im.save(save_directory + filename + target, quality=40)

print("Jpgs saved")
