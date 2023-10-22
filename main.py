import matplotlib.pyplot as plt
import numpy as np
import math
from datahandler import DataHandler

from matplotlib import cm
from rich.console import Console
import inquirer
from multiprocessing import Pool


def main():
    location = inquirer.prompt([
        inquirer.List(
            'region',
            message="Select a Region",
            choices=list(DataHandler.REGIONS.keys())
        )]
    )["region"]

    height, latitude, longitude, slope = ([], [], [], [])
    with Console().status("[bold blue]Initializing") as status:
        with Pool(processes=4) as pool:
            height, latitude, longitude, slope = pool.map(DataHandler.process_csv, DataHandler.REGIONS[location])

        dimensions = height.shape

        Console().log("Data Loaded")

        height = height.flatten()
        latitude = latitude.flatten()
        longitude = longitude.flatten()
        slope = slope.flatten()

        x = map(lambda n: (n[1] + 1737400) * math.cos(math.radians(latitude[n[0]])) * math.cos(
            math.radians(longitude[n[0]])), enumerate(height))
        y = map(lambda n: (n[1] + 1737400) * math.cos(math.radians(latitude[n[0]])) * math.sin(
            math.radians(longitude[n[0]])), enumerate(height))
        z = map(lambda n: (n[1] + 1737400) * math.sin(math.radians(latitude[n[0]])), enumerate(height))

        Console().log("Converted to Cartesian Coordinates")

        x = np.fromiter(x, dtype=np.double).reshape(dimensions)
        y = np.fromiter(y, dtype=np.double).reshape(dimensions)
        z = np.fromiter(z, dtype=np.double).reshape(dimensions)

        fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

        _ = ax.plot_surface(x, y, z, cmap=cm.viridis,
                            linewidth=0, antialiased=False)

        plt.show()

        Console().log("Plotting Started")
        status.stop()


if __name__ == '__main__':
    main()
