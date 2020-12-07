# Ari Chadda
# 3 October 2020
# PA2
from SensorlessProblem import SensorlessProblem
from Maze import Maze
from astar_search import astar_search

# null heuristic, useful for testing astar search without heuristic (uniform cost search).
def null_heuristic(state):
    return 0

# several test on different mazes, some given and some created. Uncomment to run.
# 3 different heuristics are also available
if __name__ == "__main__":

    test_maze2 = Maze("maze2.maz")
    test_mp = SensorlessProblem(test_maze2, (3, 0))
    test_maze6 = Maze("maze6.maz")
    test_mpE = SensorlessProblem(test_maze6, (6, 4))
    #print(test_mp.get_successors(test_mp.start_state))

    # this should explore a lot of nodes; it's just uniform-cost search
    # result = astar_search(test_mp, null_heuristic)
    # print(result)
    # print(test_maze2)

    # result = astar_search(test_mp, test_mp.manhattan_heuristic)
    # print(result)
    # test_mp.animate_path(result.path)

    # result = astar_search(test_mp, test_mp.euclid_heuristic)
    # print(result)
    # test_mp.animate_path(result.path)

    result = astar_search(test_mpE, test_mpE.manhattan_heuristic)
    print(result)
    test_mpE.animate_path(result.path)
