# Erläuterung des Verzeichnisses und Verzeichnisinhalts

Dieses Verzeichnis wird vom Orange Workflow `ki-trainieren-orange.ows` zur Zwischenspeicherung relevanter prozessierter Daten verwendet.

### Vorprozessierte Daten

Mittels des Orange Workflows `ki-trainieren-orange.ows` wurde ein stratifizierter Train/Test Split (80%/20%) auf den Rohdaten `../csv-rohdaten/120minutes-1.csv` durchgeführt. Resultierend:
* `train-80p-stratified-data.csv` - stratifizierte Trainingsdaten
* `test-20p-stratified-data.csv` - stratifizierte Testdaten

Diese Daten werden vom o.g. Orange Workflow generiert und im Python Scriptknoten verwendet, der eine Alternative zum manuellen Ausführen des Python-Scripts `ki-trainieren.py` für das Trainieren eines künstlichen neuronalen Netzwerks darstellt.
