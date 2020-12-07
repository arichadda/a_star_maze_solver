# Ari Chadda
# 3 October 2020
# PA2
from PriorityQueue import PriorityQueue
from SearchSolution import SearchSolution


class AstarNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object
    def __init__(self, state, heuristic=0, parent=None, transition_cost=0):
        self.state = state
        self.heuristic = heuristic # heuristic score
        self.parent = parent
        self.transition_cost = transition_cost
        self.options = [] # next nodes
        if parent is not None: # total cost is aggregate cost
            self.total_cost = parent.total_cost + transition_cost
        else:
            self.total_cost = transition_cost
        # you write this part

    def priority(self): # for the priority queue to compare
        return self.heuristic + self.total_cost

    # comparison operator,
    # needed for heappush and heappop to work with AstarNodes:
    def __lt__(self, other): # priority queue compare func
        return self.priority() < other.priority()


# take the current node, and follow its parents back
#  as far as possible. Grab the states from the nodes,
#  and reverse the resulting list of states.
def backchain(node):
    result = []
    current = node
    while current:
        result.append(current.state)
        current = current.parent
    result.reverse()
    return result


# a star search using heap priority queue implementation and dictionary to store visited
def astar_search(search_problem, heuristic_fn):
    # initializing on first time
    pqueue = PriorityQueue()
    visited_states = {}
    solution = SearchSolution(search_problem, "Astar with heuristic " + heuristic_fn.__name__)
    start_node = AstarNode(search_problem.start_state, heuristic_fn(search_problem.start_state))
    pqueue.add_task(start_node, heuristic_fn(start_node.state))
    visited_states[start_node.state[1:]] = 0

    # while there are nodes in the priority queue
    while pqueue:
        # take the first node out and update location in maze
        current_node = pqueue.pop_task()
        current_state = current_node.state[1:]
        visited_states[current_state] = current_node.transition_cost + current_node.heuristic
        search_problem.maze.robotloc = list(current_node.state)[1:]

        # if the solution has been found stop and backchain path
        if search_problem.is_goal(current_node.state):
            solution.path = backchain(current_node)
            solution.cost = current_node.total_cost
            solution.nodes_visited = len(visited_states)
            return solution
        else:
            # this is for the snesorless problem so the robot does not go through walls
            # essentially removing a wall node from the possilities and setting the state to the previous one
            if not search_problem.maze.is_floor(current_state[0], current_state[1]):
                options_holder = list(search_problem.get_successors(current_node.parent.state))
                current_node = current_node.parent
                current_node.options = options_holder
                replacement = (current_node.options[0][0], current_state[0], current_state[1])
                current_node.options.remove(replacement)
                current_options = current_node.options
            else:
                # normal traversal - get options
                current_node.options = list(search_problem.get_successors(current_node.state))
                current_options = current_node.options

            # for the next moves if they haven't been visited or if they are more optimal, add them to the queue
            for option in current_options:
                next_cost = current_node.transition_cost + 1
                heuristic_value = heuristic_fn(option)
                if option[1:] not in visited_states or visited_states[option[1:]] > (next_cost + heuristic_value):
                    move = AstarNode(option, heuristic_value, current_node, next_cost)
                    pqueue.add_task(move, move.heuristic)

    return solution
