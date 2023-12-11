from ursina import *
from enum import Enum
import json

global terrain 

class Mode(Enum):
    HEIGHT = './textures/height.png'
    SLOPE = './textures/slope.png'
    ELEVATION = './textures/elevation.png'
    AZIMUTH = './textures/azimuth.png'

mode = Mode.HEIGHT


def main():
    data = json.load(open("./textures/data.json"))

    app = Ursina(
        title="NASA - ADC",
        borderless=False,
        fullscreen=False,
        development_mode=False
    )

    window.color = color.black

    terrain = Entity(
        model=Terrain("./textures/heightmap.png"), 
        scale=(data["x_scale"] / 100, data["z_scale"] / 100, data["y_scale"] / 100)
    )

    def change_mode():
        global mode

        if mode == Mode.HEIGHT:
            mode = Mode.SLOPE
        elif mode == Mode.SLOPE:
            mode = Mode.ELEVATION
        elif mode == Mode.ELEVATION:
            mode = Mode.AZIMUTH
        else:
            mode = Mode.HEIGHT
        
        terrain.texture = mode.value

    view_mode_button = Button(
        scale=(0.075, 0.05), 
        radius=0.2,
        color=color.dark_gray, 
        text="Mode", text_size=0.5,
        origin=(9.3, 9.35),
    )
    view_mode_button.on_click = change_mode

    quit_button = Button(
        scale=(0.075, 0.05), 
        radius=0.2,
        color=color.dark_gray, 
        text="Quit", text_size=0.5, 
        text_color=color.white,
        origin=(10.4, 9.35)
    )
    quit_button.on_click = exit

    scale_background = Entity(
        parent=camera.ui,
        model='quad',
        scale=(0.03, 0.405),
        origin=(-25, 0),
        color=color.dark_gray
    )

    color_scale = Entity(
        parent=camera.ui,
        model='quad',
        texture="./textures/gradient.png",
        texture_scale=(1, 1),
        scale=(0.025, 0.4),
        origin=(-30, 0)
    )

    EditorCamera()

    change_mode()

    app.run()
    

if __name__ == "__main__":
    main()
