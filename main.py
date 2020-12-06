#!/usr/bin/env python3
import tcod
from input_handlers import EventHandler
from entity import Entity
from engine import Engine


def main() -> None:

    # Size of Screen
    screen_width = 200
    screen_height = 100

    # starting entity classes
    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "T", (255, 255, 0))
    entities = {npc, player}

    # instance of EventHandler Class
    event_handler = EventHandler()

    # instance of Engine Class
    engine = Engine(entities=entities, event_handler=event_handler, player=player)

    # creates tileset from image
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    # creates the screen that the items will be printed to
    with tcod.context.new_terminal(
            screen_width,
            screen_height,
            tileset=tileset,
            title="Lands of Trade",
            vsync=True,
    ) as context:
        # creates console that uses the tileset and prints to terminal
        root_console = tcod.Console(screen_width, screen_height, order="F")

        # main game loop
        while True:

            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)


if __name__ == "__main__":
    main()