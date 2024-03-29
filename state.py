
class State(object):

	def __init__(self, value, parent=None, switch_tup=None):

		self.value = value
		self.parent = parent
		self.hash_value = ''.join(str(i) for i in self.value)
		# self.child = []
		# self.cost = cost
		if self.parent:
			self.depth = self.parent.depth + 1
			self.path = parent.path[:]
			self.path.append(switch_tup)
		else:
			self.depth = 0
			self.path = []


	def __str__(self):
		s = ""
		for i in range(3):
			for j in range(1, 4):
				s += str(self.value[i*3+j]) + " "
			s += "\n"
		return s
		# return ','.join(str(i) for i in self.value)


	def __repr__(self):
		return self.__str__()


	def __eq__(self, other):
		return self.value == other.value


	def __lt__(self, other):
		return self.depth < other.depth


	def generate_neighbours(self):

		self.neighbours = []
		self.moves = [-1,-3,1,3]
		self.free_tile = self.value[0]

		# excluding move Left from allowed moves if the free tile is on the left boarder 
		if (self.free_tile == 4) or (self.free_tile == 7) :
			self.moves.remove(-1)

		# excluding move Right from allowed moves if the free tile is on the right boarder 
		if (self.free_tile == 3) or (self.free_tile == 6) :
			self.moves.remove(1)

		# Generate all the neighbours and add a new state for each one
		for move in self.moves:
			step = self.free_tile + move
			if 0 < step < len(self.value):
				tmp_lst = self.value[:]
				tmp_lst[self.free_tile], tmp_lst[step] = tmp_lst[step] , tmp_lst[self.free_tile]
				tmp_lst[0] = step
				self.neighbours.append(State(tmp_lst, self, (self.free_tile, step)))

		return self.neighbours




# FOR TESTING
# inital = State([6, 1,2,3,5,4,0,6,7,8], 0)
# goal = State([1,2,3,-1,4,5,6], 0)

# print(inital)


# inital.generate_neighbours()

# print(inital.path)
# print(inital.neighbours)
# for n in inital.neighbours:
# 	print(n.path)
# 	print("====")
# print(inital == goal)