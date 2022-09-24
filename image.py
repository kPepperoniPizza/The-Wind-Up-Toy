import pygame
import os

player = {
    "up": pygame.image.load(os.path.join("assets\\images\\player\\facing", "up.png")),
    "down": pygame.image.load(os.path.join("assets\\images\\player\\facing", "down.png")),
    "left": pygame.image.load(os.path.join("assets\\images\\player\\facing", "left.png")),
    "right": pygame.image.load(os.path.join("assets\\images\\player\\facing", "right.png")),
    "light": pygame.image.load(os.path.join("assets\\images\\player", "light.png"))
}

level = {
    "tutorial": {
        "wall": pygame.image.load(os.path.join("assets\\images\\level\\game", "wall.png")),
        1: pygame.image.load(os.path.join("assets\\images\\level\\game", "1.png")),
        2: pygame.image.load(os.path.join("assets\\images\\level\\game", "2.png")),
        "2_wall": pygame.image.load(os.path.join("assets\\images\\level\\game", "2_wall.png")),
        "3_wall": pygame.image.load(os.path.join("assets\\images\\level\\game", "3_wall.png")),
        "4_wall": pygame.image.load(os.path.join("assets\\images\\level\\game", "4_wall.png")),
        "5_wall": pygame.image.load(os.path.join("assets\\images\\level\\game", "5_wall.png"))
    }
}

ui = {
    "playing_screen": pygame.image.load(os.path.join("assets\\images\\ui", "playing_screen.png")),
    "ending": pygame.image.load(os.path.join("assets\\images\\ui", "ending.png"))
}