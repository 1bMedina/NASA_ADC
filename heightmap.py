import numpy as np
import pandas as pd
from PIL import Image
import math
import json

data = {}

height = np.array(pd.read_csv("data/FY23_ADC_Height_PeakNearShackleton.csv"))
latitude = np.array(pd.read_csv("data/FY23_ADC_Latitude_PeakNearShackleton.csv"))
longitude = np.array(pd.read_csv("data/FY23_ADC_Longitude_PeakNearShackleton.csv"))
slope = np.array(pd.read_csv("data/FY23_ADC_Slope_PeakNearShackleton.csv"))

dimensions = height.shape

data["data_x"] = dimensions[0]
data["data_y"] = dimensions[1]

height = height.flatten()
latitude = latitude.flatten()
longitude = longitude.flatten()

# Convert to cartesian coordinates
x = list(
    map(
        lambda n: (n[1] + 1737400)
        * math.cos(math.radians(latitude[n[0]]))
        * math.cos(math.radians(longitude[n[0]])),
        enumerate(height),
    )
)
y = list(
    map(
        lambda n: (n[1] + 1737400)
        * math.cos(math.radians(latitude[n[0]]))
        * math.sin(math.radians(longitude[n[0]])),
        enumerate(height),
    )
)
z = np.array(
    list(
        map(
            lambda n: (n[1] + 1737400) * math.sin(math.radians(latitude[n[0]])),
            enumerate(height),
        )
    )
)

print(min(x), max(x), max(x) - min(x))
print(min(y), max(y), max(y) - min(y))
print(z.min(), z.max())

# Normalize Z data
z *= -1
z -= z.min()
z /= z.max() - z.min()
z *= 255
z = np.uint8(z)
z = z.reshape(dimensions)

heightmap = Image.fromarray(z)
slope = Image.fromarray(slope)

elevation = heightmap.resize((16385, 16385), resample=Image.Resampling.BICUBIC)
heightmap.thumbnail((511, 511), Image.Resampling.LANCZOS)

slope.verify
heightmap.verify()
elevation.verify()

slope.save("./textures/slope.png")
elevation.save("./textures/elevation.png")
heightmap.save("./textures/heightmap.png")

with open("data.json", "w") as file:
    json.dump(data, file)
