from ursina import *
from enum import Enum

global terrain 

class Mode(Enum):
    HEIGHT = './textures/height.png'
    SLOPE = './textures/slope.png'
    ELEVATION = './textures/elevation.png'
    AZIMUTH = './textures/azimuth.png'

mode = Mode.ELEVATION

def change_mode():
    if mode == Mode.HEIGHT:
        mode = Mode.SLOPE
    elif mode == Mode.SLOPE:
        mode = Mode.ELEVATION
    elif mode == Mode.ELEVATION:
        mode = Mode.AZIMUTH
    else:
        mode = Mode.HEIGHT
    
    terrain.texture = mode.value


def main():
    app = Ursina(
        title="NASA - ADC",
        icon='./textures/Artemis_program.png',
        borderless=False,
        fullscreen=False,
        development_mode=False
    )

    window.color = color.black
    
    terrain = Entity(model=Terrain("./textures/heightmap.png"), texture="./textures/elevation.png")

    view_mode_button = Button(
        #model='quad',
        scale=1,
        text="Mode",
        origin=(-12, 9)
    )
    view_mode_button.on_click = change_mode

    quit_button = Button(
        model='quad', 
        scale=0.05, 
        color=color.dark_gray, 
        text="Quit", text_size=0.5, 
        text_color=color.white,
        origin=(12, 9)
    )
    quit_button.on_click = exit

    EditorCamera()

    app.run()
    

if __name__ == "__main__":
    main()
