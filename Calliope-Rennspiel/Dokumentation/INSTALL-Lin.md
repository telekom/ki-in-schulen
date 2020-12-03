# Basisinstallation des Projektes auf Linux

Das Projekt wurde in 2020 auf Basis Python 3.8 entwickelt. Ein Funktionieren mit höheren/niedrigeren Python-Versionen wurde nicht getestet.

1. Minimalvoraussetzung schaffen: Python 3.8 installieren, auf Ubuntu/Debian-basierenden Systemen bspw. mit
``sudo apt-get install python3.8``. Python ist
in den meisten Linux-Distributionen aber schon enthalten.

2. Zusätzlich für unser Projekt benötigte Python-Bibliotheken nachinstallieren. Siehe auch Sektion "Tipps & Tricks", falls hier Fehler auftauchen.

  ``pip install pyserial pynput numpy pandas sklearn pickle json pygame``

  optional für Fortgeschrittene Experimente:

  ``pip install orange3``

3. Unser Projekt als ZIP-Archiv herunterladen
    Quelle: https://github.com/telekom/ki-in-schulen/archive/master.zip

3. ZIP-Archiv entpacken
    ``unzip ki-in-schulen-master.zip``

4. Test der Installation

  Ins Python Code-Verzeichnis wechseln

    ``cd ki-in-schulen-master/Calliope-Rennspiel/Python``

  Nacheinander ausführen und schauen ob Fehler auftauchen (dann ggf. notwendige Bibliotheken nachinstallieren).
  Es sollten jeweils die Erläuterungsbildschirme für die Kommandozeilenparameter angezeigt werden.

  ``python ki-datenlogger.py``
  ``python ki-trainieren-sklearn.py``
  ``python ki-rennspiel.py``

  optional, für fortgeschrittene Experimente

  ``orange-canvas`` ausführen, darin nach Start die Projektdatei ``ki-trainieren-orange.ows`` laden.

# Tipps & Tricks

- ggf. für Python-Bibliotheken zusätzliche notwendige Linux-Basissoftware auf einer Standard Debian 20.04.1 Installation, falls bspw. die Installation von ``pynput`` fehlschlägt
    ``sudo apt-get install libpython3.8-dev`` -
    ``sudo apt-get install gcc``
