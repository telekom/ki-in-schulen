#
# ki-gui-lin.py$
#
# (C) 2022-3, Arndt Baars, Christian A. Schiller, Deutsche Telekom AG
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
# GUI fuer den KI-Workshop mit den Calliope
#
# Diese GUI ermoeglicht einen einfachen und schnellen Umgang mit den KI-Ressourcen.
#
# Folgende Features sind bereits enthalten:
#    - Kopieren der Datensammler-Software auf den Calliope. Hier stehen zwei Optionen zur Auswahl.
#         Zum einen auf Basis von OpenRoberta (Wahl des Kanals/Gruppe auf dem Calliope).
#        Zum anderen auf Basis von Makecode (Direkte Auswahl von vier Punktgruppen).
#    - Kopieren der Rennspieldateien auf den Calliope. Hier stehen zwei Optionen zur Auswahl.
#        Zum einen auf Basis von OpenRoberta (Wahl des Kanals/Gruppe auf dem Calliope).
#        Zum anderen auf Basis von Makecode (Direkte Auswahl von vier Punktgruppen).
#    - Einfacher Start des Datensammlers auf dem lokalen Rechner.
#    - Einfacher Start des KI-Trainings inkl. Layer-Konfig-Abfrage.
#    - Einfacher Start des lokalen Rennspiels mit dem aktuell trainierten Modell.
#    - Automatische USB-Port-Ermittlung
#    - Automatische Calliope-Erkennung
#     - Moeglichkeit, eigene Dateinamen vorzugeben
#    - Sicherung der Einstellungen/Konfigurationen
#
# Geplante Features:
#    - Einfaches Kopieren von trainierten Modellen auf den Calliope.
#    - Einfuegen einer Hilfe mit Verweisen auf die vorhandenen Präsentationen und Materialien.
#   - Portierung für Linux und MacOS
#
# Version 0.22 (Stand: 07.03.2023)
#
##########

from tkinter import *
from tkinter import simpledialog
import sys
import subprocess
import serial.tools.list_ports
import os
from ctypes import create_unicode_buffer, c_wchar_p, sizeof
from string import ascii_uppercase
import pickle
import locale

os_umgebung = sys.platform
os_locale = locale.getdefaultlocale()[0]
print("OS-Umgebung:")
print(os_umgebung)
print(os_locale)
print("")


# donothing
def donothing():
    win = Toplevel(fenster)
    button = Button(win, text="Do nothing button")
    button.pack()


def configEinlesen():
    try:
        f = open("ki-gui-win_conf.cfg", "rb")
        dict = pickle.load(f)
        f.close()
        return dict
    except:
        return {}


def configSpeichern(dict):
    f = open("ki-gui-win_conf.cfg", "wb")
    pickle.dump(dict, f)
    f.close()


global dictConfig
dictConfig = configEinlesen()
if (not dictConfig):
    # Default-Konfig
    dictConfig = {"PythonEXE": ".", "CalliKIDir": "/usr/local/share/ki-in-schulen/Calliope-Rennspiel",
                  "COMPort": "/dev/ttypACM0", "Dateiname": "ki-rennspiel-mein-spiel"}
print("Einstellungen:")
print(dictConfig["Dateiname"])
print(dictConfig["PythonEXE"])
print(dictConfig["CalliKIDir"])
print(dictConfig["COMPort"])
print("")


# Kopiert die notwendigen Daten fuer einen Datensammler auf den Calliope.
# Wenn keine Gruppe angegeben wird, dann wird der Datensammler von OpenRoberta genutzt.
# Sonst wird der entsprechende Datensammler auf Basis von Makecode kopiert.
def copyDatensammler(gruppe=0):
    src = None
    if gruppe == 0:
        src = os.path.join(dictConfig["CalliKIDir"], 'OpenRoberta', 'datensammler-openroberta.hex')
    else:
        src = os.path.join(dictConfig["CalliKIDir"], 'Makecode', 'datensammler-funkgruppe%d-makecode.hex' % gruppe)
    dst = get_calliope_drive()
    if dst:
        cmd = 'cp %s %s' % (src, dst)
        os.system(cmd)
    else:
        print("Leider konnte kein Ziellaufwerk ermittelt werden!")


