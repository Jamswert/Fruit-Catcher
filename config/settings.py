from pathlib import Path

# Base directory: project root (one level up from config/)
BASE_DIR = Path(__file__).parent.parent

# Directories
ASSETS_DIR = BASE_DIR / "Assets"
SPRITES_DIR = ASSETS_DIR / "Sprites"

WINDOW_HEIGHT = 720
WINDOW_WIDTH = 500
WINDOW_TITLE = "Fruit Catcher"
FPS = 60



# All colours chosen from the website:
# www.htmlcolorcodes.com/color-picker
# and the RGB values are copied.
BG_COLOUR = (163, 187, 217)

# BASE SCALE OF ALL SPRITES
BASE_SPRITE_SIZE = 16
SPRITE_SCALE = 2

# All Sprites handmade by myself.
PLAYER_SPRITE = SPRITES_DIR / "player.png"