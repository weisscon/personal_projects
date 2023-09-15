'''
Conor Weiss
10/13/22
Warhol Image

Creates a warhol art like image in a 2 by 3 grid pattern
Image filter algorithms more complex
'''
import sys
import filter as f
import graphicsPlus as gp
import random

'''
Accepts a ppm image name and then generates the graphic using filters
from filter.py. 

Prints a usage message if the incorrect number of args are given
'''


def main(argv):
   if len(sys.argv) == 2: #correct number of arguments on the command line
      
      image_title = sys.argv[1].split('.')[0]
      print(image_title)

      #load your image
      primary_image = gp.Image(gp.Point(0,0),sys.argv[1])

      #get height and width
      image_width = primary_image.getWidth()
      image_height = primary_image.getHeight()

      #create copies to filter
      #rb_swap_image = primary_image.clone()
      #sined_image = primary_image.clone()
      #saturated_image = primary_image.clone()

      image_copy_1 = primary_image.clone()
      image_copy_2 = primary_image.clone()
      image_copy_3 = primary_image.clone()
      image_copy_4 = primary_image.clone()
      image_copy_5 = primary_image.clone()

      image_list = [image_copy_1,image_copy_2,image_copy_3,image_copy_4,image_copy_5]

      #create window
      window = gp.GraphWin("Extension " + image_title, image_width * 3, image_height * 2)

      #move primary image to upper left region
      primary_image.move(image_width * 0.5, image_height * 0.5)

      #move images to be filtered toother regions
      #rb_swap_image.move(image_width * 1.5, image_height * 0.5)
      #sined_image.move(image_width * 0.5, image_height * 1.5)
      #saturated_image.move(image_width * 1.5, image_height * 1.5)
      image_copy_1.move(image_width * 1.5, image_height * 0.5)
      image_copy_2.move(image_width * 2.5, image_height * 0.5)
      image_copy_3.move(image_width * 0.5, image_height * 1.5)
      image_copy_4.move(image_width * 1.5, image_height * 1.5)
      image_copy_5.move(image_width * 2.5, image_height * 1.5)

      #use random process to select filters
      #filter_list = random.sample(range(1,9),5)
      #filter_list = [1,5,6,3,4]

      #make list to put captions in
      caption_list = list()
      #create filtered images and captions
      caption_list.append(f.pixelate(image_copy_1))
      caption_list.append(f.find_edges(image_copy_2))
      caption_list.append(f.sharpen(image_copy_3))
      caption_list.append(f.motion_blur(image_copy_4))
      caption_list.append(f.bumpmap(image_copy_5))

      #caption_2 = f.swap_red_blue(rb_swap_image)
      #f.sin_bright(sined_image)
      #f.saturator(saturated_image)

      #create text objects for each caption

      original_label = gp.Text(gp.Point(image_width * 0.5,9),image_title)
      first_image_label = gp.Text(gp.Point(image_width * 1.5,9),caption_list[0] + " " + image_title)
      second_image_label = gp.Text(gp.Point(image_width * 2.5,9),caption_list[1] + " " + image_title)
      third_image_label = gp.Text(gp.Point(image_width *0.5, image_height + 9), caption_list[2] + " " + image_title)
      fourth_image_label = gp.Text(gp.Point(image_width * 1.5, image_height + 9), caption_list[3] + " " + image_title)
      fifth_image_label = gp.Text(gp.Point(image_width * 2.5, image_height + 9), caption_list[4] + " " + image_title)

      #set fonts and colors for text
      f.format_text(original_label)
      f.format_text(first_image_label)
      f.format_text(second_image_label)
      f.format_text(third_image_label)
      f.format_text(fourth_image_label)
      f.format_text(fifth_image_label)

      #draw all images
      primary_image.draw(window)
      for i in image_list:
         i.draw(window)
      
      #rb_swap_image.draw(window)
      #sined_image.draw(window)
      #saturated_image.draw(window)

      original_label.draw(window)
      first_image_label.draw(window)
      second_image_label.draw(window)
      third_image_label.draw(window)
      fourth_image_label.draw(window)
      fifth_image_label.draw(window)


      

      #pause
      window.getMouse()



      #
      




   

   else: #wrong number of arguments on the command line
      print("To use this program to show the extension image filters, enter the name")
      print("of an image file on the command line after calling this program.")
      print("\nExample: python3 warhol.py flowers.ppm")
   
    

if __name__ == "__main__":
	main(sys.argv)
