
"""

Indicator functions, using the Pimoroni Unicorn Hat HD

Copyright 2021 J. Silverstone

"""

import time, sys, os
from PIL import Image

import unicornhathd as uhd




class Indicator:
	
	def __init__(self, brightness=0.5):
		
		# Add indicate.py directory to PATH
		self.bm_dir = os.path.join(
					os.path.dirname(os.path.realpath(__file__)), "glyphs")
		
		self.state_ = ""
		self.state = "ready"
		
		self.width, self.height = uhd.get_shape()
		
		self.img_seq = 0 # Index of image in stacked sequence
		self.n_seq = int(self.img.size[0] / self.width)
		
		self.last_update_t = time.time()
		
		uhd.rotation(90)
		uhd.brightness(brightness)
	
	@property
	def state(self):
		return self.state_
	
	@state.setter
	def state(self, new_state):
		if new_state != self.state_:
			self.img = Image.open(
						os.path.join(self.bm_dir,"bm_"+new_state+".png"))
			self.state_ = new_state
			self.update_period = 0.2
			self.img_seq = 0
		

	def tick(self):
		"""
		Function called by main run loop. Fetch new image if state has changed,
		advance animation of current image if timer has expired.
		"""
	
		t = time.time()
		
		if t - self.last_update_t > self.update_period:
			self.last_update_t = t
			
			for x in range(self.width):
				for y in range(self.height):
					pixel = self.img.getpixel(((self.img_seq * self.width) + y, x))
					r, g, b = int(pixel[0]), int(pixel[1]), int(pixel[2])
					uhd.set_pixel(x, y, r, g, b)

			uhd.show()
			self.img_seq = (self.img_seq + 1) % self.n_seq
		
		
	def __del__(self):
		uhd.off()
