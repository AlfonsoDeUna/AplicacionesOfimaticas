# importing libraries 
import cv2 
from PIL import Image 

mean_width = 0
mean_height = 0

im1 = Image.open("./1.jpg") 
width, height = im1.size 
mean_width += width 
mean_height += height 

im2 = Image.open("./2.jpg") 
width, height = im2.size 
mean_width += width 
mean_height += height 

im3 = Image.open("./3.jpg") 
width, height = im3.size 
mean_width += width 
mean_height += height

im4 = Image.open("./4.jpg") 
width, height = im4.size 
mean_width += width 
mean_height += height

im5 = Image.open("./5.jpg") 
width, height = im5.size 
mean_width += width 
mean_height += height 
	 

mean_width = int(mean_width / 5) 
mean_height = int(mean_height / 5) 

# 
# resizing 
imResize1 = im1.resize((mean_width, mean_height)) 
imResize1.save( "a.jpg", 'JPEG', quality = 95) # setting quality 

imResize2 = im2.resize((mean_width, mean_height))
imResize1.save( "b.jpg", 'JPEG', quality = 95) # setting quality 

imResize3 = im3.resize((mean_width, mean_height)) 
imResize3.save( "c.jpg", 'JPEG', quality = 95) 

imResize4 = im4.resize((mean_width, mean_height)) 
imResize4.save( "d.jpg", 'JPEG', quality = 95) 

imResize5 = im5.resize((mean_width, mean_height)) 
imResize5.save( "e.jpg", 'JPEG', quality = 95)
 
# Video Generating function 
def generate_video(): 
	
    video_name = 'mygeneratedvideo.avi'
    frame = cv2.imread("./1.jpg") 

    height, width, layers = frame.shape 

    video = cv2.VideoWriter(video_name, 0, 1, (width, height)) 
 
    video.write(cv2.imread("./a.jpg"))
    video.write(cv2.imread("./b.jpg")) 
    video.write(cv2.imread("./c.jpg"))
    video.write(cv2.imread("./d.jpg"))
    video.write(cv2.imread("./e.jpg"))    
	
	# Deallocating memories taken for window creation 
    cv2.destroyAllWindows() 
    video.release() # releasing the video generated 


# Calling the generate_video function 
generate_video() 
