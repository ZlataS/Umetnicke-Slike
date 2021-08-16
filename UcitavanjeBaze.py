import torch
import torchvision
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

info_path = 'C:\\Users\\zlata\\Downloads\\paintings\\imagesinfo.csv' 
info = pd.read_csv('C:\\Users\\zlata\\Downloads\\paintings\\imagesinfo.csv') #nazivi slika i kategorije
images_path = 'C:\\Users\\zlata\\Downloads\\paintings\\images'

one_hot_encoded_data_proba = pd.get_dummies(art, columns = ['genre'])
print(one_hot_encoded_data_proba)
