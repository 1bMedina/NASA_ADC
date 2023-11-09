import pandas as pd
import numpy as np
import inquirer
from rich.console import Console
from multiprocessing import Pool
from ursina import *

def triangulate(n, h):
    tris = []
    for i in range(h - 1):
        if i % 2 == 0:
            for j in range(0, n, 2):
                tris.append(j + (n * i))
                tris.append(j + (n * i) + 1)
                tris.append(n + j + (n * i))
                tris.append(n + j + (n * i) + 1)
        else:
            for j in range(0, n, -2):
                tris.append(j + (n * i))
                tris.append(j + (n * i) - 1)
                tris.append(n + j + (n * i))
                tris.append(n + j + (n * i) + 1)
    return tris
        

console = Console()

height, latitude, longitude, slope = ([], [], [], [])
with Console().status("[bold blue]Loading Data") as status:
    height = np.array(pd.read_csv("data/FY23_ADC_Height_PeakNearShackleton.csv"))
    latitude = np.array(pd.read_csv("data/FY23_ADC_Latitude_PeakNearShackleton.csv"))
    longitude = np.array(pd.read_csv("data/FY23_ADC_Longitude_PeakNearShackleton.csv"))
    slope = np.array(pd.read_csv("data/FY23_ADC_Slope_PeakNearShackleton.csv"))

    dimensions = height.shape

    status.update("[bold blue]Generating Vertices")

    height = height.flatten()
    latitude = latitude.flatten()
    longitude = longitude.flatten()
    slope = slope.flatten()

    print(height.size)
    print(latitude.size)

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
    print(points)

    # Create a list of vertices from your x, y, and z data
    vertices = []

    for point in points:
        # print(point)
        vertices.append(Vec3(point[0], point[1], point[2]))

    faces = triangulate(dimensions[1], dimensions[0])
 
    print(faces)

    terrain = Mesh(vertices=vertices, triangles=faces)

    terrain.save()
