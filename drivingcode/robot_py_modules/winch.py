# vim: set sw=4 sts=4 fileencoding=utf-8:
import wpilib
from wpilib.buttons.joystickbutton import JoystickButton
import sys
sys.path.append('C:/Users/Beavertronics/Desktop/2018Workstation/2018code5970/drivingcode/robot_py_modules')
			    

class Winch():
    def __init__(self):
     #Initialize ClimberIntakeWinch motors
        self.ClimberWinch_motor = []
		### Wrong; no sparks
        self.ClimberWinch_motor.append(wpilib.Spark(6))
        self.ClimberWinch_motor = []
        self.ClimberWinch_motor.append(wpilib.Spark(7))
        self.IntakeWinch_motor = []
        self.IntakeWinch_motor.append(wpilib.VictorSP(9))
        self.Gteencont = wpilib.Joystick(2)
        self.UpIntakeWinch = JoystickButton(self.Gteencont, 5)
        self.DownIntakeWinch = JoystickButton(self.Gteencont, 6)
        self.ClimberWinch = JoystickButton(self.Gteencont, 1)
    '''
    Control winches for climber & intake
    '''
    #intake winch function
    def updown_intake(self):
        if self.UpIntakeWinch.get():
            for motor in self.IntakeWinch_motor:
                motor.set(0.25)
        elif self.DownIntakeWinch.get():
            for motor in self.IntakeWinch_motor:
                motor.set(-0.25)
        else:
            for motor in self.IntakeWinch_motor:
                motor.set(0)
                
   #Climber winch function 
    def climber_func(self):
        if self.ClimberWinch.get():
            for motor in self.ClimberWinch_motor:
                motor.set(0.25)
        else:
            for motor in self.ClimberWinch_motor:
                motor.set(0)
   
