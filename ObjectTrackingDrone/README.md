The drone will be able to identify different objects in the captured footage in real time based on the color (Orange ball in my implementation) and  follows the object.

1)We first convert image into HSV plane then select only particular region of HUE, VALUE AND SATURATION by using sliders

2)After converting the color space what we have to do is to filter out the yellow color and create a mask frame. We get the binary mask of our object.

3)We then find contours for the object along with Center of Mass of contour.

Above three steps have been implemented in the script, colorpicker.py (Refer this for HSV values and load them to the code based on the respective object color)

4)We always try to put the Center  of mass of the object in the center of the frame and use PID to calculate the speed and movements of the drone
