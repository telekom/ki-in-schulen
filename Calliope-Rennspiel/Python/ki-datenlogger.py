#
# ki-datenlogger.py$
#
# (C) 2020-2022, Christian A. Schiller, Deutsche Telekom AG
#     Diese Version: V2 vom 19.12.2022 auf Basis Workshoperfahrungen 2022
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
# Modul: Datenlogger
#
# Funktion:
# Erzeugt eine CSV-Datei mit Trainingsdaten für die weitere Nutzung mit ki-trainieren-sklearn.py
# an folgendem Ort: ./csv-rohdaten/ki-rennspiel-log-<ZEITSTEMPEL>.csv")
#
# Nutzung:
#
# 	python ki-datenlogger.py <COM-Port>
#
#   <COM-Port>: COM-Port des Calliope-Datensammlers
#               Windows: z.B. COM3
#               Linux  : z.B. /dev/ttyACM1
#
# Nach Start des Programms läuft die Datensammlung sofort und wartet auf Daten vom Calliope.
# Nach 15 Sekunden ohne Datenempfang endet die Datensammlung automatisch.
# Während der Datensammlung eine beliebige Taste drücken, um die
# "Datensammlung zu beenden und die CSV-Datei zu erstellen.
# Bitte dann ggf. nochmal Calliope resetten, um Vorgang abzuschließen.
# Oder 15 Sekunden warten, dann geschieht dies automatisch.
#



# notwendige Bibliotheken laden
import serial
import pandas as pd
import sys
from pynput import keyboard
from time import gmtime, strftime

# Erkennung des Tastendrucks für Beendigung der Datensammlung
global keypress
keypress = False
def on_press(key):
    global keypress
    keypress = True
    print("\nTastendruck erkannt! Beende Datensammlung und speichere CSV.")
    print("Bitte ggf. nochmal Calliope resetten, um Vorgang abzuschließen.")
    print("Oder 15 Sekunden warten, dann geschieht dies automatisch.")
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Info zur Nutzung ausgeben, falls keine Parameter übergeben
if len(sys.argv)<2:
    print("Calliope Rennspiel mit KI. Modul: Calliope Datenlogger\n")
    print("Nutzung:\n")
    print("python ki-datenlogger.py <COM-Port>\n")
    print("     <COM-Port>: COM-Port des Calliope-Datensammlers")
    print("                 Windows: z.B. COM3")
    print("                 Linux  : z.B. /dev/ttyACM1  ")
    print("\nErzeugt eine CSV-Datei mit Trainingsdaten für die weitere Nutzung mit ki-trainieren-sklearn.py")
    print("an folgendem Ort: ./csv-rohdaten/ki-rennspiel-log-<ZEITSTEMPEL>.csv")
    print("\nNach Start des Programms läuft die Datensammlung sofort und wartet auf Daten vom Calliope.")
    print("Nach 15 Sekunden ohne Datenempfang endet die Datensammlung automatisch.")
    print("Während der Datensammlung eine beliebige Taste drücken, um die")
    print("Datensammlung zu beenden und die CSV-Datei zu erstellen.")
    print("Bitte dann ggf. nochmal Calliope resetten, um Vorgang abzuschließen.")
    print("Oder 15 Sekunden warten, dann geschieht dies automatisch.")
    raise SystemExit()

# Initialisieren der seriellen Schnittstelle mit dem übergebenen Parameter
print("Nutze COM-Port: ",sys.argv[1])
ser = serial.Serial(sys.argv[1], 115200, timeout=15, parity=serial.PARITY_EVEN, rtscts=1)
ser.flushInput()

# Initialisieren dar Datenstruktur für das Sammeln der Trainingsdaten
collect = pd.DataFrame(columns=['PlayerPos','Car1Pos','Car2Pos','Car3Pos','Car4Pos','Car5Pos','Action'])

# Warten auf serielle Daten solange, bis eine Taste gedrückt wurde oder das Timeout (15 Sekunden) erreicht wurde.
while True:
	if keypress:
		break
	line = ser.readline().decode("utf-8")
	line = line[:-2] # CRLF entfernen
	line = ''.join(line.split()) # Leerzeichen entfernen
	print(line)
	if line.startswith("P") or line.startswith("\x00") or line.startswith("R"):
		print("Header erkannt - ignorieren")
	else:
		if line[:1] == "":
			print("Leerdaten erkannt - Überspringen")
		else:
			collect = pd.concat([collect, pd.DataFrame({'PlayerPos': [line[:1]],
                                                        'Car1Pos': [line[2:3]],
                                                        'Car2Pos': [line[4:5]],
                                                        'Car3Pos': [line[6:7]],
                                                        'Car4Pos': [line[8:9]],
                                                        'Car5Pos': [line[10:11]],
                                                        'Action': [line[12:13]]})], ignore_index=True)

# Schließen der seriellen Schnittstelle und Ausgabe der gesammelten Daten
ser.close()
print(collect)

# Speichern der gesammelten Daten in CSV-Datei
stamp = strftime("%Y%m%d%H%M%S", gmtime())

# Festlegen der Ausgabedatei (ohne Endung)
try:
    file = sys.argv[2]
except:
    file = './csv-rohdaten/ki-rennspiel-log-'+stamp+'.csv'

print("Trainingsdaten gespeichert in Datei: "+file)
collect.to_csv(file,index=False)
