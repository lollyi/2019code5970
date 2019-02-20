# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

# Turns on solenoids for shifters. Shifts into high gear
class Do_Shifters_Toggle(Command):
	def __init__(self, robot):
		super().__init__()

		self.robot_shifters = robot.shifters
		# uses solenoids 0 and 1
		
		# Shifters can be in two states:
		#	1: actuated high gear
		#	2: unactuated low gear

		# state 1: possesses Shifters
		self.requires(self.robot_shifters)

	def initialize(self):
		# actuate solenoids for shifters
		self.robot_shifters.shifters_on()
		print("shifters on!")

	def execute(self):
		return None

	def isFinished(self):
		return None

	def end(self):
		self.robot_shifters.shifters_off()
		print ("shifters off!")

	def interrupted(self):
		self.end()