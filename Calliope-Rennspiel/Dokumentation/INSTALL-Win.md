# Basisinstallation des Projektes auf Windows

Das Projekt wurde in 2020 auf Basis Python 3.8 entwickelt. Ein Funktionieren mit höheren/niedrigeren Python-Versionen wurde nicht getestet.

1. Minimalvoraussetzung schaffen: Python 3.8 installieren

   Laden Sie sich das Programmpaket WinPython **3.8** für Ihre 64bit oder 32bit Windows-Version herunter. Achten Sie darauf, dass es sich um die Dateivariante **ohne** weitere Zusätze im Dateinamen hinter der Versionsnummer handelt. Installieren/entpacken Sie die Datei in einem beliebigen Verzeichnis Ihrer Wahl.

   **Download-Link:**
   https://github.com/winpython/winpython/releases/latest
   
   Zum Zeitpunkt dieser Dokumentation waren das z.B. "Winpython**32**-3.8.6.0.exe" bzw. "Winpython**64**-3.8.6.0.exe".

2. Starten Sie einen Datei-Explorer und wechseln Sie in das unter 1. erstellte Verzeichnis.

3. Starten Sie das Programm "WinPython Command Prompt.exe". Bitte haben Sie Geduld. Es kann etwas dauern, bis das Programmfenster sichtbar wird.

4. Nun müssen noch einige Python-Pakete nachinstalliert werden.
   Rufen Sie dafür folgende Kommandos auf:
   
   ``pip install --upgrade pyserial pynput numpy pandas sklearn pickle-mixin json pygame``
   
   
   
   