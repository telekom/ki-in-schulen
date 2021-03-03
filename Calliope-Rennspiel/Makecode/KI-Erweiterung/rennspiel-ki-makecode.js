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
nntest.fcnnfromjson("{\"params\":[{\"input_layer_size\":6},{\"output_layer_size\":3},{\"activation\":\"relu\",\"hidden_layer_sizes\":[5,5]}],\"coefs\":[[[-3.7618694,-2.6353294,2.0412038,2.7507570,1.6466139],[0.2206414,0.2857989,0.0036425,-0.0317820,0.0559500],[-0.3058574,0.0878977,0.0492077,0.3788245,0.5272455],[0.1418911,-0.5663988,-0.0869069,-0.2828898,-0.8718336],[-0.0322197,0.0577339,-0.1863063,-0.0384424,0.1599369],[0.0266982,0.0066587,0.0595484,-0.0287083,-0.0006110]],[[7.1437476,-2.0554118e-315,2.8380345,1.1519000,1.2869832],[2.2378122,-1.4113241e-316,-1.5034219,-1.8060312,-2.2305049],[-0.2735701,-1.0922309e-315,-7.3422328,-1.4980596,6.8257498],[1.8430388,8.5192065e-316,-0.7668328,-1.8421836,-1.0176375],[-0.8067680,-3.3015611e-315,1.2071462,1.5776832,0.5271287]],[[-4.6077195,1.5161148,1.2917883],[2.8131030e-315,2.2861011e-316,1.8319176e-315],[-13.3641057,-0.0294115,2.0165486],[0.3073160,-12.9430346,8.2265951],[2.0830323,-7.2889256,0.4762098]]],\"intercepts\":[[1.0793285,1.1360822,-1.2682957,-0.3395825,0.4240467],[-0.5619802,-0.7513708,-0.3975687,0.2460306,0.8341611],[1.2935391,1.4975659,-2.9816267]]}")
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
