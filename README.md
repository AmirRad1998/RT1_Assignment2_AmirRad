Research Track 1 Assignment 2 (ROS)
Introduction
In this assignment, the robot movements in a two-dimensional environment are simulated by implementation of ROS. Moreover, the Rviz and Gazebo are used for the graphical interfaces. So in general,  in the simulation environment, there is a robot and some walls as the obstacles that robot will avoid them using the defined functions. 
There are three new nodes defined in this a assignment:

Node A: in this node, the user enters two inputs:
-	Desired X position of the robot target
-	Desired Y position of the robot target
Then the robot start moving towards the selected target point. Now, the user can wait for the robot to reach the goal or cancel the operation.
Simultaneously, this node also publishes the robot position and velocity as a custom message, which will be used in the NodeC.

Node B:
This node, is responsible for printing the number of goals that are reached and cancelled by the robot, using service. To get the results of this node, we need to call it in a different terminal. In this project, the name of this service is: “target_results”.
Node C:
This purpose of this node is to calculate and print distance of the robot from the target and the robot’s average speed. So, in this node there are two inputs and two outputs:
Inputs:
-	Robot’s current position (by subscribing the Node A)
-	Robot’s current velocity (by subscribing the Node A)
Outputs:
-	The distance of the robot from the target
-	The robot’s average speed

In addition, a launch file is also created to run the whole project. Therefore, when the user run the launch file, three terminals will open for three nodes.

How to run the assignment:



![aaa](https://github.com/AmirRad1998/RT1_Assignment2_AmirRad/blob/main/Capture.PNG?raw=true "aaa")


Research Track 1 Assignment 2 (ROS)
Introduction
In this assignment, the robot movements in a two-dimensional environment are simulated by implementation of ROS. Moreover, the Rviz and Gazebo are used for the graphical interfaces. So in general,  in the simulation environment, there is a robot and some walls as the obstacles that robot will avoid them using the defined functions. 
There are three new nodes defined in this a assignment:

Node A: in this node, the user enters two inputs:
-	Desired X position of the robot target
-	Desired Y position of the robot target
Then the robot start moving towards the selected target point. Now, the user can wait for the robot to reach the goal or cancel the operation.
Simultaneously, this node also publishes the robot position and velocity as a custom message, which will be used in the NodeC.

Node B:
This node, is responsible for printing the number of goals that are reached and cancelled by the robot, using service. To get the results of this node, we need to call it in a different terminal. In this project, the name of this service is: “target_results”.
Node C:
This purpose of this node is to calculate and print distance of the robot from the target and the robot’s average speed. So, in this node there are two inputs and two outputs:
Inputs:
-	Robot’s current position (by subscribing the Node A)
-	Robot’s current velocity (by subscribing the Node A)
Outputs:
-	The distance of the robot from the target
-	The robot’s average speed

In addition, a launch file is also created to run the whole project. Therefore, when the user run the launch file, three terminals will open for three nodes.

How to run the assignment:

