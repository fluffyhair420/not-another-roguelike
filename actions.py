class Action:
    """
    Base class for all actions.
    """
    pass


class EscapeAction(Action):
    """
    Action to escape the game.
    Currently does nothing.

    Args:
        Action (Action): Base class for all actions.
    """
    pass


class MovementAction(Action):
    """
    Action to move the player.

    Args:
        Action (Action): Base class for all actions.
    """

    def __init__(self, dx: int, dy: int) -> None:
        super().__init__()

        self.dx = dx
        self.dy = dy
