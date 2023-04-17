from microbit import *
import microbit
microbit.install('music')

sprite = game.create_sprite(2, 2)

def on_button_pressed_a():
    if sprite.get(LedSpriteProperty.X) == 2:
        game.add_score(1)
    else:
        basic.show_icon(IconNames.SAD)
        music.play(["C4:4", "D4:4", "E4:4", "C4:4", "D4:4", "E4:4", "C4:2"])
        game.game_over()

input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    sprite.move(1)
    sprite.if_on_edge_bounce()
    basic.pause(100)

basic.forever(on_forever)