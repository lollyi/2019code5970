# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.buttons import JoystickButton
from wpilib.buttons import Trigger

from do_encoder_check import Do_Encoder_Check


from sys import path
path.append('../commands')

class OI():
	def __init__(self, robot):

		#self.left_joy = wpilib.Joystick(0) 	
		#self.right_joy = wpilib.Joystick(1) 	
		
		self.left_joy = robot.left_joy 
		self.right_joy = robot.right_joy 

		# First character indicates self.right or self.left, 
		# second indicates position,
		# third indicates which button of the position specified
		# Ex: ltop0 is self.left top 0 

		ltop1 = JoystickButton(self.left_joy, 1)
		ltop2 = JoystickButton(self.left_joy, 2)
		ltop3 = JoystickButton(self.left_joy, 3)
		ltrig0 = JoystickButton(self.left_joy, 4)

		rtop1 = JoystickButton(self.right_joy, 1)
		rtop2 = JoystickButton(self.right_joy, 2)
		rtop3 = JoystickButton(self.right_joy, 3)
		#self.press_buttons(ltrig0, Do_Encoder_Check, robot)
		ltrig0.whenPressed(Do_Encoder_Check(robot))

	#def press_buttons(self, button, func, arg):
		#button.whenPressed(func(arg))

	@classmethod
	def get_left_joy(self):
		left_joy = wpilib.Joystick(0)	
		return left_joy

	@classmethod
	def get_right_joy(self):
		right_joy = wpilib.Joystick(1)	
		return right_joy
				

		

                    




		




