#!/usr/bin/env python3

# import the necessary libraries
import math
from amirpackage1.msg import my_custom_msg
import rospy
import os

#global variables
begin_description_flag=1
number_counter =0
temporary_speed =0
avgrage_speed =0
distance_difference =0

# This function calculates the average velocity of the robot
#this average velocity is calculated by the last 10 messages and the average velocity is printed
# Moreover, the distance of the robot from the target is calculated and printed by this node (using the euclidean distance formula)

def callback_subscriber(data):
    #global variables
    global number_counter
    global temporary_speed
    global avgrage_speed
    global distance_difference

    #get the desired position from the parameter server to calculate the distance of the robot from the target
    desired_position_x = rospy.get_param("/des_pos_x")
    desired_position_y = rospy.get_param("/des_pos_y")

    #get the current position of the robot
    current_position_x = data.x
    current_position_y = data.y

    #calculate the distance of the robot from the target
    distance_difference= math.sqrt(((desired_position_x - current_position_x)**2)+((desired_position_y - current_position_y)**2))


    #current velocity is stored in the current_speed variable
    current_speed_x = data.vel_x
    current_speed_y = data.vel_y

    #calculate the current speed of the robot
    current_speed= math.sqrt((current_speed_x**2)+(current_speed_y**2))


    #calculate the average velocity of the robot
    #the average velocity is calculated over the last 10 messages
    #the average velocity is stored in the avg_vel variable
    if number_counter<10:

        temporary_speed=temporary_speed+current_speed
        number_counter +=1

    elif number_counter==10:

        number_counter=0
        temporary_speed /= 10
        avgrage_speed=temporary_speed
        temporary_speed=0


# Function: start_description function
# this function is employed to print the description of the node
def start_description(begin_description_flag):
    if begin_description_flag == 1:
        os.system('clear')
        print("\n\n-----          The Node description          -----\n\n")
        print("This node subscribes to the robot position and ")
        print("velocity and prints the ")
        print("distance of the robot from the target and the ")
        print("robot average speed. ")
        print("You can set the \"print_distance\" parameter in ")
        print("assignment_2_2022 launch flie to set how fast the")
        print("node publishes the information.")
        input("\n\nPlease press Enter to continue!")
        begin_description_flag=0   


    


#main function
if __name__ == "__main__":

    #start_description_flag is used to print the description of the node only once
    start_description(begin_description_flag)

    #logwarn is used to print a message in the terminal
    #the message is printed only once
    rospy.logwarn("NodeC started")

    #Initialize the node
    #the name of the node is NodeC
    rospy.init_node('NodeC')

    #create a rate object
    #the rate is set using the parameter /print_distance
    #the parameter is set in the launch file
    #the parameter is used to set the rate at which the node publishes the information
    rate = rospy.Rate(rospy.get_param("/print_distance"))

    #create a subscriber object
    #the subscriber subscribes to the topic /odom_custom
    #the message type is odom_custom_msg
    #the callback function is callback_subscriber
    rospy.Subscriber("position_and_velocity", my_custom_msg, callback_subscriber)

    #the node runs until it is shutdown
    #the node prints the distance of the robot from the target and the average velocity of the robot
    #the node sleeps for the time set in the rate object
    while not rospy.is_shutdown():

        print(f"distance: {distance_difference : .3f}")
        print(f'average velocity: {avgrage_speed: .3f}')
        print(f"---------------------------")
        rate.sleep()
