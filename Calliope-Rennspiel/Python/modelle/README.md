# Erläuterung des Verzeichnisses und Verzeichnisinhalts

Dieses Verzeichnis wird verwendet, um trainierte KI-Modelle zu speichern. Es wird benötigt sowohl für die Projektvariante 1A (IQ-Test auf dem Desktop mit Python-Rennspiel) als auch für die (Stand März 2021 noch nicht komplett umgesetzte) Projektvariante 1B (IQ-Test auf dem Calliope mini).

Das Python-Skript `ki-trainieren-sklearn.py` sowie der Orange Workflow `ki-trainieren-orange.ows` legen trainierte KI-Modelle hier ab:
* im JSON-Format (`.json`) für Projektvariante 1A
* im Pickle-Format (`.pkcls`) für Projektvariante 1B

Folgende trainierte Modelle werden mitgeliefert, die sofort für einen IQ-Test mit dem Python-Skript `ki-rennspiel.py` verwendet werden können. Sie wurden mit den Rohdaten `../csv-rohdaten/120minutes-1.csv` trainiert.

### Vortrainierte Modelle für IQ-Test auf dem Desktop (Projektvariante 1B)

Für das `ki-rennspiel.py` mit Backend-Option `sklearn` stehen folgende Dateien zur Verfügung:

* `sklearn-py-modell-20210302220807.pkcls` - ein neuronales Netzwerk mit (7,7) Hidden Layers - erstellt mit `ki-trainieren.py`
  * Erreichte Modellgenauigkeit (Trainingsdaten):  0.8348560354374308
  * Erreichte Modellgenauigkeit (Testdaten)     :  0.8256779192030991
* `sklearn-ows-modell-20210302221649.pkcls` - ein neuronales Netzwerk mit (7,7) Hidden Layers - erstellt mit Orange3
  * Erreichte Modellgenauigkeit (Trainingsdaten):  0.8258823529411765
  * Erreichte Modellgenauigkeit (Testdaten)     :  0.8294573643410853

Für das `ki-rennspiel.py` mit Backend-Option `orange3` stehen folgende Dateien zur Verfügung:

* `orange3-model.pkcls` - ein AdaBoost-Modell (Standardmodell im Orange3 Workflow)
  * Erreichte Modellgenauigkeit (Trainingsdaten): 0.908
  * Erreichte Modellgenauigkeit (Testdaten)     : 0.801

### Vortrainierte Modelle für IQ-Test auf dem Calliope mini (Projektvariante 1A)  

  * `sklearn-py-modell-20210302220807.json`
    * Erreichte Modellgenauigkeit (Trainingsdaten):  0.8348560354374308
    * Erreichte Modellgenauigkeit (Testdaten)     :  0.8256779192030991
  * `sklearn-ows-modell-20210302221649.json`
    * Erreichte Modellgenauigkeit (Trainingsdaten):  0.8258823529411765
    * Erreichte Modellgenauigkeit (Testdaten)     :  0.8294573643410853
