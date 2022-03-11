Here, for identifying the body poses, I've used MediaPipe 33 3D landmarks.

Let's start with implementing media pipe's pose key point detection model using webcam or static image.
https://google.github.io/mediapipe/solutions/pose.html For each frame processed we have an array of 3d coordinates of 21 key points. We use these key-points for gesture recognition To just use pretrained model refer to gesture_test.py You can use the pretrained model for gesture recognition or create your own dataset, or you can just The dataset can be created by running hand key point detection for certain time and save different gestures.

You can also first save your gesture as video and convert video into frames using the videos2frame.py script

For each frame we run the point detection and append it to the CSV file. You can refer pose_train.py script to finish the task. At the end of step3 you should have a CSV with information about key points and its label.

Now we are ready with our dataset, we now build a KNN classifier to recognize our body pose. Train_X = N * [(x0,y0), (x1,y1) …… (x20,y20)] Train_Y = N*label for each body pose

You can refer to knncvs.py to train the KNN classifier and save the model as a pickle file.

Let's test the classifier on real time, now all is left to implement drone control using our poses. You can refer tello_pose.py to test.
