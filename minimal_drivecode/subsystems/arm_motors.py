# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
#from wpilib.buttons.joystickbutton import JoystickButton
import ctre

#*********Robot-Side Initialization***************
class Arm_Motors():
	
	def __init__(self):
		#Initialize Right motors
		#self.arm_motor = (wpilib.VictorSP(12))
		self.left_arm_motor  = ctre.WPI_VictorSPX(1)	
		self.right_arm_motor = ctre.WPI_VictorSPX(2)

	def set_speed(self, value):
		if value > 1 or value < -1:
			raise(RuntimeError, "arm given an invalid speed value: " + str(value))

		self.left_arm_motor.set(value)
		self.right_arm_motor.set(-value)



