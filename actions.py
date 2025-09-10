class Action:
    """
    Base class for all actions.
    """
    pass


class EscapeAction(Action):
    """
    Action to escape the game.
    Currently does nothing.
    """
    pass


class MovementAction(Action):
    """
    Action to move the player.
    """

    def __init__(self, dx: int, dy: int) -> None:
        """
        Initialize a new MovementAction.

        Args:
            dx (int): Movement in the x direction.
            dy (int): Movement in the y direction.
        """
        super().__init__()

        self.dx = dx
        self.dy = dy
