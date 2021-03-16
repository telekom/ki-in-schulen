# Erläuterung des Verzeichnisses und Verzeichnisinhalts

In diesem Verzeichnis sind die Calliope mini Codeanteile für OpenRoberta enthalten.

Diese Codeanteile wurden vom Fraunhofer beigetragen und sind (siehe auch ../LICENSE) (c) 2021 Fraunhofer IAIS

* Dateien `datensammler-openroberta.xml/hex`
  * Das Programm für den datensammelnden Calliope mini, der Rohdaten(KI-Trainingsdaten) per Funk von mehreren Calliope mini Geräten einsammelt, die auf den gleichen Funkkanal konfiguriert wurden
    * funkgruppe1 ... funkgruppe5 sind vorkonfiguriert auf die entsprechenden Funkkanäle des Calliope
* Dateien `rennspiel-openroberta.hex/hex`
  * Das Rennspiel für den Calliope mini. Generiert Rohdaten(KI-Trainingsdaten) sowohl über USB Link als auch per Funk an einen Datensammler, sofern auf den gleichen Funkkanal konfiguriert
    * funkgruppe1 ... funkgruppe5 sind vorkonfiguriert auf die entsprechenden Funkkanäle des Calliope
