from ursina import *

def main():
    app = Ursina()

    moon = Entity(model=Terrain("./hm.png"))

    moon.color = color.white  # Color of the mesh

    print('Setting up lighting')

    # Create a light source
    light = DirectionalLight()
    light.rotation = (45, 45, 0)
    light.color = color.white
    
    EditorCamera()

    app.run()

if __name__ == '__main__':
    main()
