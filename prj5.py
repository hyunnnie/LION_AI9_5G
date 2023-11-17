import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


filename = 'C:/Users/iooju/Downloads/1023_file/202212_202212__.xlsx'
d = pd.read_excel(filename)

d.dropna(axis=0,inplace=True)
print(d.head())
