# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import CommandGroup

# commands used in commandgroup
from do_hp_rotate_actuated import Do_Hp_Rotate_Actuated 
from do_profile_move import Do_Profile_Move

# positions Arm for Hatch_Panel_Eject
class Command_Hp_Eject(CommandGroup):
	def __init__(self, robot):
		super().__init__()
		
		# uses solenoids 3 & 4 and ctre motors 1 & 2
		'''
		Hatch Panel Intake can only be in two states:
			1: unactuated(intake) & Arm at robot front (155 degrees)
			2: unactuated(eject) & Arm at robot back (0 degrees)

		State 2
		'''

		self.addSequential(Do_Profile_Move(robot, 150))
		self.addSequential(Do_Hp_Rotate_Actuated(robot))
		print("hp eject! init")



