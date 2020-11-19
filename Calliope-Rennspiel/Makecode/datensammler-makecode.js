radio.onReceivedString(function (receivedString) {
    if (gather_data) {
        serial.writeLine(receivedString)
        basic.setLedColor(Colors.Blue)
        packetCount += 1
    }
})
input.onButtonPressed(Button.B, function () {
    if (!(gather_data)) {
        serial.writeLine("PlayerPos,Car1Pos,Car2Pos,Car3Pos,Car4Pos,Car5Pos,Action")
        gather_data = true
    }
})
let load = 0
let gather_data = false
radio.setGroup(1)
radio.setTransmitPower(7)
radio.setTransmitSerialNumber(false)
gather_data = false
let packetCount = 0
let loadPoint = game.createSprite(0, 0)
loadPoint.set(LedSpriteProperty.Brightness, 0)
control.inBackground(function () {
    while (true) {
        // sending ping
        radio.sendNumber(0)
        basic.pause(200)
    }
})
control.inBackground(function () {
    while (true) {
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
})
control.inBackground(function () {
    while (true) {
        load = packetCount
        packetCount = 0
        basic.pause(1000)
    }
})
