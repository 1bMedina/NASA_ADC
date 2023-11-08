import pandas as pd
import numpy as np
import inquirer
from rich.console import Console
from multiprocessing import Pool
from ursina import *

class DataHandler:
    @staticmethod
    def process_csv(filename):
        return np.array(pd.read_csv("./data/" + filename))

    REGIONS = {
        "Peak Near Shackleton": [
            "FY23_ADC_Height_PeakNearShackleton.csv",
            "FY23_ADC_Latitude_PeakNearShackleton.csv",
            "FY23_ADC_Longitude_PeakNearShackleton.csv",
            "FY23_ADC_Slope_PeakNearShackleton.csv"
        ],
        "Connecting Ridge": [
            "FY23_ADC_Height_ConnectingRidge.csv",
            "FY23_ADC_Latitude_ConnectingRidge.csv",
            "FY23_ADC_Longitude_ConnectingRidge.csv",
            "FY23_ADC_Slope_ConnectingRidge.csv"
        ],
        "Nobile Rim 1": [
            "FY23_ADC_Height_NobileRim1.csv",
            "FY23_ADC_Latitude_NobileRim1.csv",
            "FY23_ADC_Longitude_NobileRim1.csv",
            "FY23_ADC_Slope_NobileRim1.csv"
        ],
        "Faustini Rim A": [
            "FY23_ADC_Height_FaustiniRimA.csv",
            "FY23_ADC_Latitude_FaustiniRimA.csv",
            "FY23_ADC_Longitude_FaustiniRimA.csv",
            "FY23_ADC_Slope_FaustiniRimA.csv"
        ],
        "Leibnitz Beta Plateau": [
            "FY23_ADC_Height_LeibnitzBetaPlateau.csv",
            "FY23_ADC_Latitude_LeibnitzBetaPlateau.csv",
            "FY23_ADC_Longitude_LeibnitzBetaPlateau.csv",
            "FY23_ADC_Slope_LeibnitzBetaPlateau.csv"
        ]
    }

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

console = Console()

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

    # Create a list of vertices from your x, y, and z data
    vertices = [Vec3(x[i], y[i], z[i]) for i in range(len(x))]

    terrain = Mesh(vertices=vertices, triangles=triangulate(dimensions[1], dimensions[0]))

    terrain.save()
