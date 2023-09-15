'''
Conor Weiss
10/13/22
Warhol Image

Show program:
This script should accept as command line arguments a file name and then 
display that file using the graphics Plus libary
'''

#import in the graphics libary and the libary needed for CLI
import graphicsPlus as gp
import sys
import filter as f


def main(argv):

    #check to make sure you have the correct number of arguments
    
    if len(sys.argv) == 2:
        '''
        create a variable to hold the image load it in with the Image 
        method from the imported lib
        '''
        
        pic = gp.Image(gp.Point(0,0),sys.argv[1])
        '''
        create variables for width and height load them with the 
        appropriate methods
        '''
        
        width = pic.getWidth()
        height = pic.getHeight()

        '''
        create a variable to hold a window object and create that object
        with GraphWin()
        '''
        win = gp.GraphWin('User Image',width,height)
        
        
        
        '''
        move the image to the center of the window. The center would be
        1/2 the width and 1/2 the height
        '''
        pic.move(width * 0.5, height * 0.5)
        '''
        draw the image and then call the getMouse method to pause
        '''
        #f.swap_red_blue(pic) #Testing a filter
        #f.sin_bright(pic) #Testing a filter
        #f.pixelate(pic) #Testing a filter
        #f.find_edges(pic) #testing a filter
        #f.sharpen(pic) #Testing a filter
        #f.motion_blur(pic) #testing a filter
        #f.bumpmap(pic) #Testing a filter
        #f.reddify(pic) #Testing a filter

        pic.draw(win)
        win.getMouse()
    
    #print a usage statement if needed
    else:
        print("To use this program to display an image, enter the name of an image file")
        print("on the command line after calling this program.")
        print("\nExample: python3 show.py flowers.ppm")
    
        
        


    
#What's this for?
if __name__ == "__main__":
	main(sys.argv)
