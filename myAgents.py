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
        pacmanPos = game.AgentState.getPosition(pacman)  # Pacman position tup.
        pacX = pacmanPos[0]     # Pacman x position
        pacY = pacmanPos[1]      # Pacman y position
        gX = ghost.getPosition()[0]     # Ghost x position
        gY = ghost.getPosition()[1]     # Ghost y position

        distX = abs(pacX - gX)      # Distance in from x position.
        distY = abs(pacY - gY)      # Distance in from y position.

        # If pacman and the ghost are within 3 units of each other...
        # if ghost.isScared():
        #     return Directions.STOP

        # If Pacman and Ghost are on the same Y intercept and within 3 spaces  and not scared...
        if (pacX == gX and distY <= 3 and not ghost.isScared()):
            # If Ghost is under Pacman...
            if (gY < pacY):
                return Directions.SOUTH         # Danger in the South.
            # Otherwise...
            else:
                return Directions.NORTH         # Danger in the North.

        # Elif Pacman and Ghost are on the same X intercept and within 3 spaces and not scared...
        elif pacY == gY and distX <= 3 and not ghost.isScared():
            # If Ghost is to the left...
            if gX < pacX:
                return Directions.WEST          # Danger in the West.
            # Otherwise...
            else:
                return Directions.EAST          # Danger in the East.
                """
                Ghost Heading:          Pacman Danger:          G --> P : Danger <-- Pac --> Safe
                    West                    East
                    North                   South
                    East                    West
                    South                   North
                """

        return Directions.STOP  # Otherwise, return the standard STOP direction.

    def getAction(self, state):

        # List of directions the agent can choose from
        legal = state.getLegalPacmanActions()

        """***** Pacman Info. *****"""
        pacmanState = state.getPacmanState()  # Pacman state.
        heading = pacmanState.getDirection()  # Compass direction of Pacman.

        """***** Ghosts Info. *****"""
        ghostStates = pacman.GameState.getGhostStates(state)  # List of Ghost states.

        # For every ghost in ghost List...
        for i in range(len(ghostStates)):
            heading = self.inDanger(pacmanState, ghostStates[i])  # Check if Pacman is in danger.
            # If heading is anything other than STOP...
            if heading != Directions.STOP:
                break  # break out, there is danger.

        if heading == Directions.STOP:
            return pacmanAgents.LeftTurnAgent.getAction(self, state)

        reverseDir = Directions.REVERSE[heading]  # Reverse Direction (opposite of danger direction).

        if reverseDir in legal:  # Go in reverse
            action = reverseDir
        else:
            if Directions.LEFT[reverseDir] in legal:  # Go left.
                action = Directions.LEFT[reverseDir]
            elif Directions.RIGHT[reverseDir] in legal:  # Go Right.
                action = Directions.RIGHT[reverseDir]
            else:  # No more moves, Stop.
                action = Directions.STOP
        return action
