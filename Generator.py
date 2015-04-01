# Mateusz Gawron, grupa sroda 8:00
# Klasa Generator

import random

class Generator:
	def get_data(self):
		is_left = random.random() < 0.5
		angle = random.random() * 5.0
		return (is_left, angle)
	