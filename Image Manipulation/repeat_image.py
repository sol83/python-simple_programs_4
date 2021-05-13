from simpleimage import SimpleImage

DEFAULT_FILE = 'images/quad.jpg'
NUM_REPEATS = 2

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show the image before the transform
    image.show()
    
    # Create new SimpleImage of correct dimensions
    # TODO: FILL IN THE WIDTH AND HEIGHT BELOW
    final_image = SimpleImage.blank(image.width * NUM_REPEATS, image.height)

    # TODO: your code here
    for i in range(NUM_REPEATS):
        start_x = i * image.width # x coordinate in final_image where image will be applied
        for x in range(image.width):
            for y in range(image.height):
                pixel = image.get_pixel(x, y)
                final_image.set_pixel(start_x + x, y, pixel)
        
    # Show the repeated image
    final_image.show()

def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()
