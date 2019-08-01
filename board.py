import pygame
from solver import BFS, DFS, A_star
from state import State


class Board(object):
	
	def __init__(self, x, y, width, height, value_arr, color_palette, dim=3, padding=2):
		self.x = x
		self.y = y
		self.width = width
		self.height = height 
		self.dim = dim
		self.padding = padding
		self.color_palette = color_palette
		self.tiles = value_arr
		self.value_arr = value_arr
		self.tiles_obj = []
		self.tiles_pos = []
		self.free_tile = -1
		# Drawing Game Board of size (dim*dim)
		pygame.draw.rect(display, (255,255,190), (50, 150, width, height))
		self.board_font =  pygame.font.SysFont("z003", 75)
		pygame.display.update()


	def draw_board(self):
		tile_index = 0
		tile_dim = self.width / self.dim
		y = self.y
		for i in range(self.dim):
			x = self.x
			for j in range(self.dim):
				if self.value_arr[tile_index] > 0:
					# tile = pygame.draw.rect(display, (0,50,100), (x, y, tile_dim - 2, tile_dim - 2))
					# Creating Tile object using Surface object
					tile = pygame.Surface((tile_dim -padding, tile_dim -padding))
					tile.fill(self.color_palette[1])
					# Append the number to the Tile
					text = self.board_font.render(str(self.value_arr[tile_index]), True, self.color_palette[0])
					ts = (tile_dim / 2) - (text.get_rect().width / 2)
					tile.blit(text, (ts, ts))
					# Append new Tile to Tiles list in order to make it more easier to manager later on
					self.tiles_obj.append(tile)
					self.tiles_pos.append((x, y))
					# Update the Screen Window
					display.blit(tile, (x, y))

					print(tile)
					pygame.display.update()

				else:
					tile = pygame.Surface((tile_dim, tile_dim))
					tile.fill(self.color_palette[0])

					self.tiles_obj.append(tile)
					self.tiles_pos.append((x, y))
					self.free_tile = tile_index
					print(tile)
					pygame.display.update()


				print(self.value_arr[tile_index], x ,y)
				pygame.time.delay(100)
				x += tile_dim
				tile_index += 1

			y += tile_dim
		print(self.tiles_obj)
		print(self.value_arr)
		print(self.tiles_pos)


	def switch_tile(self, tile_index):
		
		free_pos = self.tiles_pos[self.free_tile]
		switch_pos = self.tiles_pos[tile_index]
		
		self.tiles_obj[tile_index], self.tiles_obj[self.free_tile] = self.tiles_obj[self.free_tile], self.tiles_obj[tile_index]
		self.value_arr[tile_index], self.value_arr[self.free_tile] = self.value_arr[self.free_tile], self.value_arr[tile_index]

		display.blit(self.tiles_obj[tile_index], switch_pos)
		display.blit(self.tiles_obj[self.free_tile], free_pos)
		self.free_tile = tile_index

		pygame.display.update()
		pygame.time.delay(200)
		print(self.value_arr)
		print(self.tiles_pos)
		


def main():

	pygame.init()
	global display
	display = pygame.display.set_mode((400,500))
	display.fill((192, 192, 192))
	pygame.display.set_caption("8 Puzzle")
	font = pygame.font.SysFont(None, 50)
	text = font.render("8 Puzzle", True, (0,50,100))
	tw = text.get_rect().width / 2
	display.blit(text, (200 - tw, 20))
	# pygame.draw.rect(display, (255,255,190), (50, 150, 303, 303))
	pygame.display.update()

	color_palette = [(255,255,190), (0,50,100)]

	b = Board(50, 150, 300, 300, [1,2,3,-1,4,5,6,7,8], color_palette)
	b.draw_board()
	
	inital_state = State([4,1,2,3,0,4,5,6,7,8])
	goal_state = State([9,1,2,3,4,5,6,7,8,0])
	# path = BFS(inital_state, goal_state)
	path = A_star(inital_state, goal_state)

	# path = [(4, 5), (5, 6), (6, 9), (9, 8), (8, 7), (7, 4), (4, 5), (5, 8), (8, 9), (9, 6), (6, 5), (5, 4), (4, 7), (7, 8), (8, 9)]

	for s in path:
		b.switch_tile(s[1]-1)
		pygame.time.delay(500)


	# b.switch_tile(4)
	# b.switch_tile(1)


	pygame.display.update()



	pygame.time.delay(3000)
	pygame.quit()
	quit()


if __name__ == '__main__':
	main()