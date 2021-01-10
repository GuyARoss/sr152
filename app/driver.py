from abc import ABC

import time

class PWAControl(ABC):
	def __init__(self, pin: int):
		self.pin = pin

	def apply(self, on: int, off: int):
		pass

class PCA9685(PWAControl):
	def __init__(self, pin: int):
		self.pin = pin

		import Adafruit_PCA9685

		pwm = Adafruit_PCA9685.PCA9685()
		pwm.set_pwm_freq(60)

		self.pwm = pwm

	def apply(self, on: int, off: int):
		self.pwm.set_pwm(self.pin, on, off)

	
class Thumbstick:
	def __init__(self, pin: int, control_type:PWAControl= PCA9685):
		self.control = control_type(pin)

	def center(self):
		self.control.apply(0, 0)

	def linear_min(self):
		self.control.apply(0, 120)

	def linear_max(self):
		self.control.apply(0, 500)

class Controller:
	def __init__(self, left_thumbstick: Thumbstick, right_thumbstick: Thumbstick):
		self.left_thumbstick = left_thumbstick
		self.right_thumbstick = right_thumbstick

if __name__ == '__main__':
	while True:
		control = PCA9685(12)
		stick_1 = Thumbstick(control)
		stick_1.linear_min()
		time.sleep(1)
		stick_1.center()
		time.sleep(1)		
		stick_1.linear_max()
		time.sleep(1)
