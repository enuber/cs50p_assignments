from PIL import Image, ImageOps
import sys
import os

def main():
    check_args()
    check_valid_file_type()
    add_shirt()

def check_args():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguements")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguements")
    elif not os.path.exists(sys.argv[1]):
        sys.exit("Invalid input - Path")

def check_valid_file_type():
    valid_extensions = ['jpg', 'jpeg', 'png']
    image_type_1 = sys.argv[1].split(".")[1]
    image_type_2 = sys.argv[2].split(".")[1]

    if image_type_1 not in valid_extensions or image_type_2 not in valid_extensions:
        sys.exit("Invalid input")

    if image_type_1 != image_type_2:
        sys.exit("Input and output have different extensions")

def add_shirt():
    input_image = sys.argv[1]
    output_image = sys.argv[2]
    shirt = Image.open('shirt.png')
    with Image.open(input_image) as img:
        # resize and crop input image to match shirt size
        img_resized = ImageOps.fit(img, shirt.size)
        # put the shirt on the resized input image
        img_resized.paste(shirt, shirt)
        img_resized.save(output_image)

if __name__ == "__main__":
    main()

# check50 cs50/problems/2022/python/shirt
