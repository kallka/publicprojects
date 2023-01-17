# Name: Karina Kallas
# Course: CS 325
# Assignment: Assignment 8 - Portfolio Project
# Due Date: May 24, 2022
# Description: An application of Graph traversal to solve a problem.
#              The function takes a 2-D puzzle of size m by n (n rows and m columns) where  n >= 3;
#              m >= 3; and m and n can be of different sizes. Each cell in the puzzle is either marked by
#              '-' to show an empty, traversable space or by '#' to show a barrier. Two coordinates are given:
#              (a,b) for the current location and (x,y) for desired destination. The puzzle piece may only
#              move up, down, left or right. Return the path to (x,y) by covering the minimum number of cells.

import heapq

def make_graph(puzzle, total_vertices):
    """Makes an adjacency list from 3D puzzle. Each vertex is given an integer as a key name. The value
    is a dictionary containing all connected vertices, the height differential between that vertex and
    its adjacent vertices and the row and column of connected vertex."""
    graph = {num: {} for num in range(total_vertices)}
    row_length = len(puzzle[0])
    col_length = len(puzzle)
    num = -1

    for row in range(col_length):
        for col in range(row_length):
            num += 1
            # connect up
            if row != 0 and puzzle[row-1][col] != '#':
                graph[num][num - row_length] = [row-1, col]
            # connect down
            if row != col_length-1 and puzzle[row+1][col] != '#':
                graph[num][num + row_length] = [row+1, col]
            # connect left
            if col != 0 and puzzle[row][col-1] != '#':
                graph[num][num - 1] = [row, col-1]
            # connect right
            if col != row_length - 1 and puzzle[row][col+1] != '#':
                graph[num][num + 1] = [row, col+1]
    #for key,value in graph.items():
    #    print(key, ' ', value)
    print(graph)
    return graph

def solve_puzzle(puzzle, Source, Destination):
    """Uses Dijkstra's algorithm to return the minimum path from a starting point to an ending point."""
    if (not_valid(puzzle,Source,Destination)):
        return None
    total_vertices = len(puzzle)*len(puzzle[0])
    start = Source[0]*len(puzzle[0])+Source[1]
    end = Destination[0]*len(puzzle[0])+Destination[1]
    #make puzzle into graph with connected and weighted edges - weight is effort between connected vertexes
    graph = make_graph(puzzle, total_vertices)
    #store efforts in [total_distance, (row, col)]
    efforts = {num: [float('infinity'),(0,0)] for num in range(total_vertices)}
    efforts[start] = [0, Source]

    pq = [(0, start, Source)]
    while len(pq) > 0:
        current_effort, current_vertex, current_tuple = heapq.heappop(pq)

        # Traditional Dijkstra's - if connected, look for smallest distance.
        if current_effort >= efforts[current_vertex][0]:
            for neighbor, neighbor_coord in graph[current_vertex].items():
                effort = current_effort + 1
                direction_tuple = (neighbor_coord[0],neighbor_coord[1])

            # Only consider this new path if it's better than any path we've
            # already found.
                if effort < efforts[neighbor][0]:
                    efforts[neighbor] = effort, direction_tuple
                    heapq.heappush(pq, (effort, neighbor, direction_tuple))
                    # add to answer:
    # return the answer
    # for key, value in efforts.items():
        # print(key, ' ', value)
    return help_find_path(efforts, end, len(puzzle[0]))

def help_find_path(efforts, v_last, row_length):
    """Takes the stored data in efforts to reconstruct the movements. """
    if efforts[v_last][0] == float('infinity'):
        return None

    answer = [(efforts[v_last][1][0],efforts[v_last][1][1])]
    directions = ''
    key = num = v_last
    path = efforts[v_last][0]

    while path != 0:
        # connect up
        if num-row_length in efforts and efforts[num-row_length][0] == path -1:
            key = num-row_length
            answer.insert(0, (efforts[key][1][0],efforts[key][1][1]))
            directions = "D" + directions
            num = num-row_length
        # connect down
        elif num+row_length in efforts and efforts[num+row_length][0] == path -1:
            key = num+row_length
            answer.insert(0, (efforts[key][1][0], efforts[key][1][1]))
            directions = "U" + directions
            num = num+row_length
        # connect left - check not leftmost edge (col 0)
        elif efforts[key][1][1] != 0 and efforts[num-1][0] == path -1:
            key = num-1
            answer.insert(0, (efforts[key][1][0], efforts[key][1][1]))
            directions = "R" + directions
            num -=1
        # connect right - check not rightmost edge (row_length -1)
        elif efforts[key][1][1] != row_length - 1 and efforts[num+1][0] == path -1:
            key = num+1
            answer.insert(0, (efforts[key][1][0], efforts[key][1][1]))
            directions = "L" + directions
            num += 1
        path -= 1
    return (answer, directions)

def not_valid(puzzle, start, end):
    """Determines if start and end points are valid coordinates."""
    start_row = start[0]
    start_col = start[1]
    end_row = end[0]
    end_col = end[1]
    if start_col > len(puzzle[0])-1 or end_col > len(puzzle[0])-1:
        return True
    if start_row > len(puzzle)-1 or end_row > len(puzzle)-1:
        return True
    if start_col < 0 or end_col < 0 or start_row < 0 or end_row < 0:
        return True
    else:
        return False


puzzle = [['-','-','_','-','-']]
print(solve_puzzle(puzzle, (0,1), (0,3)))