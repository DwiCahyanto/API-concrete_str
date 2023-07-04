# import libarary
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
import joblib
import yaml
import pickle

PATH_CONFIG = "../config/config.yaml"
config = yaml.safe_load(open(PATH_CONFIG))

# path to the dataset
filename = config['data_source']['directory'] + config['data_source']['filename']

print(filename)

# load data
dt = pd.read_excel(filename)

# Replace column name
Column_change = config['data_source']['column_names']
                
dt = dt.rename(columns=dict(zip(dt.columns, Column_change)))

# drop BFS karena penggunaan BFS kurang populer di masyarakat
dt = dt.drop(columns = config['data_source']['drop_columns'])

# buat output data
# target yang dicari kekuatan beton pada campuran mix desain 
y = dt[config['data_source']['target_name']]

# buat imput data
x = dt.drop(config['data_source']['target_name'], axis=1)

# Train test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=config['data_source']['test_size'], random_state=config['data_source']['random_state'])

# standarisasi data
from sklearn.preprocessing import StandardScaler

# Buat fungsi
def standardizerData(data):
    """
    Fungsi untuk melakukan standarisasi data
    :param data: <pandas dataframe> sampel data
    :return standardized_data: <pandas dataframe> sampel data standard
    :return standardizer: method untuk standardisasi data
    """
    data_columns = data.columns  # agar nama kolom tidak hilang
    data_index = data.index  # agar index tidak hilang

    # buat (fit) standardizer
    standardizer = StandardScaler()
    standardizer.fit(data)

    # transform data
    standardized_data_raw = standardizer.transform(data)
    standardized_data = pd.DataFrame(standardized_data_raw)
    standardized_data.columns = data_columns
    standardized_data.index = data_index

    return standardized_data, standardizer
    
# standarisasi train data
x_train_clean,standardizer = standardizerData(data = x_train)

# Model NN Regression
model = MLPRegressor(random_state=config['model']['random_state'], max_iter=config['model']['max_iter'], solver=config['model']['solver'])
model.fit(x_train_clean, y_train)

# test our model
x_test_clean,standardizer = standardizerData(data = x_test)
result = model.score(x_test_clean, y_test)
print("Accuracy score is {:.1f} %".format(result*100))

# save our model in the model directory
model_name = config['model']['model_name']
pickle.dump(model, open('../models/{}.pkl'.format(model_name),'wb'))
print("Model saved as {}.pkl".format(model_name))