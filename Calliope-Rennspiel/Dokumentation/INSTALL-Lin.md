# Basisinstallation des Projektes auf Linux

Das Projekt wurde in 2020 auf Basis Python 3.7 entwickelt. Ein Funktionieren mit höheren/niedrigeren Python-Versionen wurde bisher nicht getestet. Python 3.7 ist bis 2023 durch Sicherheitsupdates unterstützt.

Da Debian/Ubuntu sehr weit verbreitet ist, bezieht sich diese Installationsanleitung auf Debian/Ubuntu, getestet wurde sie letztmals erfolgreich mit Kubuntu 20.04.1 LTS.

### Durchzuführende Schritte für Installation

#### Schritt 1 - Unser Projekt als ZIP-Archiv herunterladen

Quelle: https://github.com/telekom/ki-in-schulen/archive/master.zip

#### Schritt 2 - ZIP-Archiv entpacken

  `unzip ki-in-schulen-master.zip`

  Das resultierende Verzeichnis `ki-in-schulen-master` enthält alle für das Projekt notwendigen Dateien, die für den weiteren Installationsverlauf benötigt werden.

#### Schritt 3 - Python-Installation - Einleitung

Unser Projekt "Calliope-Rennspiel" wurde in der Programmiersprache __Python__ entwickelt, die für Experimente mit dem Thema Künstliche Intelligenz einen defacto Standard darstellt.

Für die Nutzung von Python-Programmen ist die Nutzung eines sogenannten "Umgebungsmanagers" wie Anaconda sehr empfohlen, da andernfalls schnell Inkompatibilitäten verschiedener Python-Paketversionen entstehen können.

Eine manuelle Installation von Python und den für das Projekt notwendigen Paketversionen ist möglich, aber aus Gründen des Komforts nicht empfohlen.

#### Schritt 4 - Download & Installation der Open Source Version ("Individual Edition") des Anaconda Python Umgebungsmanagers

Quelle: https://www.anaconda.com/products/individual

#### Schritt 5 - Erstellen der für das Projekt notwendigen Python-Umgebung mittels Anaconda (Befehl `conda`)

__Basisvariante - ohne Orange__

`conda env create -f=./ki-in-schulen-master/Calliope-Rennspiel/Python/conda-envs/ki-calliope-rennspiel-debian-x64-basis.yaml`

`conda activate ki-calliope-rennspiel-basis`

__Expertenvariante - mit Orange__

Voraussetzung für die Installation der Expertenvariante ist der C++-Compiler `gcc`. Diesen muss man ggf. vorab installieren, sofern nicht standardmäßg auf dem Linux-System installiert - siehe Sektion "Tipps & Tricks" am Ende dieses Dokuments.

Die Installation der Expertenvariante mit Orange wird wie folgt durchgeführt:

`conda env create -f=./ki-in-schulen-master/Calliope-Rennspiel/Python/conda-envs/ki-calliope-rennspiel-debian-x64-orange3.yaml`

`conda activate ki-calliope-rennspiel-orange3`

#### Schritt 6 - Test der Installation

__Test der Basisvariante - ohne Orange__

Ins Python Code-Verzeichnis wechseln:

`cd ki-in-schulen-master/Calliope-Rennspiel/Python`

Nacheinander ausführen und schauen ob Fehler auftauchen (dann ggf. notwendige Bibliotheken mit `conda install` oder `pip install` nachinstallieren).
Es sollten jeweils die Erläuterungsbildschirme für die Kommandozeilenparameter angezeigt werden, keine Fehlermeldungen.

`python ki-datenlogger.py`

`python ki-trainieren-sklearn.py`

`python ki-rennspiel.py`

__Test der Expertenvariante - mit Orange__

`orange-canvas` ausführen, darin nach Start die Projektdatei `ki-trainieren-orange.ows` laden.

#### Tipps & Tricks

* ggf. für Python-Bibliotheken zusätzliche notwendige Linux-Basissoftware nachinstallieren, falls bspw. bei Schritt 4 die Installation von `pynput` fehlschlägt. Beispiel für Debian:

    `sudo apt-get install libpython3.7-dev`

    `sudo apt-get install gcc`
