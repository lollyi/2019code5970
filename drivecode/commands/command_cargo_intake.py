# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import CommandGroup

# commands used in commandgroup
from do_cargo_intake import Do_Cargo_Intake
from do_move_arm import Do_Move_Arm
#from do_arm_go_back import Do_Arm_Go_Back
#from do_zero_encoder import Do_Zero_Encoder

# positions Arm for Cargo_Intake THEN Cargo Motor rotates inwards
class Command_Cargo_Intake(CommandGroup):
	def __init__(self, robot):
		super().__init__()

		# uses motor 6 and ctre motors 1 & 2
		'''
		Cargo Intake can only be in two states:
			1: rotating inwards(intake) & Arm at robot back (0 degrees)
			2: rotating outwards(eject) & Arm at robot front (135 degrees)

		State 1
		'''

		# BEING WEIRD
		# Estimated angle accounting for weird pid
		#XXX Can't input 0 move arm. WORKS 3/1
		#self.addSequential(Do_Move_Arm(robot, 0.1))
		#self.addSequential(Do_Arm_Go_Back(robot))
		self.addSequential(Do_Cargo_Intake(robot))
		print("cargo_intake!")


