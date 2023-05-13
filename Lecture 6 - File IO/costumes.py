import sys
from PIL import Image

# a list to store the images
images = []

# loop to iterate through the list of images from the library
for arg in sys.argv[1:]: # sys.argv is a list so we can slice it, starts at 1 and runs till the end
    image = Image.open(arg) # new variable image where we use open() to access the library, arg is the argument in the loop
    images.append(image) # appending to the images list the images stored in the line above (in image)

images[0].save(
    'costumes.gif', save_all = True, append_images = [images[1]], duration = 200, loop = 0
) # grab the 1 of those images (position 0) and save() it to my hard drive...name of image inside, save all frames set,append next image
# by index position, specify duration to 200ms, loop forever (0 meaning not set, so loops infinite number of times)