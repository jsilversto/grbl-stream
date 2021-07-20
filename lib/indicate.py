
"""

Indicator functions, using the Pimoroni Unicorn Hat HD

Copyright 2021 J. Silverstone

"""

import time
from PIL import Image

import unicornhathd as uhd




class Indicator:
	
	def __init__(self, brightness=0.5):
		
		self.state = "ready"
		
		self.width, self.height = uhd.get_shape()
		
		self.last_update_t = time.time()
		
		uhd.rotation(90)
		uhd.brightness(brightness)
	
	@property
	def state(self):
		return self.state_
	
	@state.setter
	def state(self, new_state):
		if new_state != self.state_:
			self.img = Image.open("bm_"+new_state+".png")
			self.state_ = new_state
			self.update_period = 0.5
		

	def tick(self):
		"""
		Function called by main run loop. Fetch new image if state has changed,
		advance animation of current image if timer has expired.
		"""
	
		t = time.time()
	
		if t - self.last_update_t > self.update_period:
			for i in range(int(img.size[0] / width)):
				for x in range(width):
					for y in range(height):
						pixel = img.getpixel(((i * width) + y, x))
						r, g, b = int(pixel[0]), int(pixel[1]), int(pixel[2])
						uhd.set_pixel(x, y, r, g, b)

				uhd.show()

except KeyboardInterrupt:
	uhd.off()


def tidy():
	uhd.off()