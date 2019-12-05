#Importing modules

import json
import os

from joblib import dump
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


# Load directory paths for persisting model and metadata 

MODEL_DIR = os.environ["MODEL_DIR"]
MODEL_FILE = os.environ["MODEL_FILE"]
METADATA_FILE = os.environ["METADATA_FILE"]
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILE)
METADATA_PATH = os.path.join(MODEL_DIR, METADATA_FILE)

#  Preprocessing and Model build
top_features=['OverallQual',
'GrLivArea',
 'TotalBsmtSF',
 '1stFlrSF',
 'BsmtFinSF1',
 'GarageArea',
 '2ndFlrSF',
 'TotRmsAbvGrd',
 'LotArea',
 'YearBuilt',
 'SalePrice']

print("Loading data ...")

df_train=pd.read_csv('train.csv')
df_train_sub=df_train[top_features]
labels = np.array(df_train_sub['SalePrice'])
features= df_train_sub.drop('SalePrice', axis = 1)
feature_list = list(features.columns)
features = np.array(features)

print("Splitting data ..")
train_features, test_features, train_labels, test_labels = \
            train_test_split(features, labels, test_size = 0.2, random_state = 42)

print("Building model and prediction..")

rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
rf.fit(train_features, train_labels)
predictions = rf.predict(test_features)


# Error calculation

errors = abs(predictions - test_labels)
# Calculate mean absolute percentage error (MAPE)
mape = 100 * (errors / test_labels)
# Calculate and display accuracy
accuracy = 100 - np.mean(mape)

metadata = {
    "test_accuracy": accuracy
}

# Serialize model and metadata 

print("Serializing model to: {}".format(MODEL_PATH))
dump(rf,MODEL_FILE)

print("Serializing metadata to: {}".format(METADATA_PATH))
with open(METADATA_FILE,'w') as outfile:  
    json.dump(metadata, outfile)

