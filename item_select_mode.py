from pathlib import Path

from pico2d import *
import game_framework
import game_world
import play_mode

image = None


def init():
    global image
    image = load_image(str(Path(__file__).with_name('item_select.png')))


def finish():
    pass


def handle_events():
    pass


def update():
    pass


def render():
    pass
