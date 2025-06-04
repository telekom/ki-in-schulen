/*
 * ki-in-schulen$
 *
 * (C) 2021-25, Christian A. Schiller, Ferenc Hechler, Mirko Jelinek, Dirk Wolters, Deutsche Telekom AG
 *
 * Deutsche Telekom AG and all other contributors /
 * copyright owners license this file to you under the
 * MIT License (the "License"); you may not use this
 * file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * https://opensource.org/licenses/MIT
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 *
 * v20250604
 *
 */

radio.onReceivedString(function (receivedString) {
    if (gather_data) {
        serial.writeLine(receivedString)
        basic.setLedColor(Colors.Blue)
        packetCount += 1
    }
})
input.onButtonPressed(Button.B, function () {
    if (!(init)) {
        if (!(gather_data)) {
            serial.writeLine("PlayerPos,Car1Pos,Car2Pos,Car3Pos,Car4Pos,Car5Pos,Action")
            gather_data = true
        }
    }
})
let load = 0
let packetCount = 0
let loadPoint: game.LedSprite = null
let gather_data = false
let init = false
init = true
let Funkgruppe = 1
basic.showNumber(Funkgruppe)
gather_data = false
while (init) {
    if (input.buttonIsPressed(Button.A)) {
        Funkgruppe += 1
        if (Funkgruppe > 7) {
            Funkgruppe = 1
        }
        basic.showNumber(Funkgruppe)
    }
    if (input.buttonIsPressed(Button.B)) {
        radio.setGroup(Funkgruppe)
        radio.setTransmitPower(7)
        radio.setTransmitSerialNumber(false)
        serial.writeLine("Datensammler - Funkgruppe:")
        serial.writeLine("" + (Funkgruppe))
        serial.writeLine("---------------------------")
        loadPoint = game.createSprite(0, 0)
        loadPoint.set(LedSpriteProperty.Brightness, 0)
        init = false
    }
}
control.inBackground(function () {
    while (true) {
        if (!(init)) {
            // sending ping
            radio.sendNumber(0)
            basic.pause(500)
        }
    }
})
control.inBackground(function () {
    while (true) {
        if (!(init)) {
            basic.setLedColor(Colors.Off)
            if (!(gather_data)) {
                basic.showArrow(ArrowNames.East)
                basic.clearScreen()
            } else {
                if (load > 0) {
                    if (load > 5) {
                        load = 5
                    }
                    loadPoint.set(LedSpriteProperty.X, load - 1)
                    loadPoint.set(LedSpriteProperty.Brightness, 255)
                } else {
                    loadPoint.set(LedSpriteProperty.X, 0)
                    loadPoint.set(LedSpriteProperty.Brightness, 20)
                }
            }
            basic.pause(500)
        }
    }
})
control.inBackground(function () {
    while (true) {
        if (!(init)) {
            load = packetCount
            packetCount = 0
            basic.pause(1000)
        }
    }
})
