#!/usr/bin/env python
# coding: utf-8

# 1. What does RGBA stand for?
# 

# In[ ]:


RGBA stand for Red Green Blue Alpha.


# 2. From the Pillow module, how do you get the RGBA value of any images?
# 

# In[ ]:


#import the Image module of PIL into the shell:
from PIL import Image
#create an image object and open the image for reading mode:
im=Image.open('file name','r')
#we use getdata() to extract the pixel value.this scans the image horizontally from left to right starting at the top-left corner.
pix_val = list(im.getdata())


# 3. What is a box tuple, and how does it work?
# 

# In[ ]:


Many of Pillow’s functions and methods take a box tuple argument. This means Pillow is expecting a tuple of four integer coordinates that represent a rectangular region in an image. The four integers are, in order, as follows:

Left The x-coordinate of the leftmost edge of the box.

Top The y-coordinate of the top edge of the box.

Right The x-coordinate of one pixel to the right of the rightmost edge of the box. This integer must be greater than the left integer.

Bottom The y-coordinate of one pixel lower than the bottom edge of the box. This integer must be greater than the top integer.


# 4. Use your image and load in notebook then, How can you find out the width and height of an
# Image object?
# 

# In[ ]:


# import required module
from PIL import Image
  
# get image
filepath = "photo.png"
img = Image.open(filepath)
  
# get width and height
width = img.width
height = img.height


# 5. What method would you call to get Image object for a 100×100 image, excluding the lower-left
# quarter of it?

# In[ ]:


we would call crop() method to get Image object for a 100×100 image, excluding the lower-left
quarter of it


# 6. After making changes to an Image object, how could you save it as an image file?
# 

# In[ ]:


Image.save() Saves this image under the given filename. If no format is specified, the format to use is determined from the filename extension, if possible.


# 7. What module contains Pillow’s shape-drawing code?
# 

# In[ ]:


ImageDraw module contains Pillow’s shape-drawing code


# 8. Image objects do not have drawing methods. What kind of object does? How do you get this kind
# of object?

# In[ ]:


ImageDraw have drawing methods.

# Importing Image and ImageDraw from PIL
from PIL import Image, ImageDraw
  
# Opening the image to be used
img = Image.open('img_path.png')
  
# Creating a Draw object
draw = ImageDraw.Draw(img)


# In[ ]:




