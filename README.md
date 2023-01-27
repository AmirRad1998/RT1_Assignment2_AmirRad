# Research Track 1 Assignment 2 (ROS)

## Description:

In this assignment, the robot movements in a two-dimensional environment are simulated by implementation of ROS. Moreover, the Rviz and Gazebo are used for the graphical interfaces. So in general,  in the simulation environment, there is a robot and some walls as the obstacles that robot will avoid them using the defined functions. 

Gazebo environment:
![4](https://github.com/AmirRad1998/RT1_Assignment2_AmirRad/blob/main/Photos/4_Gazebo.png?raw=true "4")

Rviz environment:
![5](https://github.com/AmirRad1998/RT1_Assignment2_AmirRad/blob/main/Photos/5_Rviz.png?raw=true "5")


## How to run the assignment:
First, the terminal should be open or directed into the workspace root. My workspace name is “my_workspace”. 

![1](https://github.com/AmirRad1998/RT1_Assignment2_AmirRad/blob/main/Photos/1_cd_workspace.png?raw=true "1")

Then the launch file should be run in the terminal using the following command:
$ roslaunch amirpackage1 my_launch.launch

![2](https://github.com/AmirRad1998/RT1_Assignment2_AmirRad/blob/main/Photos/2_roslaunch.png?raw=true "2")

After running that, three terminals will be opened.

![3](https://github.com/AmirRad1998/RT1_Assignment2_AmirRad/blob/main/Photos/3_Three_TerminalsScreenshot%20from%202023-01-27%2021-20-23.png?raw=true "3")


## The New Nodes:
There are three new nodes defined in this a assignment:
### Node A:
In this node, the user enters two inputs:
-	Desired X position of the robot target
-	Desired Y position of the robot target
Then the robot start moving towards the selected target point. Now, the user can wait for the robot to reach the goal or cancel the operation.
Simultaneously, this node also publishes the robot position and velocity as a custom message, which will be used in the NodeC.

![6](https://github.com/AmirRad1998/RT1_Assignment2_AmirRad/blob/main/Photos/6_NodeA.png?raw=true "6")

### Node B:
This node, is responsible for printing the number of goals that are reached and cancelled by the robot, using service. To get the results of this node, we need to call it in a different terminal. In this project, the name of this service is: “target_results”.

Calling the service of the nodeB in a different terminal:
![7](https://github.com/AmirRad1998/RT1_Assignment2_AmirRad/blob/main/Photos/7_Calling_Service_NodeB.png?raw=true "7")

NodeB Terminal:
![8](https://github.com/AmirRad1998/RT1_Assignment2_AmirRad/blob/main/Photos/8_NodeB.png?raw=true "8")


### Node C:
This purpose of this node is to calculate and print distance of the robot from the target and the robot’s average speed. So, in this node there are two inputs and two outputs:
Inputs:
-	Robot’s current position (by subscribing the Node A)
-	Robot’s current velocity (by subscribing the Node A)
Outputs:
-	The distance of the robot from the target
-	The robot’s average speed

![9](https://github.com/AmirRad1998/RT1_Assignment2_AmirRad/blob/main/Photos/9_NodeC.png?raw=true "9")


In addition, a launch file is also created to run the whole project. Therefore, when the user run the launch file, three terminals will open for three nodes.



 

# Node A Flowchart:

![0](https://github.com/AmirRad1998/RT1_Assignment2_AmirRad/blob/main/Photos/0_FlowChart.png?raw=true "0")

.






















