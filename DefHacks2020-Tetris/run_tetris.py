import tkinter as tk
import random
from tkinter import *
from graphics import *
from random import choice
import time


# declare canvas height and width in pixels for reference in other functions
canvas_height = 600
canvas_width = 360

# set shape drop delay time in seconds
drop_delay_time = 0.2

# declare environment
window = tk.Tk()
window.title("Tetris - DefHacks 2020")
canvas = Canvas(window, height=canvas_height, width=canvas_width);

# key event handler - use 60 for can_move functions to prevent glitches
def key(event):
	if event.keysym == "Down":
		if new_shape.can_move(canvas_width, canvas_height, board_block_coord_list, 0, 60):
			window.update()
			new_shape.move(canvas, 0, 30)

	elif event.keysym == "Left":
		if new_shape.can_move(canvas_width, canvas_height, board_block_coord_list, -30, 0):
			window.update()
			new_shape.move(canvas, -30, 0)

	elif event.keysym == "Right":
		if new_shape.can_move(canvas_width, canvas_height, board_block_coord_list, 30, 0):
			window.update()
			new_shape.move(canvas, 30, 0)

	elif event.keysym == "Up":
		if new_shape.can_rotate(canvas_width, canvas_height, board_block_coord_list):
			new_shape.rotate(canvas)

# declare canvas and root environment			
canvas.pack()
window.bind("<Key>", key)

# declare board block data structures 
board_block_dict = {}	# maps y-coord to block IDs
board_block_coord_list = []


def draw_shape():
	shapes_list = ["I", "L", "Mirrored L", "S", "Z", "O", "T"]
	random_shape_letter = random.choice(shapes_list)
	global new_shape	

	# -30 spawns the shape slightly above the top of the board
	if random_shape_letter == "I":
		new_shape = I_shape(canvas, canvas_width/2, -30)

	elif random_shape_letter == "L":
		new_shape = L_shape(canvas, canvas_width/2, -30)

	elif random_shape_letter == "Mirrored L":
		new_shape = Mirrored_L_shape(canvas, canvas_width/2, -30)

	elif random_shape_letter == "S":
		new_shape = S_shape(canvas, canvas_width/2, -30)

	elif random_shape_letter == "Z":
		new_shape = Z_shape(canvas, canvas_width/2, -30)

	elif random_shape_letter == "O":
		new_shape = O_shape(canvas, canvas_width/2, -30)

	elif random_shape_letter == "T":
		new_shape = T_shape(canvas, canvas_width/2, -30)


	while new_shape.can_move(canvas_width, canvas_height, board_block_coord_list, 0, 30):
		drop_shape(new_shape)
	update_board_data()
	clear_row(canvas, canvas_width)	

def update_board_data():
	# add shape block coordinates to dropped block list and dict
	for i in range(4):
		new_shape_y = new_shape.block_coord_list[i][1]
		if new_shape_y in board_block_dict.keys():
			board_block_dict[new_shape_y].append(new_shape.block_list[i])
		else:
			board_block_dict[new_shape_y] = [new_shape.block_list[i]]
	board_block_coord_list.extend(new_shape.block_coord_list)

def drop_shape(shape):
	window.update()
	time.sleep(drop_delay_time)
	shape.move(canvas, 0, 30)

def clear_row(canvas,canvas_width):
	rows_to_delete = []
	for row in board_block_dict.keys():
		# check if a row is full
		if len(board_block_dict[row]) == canvas_width/30:
			rows_to_delete.append(row)
			# update coord array
			for i in range(len(board_block_coord_list) - 1, -1, -1):
				if board_block_coord_list[i][1] == row:
					board_block_coord_list.remove(board_block_coord_list[i])
				elif board_block_coord_list[i][1] < row:
					board_block_coord_list[i] = (board_block_coord_list[i][0], board_block_coord_list[i][1] + 30)
	# update board representation
	new_board_dict = {}
	for row_num in board_block_dict.keys():
		if row_num in rows_to_delete:
			for block in board_block_dict[row_num]:
				canvas.delete(block)
		else:
			num_rows_dropped = 0
			for del_row in rows_to_delete:
				if row_num < del_row:
					num_rows_dropped += 1
			for block in board_block_dict[row_num]:	
				canvas.move(block, 0, 30 * num_rows_dropped)
				new_board_dict[(row_num + 30 * num_rows_dropped)] = board_block_dict[row_num]

	# update dictionary if rows are deleted
	if len(rows_to_delete) > 0:
		board_block_dict.clear()
	board_block_dict.update(new_board_dict)



def game_over():
	if (canvas_width/2, 0) in board_block_coord_list:
		return True
	return False

# run Tetris game
while not game_over():
	draw_shape()

mainloop()
