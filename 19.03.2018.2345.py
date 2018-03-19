#This is the command line to be implemented
#Scripts and 'imagefilter. Image' will be imported from the PIL
from PIL import Image

#Note: In this case the image and the 19.03.2018.2345.py are present in the same directory. Therefore I need not to copy the full path for the cause. 
#The image format can vary within JPG/JPEG, PNG and GIF. SVG is under process, for that you can import svglib.svglib
pic = "thenameoftheimage.gif"

#The Navigator opens the picture.
photo = Image.open(pic)

#Changing the mode from RGBA
if photo.mode == "RGBA":
   
   #To RGB
   photo = photo.convert("RGB")
   
#Assignage of new file generated   
picv2 = "thenameoftheimage.pdf"

if not os.path.exists(picv2):
   #Set the resolution and initialize the Portable Document Format
    photo.save(picv2, "PDF", resolution = 100.0)

#Run the Module. A new file with the specified name will be generated. Open it with any of the pdf reader. Adios!

