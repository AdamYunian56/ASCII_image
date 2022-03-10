import PIL.Image

# ASCII characters used to build the output text
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

# resize image according to a new width
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_image = image_resize((new_height, height))
    return(resized_image)
# convert each pixel to grayscale
def grayscale(image):
    grayscale_image = image.convert('L')
    return(grayscale_image)

# convert pixcels to a string of ASCII charactera
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = ''.join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)

def main(new_width=100):
    # attempt to pone image from user-input
    path = input("Enter a valid pathname to an image:\n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "is not a valid pathname to an image\n")

    # convert image to ASCII
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))

    # format
    pixels_count = len(new_image_data)
    ascii_image = '\n'.join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))
     
    # print result
    with open('ascii_image.txt', 'w') as f:
        f.write(ascii_image)

main()