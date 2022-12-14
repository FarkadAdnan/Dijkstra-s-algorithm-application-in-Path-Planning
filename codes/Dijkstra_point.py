"""
 By:@farkadadnan
"""

# header files
from utils import *
import sys

# take start and goal node as input
startRow = int(input("Enter the row coordinate for start node (between 1 and 200) : "))
startCol = int(input("Enter the column coordinate for start node (between 1 and 300) : "))
goalRow = int(input("Enter the row coordinate for goal node (between 1 and 200) : "))
goalCol = int(input("Enter the column coordinate for goal node (between 1 and 300) : "))

# define constants
start = (startRow, startCol)
goal = (goalRow, goalCol)
clearance = 0
radius = 0
dijkstra = Dijkstra(start, goal, clearance, radius)

if(dijkstra.IsValid(start[0], start[1])):
	if(dijkstra.IsValid(goal[0], goal[1])):
		if(dijkstra.IsObstacle(start[0],start[1]) == False):
			if(dijkstra.IsObstacle(goal[0], goal[1]) == False):
				(explored_states, backtrack_states, distance_from_start_to_goal) = dijkstra.Dijkstra()
				dijkstra.animate(explored_states, backtrack_states, "./dijkstra_point.avi")
				# print optimal path found or not
				if(distance_from_start_to_goal == float('inf')):
					print("\nNo optimal path found.")
				else:
					print("\nOptimal path found. Distance is " + str(distance_from_start_to_goal))
			else:
				print("The entered goal node is an obstacle ")
				print("Please check README.md file for running Dijkstra_point.py file.")
		else:
			print("The entered initial node is an obstacle ")
			print("Please check README.md file for running Dijkstra_point.py file.")
	else:
		print("The entered goal node outside the map ")
		print("Please check README.md file for running Dijkstra_point.py file.")
else:
	print("The entered initial node is outside the map ")
	print("Please check README.md file for running Dijkstra_point.py file.")
