In this assignment, we will be tracking human faces using TELLO EDU with the help of OpenCV, Python built-in libraries.

Here, face detection is implemented using the Viola-Jones algorithm, it is an object-recognition framework that allows the detection of image features in real-time. It is quite powerful, and its application has proven to be exceptionally notable in real-time face detection. Since Viola-Jones was created for frontal faces, it is better at detecting them than faces that are gazing sideways, upwards, or downwards. The image is transformed to grayscale before detecting a face since it is easier to work with and there is fewer data to process. The Viola-Jones algorithm discovers the position on the colored image after detecting the face on the grayscale image.

Viola-Jones draws a box (as shown on the right) and searches within it for a face. It's basically looking for haar-like characteristics, which will be detailed later. After cycling through all of the tiles in the photo, the box moves a step to the right. For demonstration purposes, I've used a huge box and large steps, but you can adjust the box size and step size to suit your needs.

A number of boxes identify face-like features (Haar-like features) in smaller phases, and the data from all of those boxes combined aids the algorithm in determining where the face is.

In our experiment, the entire approach was followed by three-steps

1.	Getting Frame Using Tello: Here, I’ve accessed the real-time camera feed from the Drone using built-in functions and reading the video as frame by frame. And resizing the image for faster telecasting using OpenCV.

2.	Detecting The Face in Live Video: As mentioned, earlier the detection is happened using the Viola-Jones algorithm, this algorithm captures the frontal faces accurately and fast. The frontal faces are identified using Haar Wavelets, it is a mathematical approach to identify edges, lines, four-rectangle features. 
If the frame is having multiple images, then we will be concentrating on only the image which is near to the camera, this will be updated using the maximum area of the face-detected rectangle. As the face is near to the camera then the detected portion of the face in the frame will have a higher area.

3.	Tracking The Face: Face tracking is achieved by using a PID controller, it is used in multiple industrial applications to regulate physical variables such as temperature, pressure, speed, etc., the PID controller used a control loop feedback mechanism to control process variable, and these are the most accurate and stable controller.
The speed value will be updated based on the PID equation by considering the errors, and the updated speed values will be passed to the drone control for maintaining the yaw velocity for tracking the human face.

Output Result Video: https://youtu.be/828IB02d3U4
