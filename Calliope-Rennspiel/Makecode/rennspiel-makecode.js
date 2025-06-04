/*
 * ki-in-schulen$
 *
 * (C) 2020-25, Christian A. Schiller, Ferenc Hechler, Mirko Jelinek, Dirk Wolters, Deutsche Telekom AG
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

radio.onReceivedNumber(function (receivedNumber) {
    if (radio.receivedPacket(RadioPacketProperty.SignalStrength) != 0) {
        if (isConnected < 2) {
            isConnected += 1
        }
    }
})
input.onButtonPressed(Button.A, function () {
    if (gameOn == true) {
        if (playerCar.get(LedSpriteProperty.X) > 0) {
            output = "A"
            erzeugeTrainingsdatensatz()
            playerCar.change(LedSpriteProperty.X, -1)
        }
    }
})
input.onButtonPressed(Button.B, function () {
    if (gameOn == true) {
        if (playerCar.get(LedSpriteProperty.X) < 4) {
            output = "B"
            erzeugeTrainingsdatensatz()
            playerCar.change(LedSpriteProperty.X, 1)
        }
    }
})
function erzeugeSnapshot () {
    snapshot = [
    playerCar.get(LedSpriteProperty.X),
    car1.get(LedSpriteProperty.Y) + 1,
    car2.get(LedSpriteProperty.Y) + 1,
    car3.get(LedSpriteProperty.Y) + 1,
    car4.get(LedSpriteProperty.Y) + 1,
    car5.get(LedSpriteProperty.Y) + 1
    ]
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
function erzeugeTrainingsdatensatz () {
    Ausgabe_String = ""
    erzeugeSnapshot()
    for (let Index = 0; Index <= 5; Index++) {
        Ausgabe_String = "" + Ausgabe_String + snapshot[Index] + ","
    }
    Ausgabe_String = "" + Ausgabe_String + output
    radio.sendString(Ausgabe_String)
}
let score = 0
let speedup = 0
let Ausgabe_String = ""
let snapshot: number[] = []
let playerCar: game.LedSprite = null
let car5: game.LedSprite = null
let car4: game.LedSprite = null
let car3: game.LedSprite = null
let car2: game.LedSprite = null
let car1: game.LedSprite = null
let output = ""
let isConnected = 0
let gameOn = false
gameOn = false
isConnected = 0
output = "x"
let init = true
let Funkgruppe = 1
basic.showNumber(Funkgruppe)
while (init) {
    if (input.buttonIsPressed(Button.A)) {
        Funkgruppe += 1
        if (Funkgruppe > 7) {
            Funkgruppe = 1
        }
    }
    basic.showNumber(Funkgruppe)
    if (input.buttonIsPressed(Button.B)) {
        init = false
    }
}
radio.setTransmitPower(7)
radio.setGroup(Funkgruppe)
car1 = game.createSprite(0, 0)
car1.delete()
car2 = game.createSprite(1, 0)
car2.delete()
car3 = game.createSprite(2, 0)
car3.delete()
car4 = game.createSprite(3, 0)
car4.delete()
car5 = game.createSprite(4, 0)
car5.delete()
playerCar = game.createSprite(2, 4)
gameOn = true
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
    while (true) {
        if (isConnected > 1) {
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
control.inBackground(function () {
    while (gameOn == true) {
        basic.pause(5000)
        speedup += 10
    }
})
control.inBackground(function () {
    if (gameOn == true) {
        basic.pause(Math.randomRange(0, 2500))
        car2 = game.createSprite(1, 0)
        basic.pause(500 - speedup)
        while (gameOn == true) {
            if (car2.get(LedSpriteProperty.Y) == 4) {
                if (playerCar.isTouching(car2)) {
                    gameOn = false
                    images.iconImage(IconNames.Skull).showImage(0)
                    basic.pause(1000)
                    game.gameOver()
                    control.reset()
                } else {
                    score = score + 1
                    game.setScore(score)
                    car2.delete()
                    basic.pause(Math.randomRange(0, 2500))
                    car2 = game.createSprite(1, 0)
                    basic.pause(500 - speedup)
                }
            } else {
                car2.change(LedSpriteProperty.Y, 1)
                basic.pause(500 - speedup)
            }
        }
    }
})
control.inBackground(function () {
    if (gameOn == true) {
        basic.pause(Math.randomRange(0, 2500))
        car4 = game.createSprite(3, 0)
        basic.pause(500 - speedup)
        while (gameOn == true) {
            if (car4.get(LedSpriteProperty.Y) == 4) {
                if (playerCar.isTouching(car4)) {
                    gameOn = false
                    images.iconImage(IconNames.Skull).showImage(0)
                    basic.pause(1000)
                    game.gameOver()
                    basic.pause(1000)
                    control.reset()
                } else {
                    score = score + 1
                    game.setScore(score)
                    car4.delete()
                    basic.pause(Math.randomRange(0, 2500))
                    car4 = game.createSprite(3, 0)
                    basic.pause(500 - speedup)
                }
            } else {
                car4.change(LedSpriteProperty.Y, 1)
                basic.pause(500 - speedup)
            }
        }
    }
})
control.inBackground(function () {
    if (gameOn == true) {
        basic.pause(Math.randomRange(0, 2500))
        car5 = game.createSprite(4, 0)
        basic.pause(500 - speedup)
        while (gameOn == true) {
            if (car5.get(LedSpriteProperty.Y) == 4) {
                if (playerCar.isTouching(car5)) {
                    gameOn = false
                    images.iconImage(IconNames.Skull).showImage(0)
                    basic.pause(1000)
                    game.gameOver()
                    control.reset()
                } else {
                    score = score + 1
                    game.setScore(score)
                    car5.delete()
                    basic.pause(Math.randomRange(0, 2500))
                    car5 = game.createSprite(4, 0)
                    basic.pause(500 - speedup)
                }
            } else {
                car5.change(LedSpriteProperty.Y, 1)
                basic.pause(500 - speedup)
            }
        }
    }
})
control.inBackground(function () {
    if (gameOn == true) {
        basic.pause(Math.randomRange(0, 2500))
        car1 = game.createSprite(0, 0)
        basic.pause(500 - speedup)
        while (gameOn == true) {
            if (car1.get(LedSpriteProperty.Y) == 4) {
                if (playerCar.isTouching(car1)) {
                    gameOn = false
                    images.iconImage(IconNames.Skull).showImage(0)
                    basic.pause(1000)
                    game.gameOver()
                    control.reset()
                } else {
                    score = score + 1
                    game.setScore(score)
                    car1.delete()
                    basic.pause(Math.randomRange(0, 2500))
                    car1 = game.createSprite(0, 0)
                    basic.pause(500 - speedup)
                }
            } else {
                car1.change(LedSpriteProperty.Y, 1)
                basic.pause(500 - speedup)
            }
        }
    }
})
control.inBackground(function () {
    if (gameOn == true) {
        basic.pause(Math.randomRange(0, 2500))
        car3 = game.createSprite(2, 0)
        basic.pause(500 - speedup)
        while (gameOn == true) {
            if (car3.get(LedSpriteProperty.Y) == 4) {
                if (playerCar.isTouching(car3)) {
                    gameOn = false
                    images.iconImage(IconNames.Skull).showImage(0)
                    basic.pause(1000)
                    game.gameOver()
                    basic.pause(1000)
                    control.reset()
                } else {
                    score = score + 1
                    game.setScore(score)
                    car3.delete()
                    basic.pause(Math.randomRange(0, 2500))
                    car3 = game.createSprite(2, 0)
                    basic.pause(500 - speedup)
                }
            } else {
                car3.change(LedSpriteProperty.Y, 1)
                basic.pause(500 - speedup)
            }
        }
    }
})
