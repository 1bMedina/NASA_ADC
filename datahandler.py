import pandas as pd
import numpy as np


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



