'''
Conor Weiss
10/13/22
CS 5001, Fall 2022
Lab 6 - Warhol Image

Filter library
Contains filter functions used to manipulate image files

helper functions include:
cap_255 - a function to keep color values between 0 and 255

filters include:
swap_red_blue - swaps red and blue
grey_scale - averages colors to make a greyscale
reddify - adjusts all red values to 255
greenify - adjusts all green values to 255
blueify - adjusts all blue values to 255
saturator - borrows heavily from towardsdatascience.com adjusts color values away from the pixel-mean to make colors more vibrant
sin_bright - applies cross-hatch 2d sine function to make a dotted image
pixelate - applies a "modesty pixelation" to the image
find_edges - borrows heavily from lodev.org - result of transformation that shows just edges
sharpen - borrows heavily from lodev.org - transformation that sharpens edges while retaining image
motion_blur - borrows heavily from lodev.org - transformation that adds a motion-blur effect
bumpmap - borrows heavily from lodev.org - transformation that changes image to an edge-only greyscale.

others include:
format_text - formats text for warhol image
filter_select - uses a number to select a filter to apply to an image.
'''

import graphicsPlus as gp
import sys
import math

'''
cap_255 function
inputs - 1 float
checks whether the value is between 0 and 255.  If it is not, sets the value to lower bound of 0, upper bound of 255.
'''

def cap_255(value):
    if value > 255:
        value = 255
    elif value < 0:
        value = 0
    return value

'''
swap_red_blue function
inputs - 1 Image (as in graphicsPlus library)
swaps the red and blue values in each pixels rgb color value
returns: description of transformation
'''

def swap_red_blue(src_image):
    #iterate over each pixel
    for i in range(src_image.getHeight()):
        for j in range(src_image.getWidth()):
            real_color = src_image.getPixel(j,i)  #Read pixel color values
            src_image.setPixel(j,i,gp.color_rgb(real_color[2],real_color[1],real_color[0])) #write swapped color values back

    print("Red Blue Swap ") #for monitoring progress at command line
    return "Red Blue Swap " #used to generate captions
   
'''
grey_scale function
inputs - 1 image (as in graphicsPlus library)
averages the red, green and blue values in each pixel to create a greyscale image
returns: description of transformation
'''

