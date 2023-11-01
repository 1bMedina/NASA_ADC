import matplotlib.pyplot as plt
import numpy as np
import math
from datahandler import DataHandler
from ursina import *
from matplotlib import cm
from rich.console import Console
import inquirer
from multiprocessing import Pool

console = Console()


def triangulate(n, m):
    tri = []
    for i in range(n - 1):
        for j in range(m - 1):
            a = i + j * n
            b = (i + 1) + j * n
            d = i + (j + 1) * n
            c = (i + 1) + (j + 1) * n
            if j % 2 == 1:
                tri += [[3, a, b, d], [3, b, c, d]]
            else:
                tri += [[3, a, b, c], [3, a, c, d]]
    return np.array(tri, dtype=np.int32)


def main():
    location = inquirer.prompt([
        inquirer.List(
            'region',
            message="Select a Region",
            choices=list(DataHandler.REGIONS.keys())
        )]
    )["region"]

    height, latitude, longitude, slope = ([], [], [], [])
    with Console().status("[bold blue]Loading Data") as status:
        with Pool(processes=4) as pool:
            height, latitude, longitude, slope = pool.map(DataHandler.process_csv, DataHandler.REGIONS[location])

        dimensions = height.shape

        status.update("[bold blue]Generating Vertices")

        height = height.flatten()
        latitude = latitude.flatten()
        longitude = longitude.flatten()
        slope = slope.flatten()

        x = map(lambda n: (n[1] + 1737400) * math.cos(math.radians(latitude[n[0]])) * math.cos(
            math.radians(longitude[n[0]])), enumerate(height))
        y = map(lambda n: (n[1] + 1737400) * math.cos(math.radians(latitude[n[0]])) * math.sin(
            math.radians(longitude[n[0]])), enumerate(height))
        z = map(lambda n: (n[1] + 1737400) * math.sin(math.radians(latitude[n[0]])), enumerate(height))

        x = np.fromiter(x, dtype=np.double).reshape(dimensions)
        y = np.fromiter(y, dtype=np.double).reshape(dimensions)
        z = np.fromiter(z, dtype=np.double).reshape(dimensions)

        points = np.c_[x.reshape(-1), y.reshape(-1), z.reshape(-1)]

        status.update("[bold blue]Triangulating Faces")

        faces = triangulate(dimensions[1], dimensions[0])

        # Create a list of vertices from your x, y, and z data
        vertices = [Vec3(x[i], y[i], z[i]) for i in range(len(x))]

        # Create a mesh using your data
        lunar_mesh = Mesh(vertices=vertices, triangles=faces, mode='triangles')

        # Create a camera and set it up
        perspective_camera = PerspectiveCamera()
        perspective_camera.position = (0, 0, -5)
        perspective_camera.look_at(lunar_mesh)

        # Create a light source
        light = DirectionalLight()
        light.rotation = (45, 45, 0)
        light.color = color.white

        # Add the mesh to the scene
        lunar_mesh.entity.shader.flat_shading = True  # Flat shading for the mesh
        lunar_mesh.entity.model.color = color.white  # Color of the mesh
        lunar_mesh.entity.model.generate_normals()  # Generate normals for shading

        # Set up the 3D scene
        scene.add(lunar_mesh.entity)
        scene.add(camera)
        scene.add(light)

        # Run the app
        app.run()


if __name__ == '__main__':
    main()
