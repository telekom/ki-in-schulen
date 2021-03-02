# Basisinstallation des Projektes auf Linux

Das Projekt wurde in 2020 auf Basis Python 3.7 entwickelt. Ein Funktionieren mit höheren/niedrigeren Python-Versionen wurde nicht getestet.

1. __Unser Projekt als ZIP-Archiv herunterladen__

    Quelle: https://github.com/telekom/ki-in-schulen/archive/master.zip

2. __ZIP-Archiv entpacken__

    `unzip ki-in-schulen-master.zip`

    Das resultierende Verzeichnis `ki-in-schulen-master` enthält alle für das Projekt notwendigen Dateien, die für den weiteren Installationsverlauf benötigt werden.

Unser Projekt "Calliope-Rennspiel" wurde in der Programmiersprache __Python__ entwickelt, die für Experimente mit dem Thema Künstliche Intelligenz einen defacto Standard darstellt.

Für die Nutzung von Python-Programmen ist die Nutzung eines sogenannten "Umgebungsmanagers" wie Anaconda sehr empfohlen, da andernfalls schnell Inkompatibilitäten verschiedener Python-Paketversionen entstehen können.

Eine manuelle Installation von Python und den für das Projekt notwendigen Paketversionen ist möglich, aber aus Gründen des Komforts nicht empfohlen.

3. __Download & Installation der Open Source Version ("Individual Edition") des Anaconda Python Umgebungsmanagers__

  Quelle: https://www.anaconda.com/products/individual

4. __Erstellen der für das Projekt notwendigen Python-Umgebung mittels Anaconda (Befehl `conda`)__

    __Variante A__

    `conda env create -f=/ki-in-schulen-master/Calliope-Rennspiel/Python/calliope-rennspiel.yaml`

    `conda activate calliope-rennspiel`

    __Variante B__

    `conda create -n calliope-rennspiel python=3.7.10`

    `conda activate calliope-rennspiel`

    `pip install pyqt5==5.15.3 orange3==3.26 pyserial==3.5 pynput==1.7.1 pygame==1.9.4`

5. __Test der Installation__

  Ins Python Code-Verzeichnis wechseln

    ``cd ki-in-schulen-master/Calliope-Rennspiel/Python``

  Nacheinander ausführen und schauen ob Fehler auftauchen (dann ggf. notwendige Bibliotheken mit `conda` oder `pip` nachinstallieren).
  Es sollten jeweils die Erläuterungsbildschirme für die Kommandozeilenparameter angezeigt werden, keine Fehlermeldungen.

  `python ki-datenlogger.py`

  `python ki-trainieren-sklearn.py`

  `python ki-rennspiel.py`

  optional, für fortgeschrittene Experimente:

  `orange-canvas` ausführen, darin nach Start die Projektdatei ``ki-trainieren-orange.ows`` laden.

### Tipps & Tricks

- ggf. für Python-Bibliotheken zusätzliche notwendige Linux-Basissoftware nachinstallieren, falls bspw. bei Schritt 4 die Installation von `pynput` fehlschlägt. Beispiel für Debian:

    `sudo apt-get install libpython3.7-dev`

    `sudo apt-get install gcc`
