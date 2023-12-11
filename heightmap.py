import numpy as np
import pandas as pd
from PIL import Image
import json
from math import sin, cos, sqrt, radians, atan2, asin


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
x = np.array(
    list(
        map(
            lambda h: 
            (h[1] + 1737400)
            * cos(radians(latitude[h[0]]))
            * cos(radians(longitude[h[0]])),
            enumerate(height),
        )
    )
)
y = np.array(
    list(
        map(
            lambda h: (h[1] + 1737400)
            * cos(radians(latitude[h[0]]))
            * sin(radians(longitude[h[0]])),
            enumerate(height),
        )
    )
)
z = np.array(
    list(
        map(
            lambda h: (h[1] + 1_737_400) * sin(radians(latitude[h[0]])),
            enumerate(height),
        )
    )
)

azimuth = np.array(
    list(
        map(
            lambda h: (atan2(
                sin(radians(-h[1])),
                -sin(radians(latitude[h[0]])) * cos(-radians(h[0]))
                )
            ),
            enumerate(longitude)
        )
    )
)

elav_angle = np.array(
    list(
        map( # Refrence coords are (1,737,400, 0, 0)
            lambda h: (
                asin(
                    (h[0] - 1_737_400)
                    / sqrt(
                        (h[0] - 1_737_400) ** 2
                        + h[1] ** 2
                        + h[2] ** 2
                    )
                )
            ),
            zip(x, y, z)
        )
    )
)

data["x_scale"] = (max(x) - min(x))
data["y_scale"] = (max(y) - min(y))
data["z_scale"] = (max(z) - min(z))

# Normalize Z data
z *= -1
z -= z.min()
z /= z.max()
z *= 255
z = np.uint8(z)
z = z.reshape(dimensions)

slope -= slope.min()
slope /= slope.max()
slope *= 255
slope = np.uint8(slope)
slope = slope.reshape(dimensions)

azimuth -= azimuth.min()
azimuth /= azimuth.max()
azimuth *= 255
azimuth = np.uint8(azimuth)
azimuth = azimuth.reshape(dimensions)

elav_angle -= elav_angle.min()
elav_angle /= elav_angle.max()
elav_angle *= 255
elav_angle = np.uint8(elav_angle)
elav_angle = elav_angle.reshape(dimensions)

heightmap = Image.fromarray(z)
slope = Image.fromarray(slope)
azimuth = Image.fromarray(azimuth)
elav_angle = Image.fromarray(elav_angle)

elevation = heightmap.resize((6400, 6400), resample=Image.Resampling.BICUBIC)
heightmap.thumbnail((511, 511), Image.Resampling.LANCZOS)

slope.verify
heightmap.verify()
elevation.verify()
azimuth.verify()
elav_angle.verify()

slope.save("./textures/slope.png")
elevation.save("./textures/height.png")
heightmap.save("./textures/heightmap.png")
azimuth.save("./textures/azimuth.png")
elav_angle.save("./textures/elevation.png")

with open("./textures/data.json", "w") as file:
    json.dump(data, file)
