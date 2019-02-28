# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import wpilib.drive
from wpilib.command import Command

class Do_Axis_Button_5(Command):
	'''
	Command functionally equivalent to "when controller axis is triggered, 
	do [command or command group]

	Responds to axis corresponding to xbox controller button 5
	'''
	def __init__(self, robot):

		# recognize as a wpilib command
		super().__init__()
		

		# an instance of BeaverTronicsRobot from robot.py containing its
		self.robot = robot
		self.robot_cargo = robot.cargo
		self.robot_ramp = robot.ramp
		
		# keeps track of axis inputs over time
		self.previous_axis_input = 0
	
	def initialize(self):
		"""Called just before this Command runs the first time"""
			
	
	def execute(self):
		"""Called iteratively by Scheduler"""
		# continuously check current button axis input
		self.current_axis_input = self.robot.xbox.getRawAxis(1)
		# calls command based on button axis input
		self.robot_cargo.cargo_axis_commands(self.current_axis_input, 
				self.previous_axis_input)
		
		# record previous button axis input
		self.previous_axis_input = self.current_axis_input

	def isFinished(self):
		# continuously runs
		return None

	def end(self):
		self.robot_ramp.ramp_actuate()
		print("ramp actuated")
	
	def interrupted(self):
		self.end()


	