import numpy as np
import pandas as pd
from PIL import Image as im
import math

def normalize(num):
    return 255 * ((num - z.min()) / (z.max() - z.min()))

height = np.array(pd.read_csv("data/FY23_ADC_Height_PeakNearShackleton.csv"))
latitude = np.array(pd.read_csv("data/FY23_ADC_Latitude_PeakNearShackleton.csv"))
longitude = np.array(pd.read_csv("data/FY23_ADC_Longitude_PeakNearShackleton.csv"))
slope = np.array(pd.read_csv("data/FY23_ADC_Slope_PeakNearShackleton.csv"))

dimensions = height.shape

height = height.flatten()
latitude = latitude.flatten()
longitude = longitude.flatten()
slope = slope.flatten()

x = list(map(lambda n: (n[1] + 1737400) * math.cos(math.radians(latitude[n[0]])) * math.cos(
    math.radians(longitude[n[0]])), enumerate(height)))
y = list(map(lambda n: (n[1] + 1737400) * math.cos(math.radians(latitude[n[0]])) * math.sin(
    math.radians(longitude[n[0]])), enumerate(height)))
z = np.array(list(map(lambda n: (n[1] + 1737400) * math.sin(math.radians(latitude[n[0]])), enumerate(height))))

print(min(x), max(x), max(x) - min(x))
print(min(y), max(y), max(y) - min(y))
print(z.min(), z.max())

z -= z.min()
z /= z.max() - z.min()
z *= 255
z = np.uint8(z)
z = z.reshape(dimensions)

print(z)

print("Generating image")

hm = im.fromarray(z)

hm.verify()

hm.save('./hm.png')