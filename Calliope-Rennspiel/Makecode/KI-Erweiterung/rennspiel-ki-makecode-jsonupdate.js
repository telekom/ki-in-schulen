function kiSteuerung () {
    Ausgabe_String = ""
    erzeugeSnapshot()
    for (let Index = 0; Index <= 5; Index++) {
        Ausgabe_String = "" + Ausgabe_String + snapshot[Index] + ","
    }
    serial.writeLine(Ausgabe_String)
    nntest.predict(snapshot, ergebnis)
    if (ergebnis[0] >= 0.5) {
        output = "A"
        buttonA()
    } else {
        if (ergebnis[1] >= 0.5) {
            output = "B"
            buttonB()
        } else {
            output = "x"
        }
    }
    serial.writeLine(output)
}
function buttonB () {
    if (playerCar.get(LedSpriteProperty.X) < 4) {
        playerCar.change(LedSpriteProperty.X, 1)
    }
}
function buttonA () {
    if (playerCar.get(LedSpriteProperty.X) > 0) {
        playerCar.change(LedSpriteProperty.X, -1)
    }
}
function erzeugeSnapshot () {
    snapshot = [playerCar.get(LedSpriteProperty.X) / 4, (car1.get(LedSpriteProperty.Y) + 1) / 5, (car2.get(LedSpriteProperty.Y) + 1) / 5, (car3.get(LedSpriteProperty.Y) + 1) / 5, (car4.get(LedSpriteProperty.Y) + 1) / 5, (car5.get(LedSpriteProperty.Y) + 1) / 5]
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
let score = 0
let gameOn = false
let car5: game.LedSprite = null
let car4: game.LedSprite = null
let car3: game.LedSprite = null
let car2: game.LedSprite = null
let car1: game.LedSprite = null
let playerCar: game.LedSprite = null
let output = ""
let snapshot: number[] = []
let Ausgabe_String = ""
let ergebnis: number[] = []
let isConnected = 0
ergebnis = [0, 0, 0]
nntest.fcnnfromjson("{\"params\":[{\"layers\":[6,7,7,3]},{\"act\":\"relu\"}],\"coefs\":[[[2.044017,-2.722454,2.000679,-1.514816,0.333606,-2.761747,-0.0],[0.028879,0.096323,-0.24589,0.015551,0.00977,0.001861,0.0],[-0.070218,-0.472358,0.379994,-0.024475,0.003899,-0.393389,0.0],[-0.74473,-0.013117,0.923773,0.1172,0.654482,0.33238,-0.0],[-0.03287,0.362568,0.806845,-0.332245,-0.198489,0.397769,0.0],[0.02064,0.011437,-0.209757,0.022583,0.077942,-0.015708,0.0]],[[-0.0,0.563227,-0.0,-0.196192,-2.71285,2.666878,1.751509],[0.0,-0.0,-0.0,1.679954,1.483361,-2.497833,-0.268884],[-0.0,0.118874,-0.0,-1.440332,-0.33425,0.058711,0.811402],[0.0,-5.311466,0.0,-0.468864,0.057601,-0.743952,1.867721],[-0.0,0.394793,-0.0,-0.382019,-0.52901,3.864352,1.189382],[0.0,-6.229019,0.0,2.250281,1.383958,2.699693,0.394597],[-0.0,-0.0,-0.0,-0.0,-0.0,0.0,-0.0]],[[-0.0,-0.0,0.0],[1.111976,2.797596,-2.238281],[0.0,-0.0,-0.0],[-6.529347,0.144358,3.030409],[3.251293,1.944163,-2.400912],[1.324108,-3.076313,1.005805],[-1.958187,-0.03444,2.36584]]],\"intercepts\":[[-0.449843,0.772355,-0.254264,1.384457,-0.668279,1.448058,-0.658712],[-0.591404,1.820663,-0.630498,0.797055,1.109102,0.036825,-1.220646],[-0.320211,1.158411,-1.175748]]}")
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
control.inBackground(function () {
    while (true) {
        basic.pause(200)
        if (gameOn == true) {
            kiSteuerung()
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