def grey_scale(src_image):
    for i in range(src_image.getHeight()):
        for j in range(src_image.getWidth()):
            real_color = src_image.getPixel(j,i)
            #greyscale filter sets all rgb values to the average for the pixel to make a same-brightness grey pixel.
            grey_color = gp.color_rgb((real_color[0]+real_color[1]+real_color[2])//3,(real_color[0]+real_color[1]+real_color[2])//3,(real_color[0]+real_color[1]+real_color[2])//3)
            src_image.setPixel(j,i,grey_color)
    
    print("Greyscale ")
    return "Greyscale "

'''
reddify function
inputs - 1 image (as in graphicsPlus library)
Makes all pixels redder
returns description of transformation
'''

def reddify(src_image):
    for i in range(src_image.getHeight()):
        for j in range(src_image.getWidth()):
            real_color = src_image.getPixel(j,i)
            new_red = real_color[0] + (255 - real_color[0])//2
            new_color = gp.color_rgb(new_red,real_color[1],real_color[2])
            src_image.setPixel(j,i,new_color)

    print("Reddened")
    return "Reddened "

'''
greenify function
inputs - 1 image (as in graphicsPlus library)
makes all pixels greener
returns description of transformation
'''

def greenify(src_image):
    for i in range(src_image.getHeight()):
        for j in range(src_image.getWidth()):
            real_color = src_image.getPixel(j,i)
            new_green = real_color[1] + (255 - real_color[1])//2
            new_color = gp.color_rgb(real_color[0],new_green,real_color[2])
            src_image.setPixel(j,i,new_color)

    print("Greened")
    return "Greened "

'''
blueify function
inputs - 1 image (as in graphicsPlus library)
makes all pixels bluer
returns description of transformation
'''

def blueify(src_image):
    for i in range(src_image.getHeight()):
        for j in range(src_image.getWidth()):
            real_color = src_image.getPixel(j,i)
            new_blue = real_color[2] + (255 - real_color[2])//2
            new_color = gp.color_rgb(real_color[0],real_color[1],new_blue)
            src_image.setPixel(j,i,new_color)

    print("Blueified")
    return "Bluefied "

'''
saturator function
inputs - 1 image (as in graphicsPlus library)
uses an algorithm to increase the color saturation of an image
returns: description of transformation
'''

def saturator(src_image):
    for i in range(src_image.getHeight()):
        for j in range(src_image.getWidth()):
            real_color = src_image.getPixel(j,i)
            #get the average of the color values which can be treated as the "brightness"
            pixel_average = (real_color[0] + real_color[1] + real_color[2])//3
            #if a color is brighter than the "brightness", enhance it, otherwise dim it
            new_red = int(cap_255((real_color[0] - pixel_average) + real_color[0]))
            new_green = int(cap_255((real_color[1] - pixel_average) + real_color[1]))
            new_blue = int(cap_255((real_color[2] - pixel_average) + real_color[2]))
            new_color = gp.color_rgb(new_red,new_green,new_blue)
            src_image.setPixel(j,i,new_color)

    print("Saturated")
    return "Saturated "

'''
sin_bright function
inputs - 1 image (as in graphicsPlus library)
uses an algorithm to adjust the brightness of pixels to create a periodic pattern.
returns: description of transformation
'''

def sin_bright(src_image):
    for i in range(src_image.getHeight()):
        for j in range(src_image.getWidth()):
            real_color = src_image.getPixel(j,i)
            #set a brightness change factor by adding two sine waves together
            bright_change = (math.sin(i + j) + math.sin(i - j)) * 100
            #update colors uniformly for the new brightness
            new_red = int(cap_255(real_color[0] + bright_change))
            new_green = int(cap_255(real_color[1] + bright_change))
            new_blue = int(cap_255(real_color[2] + bright_change))
            new_color = gp.color_rgb(new_red, new_green, new_blue)
            src_image.setPixel(j,i,new_color)

    print("Sine Pattern")
    return "Sine Pattern "

'''
pixelate function
inputs - 1 image (as in graphicsPlus library)
uses an algorithm to adjust pixels to provide a modesty blur to an image
returns description of transformation
'''

def pixelate(src_image):
    for i in range(0,src_image.getHeight(),10): #jump down 10 rows each iteration
        j = 0
        for j in range(src_image.getWidth()):
            #only read color values if pixel is in top left of blur-square
            if j%10 == 0:
                pixel_color = gp.color_rgb(src_image.getPixel(j,i)[0],src_image.getPixel(j,i)[1],src_image.getPixel(j,i)[2])
            for k in range(10): #iterate over the 10 rows immediately beneath the current pixel
                if i+k<src_image.getHeight(): #don't write pixels that don't exist in the image, so check if i (current row) + k (added row) is still in image
                    src_image.setPixel(j,i+k,pixel_color) #write over with pixel value from top left of blur-square
    
    print("Pixelated")
    return "Pixelated "

'''
find_edges function
inputs - 1 image, as in graphicsPlus library
uses an algorithm to adjust pixels to highlight edges between shapes.
returns description of transformation
'''

def find_edges(src_image):
    #set a matrix for how neighboring pixel values will be treated in the transformation.  
    #This will remove pixels that are similar to their neighbors, while pixels that are different will remain
    #because the negative numbers surrounding the 8 will not affect the different color of the focus pixel
    filter_matrix = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
    #initialize an empty list to save adjusted pixel color values to
    color_matrix = list()
    #iterated over every pixel
    for i in range(src_image.getHeight()):
        #append a new blank row to our updated pixel values list to match the new row of the image we are reviewing.
        color_matrix.append([])
        for j in range(src_image.getWidth()):
            #initialize empty rgb values for each pixel
            new_red = 0
            new_green = 0
            new_blue = 0
            #walk through the neighboring pixels, multiplying each pixel's rgb value by the corresponding filter matrix element. 
            #Note my for loop will go from -1 to 1, but my list elements are indexed 0 - 2, so I have to add one to the list indicators.
            for k in range(-1,2):
                for l in range(-1,2):
                    if 0 < i + k < src_image.getHeight() and 0 < j + l < src_image.getWidth(): #don't consider pixels that don't exist.
                        real_color = src_image.getPixel(j+l,i+k)
                        #add these values to the rgb values, but do not cap yet.
                        new_red = new_red + real_color[0] * filter_matrix[k+1][l+1]
                        new_green = new_green + real_color[1] * filter_matrix[k+1][l+1]
                        new_blue = new_blue + real_color[2] * filter_matrix[k+1][l+1]
            #once the entire neighborhood is passed through the filter matrix, cap your values and make a new color and save it to your list for later
            new_red = int(cap_255(new_red))
            new_green = int(cap_255(new_green))
            new_blue = int(cap_255(new_blue))
            color_matrix[i].append([new_red,new_green,new_blue])

    #write over your image with the color values saved to your list.
    for i in range(src_image.getHeight()):
        for j in range(src_image.getWidth()):
            new_color = gp.color_rgb(color_matrix[i][j][0],color_matrix[i][j][1],color_matrix[i][j][2])
            src_image.setPixel(j,i,new_color)
    
    print("Edges Highlighted")
    return "Highlighted Edges "
            
'''
sharpen function
inputs - 1 image, as in graphicsPlus library
uses an algorithm to adjust pixels to brighten edges while maintaining original image
returns description of transformation
'''

def sharpen(src_image):
    #sharpen works exactly like find_edges, except central value of matrix is 9 instead of 8.  This means that original pixel will be added one more time
    #this means that the resulting image will have the original image included prominently
    filter_matrix = [[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]
    color_matrix = list()
    for i in range(src_image.getHeight()):
        color_matrix.append([])
        for j in range(src_image.getWidth()):
            new_red = 0
            new_green = 0
            new_blue = 0
            for k in range(-1,2):
                for l in range(-1,2):
                    if 0 < i + k < src_image.getHeight() and 0 < j + l < src_image.getWidth():
                        real_color = src_image.getPixel(j+l,i+k)
                        new_red = new_red + real_color[0] * filter_matrix[k+1][l+1]
                        new_green = new_green + real_color[1] * filter_matrix[k+1][l+1]
                        new_blue = new_blue + real_color[2] * filter_matrix[k+1][l+1]
            new_red = int(cap_255(new_red))
            new_green = int(cap_255(new_green))
            new_blue = int(cap_255(new_blue))
            color_matrix[i].append([new_red,new_green,new_blue])

    for i in range(src_image.getHeight()):
        for j in range(src_image.getWidth()):
            new_color = gp.color_rgb(color_matrix[i][j][0],color_matrix[i][j][1],color_matrix[i][j][2])
            src_image.setPixel(j,i,new_color)

    print("Image Sharpened")
    return "Sharpened "

'''
motion_blur function
inputs - 1 image (as in graphicsPlus library)
uses an algorithm to apply a motion blur affect to the image
returns description of transformation
'''

def motion_blur(src_image):
    #motion_blue works similarly as well, although you can see the matrix is 5x5
    #this gives each pixel elements from pixels in a diagonal line.  If you want non-directional blur, you can make a more general blur matrix
    #or if you want to blur in a different direction, you could set up your matrix with the non-zero values along a different line.
    filter_matrix = [[0.2,0,0,0,0],[0,0.2,0,0,0],[0,0,0.2,0,0],[0,0,0,0.2,0],[0,0,0,0,0.2]]
    color_matrix = list()
    for i in range(src_image.getHeight()):
        color_matrix.append([])
        for j in range(src_image.getWidth()):
            new_red = 0
            new_green = 0
            new_blue = 0
            for k in range(-2,3):
                for l in range(-2,3):
                    if 0 < i + k < src_image.getHeight() and 0 < j + l < src_image.getWidth():
                        real_color = src_image.getPixel(j+l,i+k)
                        new_red = new_red + real_color[0] * filter_matrix[k+2][l+2]
                        new_green = new_green + real_color[1] * filter_matrix[k+2][l+2]
                        new_blue = new_blue + real_color[2] * filter_matrix[k+2][l+2]
            new_red = int(cap_255(new_red))
            new_green = int(cap_255(new_green))
            new_blue = int(cap_255(new_blue))
            color_matrix[i].append([new_red,new_green,new_blue])

    for i in range(src_image.getHeight()):
        for j in range(src_image.getWidth()):
            new_color = gp.color_rgb(color_matrix[i][j][0],color_matrix[i][j][1],color_matrix[i][j][2])
            src_image.setPixel(j,i,new_color)

    print("Motion Blur")
    return "Motion Blur "

'''
bumpmap function
inputs - 1 image, as in graphicsPlus library
uses an algorithm to to make a greyscale image where edges are retained
returns description of transformation
'''

def bumpmap(src_image):
    filter_matrix = [[-1,-1,0],[-1,0,1],[0,1,1]]
    color_matrix = list()
    for i in range(src_image.getHeight()):
        color_matrix.append([])
        for j in range(src_image.getWidth()):
            new_grey = 0
            for k in range(-1,2):
                for l in range(-1,2):
                    if 0 < i + k < src_image.getHeight() and 0 < j + l < src_image.getWidth():
                        real_color = src_image.getPixel(j+l,i+k)
                        new_grey = new_grey + (real_color[0] * filter_matrix[k+1][l+1] + real_color[1] * filter_matrix[k+1][l+1] + real_color[2] * filter_matrix[k+1][l+1])/3
            new_grey = int(cap_255(128 + new_grey))
            color_matrix[i].append([new_grey,new_grey,new_grey])

    for i in range(src_image.getHeight()):
        for j in range(src_image.getWidth()):
            new_color = gp.color_rgb(color_matrix[i][j][0],color_matrix[i][j][1],color_matrix[i][j][2])
            src_image.setPixel(j,i,new_color)

    print("Bumpmap")
    return "Bumpmap "


'''
format_text function
inputs - 1 text object as in graphicsPlus library 
takes a text object and applies my desired formatting to it.
returns: nothing
'''

def format_text(bland_text):
    bland_text.setFace('helvetica')
    bland_text.setSize(12)
    bland_text.setStyle('bold italic')
    bland_text.setTextColor('white')

'''
filter_select function
inputs - 1 image object as in graphicsPlus library, 1 integer between 1 and 8
takes the image and applies the filter selected by the number
returns image caption
'''

def filter_select(image,filter_num):
    if filter_num == 1:
        return swap_red_blue(image)
    elif filter_num == 2:
        return grey_scale(image)
    elif filter_num == 3:
        return reddify(image)
    elif filter_num == 4:
        return greenify(image)
    elif filter_num == 5:
        return blueify(image)
    elif filter_num == 6:
        return saturator(image)
    elif filter_num == 7:
        return sin_bright(image)
    elif filter_num == 8:
        return pixelate(image)

