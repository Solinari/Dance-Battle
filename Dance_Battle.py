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

    def child_node(self, parent, state, action=None):
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

class Game:

    def __init__(self, initial = None, goal = None):
        '''stating state and remember to pass goal to problem'''
        self.initial = initial
        self.goal = goal

    # REWRITE ACTIONS FOR DANCE BATTLE

    def actions(self, state):
        '''return availible actions
        this is the real meat of defining the child nodes
        this will return a list of the child Nodes to result'''

        
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

    def return_goal(self):
        '''returns boolean of if state == goal'''
        print(self.goal)
        return self.goal

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

    def peek(self):
        '''use this as a helper method to peek at the top'''
        if self.isEmpty == True:
            return 'Queue is empty'

        else:
            return self.q[-1]

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


def move_list(n):
    '''returns a 2d list of boolean True'''

    # this is going to be be my initial list where all moves are game
    moves = [[True for x in range(0,n)] for x in range(0,n)]
    return moves


def My_Game_Data(difficulty):
    '''helper function to clean up dance battle
       returns a list'''

    # Get my lines out of the in file
    MyGame = open(difficulty, 'r')
    ready_game = MyGame.readlines()
    MyGame.close()
    ready_game = [ready_game[x].rstrip('\n')
                  for x in range(len(ready_game))]

    return ready_game


def make_goal(this_state):
    '''just set every tile to false and return it as the goal state'''

    mylist = []
    for i in this_state:
        mylist.append(i)
        
    for i in mylist:    
        for j in range(len(i)):
            i[j] = False

    return mylist

def get_input(length):
    '''get user input and returns as a string.
       gets the length of the list for formatting purposes'''
    
    first = "Enter two digits 0 through "
    last = "\nEnter them: a b\nThen press enter\n"
    final = first + str(length) + last

    inp = str(input(final))

    return inp
    

def Dance_Battle(difficulty):
    '''start a dance battle with a number of moves already played
       from a file that will be passed to this function'''

    # get my game data
    game_data = My_Game_Data(difficulty)
    print(game_data)

    turn_count = 0
    list_len = int(game_data[0]) - 1
    print(list_len)
    # pull the data out of the in file
    # set moves from an int cast of the 0th index
    moves_open = move_list(int(game_data[0]))

    # sets up turns to be counted and moves populated
    turn_count = int(game_data[1])

    # remember saved states
    states = {}

    # Set up search queue & initial states
    MinMax = DFS()
    check = list(map(lambda x : x, moves_open))
    
    theGame = Game(check, make_goal(check))

    begin = True
    curr_state = move_list(int(game_data[0]))
    # don't need this anymore
    game_data.pop(0)
    game_data.pop(0)

    # now to start the game
    
    Max = True
    
    while curr_state != Game.return_goal:

        # bookkeeping
        # gotta read the moves in
        if turn_count > 0:
            turn_count -= 1
            moves = game_data.pop(0)
            first_move  = int(moves[:1])
            second_move = int(moves[1:])

            curr_state[first_move][second_move] = False
            curr_state[second_move][first_move] = False
            print(curr_state)
            
            if begin == True:
                # 1st move: Max
                Root = Node(curr_state)
                MinMax.enqueue(Root)
                states[str(Root.state)] = Root.path_cost
                begin = False
                continue

            # future moves will be Min..then Max based on depth we check later
            # I don't know if I'm suppose to check their states and append here
            # on the minimax...instructions are vague about this
            frontier = MinMax.peek()
            states[str(frontier.state)] = frontier.path_cost

            MinMax.enqueue(frontier.child_node(frontier, curr_state))
            continue

        #just testing new loop
        if len(game_data) == 0:
            break

        # after steps from the file have been enqueu'd
##        curr_node = MinMax.dequeue()
##        
##        states[str(curr_node.state)] = curr_node.path_cost

##        if curr_node.state == Game.return_goal:
##
##            return curr_node.state

    
##    while curr_state != Game.return_goal:
##        
##        
##
##        
##        # Check if Max
##        if Max:
##
##            Max = False
##            continue
##        
##        #Check  if Min
##        if not Max:
##
##            Max = True
##            continue
        
        
        
        
    
EASY   = "testcaseEasy.txt"
MEDIUM = "testcaseMed.txt"
HARD   = "testcaseHard.txt"

Dance_Battle(EASY)
Dance_Battle(MEDIUM)
Dance_Battle(HARD)
