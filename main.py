# convert an image into ascii characters
# run MAIN(imagename, newname)  and you are ready to go !

from PIL import Image

CHARS = ['@', "#", "s", "%", '?', '*', '+', ';',':', ',', '.']


def resize_image(image,new_width):
	# resize the image while maintainng its aspect ration
	# IMPORTANT !!
    width,height  = image.size
    ratio = height/width

    new_height = int(new_width * ratio)
    newsize=  new_width,new_height
    print(newsize)
    resized_image = image.resize(newsize)
    return resized_image
    
def grayscale_image(image):
	# grayscale the image
    return image.convert('L')
    


def MAIN(imagepath, new_name , new_width = 100 ):
    new_name = new_name + '.txt'
    try:
        image = Image.open(imagepath)
    except:
        print(f"COULD NOT LOAD IMAGE - {imagepath}")
        return
    new_image = grayscale_image(resize_image(image, new_width))

 	# get the pixels in the image
    pixels = new_image.getdata()

    # generate a string of characters from the pixels depending on color
    # intensity
    characters = "".join([CHARS[pixel//25] for pixel in pixels])
    count = len(characters)

    # make the ascii image  
    ascii_image = "\n".join(characters[i:(i + new_width)] for i in range(0,count,new_width))
    print(ascii_image)

    # write to afile
    with open(new_name, 'w') as file:
        file.write(ascii_image)
        print(new_name , "  saved !!")
    

##  
   
  
