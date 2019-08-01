from state import State
from collections import deque
import queue, heapq
import math







def BFS(inital_state, goal_state):

	frontier = deque()
	explored = set()
	frontier.append(inital_state)

	while frontier:
		state = frontier.popleft()
		explored.add(state.hash_value)
		# print(state)
		if state == goal_state:
			print(state.depth)
			# print(state.path)
			# print("SUCCESS!")
			return state.path

		for neighbour in state.generate_neighbours():
			if (neighbour not in frontier) and (neighbour.hash_value not in explored):
				frontier.append(neighbour)

	return -1



def DFS(inital_state, goal_state):

	frontier = deque()
	explored = set()
	frontier.append(inital_state)

	while frontier:
		state = frontier.pop()
		explored.add(state.hash_value)
		# print(state)
		if state == goal_state:
			print(state.depth)
			# print(state.path)
			# print("SUCCESS!")
			return state.path

		for neighbour in state.generate_neighbours():
			if (neighbour not in frontier) and (neighbour.hash_value not in explored):
				frontier.append(neighbour)

	return -1



def A_star(inital_state, goal_state, method="mnt"):

	def manhattan_distance(state):
		value_arr = state.value
		dist = 0
		for i, val in enumerate(value_arr):
			if val == 0:
				continue

			goal_y, goal_x = val // 3, val % 3
			y, x = i // 3, i % 3
			dist += abs(goal_y-y) + abs(goal_x-x)
		return dist


	def euclidean_distance(state):
		value_arr = state.value
		dist = 0
		for i, val in enumerate(value_arr):
			if val == 0:
				continue

			goal_y, goal_x = val // 3, val % 3
			y, x = i // 3, i % 3
			dist += math.sqrt(abs(goal_y-y)**2 + abs(goal_x-x)**2)
		return dist


	function = {"mnt": manhattan_distance, "euc": euclidean_distance}
	heuristic = function[method]

	frontier = []
	explored = set()
	heapq.heappush(frontier, (heuristic(inital_state), inital_state))
	frontier_dict = dict()
	frontier_dict[inital_state.hash_value] = inital_state
	# print(frontier)

	while frontier:
		cost, state = heapq.heappop(frontier)
		del frontier_dict[state.hash_value]
		explored.add(state.hash_value)

		# print(frontier)
		if state == goal_state:
			print(state.depth)
			# print(state.path)
			# print("SUCCESS!")
			return state.path

		for neighbour in state.generate_neighbours():
			if (neighbour.hash_value not in frontier_dict) and (neighbour.hash_value not in explored):
				heapq.heappush(frontier, (heuristic(neighbour)+ neighbour.depth, neighbour))
				frontier_dict[neighbour.hash_value] = neighbour

			elif neighbour.hash_value in frontier_dict:
				reexplored = frontier_dict[neighbour.hash_value]

				if neighbour.depth < reexplored.depth:
					reexplored.parent = state
					reexplored.depth = neighbour.depth
				

	
# FOR TESTING
# inital_state = State([4,1,2,3,0,4,5,6,7,8])
# goal_state = State([9,1,2,3,4,5,6,7,8,0])

# BFS(inital_state, goal_state)
# A_star(inital_state, goal_state, "euc")
