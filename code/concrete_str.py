# import libarary
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
import joblib
import yaml

# path to the dataset
filename = "../data/Concrete_Data.xls"

# load data
dt = pd.read_excel(filename)

# Replace column name
Column_change = ["Cement","BFS","Fly_Ash","Water",
                 "Superplasticizer","Coarse_Aggregate","Fine_Aggregate",
                 "Age","Concrete_compressive_strength"]
                
dt = dt.rename(columns=dict(zip(dt.columns, Column_change)))

# drop BFS karena penggunaan BFS kurang populer di masyarakat
dt = dt.drop(columns = "BFS")

# buat output data
# target yang dicari kekuatan beton pada campuran mix desain 
y = dt["Concrete_compressive_strength"]

# buat imput data
x = dt.drop(["Concrete_compressive_strength"],
            axis = 1)

# Train test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 20)

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
model = MLPRegressor(random_state=123, max_iter=600, solver="adam")
model.fit(x_train_clean, y_train)

# test our model
x_test_clean,standardizer = standardizerData(data = x_test)
result = model.score(x_test_clean, y_test)
print("Accuracy score is {:.1f} %".format(result*100))

# save our model in the model directory
model_name = "model"
joblib.dump(model, '../models/{}.pkl'.format(model_name))
print("Model saved as {}.pkl".format(model_name))