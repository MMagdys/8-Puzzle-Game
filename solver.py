from state import State
from collections import deque
import queue



inital_state = State([4,1,2,3,0,4,5,6,7,8])
goal_state = State([9,1,2,3,4,5,6,7,8,0])
# inital_state.generate_neighbours()
# neighbours = inital_state.neighbours
# print(neighbours)

# for neighbour in neighbours:
# 	if neighbour == goal_state:
# 		print("SUCCESS!")



def BFS(inital_state, goal_state):

	frontier = deque()
	explored = set()
	frontier.append(inital_state)

	while frontier:
		state = frontier.popleft()
		explored.add(state.hash_value)
		print(state)
		if state == goal_state:
			print(state.depth)
			print(state.path)
			print("SUCCESS!")
			return 

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
		print(state)
		if state == goal_state:
			print(state.depth)
			print(state.path)
			print("SUCCESS!")
			return 

		for neighbour in state.generate_neighbours():
			if (neighbour not in frontier) and (neighbour.hash_value not in explored):
				frontier.append(neighbour)

	return -1



def A_star(inital_state, goal_state):

	pass




BFS(inital_state, goal_state)


arr = [[1, 2, 3], [0, 4, 5], [6, 7, 8]]

def manhattan_distance():

	for i in range(3):
		for j in range(3):
			print(arr[0].index(1))


# manhattan_distance()