# Kopiert die notwendigen Daten fuer das Rennspiel auf den Calliope.
# Wenn keine Gruppe angegeben wird, dann wird das Rennspiel von OpenRoberta genutzt.
# Sonst wird das entsprechende Rennspiel auf Basis von Makecode kopiert.
def copyRennspiel(gruppe=0):
    src = None
    if gruppe == 0:
        src = os.path.join(dictConfig["CalliKIDir"], 'OpenRoberta', 'rennspiel-openroberta.hex')
    else:
        src = os.path.join(dictConfig["CalliKIDir"], 'Makecode', 'rennspiel-funkgruppe%d-makecode.hex' % gruppe)
    dst = get_calliope_drive()
    if dst:
        cmd = 'cp %s %s' % (src, dst)
        os.system(cmd)
    else:
        print("Leider konnte kein Ziellaufwerk ermittelt werden!")


def portErmitteln():
    for port, desc, hwid in serial.tools.list_ports.grep("USB Serial Device"):
        return port
    else:
        for port, desc, hwid in serial.tools.list_ports.grep("Serielles USB"):
            return port
        else:
            for port, desc, hwrid in serial.tools.list_ports.grep("Serial Port"):
                return port
            else:
                return False

    """
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        print(desc)
        if (desc.startswith('USB Serial Device')):
            # desc.startswith('Serielles USB') für Deutsch
            #'print("{}: {} [{}]".format(port, desc, hwid))
            print(f"Erkannter Port: {port}")
            return port
    """


# Unabhängig von der Konfigurationsdatei (Einstellungsseite) den Port für diesen Rechner automatisch ermitteln.
# Falls das nicht funktioniert, wird der Port aus der Konfiguration verwendet.
usbPort = portErmitteln()
if usbPort:
    dictConfig["COMPort"] = usbPort
    print(f"Erkannter Port: {usbPort}")


def get_calliope_drive():
    return "/run/media/%s/MINI" % os.getenv("USER")


# ki-datenlogger.py
def ki_datenlogger():
    # Hier wird als erster Prozessschritt ein Dateiname abgefragt und auch für die weiteren Schritte genutzt.
    # Falls hier kein Dateiname angegeben wird, wird der Dateiname aus der Konfig weiter verwendet.
    dateiname = simpledialog.askstring("Input", "Bitte einen Dateinamen angeben (ohne Leerzeichen!)",
                                       initialvalue=dictConfig["Dateiname"], parent=fenster)
    if dateiname is not None:
        dictConfig["Dateiname"] = dateiname
    cmd = os.path.join(dictConfig["CalliKIDir"], 'Python', 'ki-datenlogger.py')
    outputfile = os.path.join('csv-rohdaten', dictConfig["Dateiname"] + '.csv')
    subprocess.run([sys.executable, cmd, dictConfig["COMPort"], outputfile], check=True)


# ki-trainieren-sklearn.py
def ki_trainieren():
    cmd = os.path.join(dictConfig["CalliKIDir"], 'Python', 'ki-trainieren-sklearn.py')
    layer = simpledialog.askstring("Input", "Bitte Hidden Layer definieren - A,B oder A,B,C", initialvalue='7,7',
                                   parent=fenster)
    param = os.path.join('csv-rohdaten', dictConfig["Dateiname"] + '.csv')
    outputbase = os.path.join('modelle', dictConfig["Dateiname"])
    subprocess.run([sys.executable, cmd, param, layer, outputbase], check=True)


# ki-rennspiel.py
def ki_rennspiel():
    cmd = os.path.join(dictConfig["CalliKIDir"], 'Python', 'ki-rennspiel.py')
    param = os.path.join('modelle', dictConfig["Dateiname"] + '.pkcls')
    subprocess.run([sys.executable, cmd, 'sklearn', param], check=True)


