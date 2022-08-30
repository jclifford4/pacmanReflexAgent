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
        heading = pacman.getDirection()     # Direction Pacman is facing
        dangerHeading = ghost.getDirection()
        print(dangerHeading)

        distX = abs(pacX - gX)      # Distance in from x position.
        distY = abs(pacY - gY)      # Distance in from y position.


        # If pacman and the ghost are within 3 units of each other...
        if (pacX == gX and distY <= 3 or pacY == gY and distX <= 3):
            # If the ghosts are not scared...
            if not ghost.isScared():
                return Directions.REVERSE[dangerHeading]      # Return the compass direction of the ghost

        return Directions.STOP      # Otherwise, return the standard STOP direction.
    
    def getAction(self, state):

        # List of directions the agent can choose from
        legal = state.getLegalPacmanActions()

        """***** Pacman Info. *****"""
        pacmanState = state.getPacmanState()  # Pacman state.
        heading = pacmanState.getDirection()  # Compass direction of Pacman.

        """***** Ghosts Info. *****"""
        ghostStates = pacman.GameState.getGhostStates(state)    # List of Ghost states.



        # For every ghost in ghost List...
        for i in range(len(ghostStates)):
            heading = self.inDanger(pacmanState,ghostStates[i])  # Check if Pacman is in danger.
            # If heading is anything other than STOP...
            if heading != Directions.STOP:
                break       # break out.

        if (heading == Directions.STOP):
            return pacmanAgents.LeftTurnAgent.getAction(self, state)

        # heading = pacmanState.getDirection()
        reverseDir = Directions.REVERSE[heading]        # Reverse Direction

        if reverseDir in legal:     # Go in reverse
            action = reverseDir
        else:
            #heading = Directions.REVERSE[heading]       # Go back to forward orientation.
            if Directions.LEFT[reverseDir] in legal:       # Go left.
                action = Directions.LEFT[reverseDir]
            elif Directions.RIGHT[reverseDir] in legal:    # Go Right.
                action = Directions.RIGHT[reverseDir]
            else:
                action = Directions.STOP                     # Keep Going to danger.
        #print(action)
        return action
        # return pacmanAgents.LeftTurnAgent.getAction(self,state)
