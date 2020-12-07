# Ari Chadda
# 3 October 2020
# PA2
from MazeworldProblem import MazeworldProblem
from Maze import Maze
from astar_search import astar_search

# null heuristic, useful for testing astar search without heuristic (uniform cost search).
def null_heuristic(state):
    return 0

# Test problems

# several test on different mazes, some given and some created. Uncomment to run.
# 3 different heuristics are also available
if __name__ == "__main__":

    test_maze3 = Maze("maze3.maz")
    test_mpA = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))
    test_maze4 = Maze("maze4.maz")
    test_mpB = MazeworldProblem(test_maze4, (8, 8, 8, 9, 8, 10))
    test_maze2 = Maze("maze2.maz")
    test_mpC = MazeworldProblem(test_maze2, (3, 0))
    test_maze5 = Maze("maze5.maz")
    test_mpD = MazeworldProblem(test_maze5, (4, 8, 3, 8, 2, 8))
    test_maze6 = Maze("maze6.maz")
    test_mpE = MazeworldProblem(test_maze6, (6, 4))
    test_maze7 = Maze("maze7.maz")
    test_mpF = MazeworldProblem(test_maze7, (8, 7, 1, 7))


    # this should explore a lot of nodes; it's just uniform-cost search
    result = astar_search(test_mpA, null_heuristic)
    print(result)
    test_mpA.animate_path(result.path)

    # this should explore a lot of nodes; it's just uniform-cost search
    result = astar_search(test_mpA, test_mpA.manhattan_heuristic)
    print(result)
    test_mpA.animate_path(result.path)

    # this should do a bit better:
    # result = astar_search(test_mpB, test_mpB.manhattan_heuristic)
    # print(result)
    # test_mpB.animate_path(result.path)

    # Your additional tests here:
    # result = astar_search(test_mpC, test_mpC.euclid_heuristic)
    # print(result)
    # test_mpC.animate_path(result.path)

    # Your additional tests here:
    # result = astar_search(test_mpD, test_mpC.manhattan_heuristic)
    # print(result)
    # test_mpD.animate_path(result.path)

    # result = astar_search(test_mpE, test_mpE.manhattan_heuristic)
    # print(result)
    # test_mpE.animate_path(result.path)

    # result = astar_search(test_mpF, test_mpF.manhattan_heuristic)
    # print(result)
    # test_mpF.animate_path(result.path)

