from pathlib import Path

from pico2d import *
import game_framework
import game_mode

image = None


def init():
    global image
    image = load_image(str(Path(__file__).with_name('title.png')))


def finish():
    global image
    image = None


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN:
            if getattr(event, 'repeat', 0):
                continue
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            else:
                game_framework.change_mode(game_mode)
            return


def update():
    pass


def render():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