# Einstellungen-Win definieren
def einstellungen():
    einstellungenWin = Toplevel(fenster)
    einstellungenWin.geometry('700x250')

    def exit_btn():
        dictConfig["Dateiname"] = dateiname_feld.get()
        dictConfig["PythonEXE"] = pythonVerz_feld.get()
        dictConfig["CalliKIDir"] = kiVerz_feld.get()
        configSpeichern(dictConfig)
        einstellungenWin.destroy()
        einstellungenWin.update()

    dateiname_label = Label(einstellungenWin, text="Dateiname")
    dateiname_feld = Entry(einstellungenWin, justify=LEFT, bd=5, width=40)
    dateiname_feld.insert(END, dictConfig["Dateiname"])
    pythonVerz_label = Label(einstellungenWin, text="Python-Verzeichnis")
    pythonVerz_feld = Entry(einstellungenWin, justify=LEFT, bd=5, width=80)
    pythonVerz_feld.insert(END, dictConfig["PythonEXE"])
    kiVerz_label = Label(einstellungenWin, text="KI-Verzeichnis")
    kiVerz_feld = Entry(einstellungenWin, justify=LEFT, bd=5, width=80)
    kiVerz_feld.insert(END, dictConfig["CalliKIDir"])
    usbPort_label = Label(einstellungenWin, text="USB-Port")
    usbPort_feld = Entry(einstellungenWin, justify=LEFT, bd=5, width=20)
    usbPort_feld.insert(END, dictConfig["COMPort"])
    # uebernehmen_button = Button(einstellungenWin, text="Einstellungen übernehmen", command=einstellungenWin.destroy)
    uebernehmen_button = Button(einstellungenWin, text="Einstellungen übernehmen", command=exit_btn)

    dateiname_label.grid(row=0, column=0, pady=15, padx=20)
    dateiname_feld.grid(row=0, column=1, sticky=W)
    pythonVerz_label.grid(row=1, column=0, pady=15, padx=20)
    pythonVerz_feld.grid(row=1, column=1, sticky=W)
    kiVerz_label.grid(row=2, column=0, pady=15, padx=20)
    kiVerz_feld.grid(row=2, column=1, sticky=W)
    usbPort_label.grid(row=3, column=0, pady=15, padx=20)
    usbPort_feld.grid(row=3, column=1, sticky=W)
    uebernehmen_button.grid(row=4, column=0, columnspan=2, pady=15)


# Ein Fenster erstellen
fenster = Tk()
# Den Fenstertitle erstellen
fenster.title("KI mit dem Calliope")
# Fenstergroesse vorgeben
fenster.geometry('400x200')

# Ein Menu anlegen
menubar = Menu(fenster)
# Datei-Menu
dateimenu = Menu(menubar, tearoff=0)
dateimenu.add_command(label="Einstellungen", command=einstellungen)
dateimenu.add_separator()
dateimenu.add_command(label="Beenden", command=fenster.quit)
menubar.add_cascade(label="Datei", menu=dateimenu)

# Calli-Menu
callimenu = Menu(menubar, tearoff=0)
callimenu.add_command(label="Datensammler kopieren", command=copyDatensammler)
callimenu.add_command(label="Rennspiel kopieren", command=copyRennspiel)
callimenu.add_separator()
callimenu.add_command(label="Makecode Datensammler kopieren Gruppe 1", command=lambda: copyDatensammler(1))
callimenu.add_command(label="Makecode Datensammler kopieren Gruppe 2", command=lambda: copyDatensammler(2))
callimenu.add_command(label="Makecode Datensammler kopieren Gruppe 3", command=lambda: copyDatensammler(3))
callimenu.add_command(label="Makecode Datensammler kopieren Gruppe 4", command=lambda: copyDatensammler(4))
callimenu.add_command(label="Makecode Rennspiel kopieren Gruppe 1", command=lambda: copyRennspiel(1))
callimenu.add_command(label="Makecode Rennspiel kopieren Gruppe 2", command=lambda: copyRennspiel(2))
callimenu.add_command(label="Makecode Rennspiel kopieren Gruppe 3", command=lambda: copyRennspiel(3))
callimenu.add_command(label="Makecode Rennspiel kopieren Gruppe 4", command=lambda: copyRennspiel(4))
menubar.add_cascade(label="Calli", menu=callimenu)

# KI-Menu
kimenu = Menu(menubar, tearoff=0)
kimenu.add_command(label="Datensammler starten", command=ki_datenlogger)
kimenu.add_separator()
kimenu.add_command(label="KI anlernen", command=ki_trainieren)
kimenu.add_command(label="KI testen", command=ki_rennspiel)
# kimenu.add_separator()
# kimenu.add_command(label="KI auf Calli kopieren", command=donothing)
menubar.add_cascade(label="KI", menu=kimenu)

# Hilfe-Menu
# hilfemenu = Menu(menubar, tearoff=0)
# hilfemenu.add_command(label="Hilfe", command=donothing)
# menubar.add_cascade(label="Hilfe", menu=hilfemenu)

fenster.config(menu=menubar)
# In der Ereignisschleife auf Eingabe des Benutzers warten.
fenster.mainloop()
