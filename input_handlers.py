from typing import Optional

import tcod.event

from actions import Action, EscapeAction, MovementAction


class EventHandler(tcod.event.EventDispatch[Action]):
    """
    Handles events for the game.
    Determines what to do based on user input.
    Currently:
    - Arrow keys move the player
    - Escape key exits the game
    """

    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        """
        Exit the game when the window is closed.
        """
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        """
        Handle key down events.
        - Arrow keys move the player.
        - Escape key exits the game.

        Args:
            event (tcod.event.KeyDown): The key down event.

        Returns:
            Optional[Action]: The action to be performed, if any.
        """
        action: Optional[Action] = None  # Set to none for now, will return later

        key = event.sym

        if key == tcod.event.K_UP:  # Up arrow key
            action = MovementAction(dx=0, dy=-1)  # Move up
        elif key == tcod.event.K_DOWN:  # Down arrow key
            action = MovementAction(dx=0, dy=1)  # Move down
        elif key == tcod.event.K_LEFT:  # Left arrow key
            action = MovementAction(dx=-1, dy=0)  # Move left
        elif key == tcod.event.K_RIGHT:  # Right arrow key
            action = MovementAction(dx=1, dy=0)  # Move right

        elif key == tcod.event.K_ESCAPE:  # Escape key
            action = EscapeAction()  # Exit the game

        return action
