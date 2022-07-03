#!/usr/bin/env python2

import rospy
import math
from geometry_msgs.msg import Twist 
from std_msgs.msg import Float64
angles1 = Float64()
angles2 = Float64()
l = float(1.0)
w = float(0.6)
r = float(0.1)
u = math.atan(l/r)
def i( r):
 g = float(r)
 u = math.atan(l/g)
 x= (2 * l * (math.sin(u)))/((2 * l * (math.cos(u))-(w * (math.sin(u)))))
 return x
def j(r):
 g = float(r)
 u = math.atan(l/g)
 y = (2 * l * (math.sin(u)))/((2 * l * (math.cos(u))+(w * (math.sin(u)))))
 return y


def stop(vel_msg):
	vel_msg.linear.x = 0
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 0
angle2 = rospy.Publisher('/joint_controll/wheel_controller2/command',Float64,queue_size=10)	


angle1 = rospy.Publisher('/joint_controll/wheel_controller1/command',Float64,queue_size=10)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
rospy.init_node('bot_controller', anonymous=True)
rate = rospy.Rate(10) # 10hz

vel_msg = Twist()
stop(vel_msg)
def move():

	vel_msg.linear.x = vel_msg.linear.x - 0.5

		
	pub.publish(vel_msg)

def stop():

	vel_msg.linear.x = 0.0

		
	pub.publish(vel_msg)
def turn(r):
	if r != 0.0:
	 angles1.data = i(r)
	 angles2.data = j(r)
	
	 angle1.publish(angles1)
	 angle2.publish(angles2)
	 rospy.loginfo(r)
	 rospy.loginfo(angles1)
	 rospy.loginfo("  " + str(angles2.data))
	else:
		r = 0.0
		angle1.publish(0.0)
		angle2.publish(0.0)

def turn_back(r):
	if r != 0:
	
	 angles1.data = i(r)
	 angles2.data = j(r)
	
	 angle1.publish(angles1)
	 angle2.publish(angles2)
	 rospy.loginfo("radius" + str(r))
	 rospy.loginfo(angles1)
	 rospy.loginfo("  " + str(angles2.data))
	else:
		r =0.0
		angle1.publish(0.0)
		angle2.publish(0.0)


import sys
import pygame

# initialising pygame
pygame.init()

# creating display
display = pygame.display.set_mode((300, 300))

# creating a running loop
while True:
	
	# creating a loop to check events that
	# are occurring
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		
		# checking if keydown event happened or not
		if event.type == pygame.KEYDOWN:
			
			# checking if key "A" was pressed
			if event.key == pygame.K_w:
				move()
			
			# checking if key "J" was pressed
			if event.key == pygame.K_s:
				stop()
			
			# checking if key "P" was pressed
			if event.key == pygame.K_a:
			
				r= r+ 0.1
				turn(r)
				
			
			# checking if key "M" was pressed
			if event.key == pygame.K_d:
			
			 r = r - 0.1
			 turn_back(r)
