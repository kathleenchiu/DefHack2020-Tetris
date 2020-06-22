import tkinter as tk
from tkinter import *

# Squares are 30 by 30 pixels

class Square():
	def __init__(self, canvas, x, y, color):
		self.canvas = canvas
		self.x = x
		self.y = y
		self.color = color
	def make_block(self, canvas, x, y, color):
		return self.canvas.create_rectangle(x, y, x+30, y+30, outline="black", 
										fill=color, width=2)

class Shape(Square):
	def __init__(self):
		self.block_list = []
		self.block_coord_list = []	# holds 2-tuple coordinates of form (x,y) holding block pixel position

	# Moves a shape by dx and dy where +dx is to the right and + dy is down, 
	# 	following the convention of the canvas.
	def move(self, canvas, dx, dy):
		for block in self.block_list:
			canvas.move(block, dx, dy)
		for i in range(4):
			self.block_coord_list[i] = (self.block_coord_list[i][0] + dx, self.block_coord_list[i][1] + dy)

	# Checks if a translation of the shape by dx and dy is allowed. 
	# +dx is to the right and + dy is down, following the convention of the canvas
	# Note that we don't have to check for negative dy because shapes never move upwards
	def can_move(self, canvas_width, canvas_height, canvas_block_coord_list, dx, dy):
		for block_coord in self.block_coord_list:
			new_x = block_coord[0] + dx
			new_y = block_coord[1] + dy
			# check for outside window 
			if ((new_x >= canvas_width) or (new_x < 0) or (new_y >= canvas_height)):
				return False
			# check for collisions with existing blocks
			for existing_block_coord in canvas_block_coord_list:
				if ((new_x == existing_block_coord[0]) and (new_y == existing_block_coord[1])):
					return False
		return True

	def rotate(self, canvas):
		rotation_block_x = self.block_coord_list[0][0]
		rotation_block_y = self.block_coord_list[0][1]
		for i in range(1, 4):
			dx = rotation_block_x + rotation_block_y - self.block_coord_list[i][1] - self.block_coord_list[i][0]
			dy = self.block_coord_list[i][0] + rotation_block_y - rotation_block_x - self.block_coord_list[i][1]
			canvas.move(self.block_list[i], dx, dy)
			self.block_coord_list[i] = (self.block_coord_list[i][0] + dx, self.block_coord_list[i][1] + dy)

	# Rotates shape counterclockwise about the coordinates of the first block in the self coordinate list
	def can_rotate(self, canvas_width, canvas_height, canvas_block_coord_list):
		rotation_block_x = self.block_coord_list[0][0]
		rotation_block_y = self.block_coord_list[0][1]
		for block_coord in self.block_coord_list:
			new_x = rotation_block_x + rotation_block_y - block_coord[1] 
			new_y = block_coord[0] + rotation_block_y - rotation_block_x
			# check for outside window 
			if ((new_x >= canvas_width) or (new_x < 0) or (new_y >= canvas_height)):
				return False
			# check for collisions with existing blocks
			for existing_block_coord in canvas_block_coord_list:
				if ((new_x == existing_block_coord[0]) and (new_y == existing_block_coord[1])):
					return False
		return True			



class L_shape(Shape):
	def __init__(self, canvas, x, y, color="OliveDrab1"):
		self.canvas = canvas
		self.x = x
		self.y = y
		super(L_shape, self).__init__()

		# Create blocks - central block of L is the vertex
		s1 = self.make_block(canvas, x, y, color)
		s2 = self.make_block(canvas, x + 30, y, color)
		s3 = self.make_block(canvas, x, y + 30, color) 
		s4 = self.make_block(canvas, x, y + 60, color)

		# Update lists accordingly
		self.block_list.append(s1)
		self.block_list.append(s2)
		self.block_list.append(s3)
		self.block_list.append(s4)

		self.block_coord_list.append((x, y))
		self.block_coord_list.append((x + 30, y))
		self.block_coord_list.append((x, y + 30))
		self.block_coord_list.append((x, y + 60))

class I_shape(Shape):
	def __init__(self, canvas, x, y, color="Sky Blue"):
		self.canvas = canvas
		self.x = x
		self.y = y
		super(I_shape, self).__init__()

		# central block of I is the 2nd from top
		s1 = self.make_block(canvas, x, y, color)
		s2 = self.make_block(canvas, x, y - 30, color)
		s3 = self.make_block(canvas, x, y + 30, color) 
		s4 = self.make_block(canvas, x, y + 60, color)		

		# update lists accordingly
		self.block_list.append(s1)
		self.block_list.append(s2)
		self.block_list.append(s3)
		self.block_list.append(s4)

		self.block_coord_list.append((x, y))
		self.block_coord_list.append((x, y - 30))
		self.block_coord_list.append((x, y + 30))
		self.block_coord_list.append((x, y + 60))		
		
