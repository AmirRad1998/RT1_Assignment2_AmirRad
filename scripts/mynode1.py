#! /usr/bin/env python3 


# Libraries
import rospy
from geometry_msgs.msg import PoseStamped 
import actionlib.msg 
import assignment_2_2022.msg 
import actionlib
import rospy
from nav_msgs.msg import Odometry
from amirpackage1.msg import my_custom_msg
import os

# Global Variable
start_description_flag=1



# ----- Function: start_description -----
#this function is employed after the  starting of the program to desplay the node description
#it will wait for the user to press enter
def start_description(start_description_flag):
    if start_description_flag == 1:
        os.system('clear')
        print("\n\n-----               The Node Description               -----\n\n")
        print("This node uses the action client ")
        print(" and allows the user to set a target x and y or to cancel it ")
        print("\n\n------------------Node description------------------\n\n")
        print("Also this node publishes the robot position and velocity ")
        print("as a custom message (x,y, vel_x, vel_z) ")
        input("\n\nPress Enter to continue!")
        start_description_flag=0   

#
#
#

# ----- Function: Target_client ----- 
# This function is employed to set the target position
# it asks the user to choose the x and y position as inputs
# then the robot starts moving toward the defined target
# the goal positions are published on an topic named reaching_goal
# so the action server can get the goal by senf_goal function (action type:PlanningAction - file: assignment_2_2022/Planning.action)

def target_client():

    # asking the user to type the X and Y positions
    x_pos = input("\n Enter the X Please: ")
    y_pos = input("Enter the Y Please: ")
    
    # defining x and y positions as int variables
    x_pos = int(x_pos)
    y_pos = int(y_pos)
     
    print(f'\nTarget Pos: \npos X: {x_pos}  \npos Y: {y_pos}')
    print("\n=====================================")
    print("\nconnecting to the action server")
    print("\nplease wait...")

    #Waiting for the server to be ready to receive goals 
    client.wait_for_server()

    #Creating a goal to send to the action server.
    goal = PoseStamped()

    goal.pose.position.x = x_pos
    goal.pose.position.y = y_pos
    goal = assignment_2_2022.msg.PlanningGoal(goal)

    #Sending the goal to the action server.
    client.send_goal(goal)
    print("\nthe goal is sent to the sever successfully")
    input("\nPress Enter to select an operation!")

    #turning back to the interface function 
    interface()
      

# ----- Function: cancel_target -----
#this function is employed to cancel the operation of the robot when it is trying to reach the goal
#so the goal will be canceled when the cancel_goal function is called by the user

def cancel_target():

    #Canceling the robot goal
    client.cancel_goal()
    print(f"\nTarget canceled")
    input("\n\nPlease press Enter to choose an operation!")

    #turning back to the interface function
    interface()


# ----- Function: incorrect input -----
def wrong():

    print("the input is incorrect! Please try one more tieme...")
    #wait 1 sec
    rospy.sleep(1)
    interface()


# ----- Function: interface -----
# this function is employed to facilitate the interface between the robot and the user
#the user can choose the operation between three options:
#1. target position operation (target_client function)
#2. the cancel operation (cancel_target function)
#3. the exit operation (exit function)

def interface():
    os.system('clear')
    print("          =====-----=====-----=====-----          \n")    
    print("-----=====-----=====-----=====-----=====-----=====\n")    
    print("---              Robot controller              ---\n")
    print("=====-----=====-----=====-----=====-----=====-----\n")    
    print("          -----=====-----=====-----=====          \n") 
    print("1:Target pos\n")
    print("2:Cancel\n")
    print("3:Exit\n")   

    #Ask the user to select an operation
    user_selection = input("Select your operation: ")
    
    #Check the user selection and allocade the quantities
    if   (user_selection == "1"):
        target_client()

    elif (user_selection == "2"):
        cancel_target() 

    elif (user_selection == "3"):
        exit()

    else:
        wrong()

# ----- Function: callback -----
#this function is employed when the node receives a message from the topic
#this fuction publishes the message received from the topic as a custom message
#and then publishes it on the topic "position_and_velocity"

def callback(data):
    
    my_publisher = rospy.Publisher('position_and_velocity', my_custom_msg, queue_size=5)
    my_custom_message = my_custom_msg()
    my_custom_message.x = data.pose.pose.position.x
    my_custom_message.y = data.pose.pose.position.y
    my_custom_message.vel_x = data.twist.twist.linear.x
    my_custom_message.vel_y = data.twist.twist.linear.y

    my_publisher.publish(my_custom_message)



if __name__ == '__main__':
    start_description(start_description_flag)
    
    #Initialize the node
    rospy.init_node('NodeA')
    #Subscribe to the topic 
    #The callback function is called when the node receives a message from the topic 
    rospy.Subscriber("/odom", Odometry, callback)

    #Creating the SimpleActionClient, passing the type of the action
    #to the constructor.
    client = actionlib.SimpleActionClient('/reaching_goal',assignment_2_2022.msg.PlanningAction )
    
    #Calliing the interface function
    #the interface function prints the interface and asks the user to select an operation
    #the user can select the target position operation, the cancel operation or the exit operation
    interface()

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

