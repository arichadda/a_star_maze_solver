# Ari Chadda
# 3 October 2020
# PA2

import itertools
from math import sqrt
from Maze import Maze
from time import sleep


class SensorlessProblem:

    # keep tack of goals and current states
    # initalize class variables
    def __init__(self, maze, goal_locations):

        self.robot_goal_x, self.robot_goal_y, self.robot_current_x, self.robot_current_y = None, None, None, None
        self.maze = maze
        self.goal_state = goal_locations
        self.start_state = None
        self.check_state = tuple(self.maze.robotloc)
        self.robot_count = 0

        if len(self.maze.robotloc) > 0:
            self.robot_count = len(self.maze.robotloc)/2
            dummy_list = list(self.check_state)
            dummy_list.insert(0, 0)
            self.start_state = tuple(dummy_list)
        else:
            self.start_state = "No robots, nothing to solve"
            print(self.start_state)
            exit(0)

    # function to check if goal is reached
    def is_goal(self, state):
        if self.goal_state == state[1:]:
            return True
        else:
            return False

    def __str__(self):
        string = "Mazeworld problem: "
        return string

    # get the next available moves
    def get_successors(self, state):
        all_moves_list = []

        if not self.is_goal(state):
            move_num = state[0]
            move_num += 1
            all_moves_list.append(move_num)

            # go one point at a time
            for coordinate in range(len(state) - 1):
                if (coordinate + 1) % 2 is not 0:
                    self.robot_current_x = state[1:][coordinate]
                    self.robot_goal_x = self.goal_state[coordinate]
                else:
                    self.robot_current_y = state[1:][coordinate]
                    self.robot_goal_y = self.goal_state[coordinate]
                    # get the legal moves
                    robot_moves = self.get_valid_moves(self.robot_current_x, self.robot_current_y, self.robot_goal_x, self.robot_goal_y)
                    all_moves_list.append(robot_moves)

        # comb through moves to make sure they do no create collisions
        # imported itertools same as python heap documentation to get all the possibilities from list
        send_states = set()
        next_states = list(itertools.product(*all_moves_list[1:]))
        for nxt in next_states:
            if len(set(nxt)) != len(nxt):
                continue
            state_cache = [all_moves_list[0]]
            for point in nxt:
                state_cache.append(point[0])
                state_cache.append(point[1])
            send_states.add(tuple(state_cache))
        return send_states

        # given a sequence of states (including robot turn), modify the maze and print it out.
        #  (Be careful, this does modify the maze!)
    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state[1:])

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state[1:])
            sleep(1)

            print(str(self.maze))

    def get_valid_moves(self, current_x, current_y, goal_x, goal_y):
        moves_list = []

        # get the legal moves by maze size and but not wall locations
        if current_x is not goal_x or current_y is not goal_y:
            if (current_y + 1) <= self.maze.height:
                moves_list.append((current_x, current_y + 1))
            if (current_x + 1) <= self.maze.width:
                moves_list.append((current_x + 1, current_y))
            if (current_y - 1) > -1:
                moves_list.append((current_x, current_y - 1))
            if (current_x - 1) > -1:
                moves_list.append((current_x - 1, current_y))

        # if no moves stay in the same place
        if len(moves_list) is 0:
            moves_list.append((current_x, current_y))

        return moves_list

    def manhattan_heuristic(self, state):

        # manhattan distance heuristic for A*
        for coordinate in range(len(state) - 1):
            # go coordinate by coordinate and score
            if (coordinate + 1) % 2 is not 0:
                self.robot_current_x = state[1:][coordinate]
                self.robot_goal_x = self.goal_state[coordinate]
            else:
                self.robot_current_y = state[1:][coordinate]
                self.robot_goal_y = self.goal_state[coordinate]
                manhattan_score = self.distance_sum(self.robot_current_x, self.robot_current_y, self.robot_goal_x, self.robot_goal_y)
                return manhattan_score

    # basically compute vertical can horizontal difference
    def distance_sum(self, current_x, current_y, goal_x, goal_y):
        return abs(current_x - goal_x) + abs(current_y - goal_y)

    # euclidian distance heuristic for A*
    def euclid_heuristic(self, state):

        for coordinate in range(len(state) - 1):
            # go coordinate by coordinate and score
            if (coordinate + 1) % 2 is not 0:
                self.robot_current_x = state[1:][coordinate]
                self.robot_goal_x = self.goal_state[coordinate]
            else:
                self.robot_current_y = state[1:][coordinate]
                self.robot_goal_y = self.goal_state[coordinate]
                euclid_score = self.distance_square(self.robot_current_x, self.robot_current_y, self.robot_goal_x, self.robot_goal_y)
                return euclid_score

    # essentially pythagorean formula to get distance
    def distance_square(self, current_x, current_y, goal_x, goal_y):
        return sqrt((goal_x - current_x) ** 2 + (goal_y - current_y) ** 2)

## A bit of test code

if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_problem = SensorlessProblem(test_maze3)
