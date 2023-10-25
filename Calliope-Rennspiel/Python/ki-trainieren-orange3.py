#
# ki-trainieren-orange3.py$
#
# (C) 2021, Christian A. Schiller, Deutsche Telekom AG
#
# Deutsche Telekom AG and all other contributors /
# copyright owners license this file to you under the
# MIT License (the "License"); you may not use this
# file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# Import required libraries
import pandas as pd
import numpy as np
import sklearn
from sklearn.neural_network import MLPClassifier
import pickle
import json
from time import gmtime, strftime

#Größe des neuronalen Netzwerks
hidden_layers_raw = "7,7"
hidden_layers = hidden_layers_raw.split (",")
hidden_layers = list(map(int, hidden_layers))

# Laden der von Orange3 prozessierten Daten
filename_train = './csv-vorverarbeitet/train-80p-stratified-data.csv'
filename_test = './csv-vorverarbeitet/test-20p-stratified-data.csv'

# Trainingsdaten
df_train = pd.read_csv(filename_train)
print(df_train.shape)
df_train = df_train.drop(['Selected'], axis=1)
df_train.head()
X = df_train[['PlayerPos','Car1Pos','Car2Pos','Car3Pos','Car4Pos','Car5Pos']].values
y = df_train['Action'].values

# Testdaten
df_test = pd.read_csv(filename_test)
print(df_test.shape)
df_test = df_test.drop(['Selected'], axis=1)
df_test.head()
Xt = df_test[['PlayerPos','Car1Pos','Car2Pos','Car3Pos','Car4Pos','Car5Pos']].values
yt = df_test['Action'].values

# Instanziieren des ML-Modells
mlp = MLPClassifier(hidden_layer_sizes=tuple(hidden_layers),
                    activation='relu', # default relu
                    solver='adam', # default sgd
                    max_iter=5000, # default 200
                    alpha=0.0001, # default 0.0001
                    n_iter_no_change=100 # default 10
                   )
# Trainingsvorgang
print("Beginne Trainingsvorgang.")
mlp.fit(X,y)
print("Training beendet.")

# Ausgeben des Trainingsergebnisses
print("Erreichte Modellgenauigkeit (Trainingsdaten): ",mlp.score(X,y))
print("Erreichte Modellgenauigkeit (Testdaten)     : ",mlp.score(Xt,yt))

# Timestamp erzeugen
stamp = strftime("%Y%m%d%H%M%S", gmtime())

# Speichern des Modells (Pickle-Format zur Nutzung im Python-Rennspiel)
filename = './modelle/sklearn-ows-modell-'+stamp+'.pkcls'
mlp_file = open(filename, 'wb')
pickle.dump(mlp, mlp_file)
print("Pickle-Datei des trainierten ML-Modells gespeichert.")
print("Dateiname: "+filename)

# Speichern des Modells (JSON-Format zur Nutzung auf Calliope mini)

jsonlayers = []
jsonlayers.append(6) # input layers
jsonlayers += hidden_layers # hidden Layers
jsonlayers.append(3) # output layer

data = {}
data['params'] = []
data['params'].append({'layers': jsonlayers})
data['params'].append({'act': 'relu'})
data['coefs'] = []
for item in mlp.coefs_:
    data['coefs'].append(item.tolist())
data['intercepts'] = []
for item in mlp.intercepts_:
    data['intercepts'].append(item.tolist())

filename = './modelle/sklearn-ows-modell-'+stamp+'.json'

def round_floats(o):
    if isinstance(o, float): return round(o, 6)
    if isinstance(o, dict): return {k: round_floats(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)): return [round_floats(x) for x in o]
    return o

with open(filename, 'w') as outfile:
    json.dump(round_floats(data), outfile, separators=(',',':'))

print("JSON-Datei des trainierten ML-Modells gespeichert.")
print("Dateiname: "+filename)
