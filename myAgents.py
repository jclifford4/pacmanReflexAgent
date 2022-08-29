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
        pacmanPos = game.AgentState.getPosition(pacman)     # Pacman position tup.
        pacX = pacmanPos[0]     # Pacman x position
        pacY = pacmanPos[1]     # Pacman y position
        gX = ghost.getPosition()[0]     # Ghost x position
        gY = ghost.getPosition()[1]     # Ghost y position



        distX = abs(pacX - gX)      # Distance in from x position.
        distY = abs(pacY - gY)      # Distance in from y position.

        # If pacman and the ghost are within 3 units of each other...
        if (pacX == gX and distY <=3 or pacY == gY and distX <= 3):
            print("Within MinDist: {0} {1}" .format(pacman,ghost))







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

        # Get the agent's state from the game state and find agent heading
        pacmanState = state.getPacmanState()
        # pacmanPos = state.getPacmanPosition()       # Pacman state
        pacmanPos = pacman.GameState.getPacmanPosition(state)


        heading = pacmanState.getDirection()

        if heading == Directions.STOP:
            # Pacman is stopped, assume North (true at beginning of game)
            heading = Directions.NORTH


        # List of Ghost states
        ghostStates = pacman.GameState.getGhostStates(state)


        for i in range(len(ghostStates)):
            action = self.inDanger(pacmanState,ghostStates[i])

        return pacmanAgents.LeftTurnAgent.getAction(self,state)
