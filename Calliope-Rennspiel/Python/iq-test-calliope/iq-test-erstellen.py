#
# iq-test-erstellen.py$
#
# (C) 2021, Ferenc Hechler, Christian A. Schiller, Deutsche Telekom AG
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
# Calliope Rennspiel mit Künstlicher Intelligenz
# ----------------------------------------------
# Modul: IQ-Test mit Calliope
#
# Funktion:
# Übernimmt ein trainiertes neuronales Netzwerk im JSON-Format
# in das Calliope-Rennspiel, sodass dort die Leistung beobachtet werden kann.
#
# Nutzung:
#
# 	python iq-test-erstellen.py -r <JSON-Modelldatei>
#
# 	<JSON-Modelldatei>: Name der JSON-Datei, die ein trainiertes neuronales Netzwerk enthält (erzeugt durch ki-trainieren-sklearn.py)
#

import argparse

def c2hx(c):
    return "%0.2X" % (c & 255)


def replaceText(outfile, line, replacement_text):
    start = line[0:9]
    chk = 0;
    for i in range(0, 4):
        b = int(start[1+2*i:3+2*i], 16)
        chk += b
    replace = "";
    for i in range(0, 16):
        c = ord((replacement_text+"                ")[i])
        chk += c
        hx = c2hx(c)
        replace += hx
    check = c2hx(-chk)
    outfile.write(start+replace+check+"\n")
    print(start+replace+check)


def startOverwrite(outfile, previous_line, line, infile, replacement_text):
    if len(replacement_text)<33:
        replacement_text += "                                 "[len(replacement_text):]
    replaceText(outfile, previous_line, replacement_text)
    replacement_text = replacement_text[16:]
    replaceText(outfile, line, replacement_text)
    while len(replacement_text)>16:
        replacement_text = replacement_text[16:]
        line = infile.readline();
        line = line.replace("\r", "").replace("\n", "")
        replaceText(outfile, line, replacement_text)
    if line[9:41] != "20202020202020202020202020202020":
        raise Exception("replacement_text too long!")


def patch_hex_file(input_file, output_file, search_pattern, replacement_text):
    print(f"input_file: {input_file}")
    print(f"output_file: {output_file}")
    print(f"search_pattern: {search_pattern}")
    print(f"replacement_text: {replacement_text}")

    with open (input_file, "r") as infile:
        line=infile.readline()
        with open (output_file, "w") as outfile:
            previous_line = None
            while line:
                line = line.replace("\r", "").replace("\n", "")
                if line.find(search_pattern) != -1:
                    startOverwrite(outfile, previous_line, line, infile, replacement_text)
                    previous_line = None
                    line = infile.readline()
                if previous_line is not None:
                    outfile.write(previous_line+"\n")
                    print(previous_line)
                previous_line = line;
                line=infile.readline()
            if previous_line is not None:
                outfile.write(previous_line+"\n")
                print(previous_line)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', type=str, default="./base.hex", help="base hex input file to be patched")
    parser.add_argument('-o', '--output-file', type=str, default="./iq-test-calliope.hex", help="output file to write the patched hex into")
    parser.add_argument('-s', '--search-pattern', type=str, default="5465537454655874", help="hex search pattern")
    parser.add_argument('-r', '--replacement-file', type=str, default="./replacement.txt", help="file with the text to overwrite")
    parser.add_argument('-t', '--replacement-text', type=str, required=False, help="text to overwrite")
    args = parser.parse_args()
    input_file = args.input_file
    output_file = args.output_file
    search_pattern = args.search_pattern
    replacement_file = args.replacement_file
    if (args.replacement_text):
        replacement_text = args.replacement_text
    else:
        with open(replacement_file, 'r') as file:
            replacement_text = file.read()
    patch_hex_file(input_file, output_file, search_pattern, replacement_text)
