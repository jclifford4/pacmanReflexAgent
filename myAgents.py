import game
import ghostAgents
import pacman
import pacmanAgents
from pacman import Directions
from game import Agent, Actions
from pacmanAgents import LeftTurnAgent


class TimidAgent(Agent):
    """
    A simple agent for PacMan
    """

    def __init__(self):
        super().__init__()  # Call parent constructor
        # Add anything else you think you need here

    def inDanger(self, pacman, ghost, dist=3):
        """inDanger(pacman, ghost) - Is the pacman in danger
        For better or worse, our definition of danger is when the pacman and
        the specified ghost are:
           in the same row or column,
           the ghost is not scared,
           and the agents are <= dist units away from one another

        If the pacman is not in danger, we return Directions.STOP
        If the pacman is in danger we return the direction to the ghost.
        """





        return Directions.STOP





        # Your code
        raise NotImplemented
    
    def getAction(self, state):
        """
        state - GameState

        
        Fill in appropriate documentation
        """
        # List of directions the agent can choose from
        legal = state.getLegalPacmanActions()
        action = None
        dir = None

        # Get the agent's state from the game state and find agent heading
        pacmanState = state.getPacmanState()
        pacmanPos = state.getPacmanPosition()       # Pacman state
        pacX = pacmanPos[0]     # Pacman x position
        pacY = pacmanPos[1]     # Pacman y position

        heading = pacmanState.getDirection()

        if heading == Directions.STOP:
            # Pacman is stopped, assume North (true at beginning of game)
            heading = Directions.NORTH


        # List of Ghost states
        ghostStates = pacman.GameState.getGhostStates(state)
        ghost1 = ghostStates[0]     # Ghost1 state
        ghost2 = ghostStates[1]     # Ghost2 state
        g1X = ghost1.getPosition()[0]   # Ghost1 x position
        g1Y = ghost1.getPosition()[1]   # Ghost2 y position
        g2X = ghost2.getPosition()[0]   # Ghost1 x position
        g2Y = ghost2.getPosition()[1]   # Ghost2 y position
        action = None

        for i in range(len(ghostStates)):
            minDist = min(abs(pacX - g1X),abs(pacY - g1Y))
            print(minDist)
            if (pacX == g1X or pacY == g1Y) and (minDist <= 3):
                dir = self.inDanger(self,pacmanState,ghost1)
                print(dir)













        # for ghostState in ghostStates:
        #     print(len(ghostStates))
        #     #print("{0} Index: {1}".format(ghostState.getPosition(), i))
        #     #print(ghostState.getPosition())
        #     print("Ghost 1: {0}\nGhost 2: {1}".format(ghostStates[0],ghostStates[1]))
        #
        #     i += 1
        #     if not self.inDanger(self, pacmanState, ghostState):
        #         return Directions.STOP


        return pacmanAgents.LeftTurnAgent.getAction(self,state)
