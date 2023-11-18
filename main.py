from ursina import *
from ursina.shaders import lit_with_shadows_shader

def main():
    app = Ursina()

    moon = Entity(
        model=Terrain("hm"),
        shader=lit_with_shadows_shader,
        scale=(40,5,20))
    
    hv = moon.model.height_values.tolist()
    moon_terrain = Entity(model=Terrain(height_values=hv), scale=(40,5,20), texture='hm', x=40)

    moon.color = color.gray  # Color of the mesh

    print("Setting up lighting")

    # Create a light source
    #light = AmbientLight(color = color.rgba(100, 100, 100, 0.1))
    light = DirectionalLight(parent=moon, shadows=True)
    light.rotation = (45, 45, 0)
    light.color = color.white

    EditorCamera()

    app.run()


if __name__ == "__main__":
    main()
