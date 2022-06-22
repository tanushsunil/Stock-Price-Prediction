# Importing the libraries
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

# Importing Dataset [patient_data.csv file]
dataset = pd.read_csv(
    r'C:\Users\tanus\OneDrive\Desktop\Internship Assests\Data\patient_data.csv')


# Categorical Data into Numerical Data
df = pd.get_dummies(dataset.Gender)
dataset = pd.concat([dataset, df], axis='columns')
dataset = dataset.drop(['Gender', 'Male'], axis='columns')
dataset.rename(columns={'Female': 'Gender'}, inplace=True)

# exporting the processed dataset to train & test the models
dataset.to_csv(r'data\pat_dat_clean.csv')
