
"""

Run daemon either with gcode target or in listening mode.

Copyright 2021 J. Silverstone

"""








from curtsies import FullscreenWindow, Input, FSArray
from curtsies.fmtfuncs import red, bold, green, on_blue, yellow, on_red



from lib.indicate import Indicator
import time, random



def setup():
	"""
	Setup and initialisation.
	"""
	
	global indicator
	
	indicator = Indicator()
	
	return


def run_loop():
	"""
	Run loop.
	"""
	
	t_start = time.time()
	
	try:
		with FullscreenWindow() as window:
			width0, height0 = window.width, window.height
			print('Press escape to exit')
			with Input() as input_generator:
				a = FSArray(window.height, window.width)
			
				while time.time() - t_start < 20:
				
					# Update indicator
					indicator.tick()
					
					# Protect window buffer against terminal resizing
					if window.width != width0 or window.height != height0:
						a = FSArray(window.height, window.width)
						width0, height0 = window.width, window.height
				
					# Capture keyboard input
					temp_c = input_generator.send(timeout=0.5)
					if temp_c is not None:
						c = temp_c
						row = random.choice(range(window.height))
						column = random.choice(range(window.width-len(c)))
						a[row:row+1, column:column+len(c)] = [c]

						window.render_to_terminal(a)
			

	except KeyboardInterrupt:
		return


def tidy():
	"""
	Park hardware, close ports, tidy up.
	"""
	
	return


setup()

run_loop()

tidy()