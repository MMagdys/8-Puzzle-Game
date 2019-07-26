import pygame


class Board(object):
	
	def __init__(self, x, y, width, height, tiles,dim=3, padding=2):
		self.x = x
		self.y = y
		self.width = width
		self.height = height 
		self.dim = dim
		self.padding = padding
		self.tiles = tiles
		self.tiles_obj = []
		self.free_tile = -1
		# Drawing Game Board of size (dim*dim)
		pygame.draw.rect(display, (255,255,190), (50, 150, width, height))
		self.board_font =  pygame.font.SysFont("z003", 75)
		pygame.display.update()


	def draw_board(self):
		# pygame.draw.rect(display, (255,255,190), (50, 150, self.width, self.height))
		# self.board_font =  pygame.font.SysFont("z003", 75)
		# pygame.display.update()
		# self.tiles = tiles
		tile_index = 0
		tile_dim = self.width / self.dim
		y = self.y
		for i in range(self.dim):
			x = self.x
			for j in range(self.dim):
				if self.tiles[tile_index] > 0:
					# tile = pygame.draw.rect(display, (0,50,100), (x, y, tile_dim - 2, tile_dim - 2))
					# Creating Tile object using Surface object
					tile = pygame.Surface((tile_dim, tile_dim))
					tile.fill((0,50,100))
					# Append the number to the Tile
					text = self.board_font.render(str(self.tiles[tile_index]), True, (255,255,190))
					ts = (tile_dim / 2) - (text.get_rect().width / 2)
					tile.blit(text, (ts, ts))
					# Append new Tile to Tiles list in order to make it more easier to manager later on
					self.tiles_obj.append(tile)
					# Update the Screen Window
					display.blit(tile, (x, y))
					pygame.display.update()

				else:
					tile = pygame.Surface((tile_dim, tile_dim))
					tile.fill((255, 255, 190))
					self.free_tile = tile_index
					self.tiles_obj.append(tile)

				print(self.tiles[tile_index], x ,y)
				pygame.time.delay(100)
				x += tile_dim
				tile_index += 1

			y += tile_dim
		print(self.tiles_obj)


	def switch_tile(self, tile_index):
		# if tile_index - self.free_tile == 1:
		self.tiles_obj[tile_index], self.tiles_obj[self.free_tile] = self.tiles_obj[self.free_tile], self.tiles_obj[tile_index]
		# display.blit(self.tiles_obj[tile_index], (0, 0))
		# self.tiles_obj.remove(self.tiles_obj[tile_index])
		# print(self.tiles_obj[self.free_tile].get_height())
		# self.tiles_obj[tile_index] = pygame.Surface((100, 100))
		# self.tiles_obj[tile_index].fill((255, 255, 190))
		display.blit(self.tiles_obj[tile_index], (150,250))
		pygame.display.update()
		# self.tiles_obj[tile_index]
		print(self.tiles_obj)
		# print(self.tiles_obj[tile_index].get_abs_offset())

		# pygame.display.update(self.tiles_obj[tile_index])

		# self.draw_board()






pygame.init()
display = pygame.display.set_mode((400,500))
display.fill((192, 192, 192))
pygame.display.set_caption("8 Puzzle")
font = pygame.font.SysFont(None, 50)
text = font.render("8 Puzzle", True, (0,50,100))
tw = text.get_rect().width / 2
display.blit(text, (200 - tw, 20))
# pygame.draw.rect(display, (255,255,190), (50, 150, 303, 303))
pygame.display.update()

b = Board(50, 150, 300, 300, [1,2,3,-1,4,5,6,7,8])
b.draw_board()
b.switch_tile(4)


pygame.time.delay(3000)
pygame.quit()
quit()