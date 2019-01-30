import wpilib
from wpilib.drive import DifferentialDrive
from wpilib.command import Subsystem
from left_motors import Left_Motors
from right_motors import Right_Motors
from sys import path
path.append('../commands')
from do_tank_drive import Do_Tank_Drive

class Drivetrain(Subsystem):
	def __init__(self, robot):
		# Super from subsystem allows scheduler class to understand things like
		# interupt and execute etc...
		print("$$$$$$$$$$$$$$")
		super().__init__()
		print("$$$$$$$$$$$$$$")
	
		# Init motors here or import from robot.py
		left_motors_instance = Left_Motors()
		right_motors_instance = Right_Motors()
		left_motors = left_motors_instance.left_motor_group
		right_motors = right_motors_instance.right_motor_group

		# Set the drive train to use tank drive, self because used in commands
		self.drive = self.set_drivetrain_type(
			DifferentialDrive, left_motors, right_motors)

		self.robot = robot

	def initDefaultCommand(self):
		self.setDefaultCommand(Do_Tank_Drive(self.robot))

	# Sets driving mode to tank drive, should be periodically called
	def set_drivetrain_type(self, drivetrain_type, left_motors, right_motors):
		# DifferentialDrive for tank
		drive = drivetrain_type(left_motors, right_motors)
		return drive

	def set_tank_speed(self, left_joy, right_joy, drive):
		left_speed = left_joy.getY()
		right_speed = right_joy.getY()
		print("left_speed: " + str(left_speed))
		drive.tankDrive(left_speed, right_speed)

	def stop_robot(self, drive):
		drive.tankDrive(0,0)

	

		
		
