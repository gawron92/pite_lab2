# Mateusz Gawron, grupa sroda 8:00
# Sposob uruchamiania:
# np. python main.py

import time
from Pilot import Pilot
from Generator import Generator
		
def run():
	gen = Generator()
	pilot = Pilot(gen)
	try:
		while True:
			pilot.make_correction(True)
			time.sleep(1)
			pilot.make_timestep(True)
	except KeyboardInterrupt:
		print "Koniec symulacji",
		
if __name__ == "__main__":
	run()