import pyvista as pv
import numpy as np
import math
from datahandler import DataHandler

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

        dimensions = latitude.shape

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

        surface = pv.PolyData(points, faces)

        status.update("[bold blue]Smoothing Faces")

        surface = surface.smooth_taubin(n_iter=500, pass_band=0.05)

        status.update("[bold blue]Setting up Plot")

        plotter = pv.Plotter()
        plotter.add_camera_orientation_widget()
        plotter.set_background("black")

        pv.default_theme.full_screen = True
        pv.default_theme.interpolate_before_map = True

        plotter.add_mesh(surface, scalars=slope, scalar_bar_args={"color": "white"})

        status.stop()
        console.log("[bold blue]Plot Initialized")

        _ = plotter.show()


if __name__ == "__main__":
    main()
