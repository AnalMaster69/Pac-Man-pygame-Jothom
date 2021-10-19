from collections import defaultdict

"""
'#' for obstacle
'-' for no power points
'b' for the ghost barrier
"""


map_1 = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '-'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '-'],
    ['#', ' ', '#', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', '-'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '-'],
    ['#', ' ', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', ' ', '#', '-'],
    ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', '-'],
    ['#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '-'],
    ['-', '-', '-', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '-', '-', '-', '-'],
    ['#', '#', '#', '#', ' ', '#', ' ', '#', '#', 'b', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '-'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '-', '-', '-', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-'],
    ['#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '-'],
    ['-', '-', '-', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '-', '-', '-', '-'],
    ['#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '-'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '-'],
    ['#', ' ', '#', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', '-'],
    ['#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', '-'],
    ['#', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', '#', '-'],
    ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', '-'],
    ['#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', '-'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '-'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '-'],

]
# Python program to convert Adjacency matrix
# representation to Adjacency List


def convert(m):
    adj_list = defaultdict(list)
    obstacles = ("#",)
    for y_index in range(len(m)):
        for x_index in range(len(m[y_index])):
            if m[y_index][x_index] not in obstacles:
                if x_index > 0:  # check tile at the left
                    if m[y_index][x_index - 1] not in obstacles:
                        adj_list[(x_index, y_index)].append((x_index - 1, y_index))
                if x_index < len(m[y_index]) - 1:  # check tile at the right
                    if m[y_index][x_index + 1] not in obstacles:
                        adj_list[(x_index, y_index)].append((x_index + 1, y_index))
                if x_index > 0:  # check tile at the top
                    if m[y_index - 1][x_index] not in obstacles:
                        adj_list[(x_index, y_index)].append((x_index, y_index - 1))
                if x_index < len(m[y_index]) - 1:  # check tile at the bottom
                    if m[y_index + 1][x_index] not in obstacles:
                        adj_list[(x_index, y_index)].append((x_index, y_index + 1))
    return adj_list


adjList_map_1 = convert(map_1)

# from collections import defaultdict
# # converts from adjacency matrix to adjacency list
# def convert(a):
#     adjList = defaultdict(list)
#     for i in range(len(a)):
#         for j in range(len(a[i])):
#                 if
#                        if a[i][j]== " ":
#                            adjList[(i)].append(j)
#     return adjList
#
# # driver code
# AdjList = convert(map_1)
# print(AdjList)
# print("Adjacency List:")
# # print the adjacency list
# for i in AdjList:
#     print(i, end ="")
#     for j in AdjList[i]:
#         print(" -> {}".format(j), end ="")
#     print()
#
# # This code is contributed by Muskan Kalra.
