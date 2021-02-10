/*
 * ki-in-schulen$
 *
 * (C) 2021, Christian A. Schiller, Ferenc Hechler, Mirko Jelinek, Dirk Wolters, Deutsche Telekom AG
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
 */

input.onButtonPressed(Button.B, function () {
    if (playerCar.get(LedSpriteProperty.X) < 4) {
        output = "B"
        erzeugeTrainingsdatensatz()
        playerCar.change(LedSpriteProperty.X, 1)
    }
})
function erzeugeSnapshot () {
    snapshot = [playerCar.get(LedSpriteProperty.X), car1.get(LedSpriteProperty.Y) + 1, car2.get(LedSpriteProperty.Y) + 1, car3.get(LedSpriteProperty.Y) + 1, car4.get(LedSpriteProperty.Y) + 1, car5.get(LedSpriteProperty.Y) + 1]
    if (car1.isDeleted()) {
        snapshot[1] = 0
    }
    if (car2.isDeleted()) {
        snapshot[2] = 0
    }
    if (car3.isDeleted()) {
        snapshot[3] = 0
    }
    if (car4.isDeleted()) {
        snapshot[4] = 0
    }
    if (car5.isDeleted()) {
        snapshot[5] = 0
    }
}
radio.onReceivedNumber(function (receivedNumber) {
    if (radio.receivedPacket(RadioPacketProperty.SignalStrength) != 0) {
        if (radio.receivedPacket(RadioPacketProperty.SignalStrength) > -90) {
            if (isConnected < 2) {
                isConnected += 1
            }
        }
    }
})
function erzeugeTrainingsdatensatz () {
    Ausgabe_String = ""
    erzeugeSnapshot()
    for (let Index = 0; Index <= 5; Index++) {
        Ausgabe_String = "" + Ausgabe_String + snapshot[Index] + ","
    }
    Ausgabe_String = "" + Ausgabe_String + output
    radio.sendString(Ausgabe_String)
    serial.writeLine(Ausgabe_String)
}
input.onButtonPressed(Button.A, function () {
    if (playerCar.get(LedSpriteProperty.X) > 0) {
        output = "A"
        erzeugeTrainingsdatensatz()
        playerCar.change(LedSpriteProperty.X, -1)
    }
})
let score = 0
let gameOn = false
let Ausgabe_String = ""
let car5: game.LedSprite = null
let car4: game.LedSprite = null
let car3: game.LedSprite = null
let car2: game.LedSprite = null
let car1: game.LedSprite = null
let snapshot: number[] = []
let playerCar: game.LedSprite = null
let output = ""
let isConnected = 0
let funkGruppe = 1
isConnected = 0
output = "x"
radio.setGroup(funkGruppe)
radio.setTransmitPower(7)
serial.writeLine("Rennspiel - Funkgruppe " + funkGruppe)
serial.writeLine("------------------------")
basic.showNumber(funkGruppe)
basic.pause(3000)

basic.forever(function () {
    basic.pause(100)
    if (gameOn == true) {
        car1 = game.createSprite(0, 0)
        basic.pause(Math.randomRange(0, 5001))
        while (gameOn == true) {
            if (car1.get(LedSpriteProperty.Y) == 4) {
                if (playerCar.isTouching(car1)) {
                    gameOn = false
                } else {
                    score = score + 1
                    car1.delete()
                    basic.pause(Math.randomRange(0, 5001))
                    car1 = game.createSprite(0, 0)
                    basic.pause(500)
                }
            } else {
                car1.change(LedSpriteProperty.Y, 1)
                basic.pause(500)
            }
        }
    }
})
basic.forever(function () {
    basic.pause(100)
    if (gameOn == true) {
        car2 = game.createSprite(1, 0)
        basic.pause(Math.randomRange(0, 5001))
        while (gameOn == true) {
            if (car2.get(LedSpriteProperty.Y) == 4) {
                if (playerCar.isTouching(car2)) {
                    gameOn = false
                } else {
                    score = score + 1
                    car2.delete()
                    basic.pause(Math.randomRange(0, 5001))
                    car2 = game.createSprite(1, 0)
                    basic.pause(500)
                }
            } else {
                car2.change(LedSpriteProperty.Y, 1)
                basic.pause(500)
            }
        }
    }
})
basic.forever(function () {
    basic.pause(100)
    if (gameOn == true) {
        car3 = game.createSprite(2, 0)
        basic.pause(Math.randomRange(0, 5001))
        while (gameOn == true) {
            if (car3.get(LedSpriteProperty.Y) == 4) {
                if (playerCar.isTouching(car3)) {
                    gameOn = false
                } else {
                    score = score + 1
                    car3.delete()
                    basic.pause(Math.randomRange(0, 5001))
                    car3 = game.createSprite(2, 0)
                    basic.pause(500)
                }
            } else {
                car3.change(LedSpriteProperty.Y, 1)
                basic.pause(500)
            }
        }
    }
})
basic.forever(function () {
    basic.pause(100)
    if (gameOn == true) {
        car4 = game.createSprite(3, 0)
        basic.pause(Math.randomRange(0, 5001))
        while (gameOn == true) {
            if (car4.get(LedSpriteProperty.Y) == 4) {
                if (playerCar.isTouching(car4)) {
                    gameOn = false
                } else {
                    score = score + 1
                    car4.delete()
                    basic.pause(Math.randomRange(0, 5001))
                    car4 = game.createSprite(3, 0)
                    basic.pause(500)
                }
            } else {
                car4.change(LedSpriteProperty.Y, 1)
                basic.pause(500)
            }
        }
    }
})
basic.forever(function () {
    basic.pause(100)
    if (gameOn == true) {
        car5 = game.createSprite(4, 0)
        basic.pause(Math.randomRange(0, 5001))
        while (gameOn == true) {
            if (car5.get(LedSpriteProperty.Y) == 4) {
                if (playerCar.isTouching(car5)) {
                    gameOn = false
                } else {
                    score = score + 1
                    car5.delete()
                    basic.pause(Math.randomRange(0, 5001))
                    car5 = game.createSprite(4, 0)
                    basic.pause(500)
                }
            } else {
                car5.change(LedSpriteProperty.Y, 1)
                basic.pause(500)
            }
        }
    }
})
control.inBackground(function () {
    while (true) {
        basic.pause(500)
        if (gameOn == true) {
            if (output == "x") {
                erzeugeTrainingsdatensatz()
            }
            output = "x"
        }
    }
})
control.inBackground(function () {
    score = 0
    playerCar = game.createSprite(2, 4)
    gameOn = true
    while (gameOn == true) {
        basic.pause(100)
    }
    game.addScore(score)
    game.gameOver()
})
control.inBackground(function () {
    while (true) {
        if (isConnected) {
            basic.setLedColor(Colors.Blue)
        } else {
            basic.turnRgbLedOff()
        }
        if (isConnected > 0) {
            isConnected += -1
        }
        basic.pause(500)
    }
})
