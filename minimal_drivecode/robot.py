#!/usr/bin/env python3
# vim: set sw=4 noet ts=4 fileencoding=utf-8:

# Robotics specifc libraries
import wpilib
from wpilib.command import Scheduler
# for Automous Scheduler
# from commands.autonomous import Autonomous
from wpilib.buttons.joystickbutton import JoystickButton
import time
from networktables import NetworkTables

# Non robot specific libraries
import os
import sys
import math

#Linux path
sys.path.append('./subsystems') 
sys.path.append('./commands') 

#Windows RobotPyModules path
sys.path.append('C:/Users/Beavertronics/Desktop/2019code5970/drivingcode/\
subsystems')
sys.path.append('C:/Users/Beavertronics/Desktop/2019code5970/drivingcode/\
commands') 

#RoboRIO path
sys.path.insert(0, '/home/lvuser/py/subsystems')
sys.path.insert(0, '/home/lvuser/py/commands')

# Subsidiary objects on the robot. Ex: Cube Intake from 2017/18 season

#from arm import Arm
from left_motors import Left_Motors
from right_motors import Right_Motors
#from arm_motors import Arm_Motors
#from cargo_motors import Cargo_Motors
from arm import Arm


from drivetrain import Drivetrain
from cargo import Cargo
from hatch_panel import Hatch_Panel
from hatch_panel_rotate import Hatch_Panel_Rotate
from ramp import Ramp
from shifters import Shifters

#from encoders import Encoders
from oi import OI

#from oi_buttons import OI_Buttons

class BeaverTronicsRobot(wpilib.TimedRobot): 

	def robotInit(self):
		# Instances of classes

		# Instantiate Subsystems
		self.drivetrain = Drivetrain(self)
		self.arm = Arm(self)
		self.cargo = Cargo(self)
		self.hatch_panel = Hatch_Panel()
		self.hatch_panel_rotate = Hatch_Panel_Rotate()
		self.ramp = Ramp()
		self.shifters = Shifters()

		# instantiate Encoders
		#self.encoders = Encoders(self)

		# Instantiate Joysticks
		self.left_joy = wpilib.Joystick(0) 
		self.right_joy = wpilib.Joystick(1)
		
		# Instantiate Xbox
		self.xbox = wpilib.XboxController(2)

		# Instantiate OI; must be AFTER joysticks are inited
		self.oi = OI(self)

		self.timer = wpilib.Timer()
		self.loops = 0
		
		

		# instantiate Autonomous scheduler
		#self.autonomousCommand = Autonomous(self)
		
	def autonomousInit(self):
		# Set up encoders
		# Loop counter to stop/start auto?
		# Reset encoders (zero them) upon init
		# Get Driverstation data from field
		data = wpilib.DriverStation.getInstance().getGameSpecificMessage()
		# Initialize pid variables

		# Autonomous Scheduler
		# self.autonomousCommand.start()
		
	def autonomousPeriodic(self):
		Scheduler.getInstance().run()

	def teleopInit(self):
		self.loops = 0
		self.timer.reset()
		self.timer.start()
		self.arm.l_arm_encoder.reset()

	def teleopPeriodic(self):
	# Before, button functions were executed here. Now scheduler will do that
		Scheduler.getInstance().run()

		# Keeping track of TimedRobot loops through code
		self.loops += 1
		if self.timer.hasPeriodPassed(1):
			self.logger.info("%d loops / second", self.loops)
			self.loops = 0

	def disabledInit(self):
		return None
	
	def disabledPeriodic(self):
		return None

	def robotPeriodic(self):
		return None
	
if __name__ == "__main__":
	wpilib.run(BeaverTronicsRobot)
