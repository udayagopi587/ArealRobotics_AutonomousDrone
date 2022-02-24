# ArealRobotics_AutonomousDrone
This Repository contains multiple applications (such as controlling the drone using python, face tracking using tello, object tracking using tello, Controlling Drone with Body Postures, Controlling Drone with Hand Gestures, YELLO (YOLO + TELLO), Collision Avoidance Drone) on TELLO EDU drone using python


Firstly, let’s understand the physics behind the motion of a quadcopter. The quadcopter's rotors behave as wings. They generate lift by spinning quickly, pulling the air downward, and propelling the quadcopter into the air. If the lift cancels out against gravity's acting force, then the net force is zero, and the quad hovers in mid-air. The quadcopter is propelled in a certain direction using a directional force. The Drone's height is reduced as the lift decreases. 
Quadcopter Motor Setup: - The two adjacent motors rotate in the opposite direction, and the two opposite motors rotate in the same direction, this is for stabilizing the net force acting on the drone’s body to zero. If we make all the motors rotate in the same direction, then the resulting torque causes the complete drone to rotate. [Image Source: - Weird]
![motion](https://user-images.githubusercontent.com/29915714/155453300-019df786-6485-49bc-8561-cc4aa726528e.png)


Hovering: The hovering of the drone is very easy to understand. First, the motors create a lift, the lift should be equal to the force of gravity acting on the body. Thus, both lift and gravity cancel out and this creates the quadcopter to hover in the mid-air.
The Drone’s Motion: The nomenclature used to describe drone movement is similar to which used to describe naval maneuver. I'll use the same terminology to describe our drone's movements.


Roll: Moving Side by side with respect to the front side of the drone, can be achieved by lowering the lift of motors based on the direction of movement. 
That is, if we need to roll to the left, then we should decrease the lift on the left side of the motors and should increase the lift on the right side of the motors. This causes the motion of the drone towards the left, and vice versa creates a motion towards the right side of the drone. [Image Source: - Hackermoon]
![roll](https://user-images.githubusercontent.com/29915714/155452937-6538623f-66c3-4570-87b4-31aa25354c7d.gif)

Pitch: Forward and Backward movement, to cause the drone to pitch forward (approach) you. The power that is applied to the rear motors is enhanced. This causes the Drone's nose to tilt downward due to a forward net push. To maintain angular momentum, you must also reduce the power delivered to the two front motors. The exact opposite will cause the drone to move (pitch) backward. [Image Source: - Hackermoon]
![pitch](https://user-images.githubusercontent.com/29915714/155452933-43c6d60a-64ec-4255-a122-b12b731d3b55.gif)

Yaw: Rotating clockwise/anticlockwise around the center, for rotating the drone in a clockwise direction. The lift on the anti-clockwise rotating motors must be increased, and on clockwise rotating motors, you must additionally reduce the lift. This is done in order to keep both the upward and downward net forces at zero. There is also an anti-clockwise torque as a result. To save Angular Momentum, the drone turns clockwise. [Image Source: - Hackermoon]
![yaw](https://user-images.githubusercontent.com/29915714/155452938-da8967ba-356c-4b8b-a8be-c6f79fba1dec.gif)

Take Off: You'll need a net upward force to take off the drone from the ground. The drone takes flight because the motors provide a lift higher than the force of gravity. The exact reverse is for a safe drone landing. [Image Source: - Hackermoon]
![takeoff](https://user-images.githubusercontent.com/29915714/155453361-5c615a7e-d75c-4d86-8b9a-66fc06c7ecbb.png)

 