class Mirrored_L_shape(Shape):
	def __init__(self, canvas, x, y, color = "DarkOrchid2"):
		self.canvas = canvas
		self.x = x
		self.y = y
		super(Mirrored_L_shape, self).__init__()

		# central block of mirrored L is the vertex
		s1 = self.make_block(canvas, x, y, color)
		s2 = self.make_block(canvas, x - 30, y, color)
		s3 = self.make_block(canvas, x, y + 30, color) 
		s4 = self.make_block(canvas, x, y + 60, color)

		# update lists accordingly
		self.block_list.append(s1)
		self.block_list.append(s2)
		self.block_list.append(s3)
		self.block_list.append(s4)

		self.block_coord_list.append((x, y))
		self.block_coord_list.append((x - 30, y))
		self.block_coord_list.append((x, y + 30))
		self.block_coord_list.append((x, y + 60))

class S_shape(Shape):
	def __init__(self, canvas, x, y, color="gold"):
		self.canvas = canvas
		self.x = x
		self.y = y
		super(S_shape, self).__init__()

		# central block of S is in middle
		s1 = self.make_block(canvas, x, y, color)
		s2 = self.make_block(canvas, x + 30, y, color)
		s3 = self.make_block(canvas, x + 30, y + 30, color) 
		s4 = self.make_block(canvas, x, y - 30, color)

		# update lists accordingly
		self.block_list.append(s1)
		self.block_list.append(s2)
		self.block_list.append(s3)
		self.block_list.append(s4)

		self.block_coord_list.append((x, y))
		self.block_coord_list.append((x + 30, y))
		self.block_coord_list.append((x + 30, y + 30))
		self.block_coord_list.append((x, y - 30))

class Z_shape(Shape):
	def __init__(self, canvas, x, y, color="light slate blue"):
		self.canvas = canvas
		self.x = x
		self.y = y
		super(Z_shape, self).__init__()

		#central block of Z is in the middle
		s1 = self.make_block(canvas, x, y, color)
		s2 = self.make_block(canvas, x + 30, y, color)
		s3 = self.make_block(canvas, x, y + 30, color) 
		s4 = self.make_block(canvas, x + 30, y - 30, color)		

		# update lists accordingly
		self.block_list.append(s1)
		self.block_list.append(s2)
		self.block_list.append(s3)
		self.block_list.append(s4)

		self.block_coord_list.append((x, y))
		self.block_coord_list.append((x + 30, y))
		self.block_coord_list.append((x, y + 30))
		self.block_coord_list.append((x + 30, y - 30))

class O_shape(Shape):
	def __init__(self, canvas, x, y, color="salmon"):
		self.canvas = canvas
		self.x = x
		self.y = y
		super(O_shape, self).__init__()

		#central block of O is the top right corner
		s1 = self.make_block(canvas, x, y, color)
		s2 = self.make_block(canvas, x - 30, y, color)
		s3 = self.make_block(canvas, x - 30, y + 30, color) 
		s4 = self.make_block(canvas, x, y + 30, color)	

		# update lists accordingly	
		self.block_list.append(s1)
		self.block_list.append(s2)
		self.block_list.append(s3)
		self.block_list.append(s4)

		self.block_coord_list.append((x, y))
		self.block_coord_list.append((x - 30, y))
		self.block_coord_list.append((x - 30, y + 30))
		self.block_coord_list.append((x, y + 30))

class T_shape(Shape):
	def __init__(self, canvas, x, y, color="spring green"):
		self.canvas = canvas
		self.x = x
		self.y = y
		super(T_shape, self).__init__()

		s1 = self.make_block(canvas, x, y, color)
		s2 = self.make_block(canvas, x + 30, y, color)
		s3 = self.make_block(canvas, x - 30, y, color) 
		s4 = self.make_block(canvas, x, y - 30, color)

		# update lists accordingly
		self.block_list.append(s1)
		self.block_list.append(s2)
		self.block_list.append(s3)
		self.block_list.append(s4)

		self.block_coord_list.append((x, y))
		self.block_coord_list.append((x + 30, y))
		self.block_coord_list.append((x - 30, y))
		self.block_coord_list.append((x, y - 30))
