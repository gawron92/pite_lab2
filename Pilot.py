# Mateusz Gawron, grupa sroda 8:00
# Klasa Pilot

import random
from Generator import Generator
		
class Pilot:
	def __init__(self, generator):
		self.generator = generator
		self.minute = 0
		self.second = 0
		self.angle = 0
		self.is_left = 0

	def make_correction(self, print_info):
		if print_info == True:
			self.print_info()
		if self.angle > 0:
			if self.angle >= 1:
				self.angle = self.angle - 1
			else:
				self.angle = 0
		
	def print_info(self):
		self.before_side = ""
		self.after_side = ""
		if self.angle > 0 and self.is_left:
			self.before_side = "lewo"
			self.after_side = "prawo"
		else:
			self.before_side = "prawo"
			self.after_side = "lewo"
		minute_str = str(self.minute).zfill(2)
		second_str = str(self.second).zfill(2)
		print "["+minute_str+":"+second_str+"]",
		if self.angle > 0:
			print "Wykryto przechylenie w "+self.before_side,
			print "o " + str(round(self.angle,2)) + " stopni"
			print (8*" ")+"Korekcja w "+self.after_side+" o",
			if self.angle < 1:
				print str(round(self.angle,2))+" stopnia"
			else:
				print "1 stopien"
		else:
			print "Brak przechylenia"
		print ""
				
	def make_timestep(self, is_generation):
		self.second = self.second+1
		if (self.second == 60):
			self.second = 0
			self.minute = self.minute+1
			if (self.minute == 60):
				self.minute = 0
		if is_generation:
			self.process_generation()

	def process_generation(self):
		if self.angle == 0:
			if random.random() < 0.3:
				self.data = self.generator.get_data()
				self.is_left = self.data[0]
				self.angle = self.data[1]