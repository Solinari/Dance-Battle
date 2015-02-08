# Justin Tyme Dejesus
# AI 380/480
# Assignment 2

class Node:

    def __init__(self, state, parent = None, action = None,
                 path_cost = 0, depth = 0):
        '''instantiate the node but also the root if first node
        also handles how the graph to the goal is formed'''
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = depth

    def child_node(self, parent, action, state):
        '''pass a problem object to store in the child '''

        #return cost - this is kind of like abstract method tucking
        is_cost = self.depth + 1
        self.depth = is_cost

        # think about parent...
        # I think since you don't pass it, it's not none
        # and self is the pointer because it is a class object
        # and has implicit __iter__ and __next__
        # I still think you need to pass it..
        # parent = self
        return Node(state, parent, action, is_cost, self.depth)

    def path(self):
        '''return the path from root to current node'''
        this_node = self
        the_path = []
        
        while this_node:
            the_path.append(this_node)
            this_node = this_node.parent
        return the_path

    def solution(self):
        ''' return the solution along a path'''

        sol = []

        for node in self.path()[1:]:
            sol.insert(0, node.action)

        return sol

    def __eq__(self, other):
        '''returns checking to see if states are the same
        and if both are Nodes'''
        is_node = isinstance(other, Node)

        return is_node and self.state == other.state
        
    
    def __repr__(self):
        '''return the state in the node'''
        return "Node {}".format(self.state)

class Problem:

    def __init__(self, initial = None, goal = None):
        '''stating state and remember to pass goal to problem'''
        self.initial = initial
        self.goal = goal

    # REWRITE ACTIONS FOR DANCE BATTLE

    def actions(self, state):
        '''return availible actions
        this is the real meat of defining the child nodes
        this will return a list of the child Nodes to result'''

        # So here is where 0 is in the state
        # do I just want to make 9 cases? (all 9 positions)
        # Notice I am only going to read state, never alter state
        # 99% of the work is done inside this method
        z = state
        child_actions = []
            
            return child_actions

    def action_result(self, action):
        '''returns an action from self.actions(state)'''
        return action

    def state_result(self, state):
        '''returns a state from self.actions(state)'''
        return state

    def goal_test(self, state):
        '''returns boolean of if state == goal'''

        return state == self.goal

    def path_cost(self, cost):
        '''defines current path cost'''
        
        return cost + 1

class DFS:

    def __init__(self):
        '''intitalizes queue'''
        self.q = []

    def isEmpty(self):
        '''returns if queue is empty'''
        return len(self.q) == 0

    def enqueue (self, item):
        '''appends an item to queue'''
        return self.q.append(item)

    def dequeue(self):
        '''checks if empty, if not deappends an item
           since DFS, pops rearmost node(last node in queue'''
        # Remember we are comparing the return of a class method
        # against a boolean condition
        
        if self.isEmpty == True:
            return 'Queue is empty'

        else:
            return self.q.pop()

    def __eq__(self, other):
        '''checks if self.q == other.q'''
        return self.q == other.q

    def __len__(self):
        '''overloaded operator to take the length on self.q'''
        return len(self.q)

    def __repr__(self):
        '''define how to represent this object canonically'''
        # shell will call repr on variables
        return 'Queue: {}'.format(self.q)

    def __str__(self):
        '''represent the self.q object in string form'''
        # print() will call on this overloaded method
        return 'Queue is: {}'.format(self.q)
