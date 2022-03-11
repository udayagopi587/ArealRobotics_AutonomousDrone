Here, for identifying the hand guesture I've used MediaPipe 21 3D landmarks.
2 stage detection:
	A palm detection - returns an oriented hand bounding box. 
	A hand landmark model - returns high-fidelity 3D hand key points 
1) Let's start with  implementing media pipes hand key point detection model using webcam or static image.

  https://google.github.io/mediapipe/solutions/hands.html
  For each frame processed we have an array of 3d coordinates of 21 key points. We use these key-points for gesture recognition
  To just use pretrained model refer to gesture_test.py
  You can use the pretrained model for gesture recognition or create your own dataset, or you can just
  The dataset can be created by running hand key point detection for certain time and save  different gestures.

2) You can also first save your gesture as video and convert video into frames using the videos2frame.py script


3) For each frame we run the hand key point detection and append it to the CSV file. You can refer my_pose_train.py script to finish the task. At the end of step3 you should have a CSV with information about key points and its label.

4) Now we are ready with our dataset, we now build a KNN classifier to recognize our gestures. 
    Train_X  =  N * [(x0,y0), (x1,y1) …… (x20,y20)]
    Train_Y = N*label for each hand gesture

5) Let's test the classifier on real time. You can refer tello_gesture_controller.py to test our classifier out.

6) Now all is left to implement drone control using our gestures. You can refer to gesture_test_drone.py
