from util import manhattanDistance
from game import Directions
import random, util
from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and child states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        The evaluation function takes in the current and proposed child
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.
        """
        # Useful information you can extract from a GameState (pacman.py)
        childGameState = currentGameState.getPacmanNextState(action)
        newPos = childGameState.getPacmanPosition()
        newFood = childGameState.getFood()
        newGhostStates = childGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        minGhostDistance = min([manhattanDistance(newPos, state.getPosition()) for state in newGhostStates])

        scoreDiff = childGameState.getScore() - currentGameState.getScore()

        pos = currentGameState.getPacmanPosition()
        nearestFoodDistance = min([manhattanDistance(pos, food) for food in currentGameState.getFood().asList()])
        newFoodsDistances = [manhattanDistance(newPos, food) for food in newFood.asList()]
        newNearestFoodDistance = 0 if not newFoodsDistances else min(newFoodsDistances)
        isFoodNearer = nearestFoodDistance - newNearestFoodDistance

        direction = currentGameState.getPacmanState().getDirection()
        if minGhostDistance <= 1 or action == Directions.STOP:
            return 0
        if scoreDiff > 0:
            return 8
        elif isFoodNearer > 0:
            return 4
        elif action == direction:
            return 2
        else:
            return 1


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (Part 1)
    """
    ###################
    
    ###################
    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.getNextState(agentIndex, action):
        Returns the child game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        # Begin your code (Part 1)
        #raise NotImplementedError("To be implemented")
        """
        Starting from depth=1 and agentIndex=0, we have to check the ghost. Go into "minimax" with agentIndex=1.
        Do the same things, go into "minimax" with agentIndex=2. After checking all the pacman and ghosts in this depth
        , we go to "minimax" with depth=2 and agentIndex again. Repeat the process until we meet the depth we want to search
        , and the code will return evaluationFunction(gameState), the value. Because of the recursive, we trace back to agentIndex=2
        and depth = self.depth-1. After returning the minimax, we returns to agentIndex=1 and do the same thing.
        Only if agentIndex=0, we returns the maximum. If depth=1 and agentIndex=0, it means we have finished the function
        and we have to return the action that we should do.
        """
        def minimax(depth, agentIndex, gameState):
            if (gameState.isWin() or gameState.isLose() or depth > self.depth):
                return self.evaluationFunction(gameState)
            ret = [] # store the value of the state after the actions
            todo = gameState.getLegalActions(agentIndex) # store all the legal actions in this gamestate and agentIndex
            for action in todo:
                successor = gameState.getNextState(agentIndex, action) #after doing the action, successor stores next state
                if((agentIndex+1) >= gameState.getNumAgents()):
                    ret = ret + [minimax(depth+1, 0, successor)]
                else:
                    ret = ret + [minimax(depth, agentIndex+1, successor)]
            if agentIndex == 0:
                if(depth == 1):
                    maxscore = max(ret)
                    for i in range(len(ret)):
                        if (ret[i] == maxscore):
                            return todo[i]
                else:
                    retVal = max(ret)
            elif agentIndex > 0:
                retVal = min(ret)
            return retVal
        return minimax(1,0,gameState)
        # End your code (Part 1)


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (Part 2)
    """
    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        # Begin your code (Part 2)
        #raise NotImplementedError("To be implemented")
        """
        AlphaBeta is almost the same as minimax. The only difference is that we have alpha and beta.
        Beta means best option from min node to the root.
        Alpha means best option from max node to the root.
        """
        def alphaBeta(depth, agentIndex, gameState, a, b):
            alpha = a
            beta = b
            if (gameState.isWin() or gameState.isLose() or depth > self.depth):
                return self.evaluationFunction(gameState)
            retList = []
            todo = gameState.getLegalActions(agentIndex)
            for action in todo:
                successor = gameState.getNextState(agentIndex, action)
                if((agentIndex+1) >= gameState.getNumAgents()):
                    ret = alphaBeta(depth+1, 0, successor, alpha, beta)
                else:
                    ret = alphaBeta(depth, agentIndex+1, successor, alpha, beta)
                if(agentIndex == 0 and ret > beta): # cut the node
                    return ret
                if (agentIndex > 0 and ret < alpha): # cut the node
                    return ret
                if (agentIndex == 0 and ret > alpha): # replace
                    alpha = ret
                if (agentIndex > 0 and ret < beta): # replace
                    beta = ret
                retList += [ret]
            if agentIndex == 0:
                if(depth == 1):
                    maxscore = max(retList)
                    length = len(retList)
                    for i in range(length):
                        if (retList[i] == maxscore):
                            return todo[i]
                else:
                    retVal = max(retList)

            elif agentIndex > 0:
                retVal = min(retList)
            return retVal
        return alphaBeta(1,0, gameState, -99999, 99999)
        # End your code (Part 2)


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (Part 3)
    """
    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        # Begin your code (Part 3)
        #raise NotImplementedError("To be implemented")
        """
        It's also the same as minimax, but the ghosts will move ramdomly.
        As a result, the value of the ghosts is the average of values of all the actions.
        """
        def performExpectimax(depth, agentIndex, gameState):
            if (gameState.isWin() or gameState.isLose() or depth > self.depth):
                return self.evaluationFunction(gameState)
            ret = []
            todo = gameState.getLegalActions(agentIndex)
            for action in todo:
                successor = gameState.getNextState(agentIndex, action)
                if((agentIndex+1) >= gameState.getNumAgents()):
                    ret += [performExpectimax(depth+1, 0, successor)]
                else:
                    ret += [performExpectimax(depth, agentIndex+1, successor)]
            if agentIndex == 0:
                if(depth == 1):
                    maxscore = max(ret)
                    length = len(ret)
                    for i in range(length):
                        if (ret[i] == maxscore):
                            return todo[i]
                else:
                    retVal = max(ret)
            elif agentIndex > 0:
                s = sum(ret)
                l = len(ret)
                retVal = float(s/l)
            return retVal
        return performExpectimax(1, 0, gameState)
        # End your code (Part 3)


def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (Part 4).
    """
    # Begin your code (Part 4)
    """
    The nearest the food, the highest the score. <- score += food / min(distancesToFoodList)
    The nearest the ghosts, the lower the schore (because ghost_weight is negative) <- score += ghost_weight / distance
    However, if the ghost is scared, the score will be very high. <- score += scared_ghost_weight / distance
    """
    Pos = currentGameState.getPacmanPosition()
    Food = currentGameState.getFood()
    GhostStates = currentGameState.getGhostStates()
    INF = 100000000.0
    food_weight = 10.0  
    ghost_weight = -10.0 
    scared_ghost_weight = 200.0 
    score = currentGameState.getScore()
    distancesToFoodList=[]
    for foodPos in Food.asList():
        distancesToFoodList = [util.manhattanDistance(Pos, foodPos) ] # distance from all the food to pacman
    if len(distancesToFoodList) > 0:
        score = score + food_weight / min(distancesToFoodList)
    else:
        score = score + food_weight
    for ghost in GhostStates:
        distance = manhattanDistance(Pos, ghost.getPosition()) # distance from all the ghosts to pacman
        if distance > 0:
            if ghost.scaredTimer > 0:
                score = score + scared_ghost_weight / distance
            else:
                score = score + ghost_weight / distance
        else:
            return -INF
    return score
    # End your code (Part 4)

# Abbreviation
better = betterEvaluationFunction
