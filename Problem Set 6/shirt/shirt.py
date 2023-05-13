import sys
from os.path import splitext
from PIL import Image, ImageOps


# Main engine
def main():
    check_command_line()
    # To open the image
    try:
        img_file = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit('Input does not exist')
    # To open shirt image
    shirt_file = Image.open('shirt.png')

    # To get the size of the shirt
    size = shirt_file.size

    # To resize the muppet so it fits the shirt
    muppet = ImageOps.fit(img_file, size)

    # To add the shirt to the muppet
    muppet.paste(shirt_file, shirt_file)

    # To save the output image of our work
    muppet.save(sys.argv[2]) # that's the file in the second position




# Conditions

def check_command_line():
    # check how many arguments in CL
    if len(sys.argv) < 3:
        sys.exit('Too few command line arguments')
    if len(sys.argv) > 3:
        sys.exit('Too many command line arguments')
    file_one = splitext(sys.argv[1])
    file_two = splitext(sys.argv[2])
# make sure each image file has the correct file extention
    if verify_extension(file_one[1]) == False or verify_extension(file_two[1]) == False:
        sys.exit('Invalid input')
# make sure the extension of both files are the same
    if file_one[1].lower() != file_two[1].lower():
        sys.exit('Input and output have different extensions')



# check if extensions of each of the files match
def verify_extension(file):
    if file in ['.jpg', '.png', '.jpeg']:
        return True
    else:
        return False


if __name__ == '__main__':
    main()