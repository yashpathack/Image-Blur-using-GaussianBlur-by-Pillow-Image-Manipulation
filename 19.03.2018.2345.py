#This is the command line to be implemented
#Scripts and 'imagefilter. Image' will be imported from the PIL
from PIL import ImageFilter, Image

#Note: In this case the image and the 19.03.2018.2345.py are present in the same directory. Therefore I need not to copy the full path for the cause. 
#The image format can vary within JPG/JPEG, PNG and GIF. SVG is under process, for that you can import svglib.svglib
imageame = "thenameoftheimage.jpg"
#Now open the file wrt to the name of the file
image = Image.open(imagename)

#Now we're gonna use Gaussian Blur to blur the image
imageBlur = image.filter(ImageFilter.GaussianBlur (radius=20))
#Radius simply specifies the amount of blur you want in the picture
#You can adjust it as per shown in the readme.
imageBlur.show() #This will just display the blurred image in the .BMP image format
   
#Run the Module. A new file with the specified name will be generated. Adios!

