import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler


def main() -> None:
    """
    Main entry point for the game.
    """
    screen_width: int = 80  # Width of window
    screen_height: int = 50  # Height of window

    # Player position
    player_x: int = int(screen_width / 2)
    player_y: int = int(screen_height / 2)

    # Load font from provided png file
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    # Create a new context for the game
    with tcod.context.new(
        columns=screen_width,
        rows=screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")

        # Main game loop
        while True:
            root_console.print(x=player_x, y=player_y, string="@")

            context.present(root_console)

            # Clear the console for the next frame
            root_console.clear()

            # Handle events
            for event in tcod.event.wait():
                # Go to correct function in input_handlers.py
                action = event_handler.dispatch(event)

                if action is None:
                    continue  # If no action, skip to next event

                # Change position on screen
                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy

                # Exit the game
                elif isinstance(action, EscapeAction):
                    raise SystemExit()


if __name__ == "__main__":
    main()
