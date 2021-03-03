# Erläuterung des Verzeichnisses und Verzeichnisinhalts

In diesem Verzeichnis sind die Calliope mini Codeanteile für Microsoft Makecode enthalten.

* Dateien `datensammler-makecode.js/hex`
  * Das Programm für den datensammelnden Calluipe mini, der Rohdaten(KI-Trainingsdaten) per Funk von mehreren Calliope mini Geräten einsammelt, die auf den gleichen Funkkanal konfiguriert wurden
    * funkgruppe1 ... funkgruppe5 sind vorkonfiguriert auf die entsprechenden Funkkanäle des Calliope
* Dateien `rennspiel-makecode.js/hex`
  * Das Rennspiel für den Calliope mini. Generiert Rohdaten(KI-Trainingsdaten) sowohl über USB Link als auch per Funk an einen Datensammler, sofern auf den gleichen Funkkanal konfiguriert
    * funkgruppe1 ... funkgruppe5 sind vorkonfiguriert auf die entsprechenden Funkkanäle des Calliope
* Verzeichnis `KI-Erweiterung`
  * siehe separate README.md
  * Diese Dateien stellen den Entwicklungsstand für die Projektvariante 1A - "IQ-Test auf dem Calliope Mini" dar, die aktuell aufgrund eines Bugs in Makecode nicht fortgeführt werden kann.
