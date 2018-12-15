from PIL import Image
from os import listdir
from os.path import splitext

target_directory = 'filtered_jpeg/'
target = '.png'
save_directory = 'filtered/'

for file in listdir(target_directory):
    filename, extension = splitext(file)
    im = Image.open(target_directory + filename + extension)
    im.save(save_directory + filename + target)

print("Pngs saved")

