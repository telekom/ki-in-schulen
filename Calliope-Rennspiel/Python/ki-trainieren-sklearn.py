#
# ki-trainieren-sklearn.py$
#
# (C) 2020, Christian A. Schiller, Deutsche Telekom AG
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
#
#
#
# Calliope Rennspiel mit Künstlicher Intelligenz
# ----------------------------------------------
# Modul: KI-Modell-Training
#
# Funktion:
# Trainiert ein künstliches neuronales Netzwerk mit dem zur Verfügung gestellten Datensatz
# und speichert es für die Nutzung mit dem IQ-Test ki-rennspiel.py ab.
# Dateinamen und Speicherort sind:
# 	./modelle/sklearn-py-modell-<YYYYMMDDHHSS>.pkcls
# 	./modelle/sklearn-py-modell-<YYYYMMDDHHSS>.json
#
# Nutzung:
#
# 	python ki-trainieren-sklearn.py <Rohdaten>
#
# 	<Rohdaten>: Name der CSV-Datei (erzeugt durch ki-datenlogger.py) für Training des ML-Modells
#

# Importieren notwendiger Bibliotheken
import pandas as pd
import numpy as np
import sklearn
from sklearn.neural_network import MLPClassifier
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import pickle
import json
import sys
from time import gmtime, strftime

# Info zur Nutzung ausgeben, falls keine Parameter übergeben
if len(sys.argv)<2:
    print("Calliope Rennspiel mit KI. Modul: KI-Modell-Training\n")
    print('Scikit-learn version: {}.'.format(sklearn.__version__))
    print('Folgende Dateien werden erzeugt:')
    print('     (1) Das trainierte ML-Modell als Pickle-Datei zur Nutzung mit ki-rennspiel.py:')
    print('     ./modelle/sklearn-py-modell-<ZEITSTEMPEL>.pkcls')
    print('     (2) Das trainierte ML-Modell als JSON-Datei zur Nutzung mit Calliope Mini:')
    print('     ./modelle/sklearn-py-modell-<ZEITSTEMPEL>.json')
    print("Nutzung:\n")
    print("python ./ki-trainieren-sklearn.py <Rohdaten>\n")
    print("     <Rohdaten>: Name der CSV-Datei (erzeugt durch ki-datenlogger.py) für Training des KI-Modells\n")
    raise SystemExit("Bye.")

# Laden der Rohdaten (Terminal-Output als CSV-Datei)
filename_raw = sys.argv[1]
df_raw = pd.read_csv(filename_raw)
Xr = df_raw[['PlayerPos','Car1Pos','Car2Pos','Car3Pos','Car4Pos','Car5Pos']].values
yr = df_raw['Action'].values

print ("Rohdaten Liste der Aktionen (sollten nur x,A,B sein!): ",df_raw['Action'].unique())
print ("Rohdaten Anzahl x: ",df_raw['Action'].str.count('x').sum())
print ("Rohdaten Anzahl A: ",df_raw['Action'].str.count('A').sum())
print ("Rohdaten Anzahl B: ",df_raw['Action'].str.count('B').sum())

# Skalieren der Rohdaten in 0..1
Xr = preprocessing.minmax_scale(Xr, feature_range=(0.0, 1.0))

# Splitten der Daten in Trainings- und Testdaten
X, Xt, y, yt = train_test_split(Xr, yr, test_size=0.2, random_state=42, shuffle=True, stratify=yr)

# Instanziieren des ML-Modells
mlp = MLPClassifier(hidden_layer_sizes=(10,10),
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
filename = './modelle/sklearn-py-modell-'+stamp+'.pkcls'
mlp_file = open(filename, 'wb')
pickle.dump(mlp, mlp_file)
print("Pickle-Datei des trainierten ML-Modells gespeichert.")
print("Dateiname: "+filename)

# Speichern des Modells (JSON-Format zur Nutzung auf Calliope Mini)
data = {}
data['params'] = []
data['params'].append({'input_layer_size': 6})
data['params'].append({'output_layer_size': 3})
data['params'].append(mlp.get_params(True))
data['coefs'] = []
for item in mlp.coefs_:
    data['coefs'].append(item.tolist())
data['intercepts'] = []
for item in mlp.intercepts_:
    data['intercepts'].append(item.tolist())

filename = './modelle/sklearn-py-modell-'+stamp+'.json'

with open(filename, 'w') as outfile:
    json.dump(data, outfile)

print("JSON-Datei des trainierten ML-Modells gespeichert.")
print("Dateiname: "+filename)
