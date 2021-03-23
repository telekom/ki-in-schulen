# Erläuterung des Verzeichnisses und Verzeichnisinhalts

In diesem Verzeichnis sind die Calliope mini Codeanteile für OpenRoberta enthalten.

Diese Codeanteile wurden vom Fraunhofer beigetragen und sind (siehe auch ../LICENSE) (c) 2021 Fraunhofer IAIS

* Datei `datensammler-openroberta.hex`
  * Das Programm für den datensammelnden Calliope mini, der Rohdaten(KI-Trainingsdaten) per Funk von mehreren Calliope mini Geräten einsammelt, die auf den gleichen Funkkanal konfiguriert wurden
    * die Funkgruppe wird beim Starten des Programmes ausgewählt
      * mit der Taste B durch die Kanäle wechseln, bis der gewünschte Kanal angezeigt wird
      * mit der Taste A den Kanal auswählen, die Datensammlung beginnt
    * Achtung: Bitte den Datensammler immer zuerst starten und dann erst die Rennspiele
* Datei `rennspiel-openroberta.hex`
  * Das Rennspiel für den Calliope mini. Generiert Rohdaten(KI-Trainingsdaten) entweder über USB Link oder per Funk an einen Datensammler, sofern auf den gleichen Funkkanal konfiguriert
    * die Funkgruppe wird beim Starten des Programmes ausgewählt
      * mit der Taste B durch die Kanäle wechseln, bis der gewünschte Kanal angezeigt wird
      * Kanal 0 schreibt die Daten direkt an den USB Link (serial out), die Kanäle 1 - 6 stehen für die Funkgruppen zur Verfügung
      * mit der Taste A den Kanal auswählen, die Datensammlung beginnt
* Datei `datensammler-openroberta.xml` und `rennspiel-openroberta.xml`
  * Programmdateien zum Import in das Open Roberta Lab
