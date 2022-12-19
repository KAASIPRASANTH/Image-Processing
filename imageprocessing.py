# -*- coding: utf-8 -*-
"""ImageProcessing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HaI65_rNJhsoKaW2Wq5MlUvDZSDafE80

**Topics:**
1. Reading an image file and converting it to numpy array
2. Resizing an image
3. Copying an image
4. Transposing an image
5. RGB image to Grayscale conversion
6. RGB image other color images
"""

#getting an image by using web get:

!wget 'https://www.1800flowers.com/blog/wp-content/uploads/2015/10/red-roses.jpg'

"""**Libraries for image processing**
1. matplotlib.image
2. pillow (PIL)
3. openCV (cv2)


"""

import matplotlib.image as mpimg

#for displaying an image
import matplotlib.pyplot as plt

#Loading an image by using matplotlib.image
img1 = mpimg.imread('/content/Rose.jpg')

#knowing an type of an image like-array structure
type(img1)

#shape of an image
print(img1.shape)

#(649,900,3) for RGB image 3 color channels

#if we print it , it will show the numpy array
print(img1)

#displaying an image from numpy array
img1_as_image = plt.imshow(img1)
plt.show()

"""Resizing an image by using pillow"""

from PIL import Image

#opening an Image
img2 = Image.open('/content/Rose.jpg')
img2_resized = img2.resize((300,300))

"""**Properties of image**

"""

print(img2_resized.size)
print(img2_resized.format)
print(img2_resized.mode)

#saving resized image
img2_resized.save('Rose_resized1.jpg')

#by using matplotlib.pyplot as plt
img = mpimg.imread('/content/Rose_resized1.jpg')
img_plt = plt.imshow(img)
plt.show()

print(img.shape)

"""**Copying Image**"""

copied_image = img.copy()
plt.imshow(copied_image)

"""**Transposing Image**
1. FLIP_LEFT_RIGHT (This inverse the rows of image) ->0
2. FLIP_TOP_BOTTOM (This inverse the columns of image) ->1
3. ROTATE_90 (This rotates the image by angle of 90) ->2
4. ROTATE_180 (This rotates the image by angle of 180) ->3
5. ROTATE_270 (This rotates the image by angle of 270) ->4
6. TRANSPOSE (This convert the rows into columns)->5
"""

img = Image.open('/content/Rose_resized1.jpg')
transpose_img1 = img.transpose(Image.TRANSPOSE)
plt.imshow(transpose_img1)

"""Converting RGB images to Grayscale image using **openCV**"""

import cv2

img3 = cv2.imread('/content/Rose.jpg')

type(img3)

print(img3.shape)

grayscale_image = cv2.cvtColor(img3,cv2.COLOR_RGB2GRAY)

print(grayscale_image.shape)

#displaying an image
from google.colab.patches import cv2_imshow
cv2_imshow(grayscale_image)

#saving grayScale_image using cv2
cv2.imwrite('grayscale_image1.jpg',grayscale_image)

"""**Converting images to other colors**"""

grayscale_image = cv2.cvtColor(img3,cv2.COLOR_RGB2HLS)

cv2_imshow(grayscale_image)

grayscale_image = cv2.cvtColor(img3,cv2.COLOR_RGB2HLS_FULL)

cv2_imshow(grayscale_image)

img3 = cv2.imread('/content/Rose.jpg')